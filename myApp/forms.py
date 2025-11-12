from django.forms import ModelForm
from .models import Tarea, Persona

class FormTarea(ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre_t', 'descripcion_t']

class FormPersona(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
