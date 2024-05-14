# Create your views here.
import asyncio
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
from User_application.utils import encrypt_password


class Cab_drivers_view(View):
    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.iscoroutinefunction(view)
        return view
    @csrf_exempt
    async def dispatch(self, request, *args, **kwargs):
        current_url = resolve(request.path_info).url_name
        if current_url == "Register_driver" and request.method == "POST":
            return self.post(request, *args, **kwargs) 
        elif current_url == "fetch any account info" and request.method == "GET":
            return self.get_specific_cab_driver_detail(request, *args, **kwargs)


    async def post(self, request, *args, **kwargs):
        try:
            if request.content_type == 'application/json':
                data = str_to_dict(request.body)
            else:
                data = request.POST.dict()
                data.update(request.FILES.dict())

            cab_driver_user = {
                "name": data.get("name"),
                "phone": data.get("phone"),
                "mail": data.get("mail"),
                "age": data.get("age"),
                "gender": data.get("gender"),
                "is_active": data.get("is_active"),
                "lisence_upload": data.get("lisence"),
                "password": data.get("password")
            }

            if len(cab_driver_user["phone"]) != 10:
                raise Exception("Phone number is not valid")
            if cab_driver_user["age"] < 18:
                raise Exception("Under age, you can't register")

            driver_data = await sync_to_async(Cab_driver_info.objects.create)(**cab_driver_user)

            return JsonResponse({"message": "created successfully"}, status=201)

        except IntegrityError as e:
            return JsonResponse({"error": "Driver's Mail or phone is already registered", "detail": str(e)}, status=400)

        except Exception as er:
            return JsonResponse({"error": str(er)}, status=400)
    # async def register_cab_drivers(self, request, *args, **kwargs):
    #     try:
    #         if request.POST:
    #             cab_driver_user = {
    #                 "name": request.POST["name"],
    #                 "phone": request.POST["phone"],
    #                 "mail": request.POST["mail"],
    #                 "age": request.POST["age"],
    #                 "gender": request.POST["gender"],
    #                 "is_active":request.POST["is_active"],
    #                 "lisence_upload":request.FILES["lisence"],
    #                 'password': request.POST['password']
    #             }
    #         else:
    #             request_body = str_to_dict(request.body)
    #             cab_driver_user = {
    #                 "name": request["name"],
    #             "phone": request_body["phone"],
    #             "mail": request_body["mail"],
    #             "age": request_body["age"],
    #             "gender": request_body["gender"],
    #             "is_active":request_body["is_active"],
    #             # "lisence_upload":request.FILES["lisence"],
    #             'password': request_body['password']
    #             }
    #         if len(cab_driver_user["phone"]) != 10:
    #             raise Exception("Phone number is not valid")
    #         if cab_driver_user["age"]<18:
    #             raise Exception("Under age, u can't register")
    #         driver_data = await sync_to_async(
    #             lambda: driver_data.objects.create(**cab_driver_user)
    #         )()

    #         return JsonResponse("created successfully", status=201, safe=False
    #         )
           
    #     except IntegrityError as e:
    #         return JsonResponse(
    #             {
    #                 "error": "Driver's Mail or phone is already registered",
    #                 "detail": str(e),
    #             },
    #             status=400,
    #         )
    #     except Exception as er:
    #         return JsonResponse({"err": str(er)}, status=400)
   
    async def get_specific_cab_driver_detail (self,request,*args, **kwargs):
        try:
            email=request.GET.get("email")
            #To check the user detail in data base ,here user_id is unique field so 
            check_user= await sync_to_async(
                lambda: Cab_driver_info.objects.get(mail=email))()
            
        
        except Exception as er:
            return JsonResponse({"error":str(er)},status=400)
