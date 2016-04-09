# coding: utf-8

from meetup.models import Meetup
from django.shortcuts import render, get_object_or_404


def home(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # return render(request, 'blog/post_list.html', {'posts':posts})
    posts = 'haha'
    return render(request, 'home.html', {'posts': posts})
