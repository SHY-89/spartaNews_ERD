from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    first_name = None
    last_name = None
    created_at = models.DateTimeField(auto_now_add=True)
    karma = models.PositiveIntegerField(default=1)
    introduction = models.TextField(null=True)

    def __str__(self):
        return self.username