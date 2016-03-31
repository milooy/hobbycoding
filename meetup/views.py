# coding: utf-8

from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Meetup
from .forms import MeetupEditForm, CommentForm
from django.shortcuts import render, get_object_or_404, redirect


def meetup_list(request):
    meetups = Meetup.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'meetup_list.html', {'meetups':meetups})


def meetup_detail(request, pk):
    meetup = get_object_or_404(Meetup, pk=pk)

    if request.method == 'GET':
        form = CommentForm()
    elif request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.meetup = meetup
            new_comment.created_date = timezone.now()
            new_comment.save()
            return redirect('meetup.views.meetup_detail', pk=pk)

    return render(request, 'meetup_detail.html', {'meetup': meetup, 'cmtForm': form})


@login_required
def meetup_new(request):
    if request.method == 'GET':
        form = MeetupEditForm()
    elif request.method == 'POST':
        form = MeetupEditForm(request.POST, request.FILES)

        if form.is_valid():
            new_meetup = form.save(commit=False)
            new_meetup.author = request.user
            new_meetup.published_date = timezone.now()
            new_meetup.save()
            return redirect('meetup.views.meetup_detail', pk=new_meetup.pk)

    return render(request, 'meetup_edit.html', {'form': form})


def meetup_edit(request, pk):
    meetup = get_object_or_404(Meetup, pk=pk)
    if request.method == 'GET':
        form = MeetupEditForm()
    elif request.method == 'POST':
        form = MeetupEditForm(request.POST, request.FILES)

        if form.is_valid():
            new_meetup = form.save(commit=False)
            new_meetup.author = request.user
            new_meetup.published_date = timezone.now()
            new_meetup.save()
            return redirect('meetup.views.meetup_detail', pk=new_meetup.pk)

    return render(request, 'meetup_edit.html', {'form': form})


def meetup_join(request, pk):
    Meetup.objects.filter(pk=pk).update(views=F('views')+1)
    # return HttpResponseRedirect(request.GET.get('next')))
    return ''


def meetup_add_comments(request, pk):
    meetup = get_object_or_404(Meetup, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.meetup = meetup
            comment.save()
            return redirect('meetup.views.meetup_detail', pk=meetup.pk)
    else:
        form = CommentForm()
    return render(request, 'meetup_add_comments.html', {'form': form})