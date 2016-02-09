from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm

from .forms import SignupForm

# def signup(request):
#     # 사용자가 입력한 값 들어간 포스트
#     if request.method == "POST":
#         # 사용자가 입력한 값을 넣고 userform객체 만든다
#         userform = UserCreationForm(request.POST)
#         if userform.is_valid(): # 사용자 입력 값 validation
#             userform.save()
#             return HttpResponseRedirect( # 저장 후 페이지 리다이렉트
#                 reverse("signup_ok")
#             )
#
#     # 걍 온 GET
#     elif request.method == "GET":
#         # UserCreationForm 클래스를 이용해 userform이라는 객체를 만들어라 그리고 request로 template에 보냄
#         userform = UserCreationForm()
#         return render(request, "accounts/signup.html", {
#             "userform": userform,
#         })

def signup(request):
    signupform = SignupForm()
    # 사용자가 입력한 값 들어간 포스트
    if request.method == "POST":
        # 사용자가 입력한 값을 넣고 userform객체 만든다
        signupform = SignupForm(request.POST)
        if signupform.is_valid():# 사용자 입력 값 validation
            user = signupform.save(commit=False)
            user.email = signupform.cleaned_data['email']
            user.save()

            return HttpResponseRedirect( # 저장 후 페이지 리다이렉트
                reverse("signup_ok")
            )

    return render(request, "signup.html", {
        "signupform": signupform,
    })
