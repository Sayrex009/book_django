from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=30)
    visited_at = models.DateTimeField(null=True)
    descriptions = models.CharField(max_length=255)
    img = models.ImageField()
    website_with = models.DateTimeField(null=True)

class Author(models.Model):
    full_name = models.CharField(max_length=30)
    descriptions = models.CharField(max_length=255)

class Category(models.Model):
    name = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=255)
    img = models.ImageField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='books')

class Comment(models.Model):
    rating = models.IntegerField()
    descriptions = models.CharField(max_length=255)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')  
