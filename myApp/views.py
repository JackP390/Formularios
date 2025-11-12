from django.shortcuts import render
from .forms import FormTarea, FormPersona
from .models import Tarea, Persona

# Create your views here.
def main(request):
    return render(request, "main.html")

def tareas(request):
    if request.method == 'POST':
        form = FormTarea(request.POST)
        if form.is_valid():
            form.save()
    form = FormTarea()
    tareas = Tarea.objects.all()
    context = {'form':form, 'tareas':tareas}
    return render(request, "tarea.html", context)

def personas(request):
    if request.method == 'POST':
        form = FormPersona(request.POST)
        if form.is_valid():
            form.save()
    form = FormPersona()
    personas = Persona.objects.all()
    context = {'form':form, 'personas':personas}
    return render(request, "persona.html", context)
