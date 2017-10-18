# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 140)
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length =50)
    file = models.FileField(upload_to='\personal\static\personal\images/%Y/%m/%d/')
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title
