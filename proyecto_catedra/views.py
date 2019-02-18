from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType

from gestionareaconocimiento.models import AreaConocimiento
from gestionautor.models import Autor
from gestioncarrera.models import Carrera
from gestionimagnes.models import Imagenes
from gestioninstitucion.models import Institucion
from gestionproyecto.models import Proyecto
from gestionayuda10.form import GuardarForm10
from django.shortcuts import redirect, render, get_object_or_404

from gestionresponsableinstitucional.models import ResponsableInstitucional
from gestiontipoproyecto.models import TipoProyecto
from gestiontutor.models import Tutor
from proyecto_catedra.forms import LoginForm, SignUpForm, Edit
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Permission, Group


def login_page(request):
    message = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('homepage')
                else:
                    message = "Tu usuario esta inactivo"
                    return render(request, 'inicio.html', {'message': message, 'form': form})
            else:
                message = "Nombre de usuario y/o password  incorrecto"
                return render(request, 'inicio.html', {'message': message, 'form': form})
    else:
        form = LoginForm()
    return render(request, 'inicio.html', {'message': message, 'form': form})


def homepage(request):
    instituciones = Institucion.objects.all()
    tutores = Tutor.objects.all()
    proyectos = Proyecto.objects.all().order_by('-id')
    imagenes = Imagenes.objects.all()
    return render(request, 'homepage.html', {'proyectos': proyectos, 'instituciones':instituciones,'tutores':tutores,'imagenes':imagenes})

@login_required
def agregar_usuario(request):
    message = None
    global correoer
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        form10 = GuardarForm10(request.POST)

        if form.is_valid():
            if form10.is_valid():
                correoer = form10.cleaned_data.get('email1')
                print(correoer)
            else:
                correoer = None

            correoe = form.cleaned_data.get('email')
            print(correoe)
            if correoe == correoer:
                print("es igual")
                form.save()
                typeuser = form.cleaned_data.get('typeuser')
                #grupo de usuarios
                g_autores, ga1 = Group.objects.get_or_create(name='Autores')
                g_tutores, gt1 = Group.objects.get_or_create(name='Tutores')
                g_responsables, gr1 = Group.objects.get_or_create(name='Responsables')
                g_administradores, gad1 = Group.objects.get_or_create(name='Administradores')
                g_superusuarios, gsp1 = Group.objects.get_or_create(name='SuperUsuarios')

                #contenttype
                cp = ContentType.objects.get_for_model(Proyecto)
                ct = ContentType.objects.get_for_model(Tutor)
                ca = ContentType.objects.get_for_model(Autor)
                ci = ContentType.objects.get_for_model(Institucion)
                cr = ContentType.objects.get_for_model(ResponsableInstitucional)
                ctp = ContentType.objects.get_for_model(TipoProyecto)
                cac = ContentType.objects.get_for_model(AreaConocimiento)
                cc = ContentType.objects.get_for_model(Carrera)

                permiso1p, pp1 = Permission.objects.get_or_create(codename='listar_proyecto', name='Puede listar Proyectos',
                                                                  content_type=cp)
                permiso2p, pp2 = Permission.objects.get_or_create(codename='agregar_proyecto', name='Puede agregar Proyectos',
                                                                  content_type=cp)
                permiso3p, pp3 = Permission.objects.get_or_create(codename='editar_proyecto', name='Puede editarar Proyectos',
                                                                  content_type=cp)
                permiso4p, pp4 = Permission.objects.get_or_create(codename='eliminar_proyecto', name='Puede eliminar Proyectos',
                                                                  content_type=cp)

                permiso1t, pt1 = Permission.objects.get_or_create(codename='listar_tutor', name='Puede listar Tutores',
                                                                  content_type=ct)
                permiso2t, pt2 = Permission.objects.get_or_create(codename='agregar_tutor', name='Puede agregar Tutores',
                                                                  content_type=ct)
                permiso3t, pt3 = Permission.objects.get_or_create(codename='editar_tutor', name='Puede editarar Tutores',
                                                                  content_type=ct)
                permiso4t, pt4 = Permission.objects.get_or_create(codename='eliminar_tutor', name='Puede eliminar Tutores',
                                                                  content_type=ct)

                permiso1a, pal = Permission.objects.get_or_create(codename='listar_autor', name='Puede listar Autores',
                                                                  content_type=ca)
                permiso2a, pa2 = Permission.objects.get_or_create(codename='agregar_autor', name='Puede agregar Autores',
                                                                  content_type=ca)
                permiso3a, pa3 = Permission.objects.get_or_create(codename='editar_autor', name='Puede editarar Autores',
                                                                  content_type=ca)
                permiso4a, pa4 = Permission.objects.get_or_create(codename='eliminar_autor', name='Puede eliminar Autores',
                                                                  content_type=ca)

                permiso1i, pi1 = Permission.objects.get_or_create(codename='listar_institucion', name='Puede listar Instituciones',
                                                                  content_type=ci)
                permiso2i, pi2 = Permission.objects.get_or_create(codename='agregar_institucion', name='Puede agregar Instituciones',
                                                                  content_type=ci)
                permiso3i, pi3 = Permission.objects.get_or_create(codename='editar_institucion', name='Puede editarar Instituciones',
                                                                  content_type=ci)
                permiso4i, pi4 = Permission.objects.get_or_create(codename='eliminar_institucion', name='Puede eliminar Instituciones',
                                                                  content_type=ci)

                permiso1r, pr1 = Permission.objects.get_or_create(codename='listar_responsableinstitucional',
                                                                  name='Puede listar Responsbles',
                                                                  content_type=cr)
                permiso2r, pr2 = Permission.objects.get_or_create(codename='agregar_responsableinstitucional',
                                                                  name='Puede agregar Responsbles',
                                                                  content_type=cr)
                permiso3r, pr3 = Permission.objects.get_or_create(codename='editar_responsableinstitucional',
                                                                  name='Puede editar Responsbles',
                                                                  content_type=cr)
                permiso4r, pr4 = Permission.objects.get_or_create(codename='eliminar_responsableinstitucional',
                                                                  name='Puede eliminar Responsbles',
                                                                  content_type=cr)

                permiso1tp, ptp1 = Permission.objects.get_or_create(codename='listar_tipoproyecto',
                                                                  name='Puede listar Tipo Proyecto',
                                                                  content_type=ctp)
                permiso2tp, ptp2 = Permission.objects.get_or_create(codename='agregar_tipoproyecto',
                                                                  name='Puede agregar Tipo Proyecto',
                                                                  content_type=ctp)
                permiso3tp, ptp3 = Permission.objects.get_or_create(codename='editar_tipoproyecto',
                                                                  name='Puede editar Tipo Proyecto',
                                                                  content_type=ctp)
                permiso4tp, ptp4 = Permission.objects.get_or_create(codename='eliminar_tipoproyecto',
                                                                  name='Puede eliminar Tipo Proyecto',
                                                                  content_type=ctp)

                permiso1ac, pac1 = Permission.objects.get_or_create(codename='listar_areaconocimiento',
                                                                    name='Puede listar Area Conocimiento',
                                                                    content_type=cac)
                permiso2ac, pac2 = Permission.objects.get_or_create(codename='agregar_areaconocimiento',
                                                                    name='Puede agregar Area Conocimiento',
                                                                    content_type=cac)
                permiso3ac, pac3 = Permission.objects.get_or_create(codename='editar_areaconocimiento',
                                                                    name='Puede editar Area Conocimiento',
                                                                    content_type=cac)
                permiso4ac, pac4 = Permission.objects.get_or_create(codename='eliminar_areaconocimiento',
                                                                    name='Puede eliminar Area Conocimiento',
                                                                    content_type=cac)

                permiso1c, pc1 = Permission.objects.get_or_create(codename='listar_carrera',
                                                                    name='Puede listar Carreras',
                                                                    content_type=cc)
                permiso2c, pc2 = Permission.objects.get_or_create(codename='agregar_carrera',
                                                                    name='Puede agregar Carreras',
                                                                    content_type=cc)
                permiso3c, pc3 = Permission.objects.get_or_create(codename='editar_carrera',
                                                                    name='Puede editar Carreras',
                                                                    content_type=cc)
                permiso4c, pc4 = Permission.objects.get_or_create(codename='eliminar_carrera',
                                                                    name='Puede eliminar Carreras',
                                                                    content_type=cc)

                # Tutor con permisos de Proyecto
                g_tutores.permissions.add(permiso1p)
                # Tutor con permisos de tutor
                g_tutores.permissions.add(permiso1t)
                # g_tutores.permissions.add(permiso2t)
                # g_tutores.permissions.add(permiso3t)
                # Tutor con permisos de Tutor
                g_tutores.permissions.add(permiso1a)
                # Tutor con permisos de insittuciones
                g_tutores.permissions.add(permiso1i)
                # Tutor con permisos de responsableinstitucional
                g_tutores.permissions.add(permiso1r)
                # Tutor con permisos de Tipo de Proyecto
                g_tutores.permissions.add(permiso1tp)
                # Tutor con permisos de Area de Conocimiento
                g_tutores.permissions.add(permiso1ac)
                # Tutor con permisos de Carrera
                g_tutores.permissions.add(permiso1c)

                # Autor con permisos de Proyecto
                g_autores.permissions.add(permiso1p)
                # Autor con permisos de tutor
                g_autores.permissions.add(permiso1t)
                # Autor con permisos de autor
                g_autores.permissions.add(permiso1a)
                # g_autores.permissions.add(permiso2a)
                # g_autores.permissions.add(permiso3a)
                # Autor con permisos de insittuciones
                g_autores.permissions.add(permiso1i)
                # Autor con permisos de responsableinstitucional
                g_autores.permissions.add(permiso1r)
                # Autor con permisos de Tipo de Proyecto
                g_autores.permissions.add(permiso1tp)
                # Autor con permisos de Area de Conocimiento
                g_autores.permissions.add(permiso1ac)
                # Autor con permisos de Carrera
                g_autores.permissions.add(permiso1c)

                # Responsable con permisos de Proyecto
                g_responsables.permissions.add(permiso1p)
                # Responsable con permisos de tutor
                g_responsables.permissions.add(permiso1p)
                # Responsable con permisos de autor
                g_responsables.permissions.add(permiso1a)
                # Responsable con permisos de insittuciones
                g_responsables.permissions.add(permiso1i)
                # Responsable con permisos de responsableinstitucional
                g_responsables.permissions.add(permiso1r)
                # g_responsables.permissions.add(permiso2r)
                # g_responsables.permissions.add(permiso3r)
                # Responsable con permisos de Tipo de Proyecto
                g_responsables.permissions.add(permiso1tp)
                # Responsable con permisos de Area de Conocimiento
                g_responsables.permissions.add(permiso1ac)
                # Responsable con permisos de Carrera
                g_responsables.permissions.add(permiso1c)

                # Administrador con permisos de Proyecto
                g_administradores.permissions.add(permiso1p)
                g_administradores.permissions.add(permiso2p)
                g_administradores.permissions.add(permiso3p)
                g_administradores.permissions.add(permiso4p)
                # Administrador con permisos de tutor
                g_administradores.permissions.add(permiso1t)
                g_administradores.permissions.add(permiso2t)
                g_administradores.permissions.add(permiso3t)
                g_administradores.permissions.add(permiso4t)
                # Administrador con permisos de autor
                g_administradores.permissions.add(permiso1a)
                g_administradores.permissions.add(permiso2a)
                g_administradores.permissions.add(permiso3a)
                g_administradores.permissions.add(permiso4a)
                # Administrador con permisos de instituciones
                g_administradores.permissions.add(permiso1i)
                g_administradores.permissions.add(permiso2i)
                g_administradores.permissions.add(permiso3i)
                g_administradores.permissions.add(permiso4i)
                # Administrador con permisos de responsableinstitucional
                g_administradores.permissions.add(permiso1r)
                g_administradores.permissions.add(permiso2r)
                g_administradores.permissions.add(permiso3r)
                g_administradores.permissions.add(permiso4r)
                # Administrador con permisos de Tipo de Proyecto
                g_administradores.permissions.add(permiso1tp)
                g_administradores.permissions.add(permiso2tp)
                g_administradores.permissions.add(permiso3tp)
                g_administradores.permissions.add(permiso4tp)
                # Administrador con permisos de Area de Conocimiento
                g_administradores.permissions.add(permiso1ac)
                g_administradores.permissions.add(permiso2ac)
                g_administradores.permissions.add(permiso3ac)
                g_administradores.permissions.add(permiso4ac)
                # Administrador con permisos de Carrera
                g_administradores.permissions.add(permiso1c)
                g_administradores.permissions.add(permiso2c)
                g_administradores.permissions.add(permiso3c)
                g_administradores.permissions.add(permiso4c)

                # super usuario con permisos de Proyecto
                g_superusuarios.permissions.add(permiso1p)
                g_superusuarios.permissions.add(permiso2p)
                g_superusuarios.permissions.add(permiso3p)
                g_superusuarios.permissions.add(permiso4p)
                # super usuario con permisos de tutor
                g_superusuarios.permissions.add(permiso1t)
                g_superusuarios.permissions.add(permiso2t)
                g_superusuarios.permissions.add(permiso3t)
                g_superusuarios.permissions.add(permiso4t)
                #super usuario con permisos de autor
                g_superusuarios.permissions.add(permiso1a)
                g_superusuarios.permissions.add(permiso2a)
                g_superusuarios.permissions.add(permiso3a)
                g_superusuarios.permissions.add(permiso4a)
                # super usuario con permisos de Insituciones
                g_superusuarios.permissions.add(permiso1i)
                g_superusuarios.permissions.add(permiso2i)
                g_superusuarios.permissions.add(permiso3i)
                g_superusuarios.permissions.add(permiso4i)
                # super usuario con permisos de responsableinstitucional
                g_superusuarios.permissions.add(permiso1r)
                g_superusuarios.permissions.add(permiso2r)
                g_superusuarios.permissions.add(permiso3r)
                g_superusuarios.permissions.add(permiso4r)
                # super usuario con permisos de Tipo de Proyecto
                g_superusuarios.permissions.add(permiso1tp)
                g_superusuarios.permissions.add(permiso2tp)
                g_superusuarios.permissions.add(permiso3tp)
                g_superusuarios.permissions.add(permiso4tp)
                # super usuario con permisos de Area de Conocimiento
                g_superusuarios.permissions.add(permiso1ac)
                g_superusuarios.permissions.add(permiso2ac)
                g_superusuarios.permissions.add(permiso3ac)
                g_superusuarios.permissions.add(permiso4ac)
                # super usuario con permisos de Carrera
                g_superusuarios.permissions.add(permiso1c)
                g_superusuarios.permissions.add(permiso2c)
                g_superusuarios.permissions.add(permiso3c)
                g_superusuarios.permissions.add(permiso4c)

                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                # user =User.objects.get(username=request.POST.get('username'))

                if typeuser =='Autores':
                    user.groups.add(g_autores)
                elif typeuser == 'Tutores':
                    user.groups.add(g_tutores)
                elif typeuser == 'Responsables':
                    user.groups.add(g_responsables)
                elif typeuser == 'Administradores':
                    user.groups.add(g_administradores)
                elif typeuser == 'Superusuarios':
                    user.groups.add(g_superusuarios)
                else:
                    print(" ")

                return redirect('usuarios')
            else:
                message = "Al parecer los correos no son iguales. "
                return render(request, 'usuario/agregar_usuario.html', {'message': message, 'form': form, 'form10':form10})
        else:
            form = SignUpForm(request.POST)
            form10 = GuardarForm10(request.POST)
            m = form.errors.as_json()
            partes = m.split('message')
            a= None
            print(len(partes))
            if (len(partes))==2:
                mt = partes[1].split(',')
                a=mt[0].split('"')
                message = a[2]
            elif (len(partes))==3:
                mt = partes[1].split(',')
                mt1 = partes[2].split(',')
                a = mt[0].split('"')
                a1 = mt1[0].split('"')
                message = (a[2]+a1[2])
            elif (len(partes))==4:
                mt = partes[1].split(',')
                mt1 = partes[2].split(',')
                mt2 = partes[3].split(',')
                a = mt[0].split('"')
                a1 = mt1[0].split('"')
                a2 = mt2[0].split('"')
                message = (a[2]+a1[2]+a2[2])

            return render(request, 'usuario/agregar_usuario.html', {'message': message, 'form': form, 'form10':form10})
    else:
        form = SignUpForm()
        form10 = GuardarForm10()
    return render(request, 'usuario/agregar_usuario.html', {'message': message, 'form': form, 'form10':form10})


def registro(request):
    message = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        form10 = GuardarForm10(request.POST)
        if form.is_valid():
            if form10.is_valid():
                correoer = form10.cleaned_data.get('email1')
                print(correoer)
            else:
                correoer = None

            correoe = form.cleaned_data.get('email')
            print(correoe)
            if correoe == correoer:
                form.save()
                typeuser = form.cleaned_data.get('typeuser')
                #grupo de usuarios
                g_autores, ga1 = Group.objects.get_or_create(name='Autores')
                g_tutores, gt1 = Group.objects.get_or_create(name='Tutores')
                g_responsables, gr1 = Group.objects.get_or_create(name='Responsables')
                g_administradores, gad1 = Group.objects.get_or_create(name='Administradores')
                g_superusuarios, gsp1 = Group.objects.get_or_create(name='SuperUsuarios')

                #contenttype
                cp = ContentType.objects.get_for_model(Proyecto)
                ct = ContentType.objects.get_for_model(Tutor)
                ca = ContentType.objects.get_for_model(Autor)
                ci = ContentType.objects.get_for_model(Institucion)
                cr = ContentType.objects.get_for_model(ResponsableInstitucional)
                ctp = ContentType.objects.get_for_model(TipoProyecto)
                cac = ContentType.objects.get_for_model(AreaConocimiento)
                cc = ContentType.objects.get_for_model(Carrera)

                permiso1p, pp1 = Permission.objects.get_or_create(codename='listar_proyecto', name='Puede listar Proyectos',
                                                                  content_type=cp)
                permiso2p, pp2 = Permission.objects.get_or_create(codename='agregar_proyecto', name='Puede agregar Proyectos',
                                                                  content_type=cp)
                permiso3p, pp3 = Permission.objects.get_or_create(codename='editar_proyecto', name='Puede editarar Proyectos',
                                                                  content_type=cp)
                permiso4p, pp4 = Permission.objects.get_or_create(codename='eliminar_proyecto', name='Puede eliminar Proyectos',
                                                                  content_type=cp)

                permiso1t, pt1 = Permission.objects.get_or_create(codename='listar_tutor', name='Puede listar Tutores',
                                                                  content_type=ct)
                permiso2t, pt2 = Permission.objects.get_or_create(codename='agregar_tutor', name='Puede agregar Tutores',
                                                                  content_type=ct)
                permiso3t, pt3 = Permission.objects.get_or_create(codename='editar_tutor', name='Puede editarar Tutores',
                                                                  content_type=ct)
                permiso4t, pt4 = Permission.objects.get_or_create(codename='eliminar_tutor', name='Puede eliminar Tutores',
                                                                  content_type=ct)

                permiso1a, pal = Permission.objects.get_or_create(codename='listar_autor', name='Puede listar Autores',
                                                                  content_type=ca)
                permiso2a, pa2 = Permission.objects.get_or_create(codename='agregar_autor', name='Puede agregar Autores',
                                                                  content_type=ca)
                permiso3a, pa3 = Permission.objects.get_or_create(codename='editar_autor', name='Puede editarar Autores',
                                                                  content_type=ca)
                permiso4a, pa4 = Permission.objects.get_or_create(codename='eliminar_autor', name='Puede eliminar Autores',
                                                                  content_type=ca)

                permiso1i, pi1 = Permission.objects.get_or_create(codename='listar_institucion', name='Puede listar Instituciones',
                                                                  content_type=ci)
                permiso2i, pi2 = Permission.objects.get_or_create(codename='agregar_institucion', name='Puede agregar Instituciones',
                                                                  content_type=ci)
                permiso3i, pi3 = Permission.objects.get_or_create(codename='editar_institucion', name='Puede editarar Instituciones',
                                                                  content_type=ci)
                permiso4i, pi4 = Permission.objects.get_or_create(codename='eliminar_institucion', name='Puede eliminar Instituciones',
                                                                  content_type=ci)

                permiso1r, pr1 = Permission.objects.get_or_create(codename='listar_responsableinstitucional',
                                                                  name='Puede listar Responsbles',
                                                                  content_type=cr)
                permiso2r, pr2 = Permission.objects.get_or_create(codename='agregar_responsableinstitucional',
                                                                  name='Puede agregar Responsbles',
                                                                  content_type=cr)
                permiso3r, pr3 = Permission.objects.get_or_create(codename='editar_responsableinstitucional',
                                                                  name='Puede editar Responsbles',
                                                                  content_type=cr)
                permiso4r, pr4 = Permission.objects.get_or_create(codename='eliminar_responsableinstitucional',
                                                                  name='Puede eliminar Responsbles',
                                                                  content_type=cr)

                permiso1tp, ptp1 = Permission.objects.get_or_create(codename='listar_tipoproyecto',
                                                                  name='Puede listar Tipo Proyecto',
                                                                  content_type=ctp)
                permiso2tp, ptp2 = Permission.objects.get_or_create(codename='agregar_tipoproyecto',
                                                                  name='Puede agregar Tipo Proyecto',
                                                                  content_type=ctp)
                permiso3tp, ptp3 = Permission.objects.get_or_create(codename='editar_tipoproyecto',
                                                                  name='Puede editar Tipo Proyecto',
                                                                  content_type=ctp)
                permiso4tp, ptp4 = Permission.objects.get_or_create(codename='eliminar_tipoproyecto',
                                                                  name='Puede eliminar Tipo Proyecto',
                                                                  content_type=ctp)

                permiso1ac, pac1 = Permission.objects.get_or_create(codename='listar_areaconocimiento',
                                                                    name='Puede listar Area Conocimiento',
                                                                    content_type=cac)
                permiso2ac, pac2 = Permission.objects.get_or_create(codename='agregar_areaconocimiento',
                                                                    name='Puede agregar Area Conocimiento',
                                                                    content_type=cac)
                permiso3ac, pac3 = Permission.objects.get_or_create(codename='editar_areaconocimiento',
                                                                    name='Puede editar Area Conocimiento',
                                                                    content_type=cac)
                permiso4ac, pac4 = Permission.objects.get_or_create(codename='eliminar_areaconocimiento',
                                                                    name='Puede eliminar Area Conocimiento',
                                                                    content_type=cac)

                permiso1c, pc1 = Permission.objects.get_or_create(codename='listar_carrera',
                                                                    name='Puede listar Carreras',
                                                                    content_type=cc)
                permiso2c, pc2 = Permission.objects.get_or_create(codename='agregar_carrera',
                                                                    name='Puede agregar Carreras',
                                                                    content_type=cc)
                permiso3c, pc3 = Permission.objects.get_or_create(codename='editar_carrera',
                                                                    name='Puede editar Carreras',
                                                                    content_type=cc)
                permiso4c, pc4 = Permission.objects.get_or_create(codename='eliminar_carrera',
                                                                    name='Puede eliminar Carreras',
                                                                    content_type=cc)

                # Tutor con permisos de Proyecto
                g_tutores.permissions.add(permiso1p)
                # Tutor con permisos de tutor
                g_tutores.permissions.add(permiso1t)
                # g_tutores.permissions.add(permiso2t)
                # g_tutores.permissions.add(permiso3t)
                # Tutor con permisos de Tutor
                g_tutores.permissions.add(permiso1a)
                # Tutor con permisos de insittuciones
                g_tutores.permissions.add(permiso1i)
                # Tutor con permisos de responsableinstitucional
                g_tutores.permissions.add(permiso1r)
                # Tutor con permisos de Tipo de Proyecto
                g_tutores.permissions.add(permiso1tp)
                # Tutor con permisos de Area de Conocimiento
                g_tutores.permissions.add(permiso1ac)
                # Tutor con permisos de Carrera
                g_tutores.permissions.add(permiso1c)

                # Autor con permisos de Proyecto
                g_autores.permissions.add(permiso1p)
                # Autor con permisos de tutor
                g_autores.permissions.add(permiso1t)
                # Autor con permisos de autor
                g_autores.permissions.add(permiso1a)
                # g_autores.permissions.add(permiso2a)
                # g_autores.permissions.add(permiso3a)
                # Autor con permisos de insittuciones
                g_autores.permissions.add(permiso1i)
                # Autor con permisos de responsableinstitucional
                g_autores.permissions.add(permiso1r)
                # Autor con permisos de Tipo de Proyecto
                g_autores.permissions.add(permiso1tp)
                # Autor con permisos de Area de Conocimiento
                g_autores.permissions.add(permiso1ac)
                # Autor con permisos de Carrera
                g_autores.permissions.add(permiso1c)

                # Responsable con permisos de Proyecto
                g_responsables.permissions.add(permiso1p)
                # Responsable con permisos de tutor
                g_responsables.permissions.add(permiso1p)
                # Responsable con permisos de autor
                g_responsables.permissions.add(permiso1a)
                # Responsable con permisos de insittuciones
                g_responsables.permissions.add(permiso1i)
                # Responsable con permisos de responsableinstitucional
                g_responsables.permissions.add(permiso1r)
                # g_responsables.permissions.add(permiso2r)
                # g_responsables.permissions.add(permiso3r)
                # Responsable con permisos de Tipo de Proyecto
                g_responsables.permissions.add(permiso1tp)
                # Responsable con permisos de Area de Conocimiento
                g_responsables.permissions.add(permiso1ac)
                # Responsable con permisos de Carrera
                g_responsables.permissions.add(permiso1c)

                # Administrador con permisos de Proyecto
                g_administradores.permissions.add(permiso1p)
                g_administradores.permissions.add(permiso2p)
                g_administradores.permissions.add(permiso3p)
                g_administradores.permissions.add(permiso4p)
                # Administrador con permisos de tutor
                g_administradores.permissions.add(permiso1t)
                g_administradores.permissions.add(permiso2t)
                g_administradores.permissions.add(permiso3t)
                g_administradores.permissions.add(permiso4t)
                # Administrador con permisos de autor
                g_administradores.permissions.add(permiso1a)
                g_administradores.permissions.add(permiso2a)
                g_administradores.permissions.add(permiso3a)
                g_administradores.permissions.add(permiso4a)
                # Administrador con permisos de instituciones
                g_administradores.permissions.add(permiso1i)
                g_administradores.permissions.add(permiso2i)
                g_administradores.permissions.add(permiso3i)
                g_administradores.permissions.add(permiso4i)
                # Administrador con permisos de responsableinstitucional
                g_administradores.permissions.add(permiso1r)
                g_administradores.permissions.add(permiso2r)
                g_administradores.permissions.add(permiso3r)
                g_administradores.permissions.add(permiso4r)
                # Administrador con permisos de Tipo de Proyecto
                g_administradores.permissions.add(permiso1tp)
                g_administradores.permissions.add(permiso2tp)
                g_administradores.permissions.add(permiso3tp)
                g_administradores.permissions.add(permiso4tp)
                # Administrador con permisos de Area de Conocimiento
                g_administradores.permissions.add(permiso1ac)
                g_administradores.permissions.add(permiso2ac)
                g_administradores.permissions.add(permiso3ac)
                g_administradores.permissions.add(permiso4ac)
                # Administrador con permisos de Carrera
                g_administradores.permissions.add(permiso1c)
                g_administradores.permissions.add(permiso2c)
                g_administradores.permissions.add(permiso3c)
                g_administradores.permissions.add(permiso4c)

                # super usuario con permisos de Proyecto
                g_superusuarios.permissions.add(permiso1p)
                g_superusuarios.permissions.add(permiso2p)
                g_superusuarios.permissions.add(permiso3p)
                g_superusuarios.permissions.add(permiso4p)
                # super usuario con permisos de tutor
                g_superusuarios.permissions.add(permiso1t)
                g_superusuarios.permissions.add(permiso2t)
                g_superusuarios.permissions.add(permiso3t)
                g_superusuarios.permissions.add(permiso4t)
                #super usuario con permisos de autor
                g_superusuarios.permissions.add(permiso1a)
                g_superusuarios.permissions.add(permiso2a)
                g_superusuarios.permissions.add(permiso3a)
                g_superusuarios.permissions.add(permiso4a)
                # super usuario con permisos de Insituciones
                g_superusuarios.permissions.add(permiso1i)
                g_superusuarios.permissions.add(permiso2i)
                g_superusuarios.permissions.add(permiso3i)
                g_superusuarios.permissions.add(permiso4i)
                # super usuario con permisos de responsableinstitucional
                g_superusuarios.permissions.add(permiso1r)
                g_superusuarios.permissions.add(permiso2r)
                g_superusuarios.permissions.add(permiso3r)
                g_superusuarios.permissions.add(permiso4r)
                # super usuario con permisos de Tipo de Proyecto
                g_superusuarios.permissions.add(permiso1tp)
                g_superusuarios.permissions.add(permiso2tp)
                g_superusuarios.permissions.add(permiso3tp)
                g_superusuarios.permissions.add(permiso4tp)
                # super usuario con permisos de Area de Conocimiento
                g_superusuarios.permissions.add(permiso1ac)
                g_superusuarios.permissions.add(permiso2ac)
                g_superusuarios.permissions.add(permiso3ac)
                g_superusuarios.permissions.add(permiso4ac)
                # super usuario con permisos de Carrera
                g_superusuarios.permissions.add(permiso1c)
                g_superusuarios.permissions.add(permiso2c)
                g_superusuarios.permissions.add(permiso3c)
                g_superusuarios.permissions.add(permiso4c)


                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                # user =User.objects.get(username=request.POST.get('username'))

                if typeuser =='Autores':
                    user.groups.add(g_autores)
                elif typeuser == 'Tutores':
                    user.groups.add(g_tutores)
                elif typeuser == 'Responsables':
                    user.groups.add(g_responsables)
                elif typeuser == 'Administradores':
                    user.groups.add(g_administradores)
                elif typeuser == 'Superusuarios':
                    user.groups.add(g_superusuarios)
                else:
                    print(" ")


                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('homepage')
                    else:
                        message = "Tu usuario esta inactivo"
                        return render(request, 'registro.html', {'message': message, 'form': form})
            else:
                message = "Al parecer los correos no son iguales."
                return render(request, 'registro.html',
                                  {'message': message, 'form': form, 'form10': form10})
        else:
            form = SignUpForm(request.POST)
            form10 = GuardarForm10(request.POST)
            m = form.errors.as_json()
            partes = m.split('message')
            a = None
            print(len(partes))
            if (len(partes)) == 2:
                mt = partes[1].split(',')
                a = mt[0].split('"')
                message = a[2]
            elif (len(partes)) == 3:
                mt = partes[1].split(',')
                mt1 = partes[2].split(',')
                a = mt[0].split('"')
                a1 = mt1[0].split('"')
                message = (a[2] + a1[2])
            elif (len(partes)) == 4:
                mt = partes[1].split(',')
                mt1 = partes[2].split(',')
                mt2 = partes[3].split(',')
                a = mt[0].split('"')
                a1 = mt1[0].split('"')
                a2 = mt2[0].split('"')
                message = (a[2] + a1[2] + a2[2])

            return render(request, 'registro.html',
                              {'message': message, 'form': form, 'form10': form10})
    else:
        form = UserCreationForm()
        form10 = GuardarForm10()
    return render(request, 'registro.html', {'message': message, 'form': form, 'form10': form10})

def registroad(request):
    message = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        form10 = GuardarForm10(request.POST)

        if form.is_valid():
            if form10.is_valid():
                correoer = form10.cleaned_data.get('email1')
                print(correoer)
            else:
                correoer = None

            correoe = form.cleaned_data.get('email')
            print(correoe)
            if correoe == correoer:
                form.save()
                typeuser = form.cleaned_data.get('typeuser')

                #grupo de usuarios
                g_autores, ga1 = Group.objects.get_or_create(name='Autores')
                g_tutores, gt1 = Group.objects.get_or_create(name='Tutores')
                g_responsables, gr1 = Group.objects.get_or_create(name='Responsables')
                g_administradores, gad1 = Group.objects.get_or_create(name='Administradores')
                g_superusuarios, gsp1 = Group.objects.get_or_create(name='SuperUsuarios')

                #contenttype
                cp = ContentType.objects.get_for_model(Proyecto)
                ct = ContentType.objects.get_for_model(Tutor)
                ca = ContentType.objects.get_for_model(Autor)
                ci = ContentType.objects.get_for_model(Institucion)
                cr = ContentType.objects.get_for_model(ResponsableInstitucional)
                ctp = ContentType.objects.get_for_model(TipoProyecto)
                cac = ContentType.objects.get_for_model(AreaConocimiento)
                cc = ContentType.objects.get_for_model(Carrera)

                permiso1p, pp1 = Permission.objects.get_or_create(codename='listar_proyecto', name='Puede listar Proyectos',
                                                                  content_type=cp)
                permiso2p, pp2 = Permission.objects.get_or_create(codename='agregar_proyecto', name='Puede agregar Proyectos',
                                                                  content_type=cp)
                permiso3p, pp3 = Permission.objects.get_or_create(codename='editar_proyecto', name='Puede editarar Proyectos',
                                                                  content_type=cp)
                permiso4p, pp4 = Permission.objects.get_or_create(codename='eliminar_proyecto', name='Puede eliminar Proyectos',
                                                                  content_type=cp)

                permiso1t, pt1 = Permission.objects.get_or_create(codename='listar_tutor', name='Puede listar Tutores',
                                                                  content_type=ct)
                permiso2t, pt2 = Permission.objects.get_or_create(codename='agregar_tutor', name='Puede agregar Tutores',
                                                                  content_type=ct)
                permiso3t, pt3 = Permission.objects.get_or_create(codename='editar_tutor', name='Puede editarar Tutores',
                                                                  content_type=ct)
                permiso4t, pt4 = Permission.objects.get_or_create(codename='eliminar_tutor', name='Puede eliminar Tutores',
                                                                  content_type=ct)

                permiso1a, pal = Permission.objects.get_or_create(codename='listar_autor', name='Puede listar Autores',
                                                                  content_type=ca)
                permiso2a, pa2 = Permission.objects.get_or_create(codename='agregar_autor', name='Puede agregar Autores',
                                                                  content_type=ca)
                permiso3a, pa3 = Permission.objects.get_or_create(codename='editar_autor', name='Puede editarar Autores',
                                                                  content_type=ca)
                permiso4a, pa4 = Permission.objects.get_or_create(codename='eliminar_autor', name='Puede eliminar Autores',
                                                                  content_type=ca)

                permiso1i, pi1 = Permission.objects.get_or_create(codename='listar_institucion', name='Puede listar Instituciones',
                                                                  content_type=ci)
                permiso2i, pi2 = Permission.objects.get_or_create(codename='agregar_institucion', name='Puede agregar Instituciones',
                                                                  content_type=ci)
                permiso3i, pi3 = Permission.objects.get_or_create(codename='editar_institucion', name='Puede editarar Instituciones',
                                                                  content_type=ci)
                permiso4i, pi4 = Permission.objects.get_or_create(codename='eliminar_institucion', name='Puede eliminar Instituciones',
                                                                  content_type=ci)

                permiso1r, pr1 = Permission.objects.get_or_create(codename='listar_responsableinstitucional',
                                                                  name='Puede listar Responsbles',
                                                                  content_type=cr)
                permiso2r, pr2 = Permission.objects.get_or_create(codename='agregar_responsableinstitucional',
                                                                  name='Puede agregar Responsbles',
                                                                  content_type=cr)
                permiso3r, pr3 = Permission.objects.get_or_create(codename='editar_responsableinstitucional',
                                                                  name='Puede editar Responsbles',
                                                                  content_type=cr)
                permiso4r, pr4 = Permission.objects.get_or_create(codename='eliminar_responsableinstitucional',
                                                                  name='Puede eliminar Responsbles',
                                                                  content_type=cr)

                permiso1tp, ptp1 = Permission.objects.get_or_create(codename='listar_tipoproyecto',
                                                                  name='Puede listar Tipo Proyecto',
                                                                  content_type=ctp)
                permiso2tp, ptp2 = Permission.objects.get_or_create(codename='agregar_tipoproyecto',
                                                                  name='Puede agregar Tipo Proyecto',
                                                                  content_type=ctp)
                permiso3tp, ptp3 = Permission.objects.get_or_create(codename='editar_tipoproyecto',
                                                                  name='Puede editar Tipo Proyecto',
                                                                  content_type=ctp)
                permiso4tp, ptp4 = Permission.objects.get_or_create(codename='eliminar_tipoproyecto',
                                                                  name='Puede eliminar Tipo Proyecto',
                                                                  content_type=ctp)

                permiso1ac, pac1 = Permission.objects.get_or_create(codename='listar_areaconocimiento',
                                                                    name='Puede listar Area Conocimiento',
                                                                    content_type=cac)
                permiso2ac, pac2 = Permission.objects.get_or_create(codename='agregar_areaconocimiento',
                                                                    name='Puede agregar Area Conocimiento',
                                                                    content_type=cac)
                permiso3ac, pac3 = Permission.objects.get_or_create(codename='editar_areaconocimiento',
                                                                    name='Puede editar Area Conocimiento',
                                                                    content_type=cac)
                permiso4ac, pac4 = Permission.objects.get_or_create(codename='eliminar_areaconocimiento',
                                                                    name='Puede eliminar Area Conocimiento',
                                                                    content_type=cac)

                permiso1c, pc1 = Permission.objects.get_or_create(codename='listar_carrera',
                                                                    name='Puede listar Carreras',
                                                                    content_type=cc)
                permiso2c, pc2 = Permission.objects.get_or_create(codename='agregar_carrera',
                                                                    name='Puede agregar Carreras',
                                                                    content_type=cc)
                permiso3c, pc3 = Permission.objects.get_or_create(codename='editar_carrera',
                                                                    name='Puede editar Carreras',
                                                                    content_type=cc)
                permiso4c, pc4 = Permission.objects.get_or_create(codename='eliminar_carrera',
                                                                    name='Puede eliminar Carreras',
                                                                    content_type=cc)

                # Tutor con permisos de Proyecto
                g_tutores.permissions.add(permiso1p)
                # Tutor con permisos de tutor
                g_tutores.permissions.add(permiso1t)
                #g_tutores.permissions.add(permiso2t)
                #g_tutores.permissions.add(permiso3t)
                # Tutor con permisos de Tutor
                g_tutores.permissions.add(permiso1a)
                # Tutor con permisos de insittuciones
                g_tutores.permissions.add(permiso1i)
                # Tutor con permisos de responsableinstitucional
                g_tutores.permissions.add(permiso1r)
                # Tutor con permisos de Tipo de Proyecto
                g_tutores.permissions.add(permiso1tp)
                # Tutor con permisos de Area de Conocimiento
                g_tutores.permissions.add(permiso1ac)
                # Tutor con permisos de Carrera
                g_tutores.permissions.add(permiso1c)

                # Autor con permisos de Proyecto
                g_autores.permissions.add(permiso1p)
                # Autor con permisos de tutor
                g_autores.permissions.add(permiso1t)
                # Autor con permisos de autor
                g_autores.permissions.add(permiso1a)
                #g_autores.permissions.add(permiso2a)
                #g_autores.permissions.add(permiso3a)
                # Autor con permisos de insittuciones
                g_autores.permissions.add(permiso1i)
                # Autor con permisos de responsableinstitucional
                g_autores.permissions.add(permiso1r)
                # Autor con permisos de Tipo de Proyecto
                g_autores.permissions.add(permiso1tp)
                # Autor con permisos de Area de Conocimiento
                g_autores.permissions.add(permiso1ac)
                # Autor con permisos de Carrera
                g_autores.permissions.add(permiso1c)

                # Responsable con permisos de Proyecto
                g_responsables.permissions.add(permiso1p)
                # Responsable con permisos de tutor
                g_responsables.permissions.add(permiso1p)
                # Responsable con permisos de autor
                g_responsables.permissions.add(permiso1a)
                # Responsable con permisos de insittuciones
                g_responsables.permissions.add(permiso1i)
                # Responsable con permisos de responsableinstitucional
                g_responsables.permissions.add(permiso1r)
                #g_responsables.permissions.add(permiso2r)
                #g_responsables.permissions.add(permiso3r)
                # Responsable con permisos de Tipo de Proyecto
                g_responsables.permissions.add(permiso1tp)
                # Responsable con permisos de Area de Conocimiento
                g_responsables.permissions.add(permiso1ac)
                # Responsable con permisos de Carrera
                g_responsables.permissions.add(permiso1c)

                # Administrador con permisos de Proyecto
                g_administradores.permissions.add(permiso1p)
                g_administradores.permissions.add(permiso2p)
                g_administradores.permissions.add(permiso3p)
                g_administradores.permissions.add(permiso4p)
                # Administrador con permisos de tutor
                g_administradores.permissions.add(permiso1t)
                g_administradores.permissions.add(permiso2t)
                g_administradores.permissions.add(permiso3t)
                g_administradores.permissions.add(permiso4t)
                # Administrador con permisos de autor
                g_administradores.permissions.add(permiso1a)
                g_administradores.permissions.add(permiso2a)
                g_administradores.permissions.add(permiso3a)
                g_administradores.permissions.add(permiso4a)
                # Administrador con permisos de instituciones
                g_administradores.permissions.add(permiso1i)
                g_administradores.permissions.add(permiso2i)
                g_administradores.permissions.add(permiso3i)
                g_administradores.permissions.add(permiso4i)
                # Administrador con permisos de responsableinstitucional
                g_administradores.permissions.add(permiso1r)
                g_administradores.permissions.add(permiso2r)
                g_administradores.permissions.add(permiso3r)
                g_administradores.permissions.add(permiso4r)
                # Administrador con permisos de Tipo de Proyecto
                g_administradores.permissions.add(permiso1tp)
                g_administradores.permissions.add(permiso2tp)
                g_administradores.permissions.add(permiso3tp)
                g_administradores.permissions.add(permiso4tp)
                # Administrador con permisos de Area de Conocimiento
                g_administradores.permissions.add(permiso1ac)
                g_administradores.permissions.add(permiso2ac)
                g_administradores.permissions.add(permiso3ac)
                g_administradores.permissions.add(permiso4ac)
                # Administrador con permisos de Carrera
                g_administradores.permissions.add(permiso1c)
                g_administradores.permissions.add(permiso2c)
                g_administradores.permissions.add(permiso3c)
                g_administradores.permissions.add(permiso4c)

                # super usuario con permisos de Proyecto
                g_superusuarios.permissions.add(permiso1p)
                g_superusuarios.permissions.add(permiso2p)
                g_superusuarios.permissions.add(permiso3p)
                g_superusuarios.permissions.add(permiso4p)
                # super usuario con permisos de tutor
                g_superusuarios.permissions.add(permiso1t)
                g_superusuarios.permissions.add(permiso2t)
                g_superusuarios.permissions.add(permiso3t)
                g_superusuarios.permissions.add(permiso4t)
                #super usuario con permisos de autor
                g_superusuarios.permissions.add(permiso1a)
                g_superusuarios.permissions.add(permiso2a)
                g_superusuarios.permissions.add(permiso3a)
                g_superusuarios.permissions.add(permiso4a)
                # super usuario con permisos de Insituciones
                g_superusuarios.permissions.add(permiso1i)
                g_superusuarios.permissions.add(permiso2i)
                g_superusuarios.permissions.add(permiso3i)
                g_superusuarios.permissions.add(permiso4i)
                # super usuario con permisos de responsableinstitucional
                g_superusuarios.permissions.add(permiso1r)
                g_superusuarios.permissions.add(permiso2r)
                g_superusuarios.permissions.add(permiso3r)
                g_superusuarios.permissions.add(permiso4r)
                # super usuario con permisos de Tipo de Proyecto
                g_superusuarios.permissions.add(permiso1tp)
                g_superusuarios.permissions.add(permiso2tp)
                g_superusuarios.permissions.add(permiso3tp)
                g_superusuarios.permissions.add(permiso4tp)
                # super usuario con permisos de Area de Conocimiento
                g_superusuarios.permissions.add(permiso1ac)
                g_superusuarios.permissions.add(permiso2ac)
                g_superusuarios.permissions.add(permiso3ac)
                g_superusuarios.permissions.add(permiso4ac)
                # super usuario con permisos de Carrera
                g_superusuarios.permissions.add(permiso1c)
                g_superusuarios.permissions.add(permiso2c)
                g_superusuarios.permissions.add(permiso3c)
                g_superusuarios.permissions.add(permiso4c)

                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                # user =User.objects.get(username=request.POST.get('username'))

                if typeuser =='Autores':
                    user.groups.add(g_autores)
                elif typeuser == 'Tutores':
                    user.groups.add(g_tutores)
                elif typeuser == 'Responsables':
                    user.groups.add(g_responsables)
                elif typeuser == 'Administradores':
                    user.groups.add(g_administradores)
                elif typeuser == 'Superusuarios':
                    user.groups.add(g_superusuarios)
                else:
                    print(" ")
                    #print("aquisp")

                #print(typeuser)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('homepage')
                    else:
                        message = "Tu usuario esta inactivo"
                        return render(request, 'usuario/registroad.html', {'message': message, 'form': form})
            else:
                message = "Al parecer los correos no son iguales."
                return render(request, 'usuario/registroad.html',
                                  {'message': message, 'form': form, 'form10': form10})
        else:
            form = SignUpForm(request.POST)
            form10 = GuardarForm10(request.POST)
            m = form.errors.as_json()
            partes = m.split('message')
            a = None
            print(len(partes))
            if (len(partes)) == 2:
                mt = partes[1].split(',')
                a = mt[0].split('"')
                message = a[2]
            elif (len(partes)) == 3:
                mt = partes[1].split(',')
                mt1 = partes[2].split(',')
                a = mt[0].split('"')
                a1 = mt1[0].split('"')
                message = (a[2] + a1[2])
            elif (len(partes)) == 4:
                mt = partes[1].split(',')
                mt1 = partes[2].split(',')
                mt2 = partes[3].split(',')
                a = mt[0].split('"')
                a1 = mt1[0].split('"')
                a2 = mt2[0].split('"')
                message = (a[2] + a1[2] + a2[2])

            return render(request, 'usuario/registroad.html', {'message': message, 'form': form, 'form10': form10})
    else:
        form = UserCreationForm()
        form10 = GuardarForm10()
    return render(request, 'usuario/registroad.html', {'message': message, 'form': form, 'form10': form10})


def registrosp(request):
    message = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        form10 = GuardarForm10(request.POST)

        if form.is_valid():
            if form10.is_valid():
                correoer = form10.cleaned_data.get('email1')
                print(correoer)
            else:
                correoer = None

            correoe = form.cleaned_data.get('email')
            print(correoe)
            if correoe == correoer:
                form.save()
                typeuser = form.cleaned_data.get('typeuser')

                #grupo de usuarios
                g_autores, ga1 = Group.objects.get_or_create(name='Autores')
                g_tutores, gt1 = Group.objects.get_or_create(name='Tutores')
                g_responsables, gr1 = Group.objects.get_or_create(name='Responsables')
                g_administradores, gad1 = Group.objects.get_or_create(name='Administradores')
                g_superusuarios, gsp1 = Group.objects.get_or_create(name='SuperUsuarios')

                #contenttype
                cp = ContentType.objects.get_for_model(Proyecto)
                ct = ContentType.objects.get_for_model(Tutor)
                ca = ContentType.objects.get_for_model(Autor)
                ci = ContentType.objects.get_for_model(Institucion)
                cr = ContentType.objects.get_for_model(ResponsableInstitucional)
                ctp = ContentType.objects.get_for_model(TipoProyecto)
                cac = ContentType.objects.get_for_model(AreaConocimiento)
                cc = ContentType.objects.get_for_model(Carrera)

                permiso1p, pp1 = Permission.objects.get_or_create(codename='listar_proyecto', name='Puede listar Proyectos',
                                                                  content_type=cp)
                permiso2p, pp2 = Permission.objects.get_or_create(codename='agregar_proyecto', name='Puede agregar Proyectos',
                                                                  content_type=cp)
                permiso3p, pp3 = Permission.objects.get_or_create(codename='editar_proyecto', name='Puede editarar Proyectos',
                                                                  content_type=cp)
                permiso4p, pp4 = Permission.objects.get_or_create(codename='eliminar_proyecto', name='Puede eliminar Proyectos',
                                                                  content_type=cp)

                permiso1t, pt1 = Permission.objects.get_or_create(codename='listar_tutor', name='Puede listar Tutores',
                                                                  content_type=ct)
                permiso2t, pt2 = Permission.objects.get_or_create(codename='agregar_tutor', name='Puede agregar Tutores',
                                                                  content_type=ct)
                permiso3t, pt3 = Permission.objects.get_or_create(codename='editar_tutor', name='Puede editarar Tutores',
                                                                  content_type=ct)
                permiso4t, pt4 = Permission.objects.get_or_create(codename='eliminar_tutor', name='Puede eliminar Tutores',
                                                                  content_type=ct)

                permiso1a, pal = Permission.objects.get_or_create(codename='listar_autor', name='Puede listar Autores',
                                                                  content_type=ca)
                permiso2a, pa2 = Permission.objects.get_or_create(codename='agregar_autor', name='Puede agregar Autores',
                                                                  content_type=ca)
                permiso3a, pa3 = Permission.objects.get_or_create(codename='editar_autor', name='Puede editarar Autores',
                                                                  content_type=ca)
                permiso4a, pa4 = Permission.objects.get_or_create(codename='eliminar_autor', name='Puede eliminar Autores',
                                                                  content_type=ca)

                permiso1i, pi1 = Permission.objects.get_or_create(codename='listar_institucion', name='Puede listar Instituciones',
                                                                  content_type=ci)
                permiso2i, pi2 = Permission.objects.get_or_create(codename='agregar_institucion', name='Puede agregar Instituciones',
                                                                  content_type=ci)
                permiso3i, pi3 = Permission.objects.get_or_create(codename='editar_institucion', name='Puede editarar Instituciones',
                                                                  content_type=ci)
                permiso4i, pi4 = Permission.objects.get_or_create(codename='eliminar_institucion', name='Puede eliminar Instituciones',
                                                                  content_type=ci)

                permiso1r, pr1 = Permission.objects.get_or_create(codename='listar_responsableinstitucional',
                                                                  name='Puede listar Responsbles',
                                                                  content_type=cr)
                permiso2r, pr2 = Permission.objects.get_or_create(codename='agregar_responsableinstitucional',
                                                                  name='Puede agregar Responsbles',
                                                                  content_type=cr)
                permiso3r, pr3 = Permission.objects.get_or_create(codename='editar_responsableinstitucional',
                                                                  name='Puede editar Responsbles',
                                                                  content_type=cr)
                permiso4r, pr4 = Permission.objects.get_or_create(codename='eliminar_responsableinstitucional',
                                                                  name='Puede eliminar Responsbles',
                                                                  content_type=cr)

                permiso1tp, ptp1 = Permission.objects.get_or_create(codename='listar_tipoproyecto',
                                                                  name='Puede listar Tipo Proyecto',
                                                                  content_type=ctp)
                permiso2tp, ptp2 = Permission.objects.get_or_create(codename='agregar_tipoproyecto',
                                                                  name='Puede agregar Tipo Proyecto',
                                                                  content_type=ctp)
                permiso3tp, ptp3 = Permission.objects.get_or_create(codename='editar_tipoproyecto',
                                                                  name='Puede editar Tipo Proyecto',
                                                                  content_type=ctp)
                permiso4tp, ptp4 = Permission.objects.get_or_create(codename='eliminar_tipoproyecto',
                                                                  name='Puede eliminar Tipo Proyecto',
                                                                  content_type=ctp)

                permiso1ac, pac1 = Permission.objects.get_or_create(codename='listar_areaconocimiento',
                                                                    name='Puede listar Area Conocimiento',
                                                                    content_type=cac)
                permiso2ac, pac2 = Permission.objects.get_or_create(codename='agregar_areaconocimiento',
                                                                    name='Puede agregar Area Conocimiento',
                                                                    content_type=cac)
                permiso3ac, pac3 = Permission.objects.get_or_create(codename='editar_areaconocimiento',
                                                                    name='Puede editar Area Conocimiento',
                                                                    content_type=cac)
                permiso4ac, pac4 = Permission.objects.get_or_create(codename='eliminar_areaconocimiento',
                                                                    name='Puede eliminar Area Conocimiento',
                                                                    content_type=cac)

                permiso1c, pc1 = Permission.objects.get_or_create(codename='listar_carrera',
                                                                    name='Puede listar Carreras',
                                                                    content_type=cc)
                permiso2c, pc2 = Permission.objects.get_or_create(codename='agregar_carrera',
                                                                    name='Puede agregar Carreras',
                                                                    content_type=cc)
                permiso3c, pc3 = Permission.objects.get_or_create(codename='editar_carrera',
                                                                    name='Puede editar Carreras',
                                                                    content_type=cc)
                permiso4c, pc4 = Permission.objects.get_or_create(codename='eliminar_carrera',
                                                                    name='Puede eliminar Carreras',
                                                                    content_type=cc)

                # Tutor con permisos de Proyecto
                g_tutores.permissions.add(permiso1p)
                # Tutor con permisos de tutor
                g_tutores.permissions.add(permiso1t)
                #g_tutores.permissions.add(permiso2t)
                #g_tutores.permissions.add(permiso3t)
                # Tutor con permisos de Tutor
                g_tutores.permissions.add(permiso1a)
                # Tutor con permisos de insittuciones
                g_tutores.permissions.add(permiso1i)
                # Tutor con permisos de responsableinstitucional
                g_tutores.permissions.add(permiso1r)
                # Tutor con permisos de Tipo de Proyecto
                g_tutores.permissions.add(permiso1tp)
                # Tutor con permisos de Area de Conocimiento
                g_tutores.permissions.add(permiso1ac)
                # Tutor con permisos de Carrera
                g_tutores.permissions.add(permiso1c)

                # Autor con permisos de Proyecto
                g_autores.permissions.add(permiso1p)
                # Autor con permisos de tutor
                g_autores.permissions.add(permiso1t)
                # Autor con permisos de autor
                g_autores.permissions.add(permiso1a)
                #g_autores.permissions.add(permiso2a)
                #g_autores.permissions.add(permiso3a)
                # Autor con permisos de insittuciones
                g_autores.permissions.add(permiso1i)
                # Autor con permisos de responsableinstitucional
                g_autores.permissions.add(permiso1r)
                # Autor con permisos de Tipo de Proyecto
                g_autores.permissions.add(permiso1tp)
                # Autor con permisos de Area de Conocimiento
                g_autores.permissions.add(permiso1ac)
                # Autor con permisos de Carrera
                g_autores.permissions.add(permiso1c)

                # Responsable con permisos de Proyecto
                g_responsables.permissions.add(permiso1p)
                # Responsable con permisos de tutor
                g_responsables.permissions.add(permiso1p)
                # Responsable con permisos de autor
                g_responsables.permissions.add(permiso1a)
                # Responsable con permisos de insittuciones
                g_responsables.permissions.add(permiso1i)
                # Responsable con permisos de responsableinstitucional
                g_responsables.permissions.add(permiso1r)
                #g_responsables.permissions.add(permiso2r)
                #g_responsables.permissions.add(permiso3r)
                # Responsable con permisos de Tipo de Proyecto
                g_responsables.permissions.add(permiso1tp)
                # Responsable con permisos de Area de Conocimiento
                g_responsables.permissions.add(permiso1ac)
                # Responsable con permisos de Carrera
                g_responsables.permissions.add(permiso1c)

                # Administrador con permisos de Proyecto
                g_administradores.permissions.add(permiso1p)
                g_administradores.permissions.add(permiso2p)
                g_administradores.permissions.add(permiso3p)
                g_administradores.permissions.add(permiso4p)
                # Administrador con permisos de tutor
                g_administradores.permissions.add(permiso1t)
                g_administradores.permissions.add(permiso2t)
                g_administradores.permissions.add(permiso3t)
                g_administradores.permissions.add(permiso4t)
                # Administrador con permisos de autor
                g_administradores.permissions.add(permiso1a)
                g_administradores.permissions.add(permiso2a)
                g_administradores.permissions.add(permiso3a)
                g_administradores.permissions.add(permiso4a)
                # Administrador con permisos de instituciones
                g_administradores.permissions.add(permiso1i)
                g_administradores.permissions.add(permiso2i)
                g_administradores.permissions.add(permiso3i)
                g_administradores.permissions.add(permiso4i)
                # Administrador con permisos de responsableinstitucional
                g_administradores.permissions.add(permiso1r)
                g_administradores.permissions.add(permiso2r)
                g_administradores.permissions.add(permiso3r)
                g_administradores.permissions.add(permiso4r)
                # Administrador con permisos de Tipo de Proyecto
                g_administradores.permissions.add(permiso1tp)
                g_administradores.permissions.add(permiso2tp)
                g_administradores.permissions.add(permiso3tp)
                g_administradores.permissions.add(permiso4tp)
                # Administrador con permisos de Area de Conocimiento
                g_administradores.permissions.add(permiso1ac)
                g_administradores.permissions.add(permiso2ac)
                g_administradores.permissions.add(permiso3ac)
                g_administradores.permissions.add(permiso4ac)
                # Administrador con permisos de Carrera
                g_administradores.permissions.add(permiso1c)
                g_administradores.permissions.add(permiso2c)
                g_administradores.permissions.add(permiso3c)
                g_administradores.permissions.add(permiso4p)

                # super usuario con permisos de Proyecto
                g_superusuarios.permissions.add(permiso1p)
                g_superusuarios.permissions.add(permiso2p)
                g_superusuarios.permissions.add(permiso3p)
                g_superusuarios.permissions.add(permiso4p)
                # super usuario con permisos de tutor
                g_superusuarios.permissions.add(permiso1t)
                g_superusuarios.permissions.add(permiso2t)
                g_superusuarios.permissions.add(permiso3t)
                g_superusuarios.permissions.add(permiso4t)
                #super usuario con permisos de autor
                g_superusuarios.permissions.add(permiso1a)
                g_superusuarios.permissions.add(permiso2a)
                g_superusuarios.permissions.add(permiso3a)
                g_superusuarios.permissions.add(permiso4a)
                # super usuario con permisos de Insituciones
                g_superusuarios.permissions.add(permiso1i)
                g_superusuarios.permissions.add(permiso2i)
                g_superusuarios.permissions.add(permiso3i)
                g_superusuarios.permissions.add(permiso4i)
                # super usuario con permisos de responsableinstitucional
                g_superusuarios.permissions.add(permiso1r)
                g_superusuarios.permissions.add(permiso2r)
                g_superusuarios.permissions.add(permiso3r)
                g_superusuarios.permissions.add(permiso4r)
                # super usuario con permisos de Tipo de Proyecto
                g_superusuarios.permissions.add(permiso1tp)
                g_superusuarios.permissions.add(permiso2tp)
                g_superusuarios.permissions.add(permiso3tp)
                g_superusuarios.permissions.add(permiso4tp)
                # super usuario con permisos de Area de Conocimiento
                g_superusuarios.permissions.add(permiso1ac)
                g_superusuarios.permissions.add(permiso2ac)
                g_superusuarios.permissions.add(permiso3ac)
                g_superusuarios.permissions.add(permiso4ac)
                # super usuario con permisos de Carrera
                g_superusuarios.permissions.add(permiso1c)
                g_superusuarios.permissions.add(permiso2c)
                g_superusuarios.permissions.add(permiso3c)
                g_superusuarios.permissions.add(permiso4c)


                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                # user =User.objects.get(username=request.POST.get('username'))

                if typeuser =='Autores':
                    user.groups.add(g_autores)
                elif typeuser == 'Tutores':
                    user.groups.add(g_tutores)
                elif typeuser == 'Responsables':
                    user.groups.add(g_responsables)
                elif typeuser == 'Administradores':
                    user.groups.add(g_administradores)
                elif typeuser == 'Superusuarios':
                    user.groups.add(g_superusuarios)
                else:
                    print(" ")
                    #print("aquisp")
                #print(typeuser)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('homepage')
                    else:
                        message = "Tu usuario esta inactivo"
                        return render(request, 'usuario/registrosp.html', {'message': message, 'form': form})
            else:
                message = "Al parecer los correos no son iguales."
                return render(request, 'usuario/registrosp.html',
                                  {'message': message, 'form': form, 'form10': form10})
        else:
            form = SignUpForm(request.POST)
            form10 = GuardarForm10(request.POST)
            m = form.errors.as_json()
            partes = m.split('message')
            a = None
            print(len(partes))
            if (len(partes)) == 2:
                mt = partes[1].split(',')
                a = mt[0].split('"')
                message = a[2]
            elif (len(partes)) == 3:
                mt = partes[1].split(',')
                mt1 = partes[2].split(',')
                a = mt[0].split('"')
                a1 = mt1[0].split('"')
                message = (a[2] + a1[2])
            elif (len(partes)) == 4:
                mt = partes[1].split(',')
                mt1 = partes[2].split(',')
                mt2 = partes[3].split(',')
                a = mt[0].split('"')
                a1 = mt1[0].split('"')
                a2 = mt2[0].split('"')
                message = (a[2] + a1[2] + a2[2])

            return render(request, 'usuario/registrosp.html', {'message': message, 'form': form, 'form10':form10})
    else:
        form = UserCreationForm()
        form10 = GuardarForm10()
    return render(request, 'usuario/registrosp.html', {'message': message, 'form': form, 'form10':form10})


def logout_view(request):
    logout(request)
    return redirect('homepage')

def login_view(request):
    return redirect('login')

@login_required
def usuarios(request):
    usuarios = User.objects.all().order_by('id')
    return render(request, 'usuario/usuarios.html', {'usuarios': usuarios})


def cambiar_clave(request, usuario_id ):
    form = Edit(request.POST)
    if form.is_valid():
        print(" ")

    password1 = form.cleaned_data.get('password1')
    password2 = form.cleaned_data.get('password2')
    us = User.objects.get(id=usuario_id)
    username = us.username
    if us is None:
        print(" ")
    else:
        if (password1 == password2) and password2 is not None :
            us.set_password(password1)
            us.save()
            us = authenticate(username=username, password=password1)
            if us is not None:
                if us.is_active:
                    login(request, us)
                    return redirect('homepage')
                else:
                    message = "Tu usuario esta inactivo"
                    return render(request, 'usuario/editar_clave.html', {'message': message, 'form': form})
            else:
                message = "Nombre de usuario y/o password  incorrecto"
                return render(request, 'usuario/editar_clave.html', {'message': message, 'form': form})
        elif password1 is None and password2 is None:
            return render(request, 'usuario/editar_clave.html', {'form': form})
        else:
            message = "No son iguales las claves"
            return render(request, 'usuario/editar_clave.html', {'message': message, 'form': form})

    return render(request, 'usuario/editar_clave.html')

@login_required
def editar_usuario(request, usuario_id):
    grupo = None
    form = Edit(request.POST)
    if form.is_valid():
        print(" ")

    typeuser = form.cleaned_data.get('typeuser')
    usuario = User.objects.get(id=usuario_id)
    if typeuser is None:
        print(" ")
    else:
        print(" ")
        if usuario.groups.all().exists():
            # Action if existing
            grupo = Group.objects.get(user=usuario)
            usuario.groups.clear()
            typeuser = form.cleaned_data.get('typeuser')

            # grupo de usuarios
            g_autores, ga1 = Group.objects.get_or_create(name='Autores')
            g_tutores, gt1 = Group.objects.get_or_create(name='Tutores')
            g_responsables, gr1 = Group.objects.get_or_create(name='Responsables')
            g_administradores, gad1 = Group.objects.get_or_create(name='Administradores')
            g_superusuarios, gsp1 = Group.objects.get_or_create(name='SuperUsuarios')

            # contenttype
            cp = ContentType.objects.get_for_model(Proyecto)
            ct = ContentType.objects.get_for_model(Tutor)
            ca = ContentType.objects.get_for_model(Autor)
            ci = ContentType.objects.get_for_model(Institucion)
            cr = ContentType.objects.get_for_model(ResponsableInstitucional)
            ctp = ContentType.objects.get_for_model(TipoProyecto)
            cac = ContentType.objects.get_for_model(AreaConocimiento)
            cc = ContentType.objects.get_for_model(Carrera)

            permiso1p, pp1 = Permission.objects.get_or_create(codename='listar_proyecto', name='Puede listar Proyectos',
                                                              content_type=cp)
            permiso2p, pp2 = Permission.objects.get_or_create(codename='agregar_proyecto',
                                                              name='Puede agregar Proyectos',
                                                              content_type=cp)
            permiso3p, pp3 = Permission.objects.get_or_create(codename='editar_proyecto',
                                                              name='Puede editarar Proyectos',
                                                              content_type=cp)
            permiso4p, pp4 = Permission.objects.get_or_create(codename='eliminar_proyecto',
                                                              name='Puede eliminar Proyectos',
                                                              content_type=cp)

            permiso1t, pt1 = Permission.objects.get_or_create(codename='listar_tutor', name='Puede listar Tutores',
                                                              content_type=ct)
            permiso2t, pt2 = Permission.objects.get_or_create(codename='agregar_tutor', name='Puede agregar Tutores',
                                                              content_type=ct)
            permiso3t, pt3 = Permission.objects.get_or_create(codename='editar_tutor', name='Puede editarar Tutores',
                                                              content_type=ct)
            permiso4t, pt4 = Permission.objects.get_or_create(codename='eliminar_tutor', name='Puede eliminar Tutores',
                                                              content_type=ct)

            permiso1a, pal = Permission.objects.get_or_create(codename='listar_autor', name='Puede listar Autores',
                                                              content_type=ca)
            permiso2a, pa2 = Permission.objects.get_or_create(codename='agregar_autor', name='Puede agregar Autores',
                                                              content_type=ca)
            permiso3a, pa3 = Permission.objects.get_or_create(codename='editar_autor', name='Puede editarar Autores',
                                                              content_type=ca)
            permiso4a, pa4 = Permission.objects.get_or_create(codename='eliminar_autor', name='Puede eliminar Autores',
                                                              content_type=ca)

            permiso1i, pi1 = Permission.objects.get_or_create(codename='listar_institucion',
                                                              name='Puede listar Instituciones',
                                                              content_type=ci)
            permiso2i, pi2 = Permission.objects.get_or_create(codename='agregar_institucion',
                                                              name='Puede agregar Instituciones',
                                                              content_type=ci)
            permiso3i, pi3 = Permission.objects.get_or_create(codename='editar_institucion',
                                                              name='Puede editarar Instituciones',
                                                              content_type=ci)
            permiso4i, pi4 = Permission.objects.get_or_create(codename='eliminar_institucion',
                                                              name='Puede eliminar Instituciones',
                                                              content_type=ci)

            permiso1r, pr1 = Permission.objects.get_or_create(codename='listar_responsableinstitucional',
                                                              name='Puede listar Responsbles',
                                                              content_type=cr)
            permiso2r, pr2 = Permission.objects.get_or_create(codename='agregar_responsableinstitucional',
                                                              name='Puede agregar Responsbles',
                                                              content_type=cr)
            permiso3r, pr3 = Permission.objects.get_or_create(codename='editar_responsableinstitucional',
                                                              name='Puede editar Responsbles',
                                                              content_type=cr)
            permiso4r, pr4 = Permission.objects.get_or_create(codename='eliminar_responsableinstitucional',
                                                              name='Puede eliminar Responsbles',
                                                              content_type=cr)

            permiso1tp, ptp1 = Permission.objects.get_or_create(codename='listar_tipoproyecto',
                                                                name='Puede listar Tipo Proyecto',
                                                                content_type=ctp)
            permiso2tp, ptp2 = Permission.objects.get_or_create(codename='agregar_tipoproyecto',
                                                                name='Puede agregar Tipo Proyecto',
                                                                content_type=ctp)
            permiso3tp, ptp3 = Permission.objects.get_or_create(codename='editar_tipoproyecto',
                                                                name='Puede editar Tipo Proyecto',
                                                                content_type=ctp)
            permiso4tp, ptp4 = Permission.objects.get_or_create(codename='eliminar_tipoproyecto',
                                                                name='Puede eliminar Tipo Proyecto',
                                                                content_type=ctp)

            permiso1ac, pac1 = Permission.objects.get_or_create(codename='listar_areaconocimiento',
                                                                name='Puede listar Area Conocimiento',
                                                                content_type=cac)
            permiso2ac, pac2 = Permission.objects.get_or_create(codename='agregar_areaconocimiento',
                                                                name='Puede agregar Area Conocimiento',
                                                                content_type=cac)
            permiso3ac, pac3 = Permission.objects.get_or_create(codename='editar_areaconocimiento',
                                                                name='Puede editar Area Conocimiento',
                                                                content_type=cac)
            permiso4ac, pac4 = Permission.objects.get_or_create(codename='eliminar_areaconocimiento',
                                                                name='Puede eliminar Area Conocimiento',
                                                                content_type=cac)

            permiso1c, pc1 = Permission.objects.get_or_create(codename='listar_carrera',
                                                              name='Puede listar Carreras',
                                                              content_type=cc)
            permiso2c, pc2 = Permission.objects.get_or_create(codename='agregar_carrera',
                                                              name='Puede agregar Carreras',
                                                              content_type=cc)
            permiso3c, pc3 = Permission.objects.get_or_create(codename='editar_carrera',
                                                              name='Puede editar Carreras',
                                                              content_type=cc)
            permiso4c, pc4 = Permission.objects.get_or_create(codename='eliminar_carrera',
                                                              name='Puede eliminar Carreras',
                                                              content_type=cc)

            # Tutor con permisos de Proyecto
            g_tutores.permissions.add(permiso1p)
            # Tutor con permisos de tutor
            g_tutores.permissions.add(permiso1t)
            # g_tutores.permissions.add(permiso2t)
            # g_tutores.permissions.add(permiso3t)
            # Tutor con permisos de Tutor
            g_tutores.permissions.add(permiso1a)
            # Tutor con permisos de insittuciones
            g_tutores.permissions.add(permiso1i)
            # Tutor con permisos de responsableinstitucional
            g_tutores.permissions.add(permiso1r)
            # Tutor con permisos de Tipo de Proyecto
            g_tutores.permissions.add(permiso1tp)
            # Tutor con permisos de Area de Conocimiento
            g_tutores.permissions.add(permiso1ac)
            # Tutor con permisos de Carrera
            g_tutores.permissions.add(permiso1c)

            # Autor con permisos de Proyecto
            g_autores.permissions.add(permiso1p)
            # Autor con permisos de tutor
            g_autores.permissions.add(permiso1t)
            # Autor con permisos de autor
            g_autores.permissions.add(permiso1a)
            # g_autores.permissions.add(permiso2a)
            # g_autores.permissions.add(permiso3a)
            # Autor con permisos de insittuciones
            g_autores.permissions.add(permiso1i)
            # Autor con permisos de responsableinstitucional
            g_autores.permissions.add(permiso1r)
            # Autor con permisos de Tipo de Proyecto
            g_autores.permissions.add(permiso1tp)
            # Autor con permisos de Area de Conocimiento
            g_autores.permissions.add(permiso1ac)
            # Autor con permisos de Carrera
            g_autores.permissions.add(permiso1c)

            # Responsable con permisos de Proyecto
            g_responsables.permissions.add(permiso1p)
            # Responsable con permisos de tutor
            g_responsables.permissions.add(permiso1p)
            # Responsable con permisos de autor
            g_responsables.permissions.add(permiso1a)
            # Responsable con permisos de insittuciones
            g_responsables.permissions.add(permiso1i)
            # Responsable con permisos de responsableinstitucional
            g_responsables.permissions.add(permiso1r)
            # g_responsables.permissions.add(permiso2r)
            # g_responsables.permissions.add(permiso3r)
            # Responsable con permisos de Tipo de Proyecto
            g_responsables.permissions.add(permiso1tp)
            # Responsable con permisos de Area de Conocimiento
            g_responsables.permissions.add(permiso1ac)
            # Responsable con permisos de Carrera
            g_responsables.permissions.add(permiso1c)

            # Administrador con permisos de Proyecto
            g_administradores.permissions.add(permiso1p)
            g_administradores.permissions.add(permiso2p)
            g_administradores.permissions.add(permiso3p)
            g_administradores.permissions.add(permiso4p)
            # Administrador con permisos de tutor
            g_administradores.permissions.add(permiso1t)
            g_administradores.permissions.add(permiso2t)
            g_administradores.permissions.add(permiso3t)
            g_administradores.permissions.add(permiso4t)
            # Administrador con permisos de autor
            g_administradores.permissions.add(permiso1a)
            g_administradores.permissions.add(permiso2a)
            g_administradores.permissions.add(permiso3a)
            g_administradores.permissions.add(permiso4a)
            # Administrador con permisos de instituciones
            g_administradores.permissions.add(permiso1i)
            g_administradores.permissions.add(permiso2i)
            g_administradores.permissions.add(permiso3i)
            g_administradores.permissions.add(permiso4i)
            # Administrador con permisos de responsableinstitucional
            g_administradores.permissions.add(permiso1r)
            g_administradores.permissions.add(permiso2r)
            g_administradores.permissions.add(permiso3r)
            g_administradores.permissions.add(permiso4r)
            # Administrador con permisos de Tipo de Proyecto
            g_administradores.permissions.add(permiso1tp)
            g_administradores.permissions.add(permiso2tp)
            g_administradores.permissions.add(permiso3tp)
            g_administradores.permissions.add(permiso4tp)
            # Administrador con permisos de Area de Conocimiento
            g_administradores.permissions.add(permiso1ac)
            g_administradores.permissions.add(permiso2ac)
            g_administradores.permissions.add(permiso3ac)
            g_administradores.permissions.add(permiso4ac)
            # Administrador con permisos de Carrera
            g_administradores.permissions.add(permiso1c)
            g_administradores.permissions.add(permiso2c)
            g_administradores.permissions.add(permiso3c)
            g_administradores.permissions.add(permiso4p)

            # super usuario con permisos de Proyecto
            g_superusuarios.permissions.add(permiso1p)
            g_superusuarios.permissions.add(permiso2p)
            g_superusuarios.permissions.add(permiso3p)
            g_superusuarios.permissions.add(permiso4p)
            # super usuario con permisos de tutor
            g_superusuarios.permissions.add(permiso1t)
            g_superusuarios.permissions.add(permiso2t)
            g_superusuarios.permissions.add(permiso3t)
            g_superusuarios.permissions.add(permiso4t)
            # super usuario con permisos de autor
            g_superusuarios.permissions.add(permiso1a)
            g_superusuarios.permissions.add(permiso2a)
            g_superusuarios.permissions.add(permiso3a)
            g_superusuarios.permissions.add(permiso4a)
            # super usuario con permisos de Insituciones
            g_superusuarios.permissions.add(permiso1i)
            g_superusuarios.permissions.add(permiso2i)
            g_superusuarios.permissions.add(permiso3i)
            g_superusuarios.permissions.add(permiso4i)
            # super usuario con permisos de responsableinstitucional
            g_superusuarios.permissions.add(permiso1r)
            g_superusuarios.permissions.add(permiso2r)
            g_superusuarios.permissions.add(permiso3r)
            g_superusuarios.permissions.add(permiso4r)
            # super usuario con permisos de Tipo de Proyecto
            g_superusuarios.permissions.add(permiso1tp)
            g_superusuarios.permissions.add(permiso2tp)
            g_superusuarios.permissions.add(permiso3tp)
            g_superusuarios.permissions.add(permiso4tp)
            # super usuario con permisos de Area de Conocimiento
            g_superusuarios.permissions.add(permiso1ac)
            g_superusuarios.permissions.add(permiso2ac)
            g_superusuarios.permissions.add(permiso3ac)
            g_superusuarios.permissions.add(permiso4ac)
            # super usuario con permisos de Carrera
            g_superusuarios.permissions.add(permiso1c)
            g_superusuarios.permissions.add(permiso2c)
            g_superusuarios.permissions.add(permiso3c)
            g_superusuarios.permissions.add(permiso4c)

            if typeuser == 'Autores':
                usuario.groups.add(g_autores)
            elif typeuser == 'Tutores':
                usuario.groups.add(g_tutores)
            elif typeuser == 'Responsables':
                usuario.groups.add(g_responsables)
            elif typeuser == 'Administradores':
                usuario.groups.add(g_administradores)
            elif typeuser == 'Superusuarios':
                usuario.groups.add(g_superusuarios)
            else:
                print(" ")
                # print("aquisp")
            #print(typeuser)
            return redirect('usuarios')

        else:
            # Action if not existing
            # grupo de usuarios
            g_autores, ga1 = Group.objects.get_or_create(name='Autores')
            g_tutores, gt1 = Group.objects.get_or_create(name='Tutores')
            g_responsables, gr1 = Group.objects.get_or_create(name='Responsables')
            g_administradores, gad1 = Group.objects.get_or_create(name='Administradores')
            g_superusuarios, gsp1 = Group.objects.get_or_create(name='SuperUsuarios')

            # contenttype
            cp = ContentType.objects.get_for_model(Proyecto)
            ct = ContentType.objects.get_for_model(Tutor)
            ca = ContentType.objects.get_for_model(Autor)
            ci = ContentType.objects.get_for_model(Institucion)
            cr = ContentType.objects.get_for_model(ResponsableInstitucional)
            ctp = ContentType.objects.get_for_model(TipoProyecto)
            cac = ContentType.objects.get_for_model(AreaConocimiento)
            cc = ContentType.objects.get_for_model(Carrera)

            permiso1p, pp1 = Permission.objects.get_or_create(codename='listar_proyecto', name='Puede listar Proyectos',
                                                              content_type=cp)
            permiso2p, pp2 = Permission.objects.get_or_create(codename='agregar_proyecto',
                                                              name='Puede agregar Proyectos',
                                                              content_type=cp)
            permiso3p, pp3 = Permission.objects.get_or_create(codename='editar_proyecto',
                                                              name='Puede editarar Proyectos',
                                                              content_type=cp)
            permiso4p, pp4 = Permission.objects.get_or_create(codename='eliminar_proyecto',
                                                              name='Puede eliminar Proyectos',
                                                              content_type=cp)

            permiso1t, pt1 = Permission.objects.get_or_create(codename='listar_tutor', name='Puede listar Tutores',
                                                              content_type=ct)
            permiso2t, pt2 = Permission.objects.get_or_create(codename='agregar_tutor', name='Puede agregar Tutores',
                                                              content_type=ct)
            permiso3t, pt3 = Permission.objects.get_or_create(codename='editar_tutor', name='Puede editarar Tutores',
                                                              content_type=ct)
            permiso4t, pt4 = Permission.objects.get_or_create(codename='eliminar_tutor', name='Puede eliminar Tutores',
                                                              content_type=ct)

            permiso1a, pal = Permission.objects.get_or_create(codename='listar_autor', name='Puede listar Autores',
                                                              content_type=ca)
            permiso2a, pa2 = Permission.objects.get_or_create(codename='agregar_autor', name='Puede agregar Autores',
                                                              content_type=ca)
            permiso3a, pa3 = Permission.objects.get_or_create(codename='editar_autor', name='Puede editarar Autores',
                                                              content_type=ca)
            permiso4a, pa4 = Permission.objects.get_or_create(codename='eliminar_autor', name='Puede eliminar Autores',
                                                              content_type=ca)

            permiso1i, pi1 = Permission.objects.get_or_create(codename='listar_institucion',
                                                              name='Puede listar Instituciones',
                                                              content_type=ci)
            permiso2i, pi2 = Permission.objects.get_or_create(codename='agregar_institucion',
                                                              name='Puede agregar Instituciones',
                                                              content_type=ci)
            permiso3i, pi3 = Permission.objects.get_or_create(codename='editar_institucion',
                                                              name='Puede editarar Instituciones',
                                                              content_type=ci)
            permiso4i, pi4 = Permission.objects.get_or_create(codename='eliminar_institucion',
                                                              name='Puede eliminar Instituciones',
                                                              content_type=ci)

            permiso1r, pr1 = Permission.objects.get_or_create(codename='listar_responsableinstitucional',
                                                              name='Puede listar Responsbles',
                                                              content_type=cr)
            permiso2r, pr2 = Permission.objects.get_or_create(codename='agregar_responsableinstitucional',
                                                              name='Puede agregar Responsbles',
                                                              content_type=cr)
            permiso3r, pr3 = Permission.objects.get_or_create(codename='editar_responsableinstitucional',
                                                              name='Puede editar Responsbles',
                                                              content_type=cr)
            permiso4r, pr4 = Permission.objects.get_or_create(codename='eliminar_responsableinstitucional',
                                                              name='Puede eliminar Responsbles',
                                                              content_type=cr)

            permiso1tp, ptp1 = Permission.objects.get_or_create(codename='listar_tipoproyecto',
                                                                name='Puede listar Tipo Proyecto',
                                                                content_type=ctp)
            permiso2tp, ptp2 = Permission.objects.get_or_create(codename='agregar_tipoproyecto',
                                                                name='Puede agregar Tipo Proyecto',
                                                                content_type=ctp)
            permiso3tp, ptp3 = Permission.objects.get_or_create(codename='editar_tipoproyecto',
                                                                name='Puede editar Tipo Proyecto',
                                                                content_type=ctp)
            permiso4tp, ptp4 = Permission.objects.get_or_create(codename='eliminar_tipoproyecto',
                                                                name='Puede eliminar Tipo Proyecto',
                                                                content_type=ctp)

            permiso1ac, pac1 = Permission.objects.get_or_create(codename='listar_areaconocimiento',
                                                                name='Puede listar Area Conocimiento',
                                                                content_type=cac)
            permiso2ac, pac2 = Permission.objects.get_or_create(codename='agregar_areaconocimiento',
                                                                name='Puede agregar Area Conocimiento',
                                                                content_type=cac)
            permiso3ac, pac3 = Permission.objects.get_or_create(codename='editar_areaconocimiento',
                                                                name='Puede editar Area Conocimiento',
                                                                content_type=cac)
            permiso4ac, pac4 = Permission.objects.get_or_create(codename='eliminar_areaconocimiento',
                                                                name='Puede eliminar Area Conocimiento',
                                                                content_type=cac)

            permiso1c, pc1 = Permission.objects.get_or_create(codename='listar_carrera',
                                                              name='Puede listar Carreras',
                                                              content_type=cc)
            permiso2c, pc2 = Permission.objects.get_or_create(codename='agregar_carrera',
                                                              name='Puede agregar Carreras',
                                                              content_type=cc)
            permiso3c, pc3 = Permission.objects.get_or_create(codename='editar_carrera',
                                                              name='Puede editar Carreras',
                                                              content_type=cc)
            permiso4c, pc4 = Permission.objects.get_or_create(codename='eliminar_carrera',
                                                              name='Puede eliminar Carreras',
                                                              content_type=cc)

            # Tutor con permisos de Proyecto
            g_tutores.permissions.add(permiso1p)
            # Tutor con permisos de tutor
            g_tutores.permissions.add(permiso1t)
            # g_tutores.permissions.add(permiso2t)
            # g_tutores.permissions.add(permiso3t)
            # Tutor con permisos de Tutor
            g_tutores.permissions.add(permiso1a)
            # Tutor con permisos de insittuciones
            g_tutores.permissions.add(permiso1i)
            # Tutor con permisos de responsableinstitucional
            g_tutores.permissions.add(permiso1r)
            # Tutor con permisos de Tipo de Proyecto
            g_tutores.permissions.add(permiso1tp)
            # Tutor con permisos de Area de Conocimiento
            g_tutores.permissions.add(permiso1ac)
            # Tutor con permisos de Carrera
            g_tutores.permissions.add(permiso1c)

            # Autor con permisos de Proyecto
            g_autores.permissions.add(permiso1p)
            # Autor con permisos de tutor
            g_autores.permissions.add(permiso1t)
            # Autor con permisos de autor
            g_autores.permissions.add(permiso1a)
            # g_autores.permissions.add(permiso2a)
            # g_autores.permissions.add(permiso3a)
            # Autor con permisos de insittuciones
            g_autores.permissions.add(permiso1i)
            # Autor con permisos de responsableinstitucional
            g_autores.permissions.add(permiso1r)
            # Autor con permisos de Tipo de Proyecto
            g_autores.permissions.add(permiso1tp)
            # Autor con permisos de Area de Conocimiento
            g_autores.permissions.add(permiso1ac)
            # Autor con permisos de Carrera
            g_autores.permissions.add(permiso1c)

            # Responsable con permisos de Proyecto
            g_responsables.permissions.add(permiso1p)
            # Responsable con permisos de tutor
            g_responsables.permissions.add(permiso1p)
            # Responsable con permisos de autor
            g_responsables.permissions.add(permiso1a)
            # Responsable con permisos de insittuciones
            g_responsables.permissions.add(permiso1i)
            # Responsable con permisos de responsableinstitucional
            g_responsables.permissions.add(permiso1r)
            # g_responsables.permissions.add(permiso2r)
            # g_responsables.permissions.add(permiso3r)
            # Responsable con permisos de Tipo de Proyecto
            g_responsables.permissions.add(permiso1tp)
            # Responsable con permisos de Area de Conocimiento
            g_responsables.permissions.add(permiso1ac)
            # Responsable con permisos de Carrera
            g_responsables.permissions.add(permiso1c)

            # Administrador con permisos de Proyecto
            g_administradores.permissions.add(permiso1p)
            g_administradores.permissions.add(permiso2p)
            g_administradores.permissions.add(permiso3p)
            g_administradores.permissions.add(permiso4p)
            # Administrador con permisos de tutor
            g_administradores.permissions.add(permiso1t)
            g_administradores.permissions.add(permiso2t)
            g_administradores.permissions.add(permiso3t)
            g_administradores.permissions.add(permiso4t)
            # Administrador con permisos de autor
            g_administradores.permissions.add(permiso1a)
            g_administradores.permissions.add(permiso2a)
            g_administradores.permissions.add(permiso3a)
            g_administradores.permissions.add(permiso4a)
            # Administrador con permisos de instituciones
            g_administradores.permissions.add(permiso1i)
            g_administradores.permissions.add(permiso2i)
            g_administradores.permissions.add(permiso3i)
            g_administradores.permissions.add(permiso4i)
            # Administrador con permisos de responsableinstitucional
            g_administradores.permissions.add(permiso1r)
            g_administradores.permissions.add(permiso2r)
            g_administradores.permissions.add(permiso3r)
            g_administradores.permissions.add(permiso4r)
            # Administrador con permisos de Tipo de Proyecto
            g_administradores.permissions.add(permiso1tp)
            g_administradores.permissions.add(permiso2tp)
            g_administradores.permissions.add(permiso3tp)
            g_administradores.permissions.add(permiso4tp)
            # Administrador con permisos de Area de Conocimiento
            g_administradores.permissions.add(permiso1ac)
            g_administradores.permissions.add(permiso2ac)
            g_administradores.permissions.add(permiso3ac)
            g_administradores.permissions.add(permiso4ac)
            # Administrador con permisos de Carrera
            g_administradores.permissions.add(permiso1c)
            g_administradores.permissions.add(permiso2c)
            g_administradores.permissions.add(permiso3c)
            g_administradores.permissions.add(permiso4p)

            # super usuario con permisos de Proyecto
            g_superusuarios.permissions.add(permiso1p)
            g_superusuarios.permissions.add(permiso2p)
            g_superusuarios.permissions.add(permiso3p)
            g_superusuarios.permissions.add(permiso4p)
            # super usuario con permisos de tutor
            g_superusuarios.permissions.add(permiso1t)
            g_superusuarios.permissions.add(permiso2t)
            g_superusuarios.permissions.add(permiso3t)
            g_superusuarios.permissions.add(permiso4t)
            # super usuario con permisos de autor
            g_superusuarios.permissions.add(permiso1a)
            g_superusuarios.permissions.add(permiso2a)
            g_superusuarios.permissions.add(permiso3a)
            g_superusuarios.permissions.add(permiso4a)
            # super usuario con permisos de Insituciones
            g_superusuarios.permissions.add(permiso1i)
            g_superusuarios.permissions.add(permiso2i)
            g_superusuarios.permissions.add(permiso3i)
            g_superusuarios.permissions.add(permiso4i)
            # super usuario con permisos de responsableinstitucional
            g_superusuarios.permissions.add(permiso1r)
            g_superusuarios.permissions.add(permiso2r)
            g_superusuarios.permissions.add(permiso3r)
            g_superusuarios.permissions.add(permiso4r)
            # super usuario con permisos de Tipo de Proyecto
            g_superusuarios.permissions.add(permiso1tp)
            g_superusuarios.permissions.add(permiso2tp)
            g_superusuarios.permissions.add(permiso3tp)
            g_superusuarios.permissions.add(permiso4tp)
            # super usuario con permisos de Area de Conocimiento
            g_superusuarios.permissions.add(permiso1ac)
            g_superusuarios.permissions.add(permiso2ac)
            g_superusuarios.permissions.add(permiso3ac)
            g_superusuarios.permissions.add(permiso4ac)
            # super usuario con permisos de Carrera
            g_superusuarios.permissions.add(permiso1c)
            g_superusuarios.permissions.add(permiso2c)
            g_superusuarios.permissions.add(permiso3c)
            g_superusuarios.permissions.add(permiso4c)

            if typeuser == 'Autores':
                usuario.groups.add(g_autores)
            elif typeuser == 'Tutores':
                usuario.groups.add(g_tutores)
            elif typeuser == 'Responsables':
                usuario.groups.add(g_responsables)
            elif typeuser == 'Administradores':
                usuario.groups.add(g_administradores)
            elif typeuser == 'Superusuarios':
                usuario.groups.add(g_superusuarios)
            else:
                print(" ")

            #print(typeuser)
            return redirect('usuarios')

    return render(request, 'usuario/editar_usuario.html', {'usuario': usuario})

@login_required
def eliminar(request, usuario_id):
    usuario= get_object_or_404(User, id=usuario_id)
    usuario.delete()
    usuarios = User.objects.all().order_by('id')
    return render(request, 'usuario/usuarios.html', {'usuarios': usuarios})