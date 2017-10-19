# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
    title = models.CharField(max_length = 140)
    content = models.TextField()
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length =50)
    file = models.FileField(null=True, blank=True)
    date = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
    	return reverse("personal:detail", kwargs={"id": self.id})
    	