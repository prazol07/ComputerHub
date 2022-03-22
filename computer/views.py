from pyexpat import model
from re import template
from statistics import mode
from django.http import HttpResponse, QueryDict
from django.shortcuts import redirect, render,reverse
from django.urls import reverse_lazy
from django.views import generic
from .models import *
from .forms import ComputerForm
from django.contrib import messages
# Create your views here.

  

class LandingPage(generic.TemplateView):
    template_name ="listing.html"

class FilterBrand(generic.ListView):
    template_name="computerbrand_list.html"
    model= Computer

    def get_queryset(self):
        val = self.kwargs.get('brandname')
        brands=ComputerBrand.objects.filter(brand_name__icontains=val)
        return brands

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

    def form_valid(self, form):
        specific = form.cleaned_data.get("computer_specification")
        rate = form.cleaned_data.get("unit_rate")
        quantities=form.cleaned_data.get("quantity")
        if rate>=specific.price_max and rate<=specific.price_min:
            form.instance.total_price =rate * quantities
        else:
           messages.warning(self.request, "Your unit price range must be in between "+str(specific.price_min)+" to "+str(specific.price_max)) 
           return redirect("create")
        return super(ComputerCreate, self).form_valid(form)
        

        


class ComputerUpdate(generic.UpdateView):
    model = Computer
    form_class =ComputerForm
    template_name = "computer/computer_update.html"
    queryset = Computer.objects.all()

    def get_success_url(self):
        return reverse("home")
    
    
        




    

