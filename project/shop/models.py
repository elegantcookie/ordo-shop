from django.db import models
from os.path import join
from django.shortcuts import reverse
from django.template.defaultfilters import slugify as django_slugify


alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}


def slugify(s):
    """
    Overriding django slugify that allows to use russian words as well.
    """
    return django_slugify(''.join(alphabet.get(w, w) for w in s[0].lower()))


def get_upload_path(instance, filename):
    filename = slugify(filename.split('.'[0])) + '.' + filename.split('.')[1]
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

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id])


class ProductImages(models.Model):
    iproduct = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_upload_path, blank=True, verbose_name='')

    class Meta:
        verbose_name = 'Дополнительное изображение'
        verbose_name_plural = 'Дополнительные изображения'

    def __str__(self):
        return ''


class Promotion(models.Model):
    proms = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, verbose_name='Товар',
                              related_name='promo')

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

    def __str__(self):
        return str(self.pk)