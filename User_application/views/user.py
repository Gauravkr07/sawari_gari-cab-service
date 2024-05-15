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

from User_application.models import Customer_info

class User_view(View):
    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        current_url = resolve(request.path_info).url_name
        if current_url == "Register_user" and request.method == "POST":
            return self.register_user(request, *args, **kwargs)
        elif current_url == "fetch any account info" and request.method == "GET":
            return self.get_specific_user_detail(request, *args, **kwargs)
        elif current_url == "fetch all recoreds of user" and request.method == "GET":
            return self.get_specific_user_detail(request, *args, **kwargs)

    async def register_user(self, request, *args, **kwargs):
        try:
            if not request.POST:
                request_body = str_to_dict(request.body)
                user_details = {
                    "name": request_body["name"],
                    "phone": request_body["phone"],
                    "mail": request_body.get("mail"),
                    "age": request_body.get("age"),
                    "gender": request_body.get("gender"),
                    "is_active":request_body.get("is_active")

                }
            else:
                user_details = {
                    "name": request.POST["name"],
                    "phone": request.POST["phone"],
                    "mail": request.POST["mail"],
                    "age": request.POST["age"],
                    "gender": request.POST["gender"],
                    "is_active":request.POST["is_active"]
                }
            if len(user_details["phone"]) != 10:
                raise Exception("Phone number is not valid")
            user_data = await sync_to_async(
                lambda: Customer_info.objects.create(**user_details)
            )()

            return JsonResponse(
                {"Response": "User created successfully"}, status=201, safe=False
            )
        except IntegrityError as e:
            return JsonResponse(
                {
                    "error": "User's Mail or phone is already registered",
                    "detail": str(e),
                },
                status=400,
            )
        except Exception as er:
            return JsonResponse({"err": str(er)}, status=400)

    async def get_specific_user_detail(self, request, *args, **kwargs):
        phone = request.GET.get("phone")
        mail = request.GET.get("mail")
        if phone:
            data = {"phone": phone}
        if not phone:
            data = {"mail": mail}
        try:
            check_user_account = await sync_to_async(
                lambda: Customer_info.objects.get(**data)
            )()
            data = {
                "name": check_user_account.name,
                "phone": check_user_account.phone,
                "mail": check_user_account.mail,
                "age": check_user_account.age,
                "gender": check_user_account.gender,
                "created_time": str(check_user_account.created_time),
                "is_active":check_user_account.is_active
            }
            data = json.dumps(data)
            result = json.loads(data)

            return JsonResponse({"Response": result}, safe=False, status=200)
        except Customer_info.DoesNotExist:
            return JsonResponse(
                {"Error": "User not found! enter correct mail or phone number"},
                status=404,
            )
        except Exception as er:
            return JsonResponse({"Error": str(er)}, status=400)

    # async def get_all_user_data(self, request, *args, **kwargs):
    #     page_number = request.GET.get('page', 1)

    #     objects_per_page = 50
    #     total_count = all_objects.count()
    #     all_objects = Customer_info.objects.all()
    #     pritn()
    #     paginator = Paginator(all_objects, objects_per_page)
