from django.db import models
from accounts.models import User

# Create your models here.
class Category(models.Model):
    subject= models.CharField(max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")

    favorite = models.ManyToManyField(User, related_name="articles_favo")
    vote = models.ManyToManyField(User, related_name="articles_vote")

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments_user" )
    article  = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments_aticle" )
    #대댓글
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True )

    favorite = models.ManyToManyField(User, related_name="comments_favo")
    vote = models.ManyToManyField(User, related_name="comments_vote")

    def __str__(self):
        return self.content