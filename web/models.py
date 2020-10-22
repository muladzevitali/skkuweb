from django.db import models
from django.utils import timezone


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000, null=False)
    email = models.CharField(max_length=1000)
    message = models.TextField()
    sent_date = models.DateTimeField(default=timezone.now)


class Preset(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=10000)
    image_path = models.CharField(max_length=10000)
    file_path = models.CharField(max_length=10000)
