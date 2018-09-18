from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def validate_email_unique(value):
    exists = User.objects.filter(email=value)
    if exists and exists[0].is_active:
        raise ValidationError("Пользователь с таким email уже зарегистрирован.")


class SignUpForm(UserCreationForm):

    email = forms.EmailField(max_length=200, validators=[validate_email_unique])

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']