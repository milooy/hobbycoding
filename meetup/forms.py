# coding: utf-8

from __future__ import unicode_literals
from io import BytesIO
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from PIL import Image as pil
from django.utils import timezone
# from .models import Meetup, Comment
from .models import Meetup


class MeetupEditForm(forms.ModelForm):
    desc = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Meetup
        exclude = ('created_date', 'modified_date', )
        fields = ('title', 'desc', 'image_file', 'location', 'meetup_date', 'lat', 'lon', 'tags', )
        # fields = '__all__' #에러나서 추가함

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(MeetupEditForm, self).__init__(*args, **kwargs)

    def rescale(self, data, width, height, force=True):
        """
        Rescale the given image, optionally cropping it to make sure the result image has the specified width and height.
        https://djangosnippets.org/snippets/224/
        """
        max_width = width
        max_height = height

        input_file = BytesIO(data.read())
        img = pil.open(input_file)
        if not force:
            img.thumbnail((max_width, max_height), pil.ANTIALIAS)
        else:
            src_width, src_height = img.size
            src_ratio = float(src_width) / float(src_height)
            dst_width, dst_height = max_width, max_height
            dst_ratio = float(dst_width) / float(dst_height)

            print(src_width, src_height)
            print(src_ratio, dst_ratio)
            if dst_ratio < src_ratio:
                crop_height = src_height
                crop_width = crop_height * dst_ratio
                x_offset = int(src_width - crop_width) // 2
                y_offset = 0
            else:
                crop_width = src_width
                crop_height = crop_width / dst_ratio
                x_offset = 0
                y_offset = int(src_height - crop_height) // 3
            img = img.crop((x_offset, y_offset, x_offset+int(crop_width), y_offset+int(crop_height)))
            img = img.resize((dst_width, dst_height), pil.ANTIALIAS)

        image_file = BytesIO()
        img.save(image_file, 'JPEG')
        data.file = image_file
        return data

    def save(self, commit=True):
        instance = super(MeetupEditForm, self).save(commit=False)
        instance.author = self.request.user
        instance.published_date = timezone.now()

        if instance.image_file:
            instance.image_file = self.rescale(self.cleaned_data.get('image_file'), 600, 600, force=True)
        if commit:
            instance.save()
        return instance

