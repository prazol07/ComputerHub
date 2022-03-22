from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.ComputerList.as_view(), name="root"),
    path('listing',views.ComputerList.as_view(), name="home"),
    path("create", views.ComputerCreate.as_view(), name="create"),
    path("<int:pk>/update", views.ComputerUpdate.as_view(), name="update"),
    path("computer_filter_bybrand/<slug:brandname>",views.FilterBrand.as_view(), name="search")
   
]