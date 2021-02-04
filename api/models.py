from django.db import models

# Create your models here.


class Book(models.Model):
    
    title = models.CharField(max_length=300)
    img = models.URLField()
    price = models.IntegerField()
    category = models.CharField(max_length=300) 

    def __str__(self):
        return self.title


class Comment(models.Model):
    pass 


class User(models.Model):
    pass 


class Cart(models.Model):
    pass 


class Student(models.Model):
    pass 