from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from applications.electronics.models import Electronic

User = get_user_model()


# class Rating(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
#     electronic = models.ForeignKey(Electronic, on_delete=models.CASCADE, related_name='ratings')
#     rating = models.PositiveSmallIntegerField(
#         validators=[
#             MinValueValidator(0),
#             MaxValueValidator(5)
#         ], blank=True, null=True
#     )

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    electronic = models.ForeignKey(Electronic, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ], blank=True, null=True
    )