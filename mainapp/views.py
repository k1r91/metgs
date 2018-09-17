from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.contrib.sites.shortcuts import get_current_site
from django.http import Http404, HttpResponse
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from mainapp.models import *
from mainapp.forms import SignUpForm
from mainapp.token import account_activation_token
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
            current_site = get_current_site(request)
            mail_subject = 'Активация вашего аккаунта на metgs.ru'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return HttpResponse('Please confirm you email address to complete registration.')
        else:
            context['form'] = form
            return render(request, 'signup.html', context)
    elif request.method == 'GET':
        context['form'] = SignUpForm()
        return render(request, 'signup.html', context)
    raise Http404
