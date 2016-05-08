from django.db import models
from django.conf import settings
from meetup.models import Meetup
from django.utils import timezone


class Comment(models.Model):
	class Meta:
		ordering = ["-created_date"]

	meetup = models.ForeignKey(Meetup, verbose_name=u'밋업', related_name='comments')
	author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'이름', related_name='comment_author')
	text = models.TextField(u'댓글', max_length=2000)
	created_date = models.DateTimeField(u'생성일', default=timezone.now)

	def __str__(self):
		return self.text

