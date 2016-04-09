from django.conf import settings
from django.db import models
from django.utils import timezone


# 태그
class TagModel(models.Model):
    title = models.CharField(max_length=20, verbose_name=u'태그')


# 밋업
class Meetup(models.Model):
    # 관계
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'주최자', related_name='my_meetup')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=u'관심', blank=True, related_name='likes')

    # 정보
    title = models.CharField(u'제목', max_length=200)
    desc = models.TextField(u'설명')
    image_file = models.ImageField(u'썸네일', upload_to='%Y/%m/%d')
    created_date = models.DateTimeField(u'생성일', default=timezone.now)
    modified_date = models.DateTimeField(u'수정일', blank=True, null=True)

    def modify(self):
        self.modified_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


# 댓글
class Comment(models.Model):
    meetup = models.ForeignKey(Meetup, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'이름', related_name='comments_author')
    text = models.TextField(u'댓글', max_length=2000)
    created_date = models.DateTimeField(u'생성일', default=timezone.now)

    def __str__(self):
        return self.text