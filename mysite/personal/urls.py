"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from . import views
from personal import views as personal_views


urlpatterns = [
	url(r'^$', personal_views.post_list, name='list'),
	url(r'^create/$', personal_views.post_create, name='create'),
	url(r'^(?P<slug>[\w-]+)/$', personal_views.post_detail, name='detail'),
	url(r'^(?P<slug>[\w-]+)/edit/$', personal_views.post_update, name="update"),
	url(r'^(?P<slug>[\w-]+)/delete/$', personal_views.post_delete, name="delete"),
]
