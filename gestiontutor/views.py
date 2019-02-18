from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy

from gestionayuda2.form import GuardarForm2
from gestioncarrera.models import Carrera
from gestiontutor.form import GuardarTutorForm
from gestioncarrera.form import GuardarCarreraForm
from gestionayuda.form import GuardarForm
from gestiontutor.models import Tutor


# Create your views here.
def index(request):
    tutores = Tutor.objects.all().order_by('id')
    return render(request, 'tutor/listar_tutor.html', {'tutores': tutores})


def tutor_detallado(request, tutor_id):
    carreras = Carrera.objects.all()
    tutor = get_object_or_404(Tutor, pk=tutor_id)
    return render(request, 'tutor/perfil_tutor.html', {'tutor': tutor, 'carreras':carreras})


@login_required
@permission_required('gestiontutor.agregar_tutor',reverse_lazy('Tutor'))
def guardar_tutor(request):
    global partes
    message = None
    carreras = Carrera.objects.all()
    if request.method == 'POST':
        form = GuardarTutorForm(request.POST, request.FILES)
        form1 = GuardarCarreraForm(request.POST, request.FILES)
        form2 = GuardarForm(request.POST)
        form4 = GuardarForm2(request.POST)

        if form2.is_valid():
            nombre = form2.cleaned_data.get('nombre')
            partes = nombre.split(';')
        elif form4.is_valid():
            nombre = form4.cleaned_data.get('nombre2')
            partes = nombre.split(';')

        if form.is_valid():
            cedula = form.cleaned_data.get('cedula_tutor')
            if len(cedula) == 10:
                if verificar(cedula) is not False:
                    form.save()
                    return redirect('Tutor')
                else:
                    data = {'nombre_tutor': partes[0],
                            'apellido_tutor': partes[1],
                            'cedula_tutor': partes[2],
                            'correo_tutor': partes[4],
                            'telefono_tutor': partes[3],
                            }
                    if len(partes[5]) == 0 or partes[5] == "null":
                        carrerasalva = None
                    else:
                        carrerasalva = Carrera.objects.filter(id=partes[5])

                    message="el numero de cedula es invalido, verifique el numero"
                    form = GuardarTutorForm(data)
                    form1 = GuardarCarreraForm()
                    return render(request, 'tutor/agregar_tutor.html',
                                  {'message': message, 'form': form, 'form1': form1, 'carreras': carreras, 'carrerasalva':carrerasalva})
            else:
                data = {'nombre_tutor': partes[0],
                        'apellido_tutor': partes[1],
                        'cedula_tutor': partes[2],
                        'correo_tutor': partes[4],
                        'telefono_tutor': partes[3],
                        }
                if len(partes[5]) == 0 or partes[5] == "null":
                    carrerasalva = None
                else:
                    carrerasalva = Carrera.objects.filter(id=partes[5])
                form = GuardarTutorForm(data)
                form1 = GuardarCarreraForm()
                message = "ingrese los 10 digitos de la cedula"
                return render(request, 'tutor/agregar_tutor.html',
                              {'message': message, 'form': form,'form1': form1, 'carreras': carreras, 'carrerasalva':carrerasalva})
        elif form1.is_valid():
            form1.save()
            data = {'nombre_tutor': partes[0],
                    'apellido_tutor': partes[1],
                    'cedula_tutor':partes[2],
                    'correo_tutor': partes[4],
                    'telefono_tutor':partes[3],
                    }
            form = GuardarTutorForm(data)
            form1 = GuardarCarreraForm()
            if len(partes[5]) == 0 or partes[5] == "null":
                carrerasalva = None
            else:
                carrerasalva = Carrera.objects.filter(id=partes[5])
            message1 = "la Carrera a sido registrada con exito."
            return render(request, 'tutor/agregar_tutor.html',
                          {'message': message, 'message1': message1, 'form': form, 'form1': form1, 'carreras': carreras, 'carrerasalva':carrerasalva})
        else:
            data = {'nombre_tutor': partes[0],
                    'apellido_tutor': partes[1],
                    'cedula_tutor': partes[2],
                    'correo_tutor': partes[4],
                    'telefono_tutor': partes[3],
                    }
            form = GuardarTutorForm(data)
            form1 = GuardarCarreraForm(request.POST)
            if len(partes[5]) == 0 or partes[5] == "null":
                carrerasalva = None
            else:
                carrerasalva = Carrera.objects.filter(id=partes[5])
            message = "uno de los campos no fue ingresado al registrar la Carrera o el Tutor."
            return render(request, 'tutor/agregar_tutor.html',
                          {'message': message, 'form': form,'form1':form1, 'carreras': carreras, 'carrerasalva':carrerasalva})
    else:
        form = GuardarTutorForm()
        form1 = GuardarCarreraForm()
    return render(request, 'tutor/agregar_tutor.html',
                              {'message':message,'form': form,'form1':form1, 'carreras':carreras})


@login_required
@permission_required('gestiontutor.editar_tutor',reverse_lazy('Tutor'))
def editar_tutor(request, tutor_id):
    global partes
    message = None
    carreras = Carrera.objects.all()
    tutor = get_object_or_404(Tutor, pk=tutor_id)
    if request.method == 'POST':
        form = GuardarTutorForm(request.POST, request.FILES, instance=tutor)
        form1 = GuardarCarreraForm(request.POST, request.FILES)
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
            data = {'nombre_tutor': partes[0],
                    'apellido_tutor': partes[1],
                    'cedula_tutor': partes[2],
                    'correo_tutor': partes[4],
                    'telefono_tutor': partes[3],
                    }
            if len(partes[5]) == 0 or partes[5] == "null":
                carrerasalva = None
            else:
                carrerasalva = Carrera.objects.filter(id=partes[5])
            form = GuardarTutorForm(data)
            form1 = GuardarCarreraForm()
            tutor = get_object_or_404(Tutor, pk=tutor_id)
            message1 = "La Carrera a sido registrada con exito."
            return render(request, 'tutor/editar_tutor.html',
                          {'message': message, 'message1': message1, 'form': form, 'form1': form1, 'tutor':tutor, 'carreras': carreras, 'carrerasalva':carrerasalva})
        elif form.is_valid():
            cedula = form.cleaned_data.get('cedula_tutor')
            if len(cedula) == 10:
                if verificar(cedula) is not False:
                    form.save()
                    return redirect('Tutor')
                else:
                    data = {'nombre_tutor': partes[0],
                            'apellido_tutor': partes[1],
                            'cedula_tutor': partes[2],
                            'correo_tutor': partes[4],
                            'telefono_tutor': partes[3],
                            }
                    if len(partes[5]) == 0 or partes[5] == "null":
                        carrerasalva = None
                    else:
                        carrerasalva = Carrera.objects.filter(id=partes[5])
                    form = GuardarTutorForm(data)
                    form1 = GuardarCarreraForm()
                    message = "el numero de cedula es invalido, verifique el numero"
                    return render(request, 'tutor/editar_tutor.html',
                                  {'message': message, 'form': form, 'form1':form1, 'tutor':tutor, 'carreras': carreras, 'carrerasalva':carrerasalva})
            else:
                data = {'nombre_tutor': partes[0],
                        'apellido_tutor': partes[1],
                        'cedula_tutor': partes[2],
                        'correo_tutor': partes[4],
                        'telefono_tutor': partes[3],
                        }
                if len(partes[5]) == 0 or partes[5] == "null":
                    carrerasalva = None
                else:
                    carrerasalva = Carrera.objects.filter(id=partes[5])
                message = "ingrese los 10 digitos de la cedula"
                form = GuardarTutorForm(data)
                form1 = GuardarCarreraForm()
                return render(request, 'tutor/editar_tutor.html',
                              {'message': message, 'form': form, 'form1':form1, 'tutor':tutor, 'carreras': carreras, 'carrerasalva':carrerasalva})

        else:
            data = {'nombre_tutor': partes[0],
                    'apellido_tutor': partes[1],
                    'cedula_tutor': partes[2],
                    'correo_tutor': partes[4],
                    'telefono_tutor': partes[3],
                    }
            if len(partes[5]) == 0 or partes[5] == "null":
                carrerasalva = None
            else:
                carrerasalva = Carrera.objects.filter(id=partes[5])

            form = GuardarTutorForm(data)
            form1 = GuardarCarreraForm(request.POST)
            message = "uno de los campos no fue ingresado al registrar la Carrera o el Tutor."
            return render(request, 'tutor/editar_tutor.html',
                          {'message': message, 'form': form, 'form1':form1, 'tutor':tutor, 'carreras': carreras, 'carrerasalva':carrerasalva})
    else:
        form = GuardarTutorForm(instance=tutor)
        form1 = GuardarCarreraForm()
    return render(request, 'tutor/editar_tutor.html',
                              {'message':message, 'form': form, 'form1':form1, 'tutor':tutor, 'carreras':carreras})


@login_required
@permission_required('gestiontutor.eliminar_tutor',reverse_lazy('Tutor'))
def eliminar_tutor(request, tutor_id):
    tutor = get_object_or_404(Tutor, id=tutor_id)
    tutor.delete()
    return redirect('Tutor')

def verificar(nro):
    l = len(nro)
    if l == 10 : # verificar la longitud correcta
        cp = int(nro[0:2])
        if cp >= 1 and cp <= 22: # verificar codigo de provincia
            tercer_dig = int(nro[2])
            if tercer_dig >= 0 and tercer_dig < 6 : # numeros enter 0 y 6
                if l == 10:
                    return __validar_ced_ruc(nro,0)
            else:
                b = False
                return b
        else:
            b = False
            return b
    else:
        b = False
        return b

def __validar_ced_ruc(nro,tipo):
    global multip, base, d_ver
    total = 0
    if tipo == 0: # cedula y r.u.c persona natural
        base = 10
        d_ver = int(nro[9])# digito verificador
        multip = (2, 1, 2, 1, 2, 1, 2, 1, 2)
    for i in range(0,len(multip)):
        p = int(nro[i]) * multip[i]
        if tipo == 0:
            total+=p if p < 10 else int(str(p)[0])+int(str(p)[1])
        else:
            total+=p
    mod = total % base
    val = base - mod if mod != 0 else 0
    return val == d_ver