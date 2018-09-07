from django.db import models
# Create your models here.


class TopMenu(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(unique=True)
    visible = models.BooleanField(default=True)
    content = models.TextField(blank=True, null=True)
