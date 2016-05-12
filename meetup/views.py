from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import Http404
from django.utils import timezone
from django.views.generic import ListView, FormView

from meetup.mixins import FilterMixin
from .models import Meetup
# from .forms import MeetupEditForm, CommentForm
from .forms import MeetupEditForm
from django.shortcuts import render, get_object_or_404, redirect
import django_filters


class MeetupFilter(django_filters.FilterSet):
    query = django_filters.MethodFilter()

    class Meta:
        model = Meetup
        fields = ['query']

    def filter_query(self, queryset, value):
        return queryset.filter(
            Q(title__contains=value) |
            Q(tags__name__contains=value)
        ).distinct()


class MeetupListView(ListView, FilterMixin):
    """
        Refer: https://github.com/carltongibson/django-filter/issues/245
    """
    model = Meetup
    template_name = 'meetup_list.html'
    paginate_by = 10
    context_object_name = 'meetup_list'

    filter_class = MeetupFilter

    def get_queryset(self, *args, **kwargs):
        qs = super(MeetupListView, self).get_queryset(*args, **kwargs)
        return self.get_filter_class()(self.request.GET, queryset=qs)

    def paginate_queryset(self, queryset, page_size):
        try:
            return super(MeetupListView, self).paginate_queryset(queryset, page_size)
        except EmptyPage:
            raise Http404


# TODO: comment 폼을 여기서 분리하고 싶은데..
def meetup_detail(request, pk):
    meetup = get_object_or_404(Meetup, pk=pk)
    return render(request, 'meetup_detail.html', {'meetup': meetup})


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


# def meetup_edit(request, pk):
#     meetup = get_object_or_404(Meetup, pk=pk)
#     if request.method == 'GET':
#         form = MeetupEditForm()
#     elif request.method == 'POST':
#         form = MeetupEditForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             new_meetup = form.save(commit=False)
#             new_meetup.author = request.user
#             new_meetup.published_date = timezone.now()
#             new_meetup.save()
#             return redirect(reverse('meetup_detail', kwargs={'pk':new_meetup.pk}))
#
#     return render(request, 'meetup_edit.html', {'form': form})


class MeetupFormView(FormView):
    template_name = "meetup_edit.html"
    form_class = MeetupEditForm

    def get_success_url(self):
        # return reverse('meetup_detail', kwargs={'pk':new_meetup.pk})
        return reverse('meetup_list')

    def form_valid(self, form):
        print("Form is valid")
        new_meetup = form.save(commit=False)
        new_meetup.author = self.request.user
        new_meetup.published_date = timezone.now()
        new_meetup.save()
        form.save_m2m() # 태그 저장
        return super(MeetupFormView, self).form_valid(form)


# def meetup_join(request, pk):
#     Meetup.objects.filter(pk=pk).update(views=F('views')+1)
#     # return HttpResponseRedirect(request.GET.get('next')))
#     return ''


def meetup_like(request, pk):
    meetup = get_object_or_404(Meetup, pk=pk) # TODO: 이렇게 밋업 가져오는걸 매번 메서드마다 해야하나
    if request.user in meetup.like_users.all():
        meetup.like_users.remove(request.user)
    else:
        meetup.like_users.add(request.user)
    return redirect('meetup.views.meetup_detail', pk=pk)

def meetup_join(request, pk):
    meetup = get_object_or_404(Meetup, pk=pk) # TODO: 이렇게 밋업 가져오는걸 매번 메서드마다 해야하나
    if request.user in meetup.join_users.all():
        meetup.join_users.remove(request.user)
    else:
        meetup.join_users.add(request.user)
    return redirect('meetup.views.meetup_detail', pk=pk)



