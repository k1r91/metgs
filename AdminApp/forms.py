from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from mainapp.models import Category, Good, TopMenu, PhotoAlbum, Price, News, Organization


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


class GoodForm(forms.ModelForm):
    related = forms.ModelMultipleChoiceField(
        required=False,
        label="Сопутствующие товары",
        queryset=Good.objects.all(),
        widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Good
        fields = '__all__'


class TopMenuForm(forms.ModelForm):
    class Meta:
        model = TopMenu
        fields = '__all__'


class PhotoAlbumForm(forms.ModelForm):
    class Meta:
        model = PhotoAlbum
        fields = '__all__'


class PriceForm(forms.ModelForm):
    class Meta:
        model = Price
        fields = '__all__'


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'


class Organization(forms.ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'
