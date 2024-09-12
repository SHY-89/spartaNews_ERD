from django.db import models
from accounts.models import User

# Create your models here.
class Category(models.Model):
    subject= models.CharField(max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)

class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    url = models.URLField()
    vote = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="new"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

    favorite = models.ManyToManyField(
        User,
        related_name="nfavorite"
    )

class Comment(models.Model):
    content = models.TextField()
    collaborate = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    article = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
    )