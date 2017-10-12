# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
	return render(request, 'personal/index.html')
	
def search(request):
	return render(request, 'personal/htmlElements.html')
# Create your views here.
