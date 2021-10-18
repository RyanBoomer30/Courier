from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class User(AbstractUser):
    pass

class Member(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="user")
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    contents = models.ManyToManyField('Article', related_name="content", blank=True)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} is an admin: {self.admin}"

class Article(models.Model):
    articleName = models.CharField(max_length=100)
    articleContent = RichTextField()
    # articleContent = models.TextField()
    articleCatagory = models.CharField(max_length=10)
    writer = models.ForeignKey('Member', on_delete=models.CASCADE, related_name="writer")
    image = models.ImageField()
    imageCredit = models.CharField(max_length=100)
    createdTime = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return f"{self.articleName} written by {self.writer.name}"