from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.ComputerList.as_view(), name="home"),
    path('listing',views.ComputerList.as_view(), name="home"),
    path("create", views.ComputerCreate.as_view(), name="create"),
    path("<int:pk>/update", views.ComputerUpdate.as_view(), name="update"),
   
]