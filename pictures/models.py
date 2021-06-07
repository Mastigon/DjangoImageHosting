from django.db import models
from django.urls import reverse


class Pictures(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Картинка')
    time_create = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('delete', kwargs={'pk': self.pk})