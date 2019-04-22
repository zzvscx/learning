from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from goods.models import Goods
User = get_user_model()
# Create your models here.

class ShoppingCart(models.Model):
    """
    购物车
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    good = models.ForeignKey(Goods, on_delete=models.CASCADE)
    good_num = models.IntegerField(default=1,)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name_plural = verbose_name = "购物车"

    def __str__(self):
        return "{} ×{}".format(self.good.name, self.goods_num)


class OrderInfo(models.Model):
    """
    订单
    """
    WAIT = 0
    CANCEL = 1
    SUCCESS = 2
    ORDER_STATUS = (
        (WAIT, '等待付款'),
        (CANCEL, '取消付款'),
        (SUCCESS, '付款成功'),
    )

    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    order_sn= models.CharField(max_length=30, unique=True, verbose_name='订单号')
    trade_no = models.CharField(max_length=100, unique=True, null=True, blank=True)
    pay_status = models.IntegerField(choices=ORDER_STATUS, verbose_name='订单状态')
    order_mount = models.FloatField(default=0.0, verbose_name='订单金额')
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name='支付时间')
    signer_name = models.CharField(max_length=30, verbose_name='姓名')
    signer_mobile = models.CharField(max_length=11, verbose_name='手机号')
    address = models.CharField(max_length=100, verbose_name='地址')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name_plural = verbose_name = "订单信息"

    def __str__(self):
        return self.order_sn


class OrderGoods(models.Model):
    """
    订单的商品详情
    """
    order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE)
    good = models.ForeignKey(Goods, on_delete=models.CASCADE)
    good_num = models.IntegerField(default=0, verbose_name='商品数量')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name_plural = verbose_name = "订单商品"

    def __str__(self):
        return self.order.order_sn