import os
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.contrib.sites.shortcuts import get_current_site
from django.http import Http404, HttpResponse
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from mainapp.models import *
from mainapp.forms import SignUpForm
from mainapp.get_token import account_activation_token
# Create your views here.

def get_common_context():
    menu_list = TopMenu.objects.all()
    organization = Organization.objects.all()[0]
    return {'organization': organization, 'menu_list': menu_list}


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
    uidb64 = uidb64[2:-1]   # removing quotes and bytes
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
    users = User.objects.all()
    context = dict()
    context['users'] = users
    if not user.is_superuser:
        raise Http404
    return render(request, os.path.join('admin', 'users.html'), context)
