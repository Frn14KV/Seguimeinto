from django.urls import reverse_lazy

from gestionautor.models import Autor
from gestionayuda2.form import GuardarForm2
from gestioncarrera.models import Carrera
from django.shortcuts import get_object_or_404, render, redirect
from gestionautor.form import GuardarAutorForm
from gestioncarrera.form import GuardarCarreraForm
from gestionayuda.form import GuardarForm
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def index(request):
    autores = Autor.objects.all().order_by('id')
    return render(request, 'autor/listar_autor.html', {'autores': autores})

def autor_detallado(request, autor_id):
    carreras = Carrera.objects.all()
    autor = get_object_or_404(Autor, pk=autor_id)
    return render(request, 'autor/perfil_autor.html', {'autor': autor, 'carreras':carreras})


@login_required
@permission_required('gestionautor.agregar_autor',reverse_lazy('Autor'))
def guardar_autor(request):
    global partes
    message = None
    carreras = Carrera.objects.all()
    if request.method == 'POST':
        form = GuardarAutorForm(request.POST, request.FILES)
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
            cedula = form.cleaned_data.get('cedula_autor')
            if len(cedula)==10:
                if verificar(cedula) is not False:
                    form.save()
                    return redirect('Autor')
                else:
                    data = {'nombre_autor': partes[0],
                            'apellido_autor': partes[1],
                            'cedula_autor': partes[2],
                            'correo_autor': partes[4],
                            'telefono_autor': partes[3],
                            }
                    if len(partes[5]) == 0 or partes[5] == "null":
                        carrerasalva = None
                    else:
                        carrerasalva = Carrera.objects.filter(id=partes[5])

                    form = GuardarAutorForm(data)
                    form1 = GuardarCarreraForm()
                    message = "el numero de cedula es invalido, verifique el numero"
                    return render(request, 'autor/agregar_autor.html',
                                  {'message': message, 'form': form, 'form1':form1, 'carreras': carreras, 'carrerasalva':carrerasalva})
            else:
                data = {'nombre_autor': partes[0],
                        'apellido_autor': partes[1],
                        'cedula_autor': partes[2],
                        'correo_autor': partes[4],
                        'telefono_autor': partes[3],
                        }
                if len(partes[5]) == 0 or partes[5] == "null":
                    carrerasalva = None
                else:
                    carrerasalva = Carrera.objects.filter(id=partes[5])
                form = GuardarAutorForm(data)
                form1 = GuardarCarreraForm()
                message = "ingrese los 10 digitos de la cedula"
                print(carrerasalva)
                return render(request, 'autor/agregar_autor.html',
                              {'message': message, 'form': form, 'form1':form1, 'carreras': carreras, 'carrerasalva':carrerasalva})
        elif form1.is_valid():
            form1.save()
            data = {'nombre_autor': partes[0],
                    'apellido_autor': partes[1],
                    'cedula_autor':partes[2],
                    'correo_autor': partes[4],
                    'telefono_autor':partes[3],
                    }
            if len(partes[5]) == 0 or partes[5] == "null":
                carrerasalva = None
            else:
                carrerasalva = Carrera.objects.filter(id=partes[5])

            form = GuardarAutorForm(data)
            form1 = GuardarCarreraForm()
            message1 = "La Carrera a sido registrada con exito."
            return render(request, 'autor/agregar_autor.html',
                          {'message': message, 'message1': message1, 'form': form, 'form1': form1, 'carreras': carreras, 'carrerasalva':carrerasalva})
        else:
            data = {'nombre_autor': partes[0],
                    'apellido_autor': partes[1],
                    'cedula_autor': partes[2],
                    'correo_autor': partes[4],
                    'telefono_autor': partes[3],
                    }
            if len(partes[5]) == 0 or partes[5] == "null":
                carrerasalva = None
            else:
                carrerasalva = Carrera.objects.filter(id=partes[5])

            form = GuardarAutorForm(data)
            form1 = GuardarCarreraForm(request.POST)
            message = "uno de los campos no fue ingresado al registrar la Carrera o el Autor."
            return render(request, 'autor/agregar_autor.html',
                          {'message': message, 'form': form,'form1':form1, 'carreras': carreras, 'carrerasalva':carrerasalva})
    else:
        form = GuardarAutorForm()
        form1 =GuardarCarreraForm()
    return render(request, 'autor/agregar_autor.html',
                  {'message':message, 'form': form, 'form1':form1 , 'carreras':carreras})


@login_required
@permission_required('gestionautor.editar_autor',reverse_lazy('Autor'))
def editar_autor(request, autor_id):
    global partes
    message = None
    carreras = Carrera.objects.all()
    autor = get_object_or_404(Autor, pk=autor_id)
    if request.method == 'POST':
        form = GuardarAutorForm(request.POST, request.FILES, instance=autor)
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
            data = {'nombre_autor': partes[0],
                    'apellido_autor': partes[1],
                    'cedula_autor': partes[2],
                    'correo_autor': partes[4],
                    'telefono_autor': partes[3],
                    }
            if len(partes[5]) == 0 or partes[5] == "null":
                carrerasalva = None
            else:
                carrerasalva = Carrera.objects.filter(id=partes[5])

            form = GuardarAutorForm(data)
            form1 = GuardarCarreraForm()
            autor = get_object_or_404(Autor, pk=autor_id)
            message1 = "La Carrera a sido registrada con exito."
            return render(request, 'autor/editar_autor.html',
                          {'message': message, 'message1': message1, 'form': form, 'form1': form1, 'autor':autor, 'carreras': carreras, 'carrerasalva':carrerasalva })
        elif form.is_valid():
            cedula = form.cleaned_data.get('cedula_autor')
            if len(cedula) == 10:
                if verificar(cedula) is not False:
                    form.save()
                    return redirect('Autor')
                else:
                    data = {'nombre_autor': partes[0],
                            'apellido_autor': partes[1],
                            'cedula_autor': partes[2],
                            'correo_autor': partes[4],
                            'telefono_autor': partes[3],
                            }
                    if len(partes[5]) == 0 or partes[5] == "null":
                        carrerasalva = None
                    else:
                        carrerasalva = Carrera.objects.filter(id=partes[5])
                    form = GuardarAutorForm(data)
                    form1 = GuardarCarreraForm()
                    message = "el numero de cedula es invalido, verifique el numero."
                    return render(request, 'autor/editar_autor.html',
                                  {'message': message, 'form': form, 'form1':form1, 'autor':autor, 'carreras': carreras, 'carrerasalva':carrerasalva})
            else:
                data = {'nombre_autor': partes[0],
                        'apellido_autor': partes[1],
                        'cedula_autor': partes[2],
                        'correo_autor': partes[4],
                        'telefono_autor': partes[3],
                        }

                if len(partes[5]) == 0 or partes[5] == "null":
                    carrerasalva = None
                else:
                    carrerasalva = Carrera.objects.filter(id=partes[5])
                print(carrerasalva)
                form = GuardarAutorForm(data)
                form1 = GuardarCarreraForm()
                message = "ingrese los 10 digitos de la cedula"
                autor = get_object_or_404(Autor, pk=autor_id)
                return render(request, 'autor/editar_autor.html',
                              {'message': message, 'form': form, 'form1':form1, 'autor':autor, 'carreras': carreras, 'carrerasalva':carrerasalva})

        else:
            data = {'nombre_autor': partes[0],
                    'apellido_autor': partes[1],
                    'cedula_autor': partes[2],
                    'correo_autor': partes[4],
                    'telefono_autor': partes[3],
                    }
            if len(partes[5]) == 0 or partes[5] == "null":
                carrerasalva = None
            else:
                carrerasalva = Carrera.objects.filter(id=partes[5])
            form = GuardarAutorForm(data)
            form1 = GuardarCarreraForm(request.POST)
            autor = get_object_or_404(Autor, pk=autor_id)
            message1 = "uno de los campos no fue ingresado al registrar la Carrera o el Autor."
            return render(request, 'autor/agregar_autor.html',
                          {'message': message, 'message1': message1, 'form': form, 'form1': form1, 'autor':autor, 'carreras': carreras,'carrerasalva':carrerasalva})
    else:
        form = GuardarAutorForm(instance=autor)
        form1 =GuardarCarreraForm()
    return render(request, 'autor/editar_autor.html',
                              {'message':message, 'form': form,'form1':form1, 'autor':autor, 'carreras':carreras})


@login_required
@permission_required('gestionautor.eliminar_autor',reverse_lazy('Autor'))
def eliminar_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    autor.delete()
    return redirect('Autor')

#verifica la cantidad de numeros de la ceudloa
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

#valida la cedula
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