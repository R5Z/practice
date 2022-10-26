from django.urls import path, include
from articles import views

urlpatterns = [
    path("index/", views.articleAPI, name="index"),
    path("<int:article_id>/", views.articleAPI, name="article_view"),
]