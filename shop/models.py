from django.db import models
from django.urls import reverse


class Category(models.Model):

    name = models.CharField(max_length=50)

    slug = models.SlugField(
        max_length=50,
        unique=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Катогории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'shop:product_list_by_category',
            args=[self.slug]
        )


class Product(models.Model):

    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70)

    image = models.ImageField(
        upload_to='products/',
        blank=True,
        verbose_name='Изображение'
    )

    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'shop:product_detail',
            args=[self.id, self.slug]
        )


class Article(models.Model):

    name = models.CharField(max_length=70, verbose_name='Заголовок статьи')
    text = models.CharField(max_length=1000, verbose_name='Текст статьи')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создана')
    image = models.ImageField(
        upload_to='articles/',
        blank=True,
        verbose_name='Изображение'
    )
    products = models.ManyToManyField(
        Product,
        related_name='products'
    )

    class Meta:
        ordering = ('created',)
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.name
