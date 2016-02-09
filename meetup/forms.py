# coding: utf-8

from __future__ import unicode_literals
from django import forms
from .models import Meetup


class MeetupEditForm(forms.ModelForm):
    class Meta:
        model = Meetup
        exclude = ('created_date', 'modified_date', )
        fields = ('title', 'desc', 'image_file', )
        # fields = '__all__' #에러나서 추가함
