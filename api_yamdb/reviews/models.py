from django.db import models

from django.db.models import IntegerField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator

from datetime import datetime

CURRENT_YEAR = datetime.now().year


User = get_user_model()


#class User():
#    pass


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя Категории')
    slug = models.SlugField(unique=True, verbose_name='Слаг')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Genre(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя Жанра')
    slug = models.SlugField(unique=True, verbose_name='Слаг')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'



class Title(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    year = models.IntegerField(
        validators=[MaxValueValidator(
            CURRENT_YEAR,
            message='Год не может быть больше текущего года')])
    description = models.TextField()
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        verbose_name='жанр',
    )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True)
    rating = models.IntegerField(null=True)


class Review(models.Model):
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews'
    )
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews'
    )
    score = IntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
     )
    pub_date = models.DateTimeField(
        'Дата публикации отзыва', auto_now_add=True
    )


class Comment(models.Model):
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments'
    )
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    pub_date = models.DateTimeField(
        'Дата публикации комментария', auto_now_add=True
    )