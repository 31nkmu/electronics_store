from django.contrib.auth import get_user_model
from django.db import models

from applications.electronics.models import Electronic

User = get_user_model()


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    electronic = models.ForeignKey(Electronic, on_delete=models.CASCADE, related_name='favorites')
    is_favorite = models.BooleanField(default=False)