from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


def move_to_api(request):
    return redirect("api/")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", move_to_api),
    path("api/", include("books_api.urls")),
]
