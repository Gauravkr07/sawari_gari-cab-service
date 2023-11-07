from django.contrib import admin

# Register your models here.
from .models import User_info,Cab_driver_info

admin.site.register(User_info)
admin.site.register(Cab_driver_info)
