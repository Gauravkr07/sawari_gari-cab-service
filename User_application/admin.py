from django.contrib import admin

# Register your models here.
from .modelss import Customer_info,Cab_driver_info,Rating,Ride_booking,vehicle_detail

admin.site.register(Customer_info)
admin.site.register(Cab_driver_info)
admin.site.register(Rating)
admin.site.register(Ride_booking)
admin.site.register(vehicle_detail)
