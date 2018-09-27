from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from mainapp.models import Category

class UserEditFrom(UserCreationForm):
    id = forms.IntegerField(label='', widget=forms.HiddenInput(attrs={'id': 'user_id'}), required=False)
    email = forms.EmailField(max_length=200)
    is_active = forms.BooleanField(label="Активен", required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'is_superuser', 'is_staff', 'is_active', 'email', 'password1', 'password2']


class CategoryForm(forms.ModelForm):
    related = forms.ModelMultipleChoiceField(
        required=False,
        label="Сопутствующие категории",
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Category
        fields = '__all__'