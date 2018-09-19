from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def validate_email_unique(value):
    exists = User.objects.filter(email=value)
    if exists and exists[0].is_active:
        raise ValidationError("Пользователь с таким email уже зарегистрирован.")


def validate_id_unique(value):
    exists = User.objects.filter(id=value)
    if exists and exists[0].is_active:
        raise ValidationError("Пользователь с таким id уже зарегистрирован.")


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, validators=[validate_email_unique])

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserEditFrom(UserCreationForm):
    id = forms.IntegerField(label='', widget=forms.HiddenInput(attrs={'id': 'user_id'}), required=False)
    email = forms.EmailField(max_length=200)
    is_active = forms.BooleanField(label="Активен", required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'is_superuser', 'is_staff', 'is_active', 'email', 'password1', 'password2']
