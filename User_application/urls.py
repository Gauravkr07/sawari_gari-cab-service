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
        "register/driver/",
        views.Cab_drivers_view.as_view(),
        name="Register_driver",
    ),
]
