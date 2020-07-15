from django.db import models
from os.path import join


def get_upload_path(instance, filename):
    #  задаем название файла названием slug`а продукта
    filename = instance.slug + '.' + filename.split('.')[1]
    return join('images/', filename)


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    slug = models.SlugField(max_length=100, db_index=True, verbose_name='Слаг')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=get_upload_path, blank=True)

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['name']

    class Meta:
        ordering = ('name',)
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=100, db_index=True, verbose_name='Наименование товара')
    slug = models.SlugField(max_length=100, db_index=True, verbose_name='Слаг')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='Наличие')
    stock = models.PositiveIntegerField(verbose_name='В наличие штук')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    edited_at = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    image = models.ImageField(upload_to=get_upload_path, blank=True, verbose_name='Изображение')
    tags = models.ManyToManyField(Category, 'Теги')

    class Meta:
        ordering = ('name',)
        index_together =(('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Promotion(models.Model):
    proms = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, verbose_name='Товар',
                              related_name='promo')

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

    def __str__(self):
        return str(self.pk)