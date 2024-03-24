from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg


# Create your models here.
class Meal(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.title


class Rating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=(MinValueValidator(1), MaxValueValidator(5)))

    def __str__(self):
        return f"{self.meal}-{self.stars} "

    class Meta:
        unique_together = (("user", "meal"),)
        index_together = (("user", "meal"),)
