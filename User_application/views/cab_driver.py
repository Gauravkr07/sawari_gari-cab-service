# Create your views here.
import asyncio
from json import loads as str_to_dict

from asgiref.sync import sync_to_async
from django.db import IntegrityError
from django.http import JsonResponse
from django.urls import resolve
from django.utils.decorators import classonlymethod, method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json

from User_application.models import Cab_driver_info


class Cab_driver_view(View):
    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        current_url = resolve(request.path_info).url_name
        if current_url == "register_cab_driver" and request.method == "POST":
            return self.register_driver(request, *args, **kwargs)
        if current_url == "get_driver_phone_mail" and request.method == "GET":
            return self.get_driver_phone_mail(request, *args, **kwargs)

    def register_driver(self, request, *args, **kwargs):
        try:
            if request.POST:
                data_source = request.POST
            else:
                data_source = str_to_dict(request.body)

            cab_driver_user = {
                "name": data_source.get("name", ""),
                "phone": data_source.get("phone", ""),
                "mail": data_source.get("mail", ""),
                "age": data_source.get("age", ""),
                "gender": data_source.get("gender", ""),
                "is_active": data_source.get("is_active", ""),
                "password": data_source.get("password", ""),
            }
            if len(cab_driver_user["phone"]) != 10:
                raise Exception("Phone number is not valid")
            if int(cab_driver_user["age"]) < 18:
                raise Exception("Under age, you can't register")

            driver_data = Cab_driver_info.objects.create(**cab_driver_user)
            # driver_data = await sync_to_async(lambda: Cab_driver_info.objects.create(**cab_driver_user))()

            return JsonResponse({"message": "created successfully"}, status=201)

        except IntegrityError as e:
            return JsonResponse(
                {
                    "error": "Driver's Mail or phone is already registered",
                    "detail": str(e),
                },
                status=400,
            )
        except Exception as er:
            return JsonResponse({"error": str(er)}, status=400)

    async def get_driver_phone_mail(self, request, *args, **kwargs):
        print("gggg")
        mail = request.GET.get("mail")
        phone = request.GET.get("phone")
        if phone:
            data = {"phone": phone}
        if not phone:
            data = {"mail": mail}

        try:
            check_user_account = await sync_to_async(
                lambda: Cab_driver_info.objects.get(**data)
            )()
            # check_user_account = await sync_to_async(
            #     Cab_driver_info.objects.get
            # )(**data)

            result = {
                "name": check_user_account.name,
                "phone": check_user_account.phone,
                "mail": check_user_account.mail,
                "age": check_user_account.age,
                "gender": check_user_account.gender,
                "is_active": check_user_account.is_active,
            }
            data = json.dumps(result)
            result = json.loads(data)

            return JsonResponse({"Response": result}, safe=False, status=200)
        except Cab_driver_info.DoesNotExist:
            return JsonResponse(
                {"Error": "User not found! enter correct mail or phone number"},
                status=404,
            )
        except Exception as er:
            return JsonResponse({"Error": str(er)}, status=400)
