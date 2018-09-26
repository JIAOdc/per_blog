
from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=10, verbose_name='账号')
    password = models.CharField(max_length=255, verbose_name='密码')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    operate_time = models.DateTimeField(auto_now=True, verbose_name='上一次修改时间')

    class Meta:
        db_table = 'User_manage'
