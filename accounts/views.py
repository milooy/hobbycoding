from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm

from .forms import SignupForm


def signup(request):
    signupform = SignupForm()
    # 사용자가 입력한 값 들어간 포스트
    if request.method == "POST":
        # 사용자가 입력한 값을 넣고 userform객체 만든다
        signupform = SignupForm(request.POST, request.FILES)
        if signupform.is_valid():
            user = signupform.save(commit=False)
            user.email = signupform.cleaned_data['email']
            user.avatar = signupform.clean_avatar()
            user.save()

            print("이이이잉")

            return HttpResponseRedirect( # 저장 후 페이지 리다이렉트
                reverse("signup_ok")
            )

    return render(request, "signup.html", {
        "signupform": signupform,
    })
