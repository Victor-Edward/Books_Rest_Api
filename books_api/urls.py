from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("Author", views.AuthorViewSet)
router.register("Book", views.BookViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
