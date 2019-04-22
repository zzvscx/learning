from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model
from goods.models import Goods

User = get_user_model()
# Create your models here.

class UserFav(models.Model):
    """
    用户收藏
    """
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    good = models.ForeignKey(Goods, verbose_name='商品', on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name_plural = verbose_name = "用户收藏"

    def __str__(self):
        return self.user.name


class UserLevingMessage(models.Model):
    """
    用户留言
    """
    MESSAGE_TYPE = (
        (1, '留言'),
        (2, '投诉'),
        (3, '询问'),
        (4, '售后'),
        (5, '求购')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    msg_type = models.IntegerField(choices=MESSAGE_TYPE, verbose_name='留言类型')
    subject = models.CharField(default="", max_length=100, verbose_name="主题")
    message = models.TextField(default="", verbose_name="留言内容")
    file = models.FileField(verbose_name="上传的文件")
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name_plural = verbose_name = "用户留言"

    def __str__(self):
        return self.user.name