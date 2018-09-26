from django.conf.urls import url

from django.contrib.auth.decorators import login_required
from users import views

urlpatterns = [
    url(r'^create_user/', views.create_user, name='create_user'),
    url(r'^login/', views.login, name='login'),
    # 登录后可以看到的页面，用Django自带login_required()方法，该方法就是一个装饰器
    url(r'^index/', login_required(views.index), name='index'),
    url(r'^logout/', views.logout, name='logout'),

]