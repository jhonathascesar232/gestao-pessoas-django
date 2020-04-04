from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    age = models.IntegerField()
    salario = models.DecimalField(max_digits = 5, decimal_places = 2) #decimal places -> numeros depois da virgula
    photo = models.ImageField(upload_to='Clientes_photos', null=True, blank=True)

    def __str__(self):
        return self.first_name+' '+self.last_name