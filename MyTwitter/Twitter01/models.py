from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    content = models.CharField(max_length=140)
    creation_date = models.DateField(auto_now_add=True)
    dependence = models.ForeignKey(User, on_delete=models.CASCADE)


