from django.urls import re_path

from . import views

urlpatterns = [
    re_path(
        "register/new_user",
        views.User_view.as_view(),
        name="Register_user",
    ),
    re_path(
        "fetch/user/info/",
        views.User_view.as_view(),
        name="fetch any account info",
    ),
    re_path(
        "register/driver/data/",
        views.Cab_driver_view.as_view(),
        name="register_cab_driver",
    ),
    re_path(
        "fetch/driver/detail",
        views.Cab_driver_view.as_view(),
        name="get_driver_phone_mail",
    ),
]
