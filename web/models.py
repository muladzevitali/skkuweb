from django.utils import timezone
from django.db import models


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000, null=False)
    email = models.CharField(max_length=1000)
    message = models.TextField()
    sent_date = models.DateTimeField(default=timezone.now)
