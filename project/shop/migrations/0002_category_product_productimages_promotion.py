# Generated by Django 3.0.7 on 2020-10-18 16:20

from django.db import migrations, models
import django.db.models.deletion
import shop.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название категории')),
                ('slug', models.SlugField(max_length=100, verbose_name='Слаг')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, upload_to=shop.models.get_upload_path)),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Наименование товара')),
                ('slug', models.SlugField(max_length=100, verbose_name='Слаг')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('available', models.BooleanField(default=True, verbose_name='Наличие')),
                ('stock', models.PositiveIntegerField(verbose_name='В наличие штук')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('edited_at', models.DateTimeField(auto_now=True, verbose_name='Изменено')),
                ('image', models.ImageField(blank=True, upload_to=shop.models.get_upload_path, verbose_name='Изображение')),
                ('tags', models.ManyToManyField(related_name='Теги', to='shop.Category')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ('name',),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proms', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='promo', to='shop.Category', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Акция',
                'verbose_name_plural': 'Акции',
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to=shop.models.get_upload_path, verbose_name='')),
                ('iproduct', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='shop.Product')),
            ],
            options={
                'verbose_name': 'Дополнительное изображение',
                'verbose_name_plural': 'Дополнительные изображения',
            },
        ),
    ]
