from pyexpat import model
from re import template
from statistics import mode
from django.http import QueryDict
from django.shortcuts import render,reverse
from django.views import generic
from .models import *
from .forms import ComputerForm
# Create your views here.

  

class LandingPage(generic.TemplateView):
    template_name ="listing.html"

class ComputerList(generic.ListView):
    model = Computer
    template_name = "computer/computer_list.html"
    queryset = Computer.objects.all()
    context_object_name ="object"


class ComputerCreate(generic.CreateView):
    model = Computer
    form_class = ComputerForm
    template_name ="computer/computer_create.html"

    def get_success_url(self):
        return reverse("home")

class ComputerUpdate(generic.UpdateView):
    model = Computer
    form_class =ComputerForm
    template_name = "computer/computer_update.html"
    queryset = Computer.objects.all()

    def get_success_url(self):
        return reverse("home")
    
        
        




    

