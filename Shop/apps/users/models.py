from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserProfile(AbstractUser):
    """
    用户
    """
    MALE = 0
    FAMALE = 1
    GENDER_CHOISE = (
        (MALE, '男'),
        (FAMALE, '女')
    )
    name = models.CharField(max_length=64, null=True, blank=True, verbose_name='用户名')
    birthday = models.DateField(null=True, blank=True, verbose_name='出生年月')
    mobile = models.CharField(max_length=11, verbose_name='手机号')
    gender = models.IntegerField(choices=GENDER_CHOISE, verbose_name='性别', default=MALE)
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def __str__(self):
        return self.name


class UserAddress(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    district = models.CharField(max_length=100, default="", verbose_name="区域")
    signer_name = models.CharField(max_length=30, verbose_name='姓名')
    signer_mobile = models.CharField(max_length=11, verbose_name='手机号')
    address = models.CharField(max_length=100, verbose_name='地址')
    default = models.BooleanField(default=False, verbose_name='默认')

    class Meta:
        verbose_name_plural = verbose_name = '用户地址'

    def __str__(self):
        return "{}-{}-{}".format(self.signer_name, self.signer_mobile, self.address)


class VerifyCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(max_length=10, verbose_name='验证码')
    mobile = models.CharField(max_length=11, verbose_name='手机号')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')