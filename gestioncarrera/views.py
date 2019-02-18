from django.urls import reverse_lazy

from gestioncarrera.models import Carrera
from django.shortcuts import get_object_or_404, render, redirect
from django.template import RequestContext
from gestioncarrera.form import GuardarCarreraForm
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q

# Create your views here.
def index(request):
    carreras = Carrera.objects.all().order_by('id')
    return render(request, 'carrera/lista_carrera.html', {'carreras': carreras})


@login_required
@permission_required('gestioncarrera.agregar_carrera',reverse_lazy('Carrera'))
def guardar_carrera(request):
    message=None
    if request.method == 'POST':
        form = GuardarCarreraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Carrera')
        else:
            message:"datos faltantes para registrar la Carrera"
            return render(request, 'carrera/agregar_carrera.html',
                          {'form': form,'message':message})
    else:
        form = GuardarCarreraForm(request.POST)
    return render(request, 'carrera/agregar_carrera.html',
                              {'message':message, 'form': form})


@login_required
@permission_required('gestioncarrera.editar_carrera',reverse_lazy('Carrera'))
def editar_carrera(request, carrera_id):
    message = None
    carrera = get_object_or_404(Carrera, pk=carrera_id)
    if request.method == 'POST':
        form = GuardarCarreraForm(request.POST, instance=carrera)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('Carrera')
        else:
            message: "datos faltantes para registrar la Carrera"
            return render(request, 'carrera/editar_carrera.html',
                          {'form': form, 'message': message,'carrera':carrera})
    else:
        form = GuardarCarreraForm(instance=carrera)
    return render(request, 'carrera/editar_carrera.html',
                              {'form': form,'message': message, 'carrera':carrera})


@login_required
@permission_required('gestioncarrera.eliminar_carrera',reverse_lazy('Carrera'))
def eliminar_carrera(request, carrera_id):
    print(request)
    carrera = get_object_or_404(Carrera, id=carrera_id)
    carrera.delete()
    return redirect('Carrera')
