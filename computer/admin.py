from django.contrib import admin
from computer.models import Computer,ComputerBrand, ComputerGeneration,ComputerSpecification

# Register your models here.
admin.site.register(Computer)
admin.site.register(ComputerBrand)
admin.site.register(ComputerSpecification)
admin.site.register(ComputerGeneration)
