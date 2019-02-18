from django.urls import reverse_lazy

from gestionareaconocimiento.models import AreaConocimiento
from django.shortcuts import get_object_or_404, render, redirect
from gestionareaconocimiento.form import GuardarAreaForm
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
def index(request):
    areasconocimientos = AreaConocimiento.objects.all().order_by('id')
    return render(request, 'areaconocimiento/lista_areaconocimiento.html', {'areasconocimientos': areasconocimientos})


@login_required
@permission_required('gestionareaconocimiento.agregar_areaconocimiento',reverse_lazy('AreaConocimiento'))
def guardar_areaconocimiento(request):
    if request.method == 'POST':
        form = GuardarAreaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AreaConocimiento')
    else:
        form = GuardarAreaForm()
    return render(request, 'areaconocimiento/agregar_areaconocimiento.html',
                              {'form': form})


@login_required
@permission_required('gestionareaconocimiento.editar_areaconocimiento',reverse_lazy('AreaConocimiento'))
def editar_areaconocimiento(request, areaconocimiento_id):
    areaconocimiento = get_object_or_404(AreaConocimiento, pk=areaconocimiento_id)
    if request.method == 'POST':
        form = GuardarAreaForm(request.POST, instance=areaconocimiento)
        if form.is_valid():
            form.save()
            return redirect('AreaConocimiento')
    else:
        form = GuardarAreaForm(instance=areaconocimiento)
    return render(request, 'areaconocimiento/editar_areaconocimiento.html',
                              {'form': form, 'areaconocimiento':areaconocimiento})


@login_required
@permission_required('gestionareaconocimiento.eliminar_areaconocimiento',reverse_lazy('AreaConocimiento'))
def eliminar_areaconocimiento(request, areaconocimiento_id):
    areaconocimiento = get_object_or_404(AreaConocimiento, id=areaconocimiento_id)
    areaconocimiento.delete()
    return redirect('AreaConocimiento')

