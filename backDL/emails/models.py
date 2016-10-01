from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Contact(models.Model):
    name    = models.CharField(max_length=200)
    email   = models.CharField(max_length=200)
    text    = models.TextField(max_length=200)

    date    = models.DateTimeField('date published')
