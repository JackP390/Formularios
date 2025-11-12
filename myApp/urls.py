from django.urls import path
from . import views

urlpatterns = [
        path('', views.main, name="main"),
        path('tareas/', views.tareas, name="tareas"),
        path('personas/', views.personas, name="personas")
        ]
