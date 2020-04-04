from django.forms import ModelForm
from .models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        #campos do form
        fields = ['first_name', 'last_name', 'age', 'salario',]