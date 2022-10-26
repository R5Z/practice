from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg import openapi

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/articles/", include("articles.urls")),
]
