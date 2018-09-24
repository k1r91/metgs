import os
import json
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib import auth
from django.contrib.sites.shortcuts import get_current_site
from django.http import Http404, HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.template import loader
from django.template.context_processors import csrf
from mainapp.models import *
from mainapp.forms import SignUpForm, UserEditFrom, CategoryForm
from mainapp.get_token import account_activation_token
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def get_common_context():
    categories = Category.objects.all()
    menu_list = TopMenu.objects.all()
    organization = Organization.objects.all()[0]
    return {'organization': organization, 'menu_list': menu_list, 'categories': categories}


def index(request):
    context = get_common_context()
    return render(request, 'index.html', context)


def login(request):
    context = get_common_context()
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            context['errors'] = True
            return render(request, 'login.html', context)
    elif request.method == 'GET':
        return render(request, 'login.html', context)
    else:
        raise Http404


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def signup(request):
    context = get_common_context()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Активация вашего аккаунта на metgs.ru'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMultiAlternatives(mail_subject, message, '', [to_email])
            email.attach_alternative(message, "text/html")
            email.send()
            context['email'] = user.email
            return render(request, 'signup_confirm.html', context)
        else:
            context['form'] = form
            return render(request, 'signup.html', context)
    elif request.method == 'GET':
        context['form'] = SignUpForm()
        return render(request, 'signup.html', context)
    raise Http404


def activate(request, uidb64, token):
    uidb64 = uidb64[2:-1]  # removing quotes and bytes
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        context = get_common_context()
        user.is_active = True
        user.save()
        auth.login(request, user)
        return render(request, 'signup_confirm.html', context)
    else:
        raise Http404


def admin(request):
    user = request.user
    if not user.is_superuser:
        raise Http404
    users = User.objects.all()
    context = dict()
    context['users'] = users
    if request.method == 'GET':
        edit_form = UserEditFrom()
        context['edit_form'] = edit_form
        return render(request, os.path.join('admin', 'users.html'), context)
    elif request.method == 'POST':
        id = request.POST.get('id')
        print(id)
        if id:
            user = get_object_or_404(User, id=id)
            form = UserEditFrom(request.POST or None, instance=user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/admin/')
    else:
        return render(request, os.path.join('admin', 'users.html'), context)


def get_user_form(request, id):
    if request.is_ajax():
        if not request.user.is_superuser:
            raise Http404
        user = get_object_or_404(User, id=id)
        form = UserEditFrom(instance=user)
        context = {'edit_form': form, 'id': id}
        context.update(csrf(request))
        html = loader.render_to_string('admin/inc_user_edit_form.html', context)
        data = {'errors': False, 'html': html}
        return JsonResponse(data)


def add_user(request):
    if request.is_ajax():
        context = {}
        data = json.loads(request.body.decode())
        print(data)
        form_data = {}
        for item in data:
            if item["name"] == "id":
                if item["value"] == "":
                    continue
            form_data[item["name"]] = item["value"]
        print(form_data)
        if form_data.get("id"):
            user = User.objects.get(id=form_data.get('id'))
            form = UserEditFrom(form_data, instance=user)
        else:
            form = UserEditFrom(form_data)
        context['users'] = User.objects.all()
        context['edit_form'] = form
        if form.is_valid():
            form.save()
            html = loader.render_to_string('admin/inc_users_list.html', context)
            data = {'errors': False, 'html': html}
            return JsonResponse(data)
        else:
            html = loader.render_to_string('admin/inc_user_edit_form.html', context)
            data = {'errors': True, 'html': html}
            return JsonResponse(data)


def get_user(request, id):
    data = {}
    try:
        user = User.objects.get(id=id)
        data['errors'] = False
    except User.DoesNotExist:
        data['errors'] = True
    html = loader.render_to_string('admin/inc_user_delete.html', {'user_delete': user})
    data['html'] = html
    return JsonResponse(data)


def delete_user(request):
    if not request.user.is_superuser:
        raise Http404
    data = json.loads(request.body.decode())
    response = {}
    try:
        user = User.objects.get(id=data['id'])
        response['errors'] = False
        user.delete()
    except User.DoesNotExist:
        data['errors'] = True
        response['errors'] = True
    context = {'users': User.objects.all()}
    html = loader.render_to_string('admin/inc_users_list.html', context)
    response['html'] = html
    return JsonResponse(response)


def admin_category(request, lpage=False):
    if not request.user.is_staff:
        raise Http404
    categories = Category.objects.all()
    paginator = Paginator(categories, 5)
    page = request.GET.get('page')
    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)
    if lpage:
        categories = paginator.page(paginator.num_pages)
    for cat in categories:
        desc = cat.desc.split(' ')
        cat.short_desc = ' '.join(desc[:15])
    return render(request, 'admin/category.html', {'categories': categories})


def add_category(request):
    if not request.user.is_staff:
        raise Http404
    if request.method == 'GET':
        form = CategoryForm()
        return render(request, 'admin/category_add.html', {'form': form})
    elif request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return admin_category(request, lpage=True)
        else:
            print("SYBHERE")
            return render(request, 'admin/category_add.html', {'form': form})
