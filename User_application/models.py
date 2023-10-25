from django.db import models


# Model related to user
class User_info(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False, default="user")
    phone = models.CharField(
        max_length=15, blank=False, null=False, default="0000000000", unique=True
    )
    mail = models.EmailField(
        blank=False, null=False, unique=True, default="user@gmail.com"
    )
    age = models.IntegerField(blank=True, null=True)

    class Gender(models.TextChoices):
        MEN = "Men"
        WOMEN = "Women"
        TRANSGENDER = "Transgender"

    gender = models.CharField(choices=Gender.choices, max_length=20)
    created_time = models.DateTimeField(auto_now_add=True)
