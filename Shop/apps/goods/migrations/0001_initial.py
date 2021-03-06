# Generated by Django 2.2 on 2019-04-22 14:26

import DjangoUeditor.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_sn', models.CharField(max_length=50, unique=True, verbose_name='商品唯一货号')),
                ('name', models.CharField(max_length=300, verbose_name='商品名')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击数')),
                ('sold_num', models.IntegerField(default=0, verbose_name='销量')),
                ('goods_num', models.IntegerField(default=0, verbose_name='库存')),
                ('market_price', models.FloatField(default=99999, verbose_name='市场价')),
                ('shop_price', models.FloatField(default=99999, verbose_name='售价')),
                ('goods_brief', models.TextField(max_length=500, verbose_name='商品简述')),
                ('goods_desc', DjangoUeditor.models.UEditorField(default='', verbose_name='商品描述')),
                ('ship_free', models.IntegerField(default=99999, verbose_name='邮费')),
                ('good_front_image', models.ImageField(blank=True, null=True, upload_to='front_image', verbose_name='封面图')),
                ('is_hot', models.BooleanField(default=False, verbose_name='是否热销')),
                ('is_new', models.BooleanField(default=False, verbose_name='是否新品')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
            },
        ),
        migrations.CreateModel(
            name='GoodsCategoryBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='品牌名')),
                ('desc', models.TextField(default='', verbose_name='品牌描述')),
                ('image', models.ImageField(upload_to='brand/')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '品牌',
                'verbose_name_plural': '品牌',
            },
        ),
        migrations.CreateModel(
            name='GoodsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='goodsImage/')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods')),
            ],
            options={
                'verbose_name': '商品图片',
                'verbose_name_plural': '商品图片',
            },
        ),
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='类别名', max_length=30, verbose_name='类别名')),
                ('code', models.CharField(default='', max_length=30, verbose_name='类别代码')),
                ('desc', models.TextField(default='', help_text='类别描述', verbose_name='类别描述')),
                ('category_type', models.IntegerField(choices=[(1, '一级类目'), (2, '二级类目'), (3, '三级类目')], help_text='类目级别', verbose_name='类目级别')),
                ('is_tab', models.BooleanField(default=False, verbose_name='是否导航')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_cat', to='goods.GoodsCategory', verbose_name='父类别')),
            ],
            options={
                'verbose_name': '商品类别',
                'verbose_name_plural': '商品类别',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='goods.GoodsCategory', verbose_name='商品类别'),
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='banner/', verbose_name='轮播图')),
                ('index', models.IntegerField(default=0, verbose_name='轮播顺序')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='商品')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
            },
        ),
    ]
