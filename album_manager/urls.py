# Ingresar tus URLs de la app aquí
from django.contrib import admin
from django.urls import path
from album_manager import views

urlpatterns = [
    path("", views.index, name="index"),
    path('admin/', admin.site.urls),
]
