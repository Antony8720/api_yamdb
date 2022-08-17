from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    USER_ROLES = [
        (USER, 'User'),
        (MODERATOR, 'Moderator'),
        (ADMIN, 'Admin'),
    ]

    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=150,
        null=True,
        unique=True
    )
    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        max_length=254,
        unique=True
    )
    bio = models.TextField(
        verbose_name='О себе',
        null=True,
        blank=True
    )
    role = models.CharField(
        verbose_name='Роль',
        max_length=50,
        choices=USER_ROLES,
        default=USER
    )
    confirmation_code = models.TextField(
        verbose_name='Код подтверждения',
        blank=True,
        null=True
    )

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    class Meta:
        verbose_name = 'Пользователь'
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'], name='unique_user')
        ]


# class Category(models.Model):
#     name = 
#     slug =


# class Genre(models.Model):
#     name = 
#     slug =


# class Title(models.Model):
#     name = 
#     year = 
#     description = 
#     genre = 
#     category =
#     rating = 


# class GenreTitle(models.Model):
#     title =
#     genre =


# class Review(models.Model):
#     title =
#     text = 
#     author =
#     score = 
#     pub_date =


# class Comment(models.Model):
#     review = 
#     text = 
#     author =
#     pub_date =




