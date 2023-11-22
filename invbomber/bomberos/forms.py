from django import forms
from .models import Articulos

class Articulosform(forms.ModelForm):
    class Meta:
        model = Articulos
        fields = '__all__'