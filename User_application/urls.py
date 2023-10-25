from django.urls import re_path

from . import views

urlpatterns = [
    re_path(
        "create/new_user",
        views.User_view.as_view(),
        name="Create_user",
    ),
    re_path(
        "fetch/user/info/",
        views.User_view.as_view(),
        name="fetch any account info",
    ),
]
