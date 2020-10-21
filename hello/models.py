from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    public = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now_add = True)



class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateField()