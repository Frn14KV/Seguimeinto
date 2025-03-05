from django.urls import reverse_lazy

from gestiontipoproyecto.models import TipoProyecto
from django.shortcuts import get_object_or_404, render, redirect
from gestiontipoproyecto.form import GuardarTipoForm
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
def index(request):
    tiposproyectos = TipoProyecto.objects.all().order_by('id')
    return render(request, 'tipoproyecto/lista_tipoproyecto.html', {'tiposproyectos': tiposproyectos})


@login_required
@permission_required('gestiontipoproyecto.agregar_tipoproyecto',reverse_lazy('TipoProyecto'))
def guardar_tipoproyecto(request):
    if request.method == 'POST':
        form = GuardarTipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('TipoProyecto')
    else:
        form = GuardarTipoForm()
    return render(request, 'tipoproyecto/agregar_tipoproyecto.html',
                              {'form': form})


@login_required
@permission_required('gestiontipoproyecto.editar_tipoproyecto',reverse_lazy('TipoProyecto'))
def editar_tipoproyecto(request, tipoproyecto_id):
    tipoproyecto = get_object_or_404(TipoProyecto, pk=tipoproyecto_id)
    if request.method == 'POST':
        form = GuardarTipoForm(request.POST, instance=tipoproyecto)
        if form.is_valid():
            form.save()
            return redirect('TipoProyecto')
    else:
        form = GuardarTipoForm(instance=tipoproyecto)
    return render(request, 'tipoproyecto/editar_tipoproyecto.html',
                              {'form': form,'tipoproyecto':tipoproyecto})


@login_required
@permission_required('gestiontipoproyecto.eliminar_tipoproyecto',reverse_lazy('TipoProyecto'))
def eliminar_tipoproyecto(request, tipoproyecto_id):
    tipoproyecto = get_object_or_404(TipoProyecto, id=tipoproyecto_id)
    tipoproyecto.delete()
    return redirect('TipoProyecto')