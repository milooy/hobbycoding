from urllib.request import urlopen
from uuid import uuid4

from django.core.files.base import ContentFile
from django.shortcuts import render_to_response
from social.pipeline.partial import partial
from social.utils import slugify, module_member

# USER_FIELDS = ['username', 'email']
from accounts.models import MyUser

USER_FIELDS = ['email', 'nickname']


@partial
def create_nickname(backend, details, response, is_new=False, *args, **kwargs):
    print("create nickname~~~!!!!!")
    print(backend.name)
    if backend.name == 'facebook' and is_new:
        data = backend.strategy.request_data()
        print(data)
        print(response['name'])
        if data.get('nickname') is None:
            # New user and didn't pick a character name yet, so we render
            # and send a form to pick one. The form must do a POST/GET
            # request to the same URL (/complete/battlenet-oauth2/). In this
            # example we expect the user option under the key:
            #   character_name
            # you have to filter the result list according to your needs.
            # In this example, only guild members are allowed to sign up.
            fb_data = {
                'city': response['location']['name'],
                'gender': response['gender'],
                'locale': response['locale'],
            }
            return render_to_response('create_nickname.html', {'fb_data': fb_data, })
        else:
            # The user selected a character name
            return {'nickname': data.get('nickname')}


def create_user(strategy, details, user=None, *args, **kwargs):
    print(details)
    print(kwargs)
    if user:
        return {'is_new': False}

    # fields = dict((name, kwargs.get(name) or details.get(name))
    #               for name in strategy.setting('USER_FIELDS',
    #                                            USER_FIELDS))
    fields = {'email': details.get('email'), 'nickname': details.get('username')}

    if not fields:
        return

    return {
        'is_new': True,
        'user': strategy.create_user(**fields)
    }


def update_avatar(backend, response, uid, user, *args, **kwargs):
    email = kwargs['details']['email']

    if backend.name == 'facebook':
        url = "http://graph.facebook.com/%s/picture?type=large" % response['id']
        avatar = urlopen(url)
        # profile = user.get_profile()
        # user = MyUser.objects.get(email=email)
        print(user)
        user.avatar.save(slugify(user.email + " social") + '.jpg', ContentFile(avatar.read()))
        user.save()
