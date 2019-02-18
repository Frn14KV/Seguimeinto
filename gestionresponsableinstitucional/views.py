from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy

from gestionayuda2.form import GuardarForm2
from gestioninstitucion.models import Institucion
from gestionresponsableinstitucional.form import GuardarResponsableForm
from gestioninstitucion.form import GuardarInstitucionForm
from gestionayuda.form import GuardarForm
from gestionresponsableinstitucional.models import ResponsableInstitucional


def index(request):
    responsablesinstitucionales = ResponsableInstitucional.objects.all().order_by('id')
    return render(request, 'responsableinstitucional/lista_responsablesinstitucional.html', {'responsablesinstitucionales': responsablesinstitucionales})


def responsableinstitucional_detalle(request, responsableinstitucional_id):
    instituciones = Institucion.objects.all()
    responsableinstitucional= get_object_or_404(ResponsableInstitucional, pk=responsableinstitucional_id)
    return render(request, 'responsableinstitucional/perfil_responsableinstitucional.html', {'responsableinstitucional': responsableinstitucional,'instituciones':instituciones})


@login_required
@permission_required('gestionresponsableinstitucional.agregar_responsableinstitucional',reverse_lazy('ResponsableInstitucional'))
def guardar_responsableinstitucional(request):
    global partes
    message = None
    insituciones = Institucion.objects.all()
    if request.method == 'POST':
        form = GuardarResponsableForm(request.POST, request.FILES)
        form1 = GuardarInstitucionForm(request.POST, request.FILES)
        form2 = GuardarForm(request.POST)
        form4 = GuardarForm2(request.POST)

        if form2.is_valid():
            nombre = form2.cleaned_data.get('nombre')
            partes = nombre.split(';')
        elif form4.is_valid():
            nombre = form4.cleaned_data.get('nombre2')
            partes = nombre.split(';')

        if form.is_valid():
            form.save()
            return redirect('ResponsableInstitucional')
        elif form1.is_valid():
            form1.save()
            data = {'nombre_responsable': partes[0],
                    'apellido_responsable': partes[1],
                    'correo_responsable': partes[2],
                    'telefono_responsable':partes[3],
                    }
            if len(partes[4]) == 0 or partes[4] == "null":
                institucionsalva = None
            else:
                institucionsalva = Institucion.objects.filter(id=partes[4])
            form = GuardarResponsableForm(data)
            form1 = GuardarInstitucionForm()
            message1 = "La Institucion a sido registrada con exito."
            return render(request, 'responsableinstitucional/agregar_responsableinstitucional.html',
                          {'message': message, 'message1': message1, 'form': form, 'form1': form1, 'instituciones':insituciones, 'institucionsalva':institucionsalva})
        else:
            data = {'nombre_responsable': partes[0],
                    'apellido_responsable': partes[1],
                    'correo_responsable': partes[2],
                    'telefono_responsable': partes[3],
                    }
            if len(partes[4]) == 0 or partes[4] == "null":
                institucionsalva = None
            else:
                institucionsalva = Institucion.objects.filter(id=partes[4])
            form = GuardarResponsableForm(data)
            form1 = GuardarInstitucionForm(request.POST, request.FILES)
            message = "uno de los campos no fue ingresado al registrar la Institucion o el Responsable Insitucional."
            return render(request, 'autor/agregar_autor.html',
                          {'message': message, 'form': form, 'form1': form1, 'instituciones':insituciones, 'institucionsalva':institucionsalva})
    else:
        form = GuardarResponsableForm()
        form1 =GuardarInstitucionForm()
    return render(request, 'responsableinstitucional/agregar_responsableinstitucional.html',
                              {'message': message, 'form': form, 'form1': form1, 'instituciones':insituciones})


@login_required
@permission_required('gestionresponsableinstitucional.editar_responsableinstitucional',reverse_lazy('ResponsableInstitucional'))
def editar_responsableinstitucional(request, responsableinstitucional_id):
    message = None
    global partes
    insituciones = Institucion.objects.all()
    responsableinstitucional = get_object_or_404(ResponsableInstitucional, id=responsableinstitucional_id)
    if request.method == 'POST':
        form = GuardarResponsableForm(request.POST, request.FILES, instance=responsableinstitucional)
        form1 = GuardarInstitucionForm(request.POST, request.FILES)
        form2 = GuardarForm(request.POST)
        form4 = GuardarForm2(request.POST)

        if form2.is_valid():
            nombre = form2.cleaned_data.get('nombre')
            partes = nombre.split(';')
        elif form4.is_valid():
            nombre = form4.cleaned_data.get('nombre2')
            partes = nombre.split(';')

        if form1.is_valid():
            form1.save()
            data = {'nombre_responsable': partes[0],
                    'apellido_responsable': partes[1],
                    'correo_responsable': partes[2],
                    'telefono_responsable': partes[3],
                    }
            if len(partes[4]) == 0 or partes[4] == "null":
                institucionsalva = None
            else:
                institucionsalva = Institucion.objects.filter(id=partes[4])
            form = GuardarResponsableForm(data)
            form1 = GuardarInstitucionForm()
            message1 = "La Institucion a sido registrada con exito."
            return render(request, 'responsableinstitucional/editar_responsableinstitucional.html',
                          {'message': message, 'message1': message1, 'form': form, 'form1': form1, 'responsableinstitucional':responsableinstitucional, 'instituciones':insituciones, 'institucionsalva':institucionsalva})
        elif form.is_valid():
            form.save()
            return redirect('ResponsableInstitucional')
        else:
            data = {'nombre_responsable': partes[0],
                    'apellido_responsable': partes[1],
                    'correo_responsable': partes[2],
                    'telefono_responsable': partes[3],
                    }
            if len(partes[4]) == 0 or partes[4] == "null":
                institucionsalva = None
            else:
                institucionsalva = Institucion.objects.filter(id=partes[4])
            form = GuardarResponsableForm(data)
            form1 = GuardarInstitucionForm(request.POST, request.FILES)
            message = "Uno de los campos no fue ingresado al editar la Institución el Responsable."
            return render(request, 'responsableinstitucional/editar_responsableinstitucional.html',
                          {'message': message, 'form': form, 'form1':form1, 'responsableinstitucional':responsableinstitucional, 'instituciones':insituciones, 'institucionsalva':institucionsalva})
    else:
        form = GuardarResponsableForm(instance=responsableinstitucional)
        form1 = GuardarInstitucionForm()
    return render(request, 'responsableinstitucional/editar_responsableinstitucional.html',
                  {'message': message, 'form': form, 'form1': form1, 'responsableinstitucional':responsableinstitucional, 'instituciones':insituciones})


@login_required
@permission_required('gestionresponsableinstitucional.eliminar_responsableinstitucional',reverse_lazy('ResponsableInstitucional'))
def eliminar_responsableinstitucional(request, responsableinstitucional_id):
    responsableinstitucional = get_object_or_404(ResponsableInstitucional, id=responsableinstitucional_id)
    responsableinstitucional.delete()
    return redirect('ResponsableInstitucional')