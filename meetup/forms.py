# coding: utf-8

from __future__ import unicode_literals
from django import forms
# from .models import Meetup, Comment
from .models import Meetup


class MeetupEditForm(forms.ModelForm):
    class Meta:
        model = Meetup
        exclude = ('created_date', 'modified_date', )
        fields = ('title', 'desc', 'image_file', 'location', 'meetup_date', 'lat', 'lon', 'tags', )
        # fields = '__all__' #에러나서 추가함


# class CommentForm2(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('text',)
#
#
# class CommentForm(forms.Form):
#     name = forms.CharField()
#     message = forms.CharField(widget=forms.Textarea)
#
#     def send_email(self):
#         # send email using the self.cleaned_data dictionary
#         pass