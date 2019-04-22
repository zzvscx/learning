from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.
class GoodsCategory(models.Model):
    """
    商品类型
    """
    CATEGORY_TYPE = (
        (1, '一级类目'),
        (2, '二级类目'),
        (3, '三级类目'),
    )
    name = models.CharField(max_length=30, verbose_name='类别名', help_text="类别名")
    code = models.CharField(default="", max_length=30, verbose_name='类别代码')
    desc = models.TextField(default="", verbose_name="类别描述", help_text="类别描述")
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name=u'类目级别', help_text="类目级别")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name=u"父类别", on_delete=models.CASCADE,
                                        related_name="sub_cat")
    is_tab = models.BooleanField(default=False, verbose_name="是否导航")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name_plural = verbose_name = "商品类别"

    def __str__(self):
        return self.name


class GoodsCategoryBrand(models.Model):
    """
    品牌名
    """
    name = models.CharField(max_length=20, verbose_name=u'品牌名')
    desc = models.TextField(default="", verbose_name='品牌描述')
    image = models.ImageField(upload_to="brand/")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name_plural = verbose_name = "品牌"

    def __str__(self):
        return self.name

class Goods(models.Model):
    """
    商品
    """
    category = models.ForeignKey(GoodsCategory, null=True, blank=True, verbose_name='商品类别',
                                 on_delete=models.SET_NULL)
    goods_sn = models.CharField(max_length=50, unique=True, verbose_name=u'商品唯一货号')
    name = models.CharField(max_length=300, verbose_name='商品名')
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    sold_num = models.IntegerField(default=0, verbose_name='销量')
    # fav_num = models.IntegerField(default=0, 收藏数)
    goods_num = models.IntegerField(default=0, verbose_name='库存')
    market_price = models.FloatField(default=99999, verbose_name='市场价')
    shop_price = models.FloatField(default=99999, verbose_name='售价')
    goods_brief = models.TextField(max_length=500, verbose_name='商品简述')
    goods_desc = UEditorField(verbose_name='商品描述', imagePath="goods/images/", width=1000, height=300,
                              filePath="goods/files/", default="")

    ship_free = models.IntegerField(default=99999, verbose_name=u'邮费')
    good_front_image = models.ImageField(upload_to="front_image", null=True, blank=True, verbose_name='封面图')
    is_hot = models.BooleanField(default=False, verbose_name='是否热销')
    is_new = models.BooleanField(default=False, verbose_name='是否新品')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name_plural = verbose_name = "商品"

    def __str__(self):
        return self.name


class GoodsImage(models.Model):
    """
    商品图片
    """
    good = models.ForeignKey(Goods, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="goodsImage/")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name_plural = verbose_name = "商品图片"

    def __str__(self):
        return self.good.name


class Banner(models.Model):
    """
    轮播的商品
    """
    goods = models.ForeignKey(Goods, verbose_name="商品", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="banner/", verbose_name="轮播图")
    index = models.IntegerField(default=0, verbose_name='轮播顺序')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name_plural = verbose_name = "轮播图"

    def __str__(self):
        return self.good.name