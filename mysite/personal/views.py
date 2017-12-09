# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from .forms import PostForm
from .models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def post_list(request):
    queryset_list = Post.objects.all().order_by("-date")

    query = request.GET.get("Query")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(firstname__icontains=query) |
            Q(lastname__icontains=query)
            ).distinct()

    paginator = Paginator(queryset_list, 10)
    page_request_var = "page"
    page = request.GET.get(page_request_var) 
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        "object_list": queryset,
        "title": "List",
        "page_request_var":page_request_var
    }
    return render(request, 'post_list.html', context)

@login_required
def post_create(request):
    if not request.user.is_authenticated():
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, 'post_form.html', context)

@login_required
def post_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    context = {
        "title": instance.title,
        "instance": instance,
    }

    return render(request, 'post_detail.html', context)

@login_required
def post_update(request, slug=None):
    if not request.user.is_authenticated():
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    if not request.user == instance.user or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None,  request.FILES or None, instance=instance)
    if form.is_valid():
        if request.user == instance.user or request.user.is_superuser:
           instance = form.save(commit=False)
           instance.save()
           return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,
        "instance": instance,
        "form":form,
    }

    return render(request, 'post_form.html', context)

@login_required
def post_delete(request, slug=None):
    if not request.user.is_authenticated():
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    if request.user == instance.user or request.user.is_superuser:
            instance.delete()
            return redirect("personal:list")
    elif not request.user == instance.user or not request.user.is_superuser:
    	raise Http404

