from django.db import models


class User():
    pass


class Category(models.Model):
    name = 
    slug =


class Genre(models.Model):
    name = 
    slug =


class Title(models.Model):
    name = 
    year = 
    description = 
    genre = 
    category =
    rating = 


class GenreTitle(models.Model):
    title =
    genre =


class Review(models.Model):
    title =
    text = 
    author =
    score = 
    pub_date =


class Comment(models.Model):
    review = 
    text = 
    author =
    pub_date =




