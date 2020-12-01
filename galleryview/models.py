from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200,   db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    def __str__(self):
        return self.name


class List(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    tag= models.ForeignKey(Tag, related_name='tags', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d',   blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list')

