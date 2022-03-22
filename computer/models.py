from django.db import models

# Create your models here.
class ComputerBrand(models.Model):
    brand_name=models.CharField(max_length=100)
    logo=models.ImageField(upload_to="static/img")

    def __str__(self):
        return self.brand_name

class ComputerSpecification(models.Model):
    processor_generation=models.CharField(max_length=50)
    price_min=models.IntegerField()
    price_max=models.IntegerField()
    ram=models.IntegerField()

    def __str__(self):
        return self.processor_generation

class ComputerGeneration(models.Model):
    gen=models.CharField(max_length=100)   

class Computer(models.Model):
    computer_code=models.IntegerField(unique=True)
    computer=models.ForeignKey(ComputerGeneration, on_delete=models.CASCADE)
    computer_specification=models.ForeignKey(ComputerSpecification, on_delete=models.CASCADE)
    brand=models.ForeignKey(ComputerBrand,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    unit_rate=models.IntegerField()
    total_price=models.IntegerField()
    
