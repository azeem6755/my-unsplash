from django.db import models
from user.models import Profile

# Create your models here.


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
