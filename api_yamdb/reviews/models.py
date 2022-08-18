from django.db import models
from django.core.validators import MaxValueValidator

from datetime import datetime

CURRENT_YEAR = datetime.now().year


class User():
    pass


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

#
# class Review(models.Model):
#     title =
#     text =
#     author =
#     score =
#     pub_date =
#
#
# class Comment(models.Model):
#     review =
#     text =
#     author =
#     pub_date =
