from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    id = models.AutoField("id", primary_key=True)
    name = models.CharField("name", max_length=20, unique=True)
    created_str = models.DateTimeField("created at", default=timezone.now)
    name2 = models.CharField("name", max_length=20)