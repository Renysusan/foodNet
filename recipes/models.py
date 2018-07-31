from django.conf import settings
from django.urls import reverse
from django.db import models

import misaka

from cuisines.models import Cuisine

from django.contrib.auth import get_user_model
User = get_user_model()


class Recipe(models.Model):
    user = models.ForeignKey(User, related_name="recipes", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    dish_title = models.CharField(max_length=255)
    dish_image = models.FileField(upload_to='images/')
    cooking_time = models.CharField(max_length=50)
    method = models.TextField()
    method_html = models.TextField(editable=False)
    votes_total = models.IntegerField(default=1)
    cuisine = models.ForeignKey(Cuisine, related_name="recipes",null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.method

    def save(self, *args, **kwargs):
        self.method_html = misaka.html(self.method)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "recipes:single",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["user", "method"]
