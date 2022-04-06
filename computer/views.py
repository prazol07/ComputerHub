from pyexpat import model
from urllib import request
from django.http import HttpResponse
from django.views import View
from django.shortcuts import get_object_or_404, render, redirect, reverse
from .models import ComputerBrands
from .models import Computer
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib import messages
from .forms import ComputerForm


class IndexView(ListView):
    model = ComputerBrands
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        queryset = ComputerBrands.get_all_computerbrands()
        context = {
            'brands': queryset
        }
        return context


class ComputerDetailsView(ListView):
    model = Computer
    template_name = 'details.html'

    def get_queryset(self):
        queryset = Computer.objects.all()
        return queryset

class FormView(CreateView):
    model = Computer
    template_name = 'form.html'
    form_class = ComputerForm

    def post(self, request):
        form = ComputerForm(request.POST)
        unitprice = int(request.POST.get('unitrate'))
        quantity = int(request.POST.get('quantity'))
        form.instance.totalprice = unitprice*quantity

        if form.is_valid():
            form.save()
            return redirect("/")
        return render(request, 'index.html')

    def get_success_url(self):
        return reverse("index")


class UpdateViewForm(UpdateView):
    template_name = 'update.html'
    form_class = ComputerForm

    def get_queryset(self):
        queryset = Computer.objects.all()
        return queryset

    def get_success_url(self):
        return reverse("index")


class IndividualDetailView(DetailView):
    model = Computer
    template_name = 'individualdetail.html'

    def get_queryset(self):
        queryset = Computer.objects.all()
        return queryset

class LogoDetailView(ListView):
    model=Computer
    template_name = "logodetail.html"

    def get_context_data(self):
        val = self.kwargs.get("brandname")
        brand = Computer.objects.filter(brandname__icontains=val)  
        context={'brand':brand,
                'val':val
        } 
        return context

       
class DeleteComputer(DeleteView):
    model=Computer
    template_name= "delete.html"
    def get_success_url(self):
        return reverse("details")