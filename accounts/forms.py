from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions

from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={ #field arguments들을 넣는다. HTML에 보여지는 태그의 속성 정의
            'class': 'form-control',
            'placeholder': 'Email',
            'required': 'True',
        } # 이렇게 변환된다. <input type="email" class="form-control" placeholder="Email" required="True"/>
    ))
    username = forms.RegexField(label="Username", max_length=30,
        regex=r'^[\w.@+-]+$',
        help_text="Required. 30 characters or fewer. Letters, digits and "
                    "@/./+/-/_ only.",
        error_messages={
            'invalid': "This value may contain only letters, numbers and "
                         "@/./+/-/_ characters."},
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'required': 'true',
        }))
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'required': 'True',
            }
        )
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password confirmation',
                'required': 'True',
            }
        ),
        help_text="Enter the same password as above, for verification."
    )
    # avatar = forms.ImageField()

    class Meta:
        model = UserProfile
        fields = ("username", "email", "password1", "password2", "avatar", "nickname") # 작성한 필드만큼 화면에 보여짐

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']

        try:
            w, h = get_image_dimensions(avatar)

            #validate dimensions
            max_width = max_height = 100
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                     '%s x %s pixels or smaller.' % (max_width, max_height))

            #validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                    'GIF or PNG image.')

            #validate file size
            if len(avatar) > (20 * 1024):
                raise forms.ValidationError(
                    u'Avatar file size may not exceed 20k.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass

        return avatar


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={ #field arguments들을 넣는다. HTML에 보여지는 태그의 속성 정의
            'class': 'form-control',
            'placeholder': 'Email',
            'required': 'True',
        } # 이렇게 변환된다. <input type="email" class="form-control" placeholder="Email" required="True"/>
    ))
    username = forms.RegexField(label="Username", max_length=30,
        regex=r'^[\w.@+-]+$',
        help_text="Required. 30 characters or fewer. Letters, digits and "
                    "@/./+/-/_ only.",
        error_messages={
            'invalid': "This value may contain only letters, numbers and "
                         "@/./+/-/_ characters."},
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'required': 'true',
        }))
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'required': 'True',
            }
        )
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password confirmation',
                'required': 'True',
            }
        ),
        help_text="Enter the same password as above, for verification."
    )

    class Meta: # SignupForm에 대한 기술서
        model = User
        fields = ("username", "email", "password1", "password2",) # 작성한 필드만큼 화면에 보여짐

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username',
                'required': 'True',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'required': 'True',
            }
        )
    )