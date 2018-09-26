from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from users.forms import UserLoginForm


# 创建普通管理员
def create_user(request):
    # password1 = 'jiao123456'
    # # 对用户密码加密，make_password()是加密方法, 创建用户密码
    # password = make_password(password1)
    # Users.objects.create(username='jiaogege', password=password)

    User.objects.create_user(username='jiaogege', password='123456')

    return HttpResponse('创建用户成功！！！')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        # 1. 表单验证
        form = UserLoginForm(request.POST)
        # 使用is_valid()：进行表单验证
        if form.is_valid():
            # form表单验证成功
            user = auth.authenticate(username=form.cleaned_data['username'],
                             password=form.cleaned_data['password'])
            if user:
                # 如果通过username和password获取到user对象，则进行登录。
                # request.user默认AnonyMouseUser
                auth.login(request, user)
                return HttpResponseRedirect(reverse('users:index'))
            else:
                # 用户名和密码
                return render(request, 'login.html')

        # 2.auth模块验证
        # 3.auth.login验证
        else:
            # form表单验证失败， 返回错误信息。
            return render(request, 'login.html', {'form': form})


# 连接首页方法
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')


# 注销方法
def logout(request):
    if request.method == 'GET':
        # 注销
        auth.logout(request)
        return HttpResponseRedirect(reverse('users:login'))
