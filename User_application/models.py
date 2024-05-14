from django.db import models

# Create your models here.


class User_info(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False, default="user")
    phone = models.CharField(
        max_length=15, blank=False, null=False, default="111111", unique=True
    )
    mail = models.EmailField(
        blank=False, null=False, unique=True, default="dev@gmail.com"
    )
    age = models.IntegerField(blank=True, null=True)

    class Gender(models.TextChoices):
        MEN = "Men"
        WOMEN = "Women"
        TRANSGENDER = "Transgender"

    gender = models.CharField(choices=Gender.choices, max_length=20)
    created_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    password=models.CharField(blank=False,null=False,max_length=50,default='null')

    def __str__(self) -> str:
        return (f"{self.name}  {self.phone}")


class Cab_driver_info(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False, default="user")
    phone = models.CharField(
        max_length=15, blank=False, null=False, default="111111", unique=True
    )
    mail = models.EmailField(
        blank=False, null=False, unique=True, default="dev@gmail.com"
    )
    age = models.IntegerField(blank=True, null=True)

    class Gender(models.TextChoices):
        MEN = "Men"
        WOMEN = "Women"
        TRANSGENDER = "Transgender"

    gender = models.CharField(choices=Gender.choices, max_length=20)
    # we have to upload this doc on aws
    # need to null or blank false
    lisence_upload = models.FileField(upload_to="files/", blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    password=models.CharField(blank=False,null=False,default='null')

    def __str__(self) -> str:
        return (f"{self.name}  {self.phone}")
