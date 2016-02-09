from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(verbose_name=u'별명', max_length=50, blank=True,)
    avatar = models.ImageField(upload_to='media/avatar/', blank=True, null=True) # TODO: 이거 앞에 media 꼭 써줘야하나
