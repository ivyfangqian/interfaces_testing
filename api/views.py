# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from models import User
import json


# Create your views here.

def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'firstpage.html', dictionary={"username": "amdin"})


def signup(request):
    return render(request, 'signup.html')


def check_username(request):
    return JsonResponse({"valid": True})


def api_login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    print username, password

    if username is None or username == "":
        return HttpResponse(content_type="application/json", content=json.dumps({"flag": 1, "msg": "用户名不能为空"}))
    if password is None or password == "":
        return HttpResponse(content_type="application/json", content=json.dumps({"flag": 1, "msg": "密码不能为空"}))
    if len(username) not in range(5, 13):
        return HttpResponse(content_type="application/json", content=json.dumps({"flag": 1, "msg": "用户名长度为5-12位"}))
    if len(password) not in range(6, 19):
        return HttpResponse(content_type="application/json", content=json.dumps({"flag": 1, "msg": "密码长度为6-18位"}))
    user = User.objects.filter(username=username, password=password)
    if not user.exists():
        return HttpResponse(content_type="application/json", content=json.dumps({"flag": 1, "msg": "用户名或密码错误"}))
    else:
        return HttpResponse(content_type="application/json",
                            content=json.dumps(
                                {"flag": 0, "msg": "登录成功", "userid": user.get("id"), "username": user.get("username")}))
