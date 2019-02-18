from django.urls import reverse_lazy

from gestioninstitucion.models import Institucion
from gestionresponsableinstitucional.models import ResponsableInstitucional
from django.shortcuts import get_object_or_404, render, redirect
from gestioninstitucion.form import GuardarInstitucionForm
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
def index(request):
    instituciones = Institucion.objects.all().order_by('id')
    return render(request, 'institucion/lista_institucion.html', {'instituciones': instituciones})


def institucion_detallada(request, institucion_id):
    institucion = get_object_or_404(Institucion, pk=institucion_id)
    responsables = ResponsableInstitucional.objects.all()
    return render(request, "institucion/perfil_institucion.html", {'institucion': institucion, 'responsables':responsables})


@login_required
@permission_required('gestioninstitucion.agregar_institucion',reverse_lazy('Institucion'))
def guardar_institucion(request):
    if request.method == 'POST':
        form = GuardarInstitucionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Institucion')
    else:
        form = GuardarInstitucionForm()
    return render(request, 'institucion/agregar_institucion.html',
                              {'form': form})


@login_required
@permission_required('gestioninstitucion.editar_institucion',reverse_lazy('Institucion'))
def editar_institucion(request, institucion_id):
    institucion = get_object_or_404(Institucion, pk=institucion_id)
    if request.method == 'POST':
        form = GuardarInstitucionForm(request.POST,request.FILES, instance=institucion)
        if form.is_valid():
            form.save()
            return redirect('Institucion')
    else:
        form = GuardarInstitucionForm(instance=institucion)
    return render(request, 'institucion/editar_institucion.html',
                              {'form': form,'institucion':institucion})


@login_required
@permission_required('gestioninstitucion.eliminar_institucion',reverse_lazy('Institucion'))
def eliminar_institucion(request, institucion_id):
    institucion = get_object_or_404(Institucion, id=institucion_id)
    institucion.delete()
    return redirect('Institucion')
