from django.conf import settings
from django.db import models
from django.utils import timezone


class Meetup(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    image_file = models.ImageField(upload_to='%Y/%m/%d')
    created_date = models.DateTimeField(
        default=timezone.now)
    modified_date = models.DateTimeField(
        blank=True, null=True)

    def modify(self):
        self.modified_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
