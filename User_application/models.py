from django.db import models


# Model related to user
class User_info(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False, default="user")
    Phone = models.IntegerField(
        blank=False, null=False, default="00000000", unique=True
    )
    mail = models.EmailField(
        blank=False, null=False, unique=True, default="user@gmail.com"
    )
    age = models.IntegerChoices(max_length=3, blank=True, null=True)

    class Gender(models.TextChoices):
        MEN = "Men"
        WOMEN = "Women"
        TRANSGENDER = "Transgender"

    gender = models.CharField(choices=Gender.choices, max_length=20)
