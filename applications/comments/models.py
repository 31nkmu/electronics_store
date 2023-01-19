from django.contrib.auth import get_user_model
from django.db import models

from applications.electronics.models import Electronic

User = get_user_model()


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    electronic = models.ForeignKey(Electronic, on_delete=models.CASCADE, related_name='comments')
