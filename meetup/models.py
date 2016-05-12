from django.conf import settings
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager


# 밋업
class Meetup(models.Model):
    class Meta:
        verbose_name = u'밋업'
        verbose_name_plural = verbose_name
        ordering = ["-created_date"]

    # 관계
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'주최자', related_name='my_meetup')
    join_users = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=u'참석', blank=True, related_name='join_meetup')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=u'관심', blank=True, related_name='like_meetup')
    tags = TaggableManager()

    # 정보
    title = models.CharField(u'제목', max_length=200)
    desc = models.TextField(u'설명')
    image_file = models.ImageField(u'썸네일', upload_to='%Y/%m/%d', blank=True, null=True)
    created_date = models.DateTimeField(u'생성일', default=timezone.now)
    modified_date = models.DateTimeField(u'수정일', blank=True, null=True)
    location = models.CharField(u'장소 이름', max_length=50)
    lon = models.FloatField(u'경도', blank=True, null=True)
    lat = models.FloatField(u'위도', blank=True, null=True)

    def modify(self):
        self.modified_date = timezone.now()
        self.save()

    def image_url(self):
        if self.image_file and hasattr(self.image_file, 'url'):
            return self.image_file.url
        else:
            return '/static/img/meetup_default.jpg'

    def __str__(self):
        return self.title
