from django.db import models
# Create your models here.


class TopMenu(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(unique=True)
    visible = models.BooleanField(default=True)
    content = models.TextField(blank=True, null=True)


class Organization(models.Model):
    logo = models.ImageField(upload_to='logo')
    phone = models.CharField(max_length=64, blank=True, null=True)
    phone_prefix = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=256, blank=True, null=True)
    contact_text = models.CharField(max_length=128, blank=True, null=True)