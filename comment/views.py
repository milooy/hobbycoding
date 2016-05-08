from base64 import b64decode

from django.contrib import messages
from django.core.files.base import ContentFile
from django.core.paginator import EmptyPage
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from django.http import Http404
from django.views.generic import ListView
from django.views.generic.edit import FormMixin, FormView
from django.utils import timezone
from meetup.models import Meetup
from .models import Comment
from .forms import CommentForm


class CommentView(FormMixin, ListView):
	template_name = '_comment_list.html'
	form_class = CommentForm
	model = Comment
	paginate_by = 5
	context_object_name = "comment_list"

	def get_queryset(self):
		meetup = get_object_or_404(Meetup, pk=self.kwargs['pk'])
		queryset = meetup.comments.all()
		return queryset

	def paginate_queryset(self, queryset, page_size):
		try:
			return super(CommentView, self).paginate_queryset(queryset, page_size)
		except EmptyPage:
			raise Http404

	def get(self, request, *args, **kwargs):
		pk = self.kwargs['pk']

		# From ProcessFormMixin
		form_class = self.get_form_class()
		self.form = self.get_form(form_class)

		# From BaseListView
		self.object_list = self.get_queryset()
		allow_empty = self.get_allow_empty()
		if not allow_empty and len(self.object_list) == 0:
			raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
						  % {'class_name': self.__class__.__name__})

		context = self.get_context_data(object_list=self.object_list, form=self.form)
		context['meetup'] = get_object_or_404(Meetup, pk=pk)
		return self.render_to_response(context)

	def post(self, request, *args, **kwargs):
		meetup = get_object_or_404(Meetup, pk=self.kwargs['pk'])

		if not request.user.is_authenticated():
			print("login하세여")
		form = self.get_form()
		print("폼은 이러하다", form)
		if form.is_valid():
			print("폼은 밸리드하다", form)
			comment_form = form.save(commit=False)
			comment_form.meetup = meetup
			comment_form.author = request.user
			comment_form.created_date = timezone.now()
			print("폼은 밸리드하다2", comment_form)
			comment_form.save()
			form.save(self.request)
		else:
			print("에러났어요~~~")
			messages.error(request, u'폼 잘좀 넣어줭')
		return self.get(request, *args, **kwargs)
