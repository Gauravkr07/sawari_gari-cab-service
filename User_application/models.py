from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Customer_info(models.Model):
    id = models.CharField(primary_key=True, editable=False,blank=False,null=False)
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
    password = models.CharField(blank=False, null=False, max_length=50, default="null")
    current_loc = models.CharField(blank=True, null=True, max_length=100)

    def __str__(self) -> str:
        return f"{self.name}  {self.phone}"


class Cab_driver_info(models.Model):
    _id = models.CharField(primary_key=True,editable=False,blank=False,null=False,default='null')
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
    password = models.CharField(blank=False, null=False, default="null")
    current_loc = models.CharField(blank=True, null=True, max_length=100)

    def __str__(self) -> str:
        return f"{self.name}  {self.phone}"


class Ride_booking(models.Model):
    _idd = models.CharField(primary_key=True, editable=False,blank=False,null=False,default='null')
    customer_id = models.CharField(blank=False, null=False, max_length=50)
    driver_id = models.CharField(blank=False, null=False, max_length=50)
    source = models.CharField(blank=False, null=False, max_length=200)
    destinantion = models.CharField(blank=False, null=False, max_length=200)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    pickup_location = models.CharField(blank=False, null=False, max_length=200)
    amount=models.FloatField(blank=True, null=True)

    class Payment_type(models.TextChoices):
        UPI = "Upi"
        CASH = "Cash"

    payment_mode = models.CharField(choices=Payment_type.choices, max_length=20)
    payment_id = models.CharField(choices=Payment_type.choices, max_length=20)

    class Payment_status(models.TextChoices):
        NOT_PAID = "Not_paid"
        PENDING = "Pending"
        COMLETED = "Completed"

    payment_status = models.CharField(choices=Payment_status.choices, max_length=20)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        blank=True,
        null=True,
        default=None,
        help_text="Rating from 1 to 5",
    )

class vehicle_detail(models.Model):
    cab_number = models.CharField(max_length=50, unique=True)
    cab_model = models.CharField(max_length=100)
    cab_color = models.CharField(max_length=50)
    cab_type=models.CharField(max_length=50)
    cab_registration=models.CharField(max_length=50)
    vehicle_no=models.CharField(max_length=50)
    year=models.CharField(max_length=4,help_text="Year of manufacture")
    driver = models.ForeignKey('Cab_driver_info', on_delete=models.CASCADE)
    
class Rating(models.Model):
    customer_id = models.CharField(blank=False, null=False, max_length=50)
    driver_id = models.CharField(blank=False, null=False, max_length=50)
    # trip_id=models.ForeignKey('Ride_booking',on_delete=models.CASCADE)
    average_rating = models.FloatField(null=False,blank=False,default=0.0)
    feedback = models.CharField(blank=True, null=True, max_length=75)



