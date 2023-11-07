# Create your views here.
import asyncio
import json
from json import loads as str_to_dict

from asgiref.sync import sync_to_async
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.http import JsonResponse
from django.urls import resolve
from django.utils.decorators import classonlymethod, method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from User_application.models import Cab_driver_info


class Cab_drivers_view(View):
    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        current_url = resolve(request.path_info).url_name
        if current_url == "Register_cab_driver" and request.method == "POST":
            return self.register_cab_drivers(request, *args, **kwargs)
        # elif current_url == "fetch any account info" and request.method == "GET":
        #     return self.get_specific_user_detail(request, *args, **kwargs)
       

    async def register_cab_drivers(self, request, *args, **kwargs):
        try:
            if request.POST:
                cab_driver_user = {
                    "name": request.POST["name"],
                    "phone": request.POST["phone"],
                    "mail": request.POST["mail"],
                    "age": request.POST["age"],
                    "gender": request.POST["gender"],
                    "is_active":request.POST["is_active"],
                    "lisence_upload":request.FILES["lisence"]
                }
            if len(cab_driver_user["phone"]) != 10:
                raise Exception("Phone number is not valid")
            driver_data = await sync_to_async(
                lambda: Cab_driver_info.objects.create(**cab_driver_user)
            )()
            cab_driver=cab_driver_user["name"]
            return JsonResponse(f"{cab_driver}created successfully", status=201, safe=False
            )
        except IntegrityError as e:
            return JsonResponse(
                {
                    "error": "Driver's Mail or phone is already registered",
                    "detail": str(e),
                },
                status=400,
            )
        except Exception as er:
            return JsonResponse({"err": str(er)}, status=400)