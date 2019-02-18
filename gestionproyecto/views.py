from django.urls import reverse_lazy

from gestionareaconocimiento.models import AreaConocimiento
from gestioncarrera.models import Carrera
from gestionproyecto.models import Proyecto
from gestioninstitucion.models import Institucion
from gestiontipoproyecto.models import TipoProyecto
from gestionresponsableinstitucional.models import ResponsableInstitucional
from gestionautor.models import Autor
from gestiontutor.models import Tutor
from gestionimagnes.models import Imagenes
from gestionarchivos.models import Archivos
from gestionactas.models import Actas
from django.shortcuts import get_object_or_404, render, redirect
from gestionproyecto.form import GuardarProyectoForm
from gestioninstitucion.form import GuardarInstitucionForm
from gestiontipoproyecto.form import GuardarTipoForm
from gestionresponsableinstitucional.form import GuardarResponsableForm
from gestiontutor.form import GuardarTutorForm
from gestionautor.form import GuardarAutorForm
from gestionareaconocimiento.form import GuardarAreaForm
from gestionayuda.form import GuardarForm
from gestionayuda1.form import GuardarForm1
from gestionayuda2.form import GuardarForm2
from gestionayuda3.form import GuardarForm3
from gestionayuda4.form import GuardarForm4
from gestionayuda5.form import GuardarForm5
from gestionayuda6.form import GuardarForm6
from gestionayuda7.form import GuardarForm7
from gestionayuda8.form import GuardarForm8
from gestionayuda9.form import GuardarForm9
from django.contrib.auth.decorators import login_required, permission_required
from django.forms import modelformset_factory


# Create your views here.
def index(request):
    proyectos = Proyecto.objects.all().order_by('id')
    return render(request, 'proyecto/lista_proyecto.html', {'proyectos': proyectos})


def proyecto_detalle(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
    autores = proyecto.Autor.all()
    tutores = proyecto.Tutor.all()
    institucion = proyecto.Institucion.all()
    tipoproyecto = proyecto.TipoProyecto.all()
    areaconocimiento = proyecto.AreaConocimiento.all()
    responsableinstitucional = proyecto.ResponsableInstitucional.all()
    return render(request, 'proyecto/perfil_proyecto.html', {'proyecto': proyecto, 'autores':autores,'responsableinstitucional':responsableinstitucional, 'tutores':tutores, 'instituciones':institucion, 'tipoproyectos':tipoproyecto, 'areaconocimientos': areaconocimiento})


@login_required
@permission_required('gestionproyecto.agregar_proyecto',reverse_lazy('Proyecto'))
def guardar_proyecto(request):
    global partes, institucionsalva, tiporsalva, tutorsalva, autorsalva, areasalva, responsablesalva, ayuda
    message = None
    message1 =None
    instituciones = Institucion.objects.all()
    tipoproyectos = TipoProyecto.objects.all()
    responsableinstitucionales = ResponsableInstitucional.objects.all()
    autores = Autor.objects.all()
    tutores = Tutor.objects.all()
    carreras = Carrera.objects.all()
    areaconocimientos = AreaConocimiento.objects.all()
    ImagenFormset = modelformset_factory(Imagenes,fields=('nombre_imagenes',),extra=3)
    ArchivosFormset = modelformset_factory(Archivos,fields=('nombre_archivos',),extra=3)
    ActasFormset = modelformset_factory(Actas,fields=('nombre_actas',),extra=3)
    if request.method == 'POST':
        form = GuardarProyectoForm(request.POST, request.FILES)
        formset = ImagenFormset(request.POST,request.FILES)
        formar = ArchivosFormset(request.POST,request.FILES)
        formac = ActasFormset(request.POST,request.FILES)
        #
        formi = GuardarInstitucionForm(request.POST, request.FILES)
        formti = GuardarTipoForm(request.POST, request.FILES)
        formre = GuardarResponsableForm(request.POST, request.FILES)
        formt = GuardarTutorForm(request.POST, request.FILES)
        forma = GuardarAutorForm(request.POST, request.FILES)
        formare = GuardarAreaForm(request.POST, request.FILES)
        #
        form2 = GuardarForm(request.POST)
        form3 = GuardarForm1(request.POST)
        form4 = GuardarForm2(request.POST)
        form5 = GuardarForm3(request.POST)
        form6 = GuardarForm4(request.POST)
        form7 = GuardarForm5(request.POST)
        form11 = GuardarForm9(request.POST)
        if form2.is_valid():
            nombre = form2.cleaned_data.get('nombre')
            partes = nombre.split(';')
        elif form3.is_valid():
            nombre = form3.cleaned_data.get('nombre1')
            partes = nombre.split(';')
        elif form4.is_valid():
            nombre = form4.cleaned_data.get('nombre2')
            partes = nombre.split(';')
        elif form5.is_valid():
            nombre = form5.cleaned_data.get('nombre3')
            partes = nombre.split(';')
        elif form6.is_valid():
            nombre = form6.cleaned_data.get('nombre4')
            partes = nombre.split(';')
        elif form7.is_valid():
            nombre = form7.cleaned_data.get('nombre5')
            partes = nombre.split(';')
        elif form11.is_valid():
            nombre = form11.cleaned_data.get('nombre9')
            partes = nombre.split(';')
        else:
            partes =[]


        if len(partes) == 0 and not form.is_valid():
            form = GuardarProyectoForm(request.POST)
            formset = ImagenFormset(queryset=Imagenes.objects.none())
            formar = ArchivosFormset(queryset=Archivos.objects.none())
            formac = ActasFormset(queryset=Actas.objects.none())
            formi = GuardarInstitucionForm()
            formti = GuardarTipoForm()
            formre = GuardarResponsableForm()
            formt = GuardarTutorForm()
            forma = GuardarAutorForm()
            formare = GuardarAreaForm()
            message = "Se debe elegir (al menos uno) en cada espacio de selección."
            return render(request, 'proyecto/agregar_proyecto.html',
                          {'message': message, 'message1': message1, 'form': form, 'formset': formset,
                           'formar': formar, 'formac': formac,
                           'formi': formi, 'formti': formti, 'formre': formre, 'formt': formt, 'forma': forma,
                           'formare': formare,
                           'carreras': carreras, 'tipoproyectos': tipoproyectos, 'instituciones': instituciones,
                           'responsableinstitucionales': responsableinstitucionales, 'autores': autores,
                           'tutores': tutores,
                           'areaconocimientos': areaconocimientos})

        elif form.is_valid() and formset.is_valid() and formar.is_valid() and formac.is_valid():
            proyecto =form.save()
            for f in formset:
                try:
                    foto = Imagenes(proyecto=proyecto, nombre_imagenes=f.cleaned_data['nombre_imagenes'])
                    foto.save()
                except Exception as e:
                    print(e)
                    break

            for f in formar:
                try:
                    arc = Archivos(proyecto=proyecto, nombre_archivos=f.cleaned_data['nombre_archivos'])
                    arc.save()
                except Exception as e:
                    print(e)
                    break

            for f in formac:
                try:
                    act = Actas(proyecto=proyecto, nombre_actas=f.cleaned_data['nombre_actas'])
                    act.save()
                except Exception as e:
                    print(e)
                    break

            return redirect('Proyecto')
        elif formi.is_valid():
            formi.save()
            data = {'Titulo': partes[0],
                    'Proposito': partes[1],
                    'Estado_proyecto':partes[2],
                    'Poblacion_utiliza': partes[3],
                    'Numero_muestra_ninos':partes[4],
                    'Tiempo_inactividad': partes[5],
                    'Sugerencias': partes[6],
                    'Fecha_Donacion': partes[13],
                    }
            print(partes)
            if len(partes[7]) == 0 or partes[7] == "null":
                institucionsalva = None
            else:
                if partes[7] != None:
                    elemetos = partes[7].split(',')
                    if len(elemetos)== 1:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4]) | Institucion.objects.filter(id=elemetos[5])

            if len(partes[8]) == 0 or partes[8] == "null":
                tiporsalva = None
            else:
                if partes[8] != None:
                    elemetos = partes[8].split(',')
                    if len(elemetos)== 1:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4]) | TipoProyecto.objects.filter(id=elemetos[5])

            if len(partes[9]) == 0 or partes[9] == "null":
                responsablesalva = None
            else:
                if partes[9] != None:
                    elemetos = partes[9].split(',')
                    if len(elemetos)== 1:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3]) | ResponsableInstitucional.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3]) | ResponsableInstitucional.objects.filter(id=elemetos[4]) | ResponsableInstitucional.objects.filter(id=elemetos[5])


            if len(partes[10]) == 0 or partes[10] == "null":
                tutorsalva = None
            else:
                if partes[10] != None:
                    elemetos = partes[10].split(',')
                    if len(elemetos)== 1:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4]) | Tutor.objects.filter(id=elemetos[5])

            if len(partes[11]) == 0 or partes[11] == "null":
                autorsalva = None
            else:
                if partes[11] != None:
                    elemetos = partes[11].split(',')
                    if len(elemetos)== 1:
                        autorsalva = Autor.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1]) | Autor.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(id=elemetos[3]) | Autor.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(id=elemetos[3]) | Autor.objects.filter(id=elemetos[4]) | Autor.objects.filter(id=elemetos[5])

            if len(partes[12]) == 0 or partes[12] == "null":
                areasalva = None
            else:
                if partes[12] != None:
                    elemetos = partes[12].split(',')
                    if len(elemetos)== 1:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3]) | AreaConocimiento.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3]) | AreaConocimiento.objects.filter(id=elemetos[4]) | AreaConocimiento.objects.filter(id=elemetos[5])

            form = GuardarProyectoForm(data)
            formset = ImagenFormset(queryset=Imagenes.objects.none())
            formar = ArchivosFormset(queryset=Archivos.objects.none())
            formac = ActasFormset(queryset=Actas.objects.none())
            formi = GuardarInstitucionForm()
            formti = GuardarTipoForm()
            formre = GuardarResponsableForm()
            formt = GuardarTutorForm()
            forma = GuardarAutorForm()
            formare = GuardarAreaForm()
            message1 = "La Institución a sido registrada con éxito."
            return render(request, 'proyecto/agregar_proyecto.html',
                          {'message': message, 'message1': message1, 'form': form, 'formset': formset, 'formar': formar, 'formac': formac,
                           'formi': formi, 'formti': formti, 'formre': formre, 'formt': formt, 'forma': forma,
                           'formare': formare,
                           'carreras': carreras, 'tipoproyectos': tipoproyectos, 'instituciones': instituciones,
                           'responsableinstitucionales': responsableinstitucionales, 'autores': autores, 'tutores': tutores,
                           'areaconocimientos': areaconocimientos,
                           'institucionsalva':institucionsalva,'tiporsalva':tiporsalva,'responsablesalva':responsablesalva,
                           'tutorsalva':tutorsalva,'autorsalva': autorsalva,'areasalva':areasalva})

        elif formti.is_valid():
            formti.save()
            data = {'Titulo': partes[0],
                    'Proposito': partes[1],
                    'Estado_proyecto': partes[2],
                    'Poblacion_utiliza': partes[3],
                    'Numero_muestra_ninos': partes[4],
                    'Tiempo_inactividad': partes[5],
                    'Sugerencias': partes[6],
                    'Fecha_Donacion': partes[13],
                    }
            if len(partes[7]) == 0 or partes[7] == "null":
                institucionsalva = None
            else:
                if partes[7] != None:
                    elemetos = partes[7].split(',')
                    if len(elemetos)== 1:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4]) | Institucion.objects.filter(id=elemetos[5])

            if len(partes[8]) == 0 or partes[8] == "null":
                tiporsalva = None
            else:
                if partes[8] != None:
                    elemetos = partes[8].split(',')
                    if len(elemetos)== 1:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4]) | TipoProyecto.objects.filter(id=elemetos[5])

            if len(partes[9]) == 0 or partes[9] == "null":
                responsablesalva = None
            else:
                if partes[9] != None:
                    elemetos = partes[9].split(',')
                    if len(elemetos)== 1:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3]) | ResponsableInstitucional.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3]) | ResponsableInstitucional.objects.filter(id=elemetos[4]) | ResponsableInstitucional.objects.filter(id=elemetos[5])


            if len(partes[10]) == 0 or partes[10] == "null":
                tutorsalva = None
            else:
                if partes[10] != None:
                    elemetos = partes[10].split(',')
                    if len(elemetos)== 1:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4]) | Tutor.objects.filter(id=elemetos[5])

            if len(partes[11]) == 0 or partes[11] == "null":
                autorsalva = None
            else:
                if partes[11] != None:
                    elemetos = partes[11].split(',')
                    if len(elemetos)== 1:
                        autorsalva = Autor.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1]) | Autor.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(id=elemetos[3]) | Autor.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(id=elemetos[3]) | Autor.objects.filter(id=elemetos[4]) | Autor.objects.filter(id=elemetos[5])

            if len(partes[12]) == 0 or partes[12] == "null":
                areasalva = None
            else:
                if partes[12] != None:
                    elemetos = partes[12].split(',')
                    if len(elemetos)== 1:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3]) | AreaConocimiento.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3]) | AreaConocimiento.objects.filter(id=elemetos[4]) | AreaConocimiento.objects.filter(id=elemetos[5])


            form = GuardarProyectoForm(data)
            formset = ImagenFormset(queryset=Imagenes.objects.none())
            formar = ArchivosFormset(queryset=Archivos.objects.none())
            formac = ActasFormset(queryset=Actas.objects.none())
            formi = GuardarInstitucionForm()
            formti = GuardarTipoForm()
            formre = GuardarResponsableForm()
            formt = GuardarTutorForm()
            forma = GuardarAutorForm()
            formare = GuardarAreaForm()
            message1 = "El Tipo de Proyecto a sido registrado con éxito."
            return render(request, 'proyecto/agregar_proyecto.html',
                          {'message': message, 'message1': message1, 'form': form, 'formset': formset, 'formar': formar, 'formac': formac,
                           'formi': formi, 'formti': formti, 'formre': formre, 'formt': formt, 'forma': forma,
                           'formare': formare,
                           'carreras': carreras, 'tipoproyectos': tipoproyectos, 'instituciones': instituciones,
                           'responsableinstitucionales': responsableinstitucionales, 'autores': autores, 'tutores': tutores,
                           'areaconocimientos': areaconocimientos,
                           'institucionsalva':institucionsalva,'tiporsalva':tiporsalva,'responsablesalva':responsablesalva,
                           'tutorsalva':tutorsalva,'autorsalva': autorsalva,'areasalva':areasalva})
        elif formre.is_valid():
            formre.save()
            data = {'Titulo': partes[0],
                    'Proposito': partes[1],
                    'Estado_proyecto': partes[2],
                    'Poblacion_utiliza': partes[3],
                    'Numero_muestra_ninos': partes[4],
                    'Tiempo_inactividad': partes[5],
                    'Sugerencias': partes[6],
                    'Fecha_Donacion': partes[13],
                    }
            if len(partes[7]) == 0 or partes[7] == "null":
                institucionsalva = None
            else:
                if partes[7] != None:
                    elemetos = partes[7].split(',')
                    if len(elemetos)== 1:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4]) | Institucion.objects.filter(id=elemetos[5])

            if len(partes[8]) == 0 or partes[8] == "null":
                tiporsalva = None
            else:
                if partes[8] != None:
                    elemetos = partes[8].split(',')
                    if len(elemetos)== 1:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4]) | TipoProyecto.objects.filter(id=elemetos[5])

            if len(partes[9]) == 0 or partes[9] == "null":
                responsablesalva = None
            else:
                if partes[9] != None:
                    elemetos = partes[9].split(',')
                    if len(elemetos)== 1:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3]) | ResponsableInstitucional.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3]) | ResponsableInstitucional.objects.filter(id=elemetos[4]) | ResponsableInstitucional.objects.filter(id=elemetos[5])


            if len(partes[10]) == 0 or partes[10] == "null":
                tutorsalva = None
            else:
                if partes[10] != None:
                    elemetos = partes[10].split(',')
                    if len(elemetos)== 1:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4]) | Tutor.objects.filter(id=elemetos[5])

            if len(partes[11]) == 0 or partes[11] == "null":
                autorsalva = None
            else:
                if partes[11] != None:
                    elemetos = partes[11].split(',')
                    if len(elemetos)== 1:
                        autorsalva = Autor.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1]) | Autor.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(id=elemetos[3]) | Autor.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(id=elemetos[3]) | Autor.objects.filter(id=elemetos[4]) | Autor.objects.filter(id=elemetos[5])

            if len(partes[12]) == 0 or partes[12] == "null":
                areasalva = None
            else:
                if partes[12] != None:
                    elemetos = partes[12].split(',')
                    if len(elemetos)== 1:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3]) | AreaConocimiento.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3]) | AreaConocimiento.objects.filter(id=elemetos[4]) | AreaConocimiento.objects.filter(id=elemetos[5])

            form = GuardarProyectoForm(data)
            formset = ImagenFormset(queryset=Imagenes.objects.none())
            formar = ArchivosFormset(queryset=Archivos.objects.none())
            formac = ActasFormset(queryset=Actas.objects.none())
            formi = GuardarInstitucionForm()
            formti = GuardarTipoForm()
            formre = GuardarResponsableForm()
            formt = GuardarTutorForm()
            forma = GuardarAutorForm()
            formare = GuardarAreaForm()
            message1 = "El Responsable Institucional a sido registrado con éxito."
            return render(request, 'proyecto/agregar_proyecto.html',
                          {'message': message, 'message1': message1, 'form': form, 'formset': formset, 'formar': formar, 'formac': formac,
                           'formi': formi, 'formti': formti, 'formre': formre, 'formt': formt, 'forma': forma,
                           'formare': formare,
                           'carreras': carreras, 'tipoproyectos': tipoproyectos, 'instituciones': instituciones,
                           'responsableinstitucionales': responsableinstitucionales, 'autores': autores, 'tutores': tutores,
                           'areaconocimientos': areaconocimientos,
                           'institucionsalva':institucionsalva,'tiporsalva':tiporsalva,'responsablesalva':responsablesalva,
                           'tutorsalva':tutorsalva,'autorsalva': autorsalva,'areasalva':areasalva})
        elif formt.is_valid():
            cedula = formt.cleaned_data.get('cedula_tutor')
            if len(cedula) == 10:
                if verificar(cedula) is not False:
                    formt.save()
                    data = {'Titulo': partes[0],
                            'Proposito': partes[1],
                            'Estado_proyecto': partes[2],
                            'Poblacion_utiliza': partes[3],
                            'Numero_muestra_ninos': partes[4],
                            'Tiempo_inactividad': partes[5],
                            'Sugerencias': partes[6],
                            'Fecha_Donacion': partes[13],
                            }
                    if len(partes[7]) == 0 or partes[7] == "null":
                        institucionsalva = None
                    else:
                        if partes[7] != None:
                            elemetos = partes[7].split(',')
                            if len(elemetos) == 1:
                                institucionsalva = Institucion.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(id=elemetos[1])
                            elif len(elemetos) == 3:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1]) | Institucion.objects.filter(
                                    id=elemetos[2]) | Institucion.objects.filter(id=elemetos[3])
                            elif len(elemetos) == 5:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1]) | Institucion.objects.filter(
                                    id=elemetos[2]) | Institucion.objects.filter(
                                    id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1]) | Institucion.objects.filter(
                                    id=elemetos[2]) | Institucion.objects.filter(
                                    id=elemetos[3]) | Institucion.objects.filter(
                                    id=elemetos[4]) | Institucion.objects.filter(id=elemetos[5])

                    if len(partes[8]) == 0 or partes[8] == "null":
                        tiporsalva = None
                    else:
                        if partes[8] != None:
                            elemetos = partes[8].split(',')
                            if len(elemetos) == 1:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1])
                            elif len(elemetos) == 3:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1]) | TipoProyecto.objects.filter(
                                    id=elemetos[2]) | TipoProyecto.objects.filter(id=elemetos[3])
                            elif len(elemetos) == 5:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1]) | TipoProyecto.objects.filter(
                                    id=elemetos[2]) | TipoProyecto.objects.filter(
                                    id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1]) | TipoProyecto.objects.filter(
                                    id=elemetos[2]) | TipoProyecto.objects.filter(
                                    id=elemetos[3]) | TipoProyecto.objects.filter(
                                    id=elemetos[4]) | TipoProyecto.objects.filter(id=elemetos[5])

                    if len(partes[9]) == 0 or partes[9] == "null":
                        responsablesalva = None
                    else:
                        if partes[9] != None:
                            elemetos = partes[9].split(',')
                            if len(elemetos) == 1:
                                responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1])
                            elif len(elemetos) == 3:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3])
                            elif len(elemetos) == 5:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[3]) | ResponsableInstitucional.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[3]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[4]) | ResponsableInstitucional.objects.filter(id=elemetos[5])

                    if len(partes[10]) == 0 or partes[10] == "null":
                        tutorsalva = None
                    else:
                        if partes[10] != None:
                            elemetos = partes[10].split(',')
                            if len(elemetos) == 1:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1])
                            elif len(elemetos) == 3:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                    id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                    id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                    id=elemetos[3])
                            elif len(elemetos) == 5:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                    id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                    id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                    id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                    id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4]) | Tutor.objects.filter(
                                    id=elemetos[5])

                    if len(partes[11]) == 0 or partes[11] == "null":
                        autorsalva = None
                    else:
                        if partes[11] != None:
                            elemetos = partes[11].split(',')
                            if len(elemetos) == 1:
                                autorsalva = Autor.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1])
                            elif len(elemetos) == 3:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                    id=elemetos[1]) | Autor.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                    id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                    id=elemetos[3])
                            elif len(elemetos) == 5:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                    id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                    id=elemetos[3]) | Autor.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                    id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                    id=elemetos[3]) | Autor.objects.filter(id=elemetos[4]) | Autor.objects.filter(
                                    id=elemetos[5])

                    if len(partes[12]) == 0 or partes[12] == "null":
                        areasalva = None
                    else:
                        if partes[12] != None:
                            elemetos = partes[12].split(',')
                            if len(elemetos) == 1:
                                areasalva = AreaConocimiento.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(id=elemetos[1])
                            elif len(elemetos) == 3:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1]) | AreaConocimiento.objects.filter(
                                    id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3])
                            elif len(elemetos) == 5:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1]) | AreaConocimiento.objects.filter(
                                    id=elemetos[2]) | AreaConocimiento.objects.filter(
                                    id=elemetos[3]) | AreaConocimiento.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1]) | AreaConocimiento.objects.filter(
                                    id=elemetos[2]) | AreaConocimiento.objects.filter(
                                    id=elemetos[3]) | AreaConocimiento.objects.filter(
                                    id=elemetos[4]) | AreaConocimiento.objects.filter(id=elemetos[5])

                    form = GuardarProyectoForm(data)
                    formset = ImagenFormset(queryset=Imagenes.objects.none())
                    formar = ArchivosFormset(queryset=Archivos.objects.none())
                    formac = ActasFormset(queryset=Actas.objects.none())
                    formi = GuardarInstitucionForm()
                    formti = GuardarTipoForm()
                    formre = GuardarResponsableForm()
                    formt = GuardarTutorForm()
                    forma = GuardarAutorForm()
                    formare = GuardarAreaForm()
                    message1 = "El Tutor a sido registrado con éxito."
                    return render(request, 'proyecto/agregar_proyecto.html',
                                  {'message': message, 'message1': message1, 'form': form, 'formset': formset, 'formar': formar,
                                   'formac': formac,
                                   'formi': formi, 'formti': formti, 'formre': formre, 'formt': formt, 'forma': forma,
                                   'formare': formare,
                                   'carreras': carreras, 'tipoproyectos': tipoproyectos, 'instituciones': instituciones,
                                   'responsableinstitucionales': responsableinstitucionales, 'autores': autores,
                                   'tutores': tutores,
                                   'areaconocimientos': areaconocimientos,
                                   'institucionsalva':institucionsalva,'tiporsalva':tiporsalva,'responsablesalva':responsablesalva,
                                   'tutorsalva':tutorsalva,'autorsalva': autorsalva,'areasalva':areasalva})
                else:
                    message = "El número de cédula del Tutor es invalido, verifique el número."
                    data = {'Titulo': partes[0],
                            'Proposito': partes[1],
                            'Estado_proyecto': partes[2],
                            'Poblacion_utiliza': partes[3],
                            'Numero_muestra_ninos': partes[4],
                            'Tiempo_inactividad': partes[5],
                            'Sugerencias': partes[6],
                            'Fecha_Donacion': partes[13],
                            }

                    if len(partes[7]) == 0 or partes[7] == "null":
                        institucionsalva = None
                    else:
                        if partes[7] != None:
                            elemetos = partes[7].split(',')
                            if len(elemetos) == 1:
                                institucionsalva = Institucion.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(id=elemetos[1])
                            elif len(elemetos) == 3:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1]) | Institucion.objects.filter(
                                    id=elemetos[2]) | Institucion.objects.filter(id=elemetos[3])
                            elif len(elemetos) == 5:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1]) | Institucion.objects.filter(
                                    id=elemetos[2]) | Institucion.objects.filter(
                                    id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1]) | Institucion.objects.filter(
                                    id=elemetos[2]) | Institucion.objects.filter(
                                    id=elemetos[3]) | Institucion.objects.filter(
                                    id=elemetos[4]) | Institucion.objects.filter(id=elemetos[5])

                    if len(partes[8]) == 0 or partes[8] == "null":
                        tiporsalva = None
                    else:
                        if partes[8] != None:
                            elemetos = partes[8].split(',')
                            if len(elemetos) == 1:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1])
                            elif len(elemetos) == 3:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1]) | TipoProyecto.objects.filter(
                                    id=elemetos[2]) | TipoProyecto.objects.filter(id=elemetos[3])
                            elif len(elemetos) == 5:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1]) | TipoProyecto.objects.filter(
                                    id=elemetos[2]) | TipoProyecto.objects.filter(
                                    id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1]) | TipoProyecto.objects.filter(
                                    id=elemetos[2]) | TipoProyecto.objects.filter(
                                    id=elemetos[3]) | TipoProyecto.objects.filter(
                                    id=elemetos[4]) | TipoProyecto.objects.filter(id=elemetos[5])

                    if len(partes[9]) == 0 or partes[9] == "null":
                        responsablesalva = None
                    else:
                        if partes[9] != None:
                            elemetos = partes[9].split(',')
                            if len(elemetos) == 1:
                                responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1])
                            elif len(elemetos) == 3:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3])
                            elif len(elemetos) == 5:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[3]) | ResponsableInstitucional.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[3]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[4]) | ResponsableInstitucional.objects.filter(id=elemetos[5])

                    if len(partes[10]) == 0 or partes[10] == "null":
                        tutorsalva = None
                    else:
                        if partes[10] != None:
                            elemetos = partes[10].split(',')
                            if len(elemetos) == 1:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1])
                            elif len(elemetos) == 3:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                    id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                    id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                    id=elemetos[3])
                            elif len(elemetos) == 5:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                    id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                    id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                    id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                    id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4]) | Tutor.objects.filter(
                                    id=elemetos[5])

                    if len(partes[11]) == 0 or partes[11] == "null":
                        autorsalva = None
                    else:
                        if partes[11] != None:
                            elemetos = partes[11].split(',')
                            if len(elemetos) == 1:
                                autorsalva = Autor.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1])
                            elif len(elemetos) == 3:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                    id=elemetos[1]) | Autor.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                    id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                    id=elemetos[3])
                            elif len(elemetos) == 5:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                    id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                    id=elemetos[3]) | Autor.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                    id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                    id=elemetos[3]) | Autor.objects.filter(id=elemetos[4]) | Autor.objects.filter(
                                    id=elemetos[5])

                    if len(partes[12]) == 0 or partes[12] == "null":
                        areasalva = None
                    else:
                        if partes[12] != None:
                            elemetos = partes[12].split(',')
                            if len(elemetos) == 1:
                                areasalva = AreaConocimiento.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(id=elemetos[1])
                            elif len(elemetos) == 3:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1]) | AreaConocimiento.objects.filter(
                                    id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3])
                            elif len(elemetos) == 5:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1]) | AreaConocimiento.objects.filter(
                                    id=elemetos[2]) | AreaConocimiento.objects.filter(
                                    id=elemetos[3]) | AreaConocimiento.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1]) | AreaConocimiento.objects.filter(
                                    id=elemetos[2]) | AreaConocimiento.objects.filter(
                                    id=elemetos[3]) | AreaConocimiento.objects.filter(
                                    id=elemetos[4]) | AreaConocimiento.objects.filter(id=elemetos[5])

                    form = GuardarProyectoForm(data)
                    formset = ImagenFormset(queryset=Imagenes.objects.none())
                    formar = ArchivosFormset(queryset=Archivos.objects.none())
                    formac = ActasFormset(queryset=Actas.objects.none())
                    formi = GuardarInstitucionForm()
                    formti = GuardarTipoForm()
                    formre = GuardarResponsableForm()
                    formt = GuardarTutorForm(request.POST, request.FILES)
                    forma = GuardarAutorForm()
                    formare = GuardarAreaForm()
                    return render(request, 'proyecto/agregar_proyecto.html',
                                  {'message': message, 'form': form, 'formset': formset, 'formar': formar,
                                   'formac': formac,
                                   'formi': formi, 'formti': formti, 'formre': formre, 'formt': formt, 'forma': forma,
                                   'formare': formare,
                                   'carreras': carreras, 'tipoproyectos': tipoproyectos, 'instituciones': instituciones,
                                   'responsableinstitucionales': responsableinstitucionales, 'autores': autores,
                                   'tutores': tutores,
                                   'areaconocimientos': areaconocimientos,
                                   'institucionsalva': institucionsalva, 'tiporsalva': tiporsalva,
                                   'responsablesalva': responsablesalva,
                                   'tutorsalva': tutorsalva, 'autorsalva': autorsalva, 'areasalva': areasalva
                                   })
            else:
                message = "Ingrese los 10 dígitos de la cédula para registrar el Tutor."
                data = {'Titulo': partes[0],
                        'Proposito': partes[1],
                        'Estado_proyecto': partes[2],
                        'Poblacion_utiliza': partes[3],
                        'Numero_muestra_ninos': partes[4],
                        'Tiempo_inactividad': partes[5],
                        'Sugerencias': partes[6],
                        'Fecha_Donacion': partes[13],
                        }
                if len(partes[7]) == 0 or partes[7] == "null":
                    institucionsalva = None
                else:
                    if partes[7] != None:
                        elemetos = partes[7].split(',')
                        if len(elemetos) == 1:
                            institucionsalva = Institucion.objects.filter(id=elemetos[0])
                        elif len(elemetos) == 2:
                            institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                                id=elemetos[1])
                        elif len(elemetos) == 3:
                            institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                                id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2])
                        elif len(elemetos) == 4:
                            institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                                id=elemetos[1]) | Institucion.objects.filter(
                                id=elemetos[2]) | Institucion.objects.filter(id=elemetos[3])
                        elif len(elemetos) == 5:
                            institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                                id=elemetos[1]) | Institucion.objects.filter(
                                id=elemetos[2]) | Institucion.objects.filter(
                                id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4])
                        elif len(elemetos) == 6:
                            institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                                id=elemetos[1]) | Institucion.objects.filter(
                                id=elemetos[2]) | Institucion.objects.filter(
                                id=elemetos[3]) | Institucion.objects.filter(
                                id=elemetos[4]) | Institucion.objects.filter(id=elemetos[5])

                if len(partes[8]) == 0 or partes[8] == "null":
                    tiporsalva = None
                else:
                    if partes[8] != None:
                        elemetos = partes[8].split(',')
                        if len(elemetos) == 1:
                            tiporsalva = TipoProyecto.objects.filter(id=elemetos[0])
                        elif len(elemetos) == 2:
                            tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                id=elemetos[1])
                        elif len(elemetos) == 3:
                            tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2])
                        elif len(elemetos) == 4:
                            tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                id=elemetos[1]) | TipoProyecto.objects.filter(
                                id=elemetos[2]) | TipoProyecto.objects.filter(id=elemetos[3])
                        elif len(elemetos) == 5:
                            tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                id=elemetos[1]) | TipoProyecto.objects.filter(
                                id=elemetos[2]) | TipoProyecto.objects.filter(
                                id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4])
                        elif len(elemetos) == 6:
                            tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                id=elemetos[1]) | TipoProyecto.objects.filter(
                                id=elemetos[2]) | TipoProyecto.objects.filter(
                                id=elemetos[3]) | TipoProyecto.objects.filter(
                                id=elemetos[4]) | TipoProyecto.objects.filter(id=elemetos[5])

                if len(partes[9]) == 0 or partes[9] == "null":
                    responsablesalva = None
                else:
                    if partes[9] != None:
                        elemetos = partes[9].split(',')
                        if len(elemetos) == 1:
                            responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0])
                        elif len(elemetos) == 2:
                            responsablesalva = ResponsableInstitucional.objects.filter(
                                id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1])
                        elif len(elemetos) == 3:
                            responsablesalva = ResponsableInstitucional.objects.filter(
                                id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2])
                        elif len(elemetos) == 4:
                            responsablesalva = ResponsableInstitucional.objects.filter(
                                id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3])
                        elif len(elemetos) == 5:
                            responsablesalva = ResponsableInstitucional.objects.filter(
                                id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[3]) | ResponsableInstitucional.objects.filter(id=elemetos[4])
                        elif len(elemetos) == 6:
                            responsablesalva = ResponsableInstitucional.objects.filter(
                                id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[3]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[4]) | ResponsableInstitucional.objects.filter(id=elemetos[5])

                if len(partes[10]) == 0 or partes[10] == "null":
                    tutorsalva = None
                else:
                    if partes[10] != None:
                        elemetos = partes[10].split(',')
                        if len(elemetos) == 1:
                            tutorsalva = Tutor.objects.filter(id=elemetos[0])
                        elif len(elemetos) == 2:
                            tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1])
                        elif len(elemetos) == 3:
                            tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2])
                        elif len(elemetos) == 4:
                            tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                id=elemetos[3])
                        elif len(elemetos) == 5:
                            tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4])
                        elif len(elemetos) == 6:
                            tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4]) | Tutor.objects.filter(
                                id=elemetos[5])

                if len(partes[11]) == 0 or partes[11] == "null":
                    autorsalva = None
                else:
                    if partes[11] != None:
                        elemetos = partes[11].split(',')
                        if len(elemetos) == 1:
                            autorsalva = Autor.objects.filter(id=elemetos[0])
                        elif len(elemetos) == 2:
                            autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1])
                        elif len(elemetos) == 3:
                            autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                id=elemetos[1]) | Autor.objects.filter(id=elemetos[2])
                        elif len(elemetos) == 4:
                            autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                id=elemetos[3])
                        elif len(elemetos) == 5:
                            autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                id=elemetos[3]) | Autor.objects.filter(id=elemetos[4])
                        elif len(elemetos) == 6:
                            autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                id=elemetos[3]) | Autor.objects.filter(id=elemetos[4]) | Autor.objects.filter(
                                id=elemetos[5])

                if len(partes[12]) == 0 or partes[12] == "null":
                    areasalva = None
                else:
                    if partes[12] != None:
                        elemetos = partes[12].split(',')
                        if len(elemetos) == 1:
                            areasalva = AreaConocimiento.objects.filter(id=elemetos[0])
                        elif len(elemetos) == 2:
                            areasalva = AreaConocimiento.objects.filter(
                                id=elemetos[0]) | AreaConocimiento.objects.filter(id=elemetos[1])
                        elif len(elemetos) == 3:
                            areasalva = AreaConocimiento.objects.filter(
                                id=elemetos[0]) | AreaConocimiento.objects.filter(
                                id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2])
                        elif len(elemetos) == 4:
                            areasalva = AreaConocimiento.objects.filter(
                                id=elemetos[0]) | AreaConocimiento.objects.filter(
                                id=elemetos[1]) | AreaConocimiento.objects.filter(
                                id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3])
                        elif len(elemetos) == 5:
                            areasalva = AreaConocimiento.objects.filter(
                                id=elemetos[0]) | AreaConocimiento.objects.filter(
                                id=elemetos[1]) | AreaConocimiento.objects.filter(
                                id=elemetos[2]) | AreaConocimiento.objects.filter(
                                id=elemetos[3]) | AreaConocimiento.objects.filter(id=elemetos[4])
                        elif len(elemetos) == 6:
                            areasalva = AreaConocimiento.objects.filter(
                                id=elemetos[0]) | AreaConocimiento.objects.filter(
                                id=elemetos[1]) | AreaConocimiento.objects.filter(
                                id=elemetos[2]) | AreaConocimiento.objects.filter(
                                id=elemetos[3]) | AreaConocimiento.objects.filter(
                                id=elemetos[4]) | AreaConocimiento.objects.filter(id=elemetos[5])

                form = GuardarProyectoForm(data)
                formset = ImagenFormset(queryset=Imagenes.objects.none())
                formar = ArchivosFormset(queryset=Archivos.objects.none())
                formac = ActasFormset(queryset=Actas.objects.none())
                formi = GuardarInstitucionForm()
                formti = GuardarTipoForm()
                formre = GuardarResponsableForm()
                formt = GuardarTutorForm(request.POST, request.FILES)
                forma = GuardarAutorForm()
                formare = GuardarAreaForm()
                return render(request, 'proyecto/agregar_proyecto.html',
                              {'message': message, 'form': form, 'formset': formset, 'formar': formar, 'formac': formac,
                               'formi': formi, 'formti': formti, 'formre': formre, 'formt': formt, 'forma': forma,
                               'formare': formare,
                               'carreras': carreras, 'tipoproyectos': tipoproyectos, 'instituciones': instituciones,
                               'responsableinstitucionales': responsableinstitucionales, 'autores': autores,
                               'tutores': tutores,
                               'areaconocimientos': areaconocimientos,
                               'institucionsalva': institucionsalva, 'tiporsalva': tiporsalva,
                               'responsablesalva': responsablesalva,
                               'tutorsalva': tutorsalva, 'autorsalva': autorsalva, 'areasalva': areasalva
                               })

        elif forma.is_valid():
            cedula = forma.cleaned_data.get('cedula_autor')
            if len(cedula) == 10:
                if verificar(cedula) is not False:
                    forma.save()
                    data = {'Titulo': partes[0],
                            'Proposito': partes[1],
                            'Estado_proyecto': partes[2],
                            'Poblacion_utiliza': partes[3],
                            'Numero_muestra_ninos': partes[4],
                            'Tiempo_inactividad': partes[5],
                            'Sugerencias': partes[6],
                            'Fecha_Donacion': partes[13],
                            }

                    if len(partes[7]) == 0 or partes[7] == "null":
                        institucionsalva = None
                    else:
                        if partes[7] != None:
                            elemetos = partes[7].split(',')
                            if len(elemetos) == 1:
                                institucionsalva = Institucion.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(id=elemetos[1])
                            elif len(elemetos) == 3:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1]) | Institucion.objects.filter(
                                    id=elemetos[2]) | Institucion.objects.filter(id=elemetos[3])
                            elif len(elemetos) == 5:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1]) | Institucion.objects.filter(
                                    id=elemetos[2]) | Institucion.objects.filter(
                                    id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1]) | Institucion.objects.filter(
                                    id=elemetos[2]) | Institucion.objects.filter(
                                    id=elemetos[3]) | Institucion.objects.filter(
                                    id=elemetos[4]) | Institucion.objects.filter(id=elemetos[5])

                    if len(partes[8]) == 0 or partes[8] == "null":
                        tiporsalva = None
                    else:
                        if partes[8] != None:
                            elemetos = partes[8].split(',')
                            if len(elemetos) == 1:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1])
                            elif len(elemetos) == 3:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1]) | TipoProyecto.objects.filter(
                                    id=elemetos[2]) | TipoProyecto.objects.filter(id=elemetos[3])
                            elif len(elemetos) == 5:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1]) | TipoProyecto.objects.filter(
                                    id=elemetos[2]) | TipoProyecto.objects.filter(
                                    id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1]) | TipoProyecto.objects.filter(
                                    id=elemetos[2]) | TipoProyecto.objects.filter(
                                    id=elemetos[3]) | TipoProyecto.objects.filter(
                                    id=elemetos[4]) | TipoProyecto.objects.filter(id=elemetos[5])

                    if len(partes[9]) == 0 or partes[9] == "null":
                        responsablesalva = None
                    else:
                        if partes[9] != None:
                            elemetos = partes[9].split(',')
                            if len(elemetos) == 1:
                                responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1])
                            elif len(elemetos) == 3:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3])
                            elif len(elemetos) == 5:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[3]) | ResponsableInstitucional.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[3]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[4]) | ResponsableInstitucional.objects.filter(id=elemetos[5])

                    if len(partes[10]) == 0 or partes[10] == "null":
                        tutorsalva = None
                    else:
                        if partes[10] != None:
                            elemetos = partes[10].split(',')
                            if len(elemetos) == 1:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1])
                            elif len(elemetos) == 3:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                    id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                    id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                    id=elemetos[3])
                            elif len(elemetos) == 5:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                    id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                    id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                    id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                    id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4]) | Tutor.objects.filter(
                                    id=elemetos[5])

                    if len(partes[11]) == 0 or partes[11] == "null":
                        autorsalva = None
                    else:
                        if partes[11] != None:
                            elemetos = partes[11].split(',')
                            if len(elemetos) == 1:
                                autorsalva = Autor.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1])
                            elif len(elemetos) == 3:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                    id=elemetos[1]) | Autor.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                    id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                    id=elemetos[3])
                            elif len(elemetos) == 5:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                    id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                    id=elemetos[3]) | Autor.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                    id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                    id=elemetos[3]) | Autor.objects.filter(id=elemetos[4]) | Autor.objects.filter(
                                    id=elemetos[5])

                    if len(partes[12]) == 0 or partes[12] == "null":
                        areasalva = None
                    else:
                        if partes[12] != None:
                            elemetos = partes[12].split(',')
                            if len(elemetos) == 1:
                                areasalva = AreaConocimiento.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(id=elemetos[1])
                            elif len(elemetos) == 3:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1]) | AreaConocimiento.objects.filter(
                                    id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3])
                            elif len(elemetos) == 5:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1]) | AreaConocimiento.objects.filter(
                                    id=elemetos[2]) | AreaConocimiento.objects.filter(
                                    id=elemetos[3]) | AreaConocimiento.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1]) | AreaConocimiento.objects.filter(
                                    id=elemetos[2]) | AreaConocimiento.objects.filter(
                                    id=elemetos[3]) | AreaConocimiento.objects.filter(
                                    id=elemetos[4]) | AreaConocimiento.objects.filter(id=elemetos[5])

                    form = GuardarProyectoForm(data)
                    formset = ImagenFormset(queryset=Imagenes.objects.none())
                    formar = ArchivosFormset(queryset=Archivos.objects.none())
                    formac = ActasFormset(queryset=Actas.objects.none())
                    formi = GuardarInstitucionForm()
                    formti = GuardarTipoForm()
                    formre = GuardarResponsableForm()
                    formt = GuardarTutorForm()
                    forma = GuardarAutorForm()
                    formare = GuardarAreaForm()
                    message1 = "El Autor a sido registrado con éxito."
                    return render(request, 'proyecto/agregar_proyecto.html',
                                  {'message': message, 'message1': message1, 'form': form, 'formset': formset, 'formar': formar,
                                   'formac': formac,
                                   'formi': formi, 'formti': formti, 'formre': formre, 'formt': formt, 'forma': forma,
                                   'formare': formare,
                                   'carreras': carreras, 'tipoproyectos': tipoproyectos, 'instituciones': instituciones,
                                   'responsableinstitucionales': responsableinstitucionales, 'autores': autores,
                                   'tutores': tutores,
                                   'areaconocimientos': areaconocimientos,
                                   'institucionsalva': institucionsalva, 'tiporsalva': tiporsalva,
                                   'responsablesalva': responsablesalva,
                                   'tutorsalva': tutorsalva, 'autorsalva': autorsalva, 'areasalva': areasalva
                                   })
                else:
                    message = "Ingrese los 10 dígitos de la cédula para registrar el Autor."
                    data = {'Titulo': partes[0],
                            'Proposito': partes[1],
                            'Estado_proyecto': partes[2],
                            'Poblacion_utiliza': partes[3],
                            'Numero_muestra_ninos': partes[4],
                            'Tiempo_inactividad': partes[5],
                            'Sugerencias': partes[6],
                            'Fecha_Donacion': partes[13],
                            }

                    if len(partes[7]) == 0 or partes[7] == "null":
                        institucionsalva = None
                    else:
                        if partes[7] != None:
                            elemetos = partes[7].split(',')
                            if len(elemetos) == 1:
                                institucionsalva = Institucion.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(id=elemetos[1])
                            elif len(elemetos) == 3:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1]) | Institucion.objects.filter(
                                    id=elemetos[2]) | Institucion.objects.filter(id=elemetos[3])
                            elif len(elemetos) == 5:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1]) | Institucion.objects.filter(
                                    id=elemetos[2]) | Institucion.objects.filter(
                                    id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1]) | Institucion.objects.filter(
                                    id=elemetos[2]) | Institucion.objects.filter(
                                    id=elemetos[3]) | Institucion.objects.filter(
                                    id=elemetos[4]) | Institucion.objects.filter(id=elemetos[5])

                    if len(partes[8]) == 0 or partes[8] == "null":
                        tiporsalva = None
                    else:
                        if partes[8] != None:
                            elemetos = partes[8].split(',')
                            if len(elemetos) == 1:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1])
                            elif len(elemetos) == 3:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1]) | TipoProyecto.objects.filter(
                                    id=elemetos[2]) | TipoProyecto.objects.filter(id=elemetos[3])
                            elif len(elemetos) == 5:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1]) | TipoProyecto.objects.filter(
                                    id=elemetos[2]) | TipoProyecto.objects.filter(
                                    id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1]) | TipoProyecto.objects.filter(
                                    id=elemetos[2]) | TipoProyecto.objects.filter(
                                    id=elemetos[3]) | TipoProyecto.objects.filter(
                                    id=elemetos[4]) | TipoProyecto.objects.filter(id=elemetos[5])

                    if len(partes[9]) == 0 or partes[9] == "null":
                        responsablesalva = None
                    else:
                        if partes[9] != None:
                            elemetos = partes[9].split(',')
                            if len(elemetos) == 1:
                                responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1])
                            elif len(elemetos) == 3:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3])
                            elif len(elemetos) == 5:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[3]) | ResponsableInstitucional.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[3]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[4]) | ResponsableInstitucional.objects.filter(id=elemetos[5])

                    if len(partes[10]) == 0 or partes[10] == "null":
                        tutorsalva = None
                    else:
                        if partes[10] != None:
                            elemetos = partes[10].split(',')
                            if len(elemetos) == 1:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1])
                            elif len(elemetos) == 3:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                    id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                    id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                    id=elemetos[3])
                            elif len(elemetos) == 5:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                    id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                    id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                    id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                    id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4]) | Tutor.objects.filter(
                                    id=elemetos[5])

                    if len(partes[11]) == 0 or partes[11] == "null":
                        autorsalva = None
                    else:
                        if partes[11] != None:
                            elemetos = partes[11].split(',')
                            if len(elemetos) == 1:
                                autorsalva = Autor.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1])
                            elif len(elemetos) == 3:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                    id=elemetos[1]) | Autor.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                    id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                    id=elemetos[3])
                            elif len(elemetos) == 5:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                    id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                    id=elemetos[3]) | Autor.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                    id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                    id=elemetos[3]) | Autor.objects.filter(id=elemetos[4]) | Autor.objects.filter(
                                    id=elemetos[5])

                    if len(partes[12]) == 0 or partes[12] == "null":
                        areasalva = None
                    else:
                        if partes[12] != None:
                            elemetos = partes[12].split(',')
                            if len(elemetos) == 1:
                                areasalva = AreaConocimiento.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(id=elemetos[1])
                            elif len(elemetos) == 3:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1]) | AreaConocimiento.objects.filter(
                                    id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3])
                            elif len(elemetos) == 5:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1]) | AreaConocimiento.objects.filter(
                                    id=elemetos[2]) | AreaConocimiento.objects.filter(
                                    id=elemetos[3]) | AreaConocimiento.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1]) | AreaConocimiento.objects.filter(
                                    id=elemetos[2]) | AreaConocimiento.objects.filter(
                                    id=elemetos[3]) | AreaConocimiento.objects.filter(
                                    id=elemetos[4]) | AreaConocimiento.objects.filter(id=elemetos[5])

                    form = GuardarProyectoForm(data)
                    formset = ImagenFormset(queryset=Imagenes.objects.none())
                    formar = ArchivosFormset(queryset=Archivos.objects.none())
                    formac = ActasFormset(queryset=Actas.objects.none())
                    formi = GuardarInstitucionForm()
                    formti = GuardarTipoForm()
                    formre = GuardarResponsableForm()
                    formt = GuardarTutorForm()
                    forma = GuardarAutorForm(request.POST, request.FILES)
                    formare = GuardarAreaForm()
                    return render(request, 'proyecto/agregar_proyecto.html',
                                  {'message': message, 'form': form, 'formset': formset, 'formar': formar,
                                   'formac': formac,
                                   'formi': formi, 'formti': formti, 'formre': formre, 'formt': formt, 'forma': forma,
                                   'formare': formare,
                                   'carreras': carreras, 'tipoproyectos': tipoproyectos, 'instituciones': instituciones,
                                   'responsableinstitucionales': responsableinstitucionales, 'autores': autores,
                                   'tutores': tutores,
                                   'areaconocimientos': areaconocimientos,
                                   'institucionsalva': institucionsalva, 'tiporsalva': tiporsalva,
                                   'responsablesalva': responsablesalva,
                                   'tutorsalva': tutorsalva, 'autorsalva': autorsalva, 'areasalva': areasalva
                                   })
            else:
                message = "Ingrese los 10 dígitos de la cédula para registrar el Autor."
                data = {'Titulo': partes[0],
                        'Proposito': partes[1],
                        'Estado_proyecto': partes[2],
                        'Poblacion_utiliza': partes[3],
                        'Numero_muestra_ninos': partes[4],
                        'Tiempo_inactividad': partes[5],
                        'Sugerencias': partes[6],
                        'Fecha_Donacion': partes[13],
                        }

                if len(partes[7]) == 0 or partes[7] == "null":
                    institucionsalva = None
                else:
                    if partes[7] != None:
                        elemetos = partes[7].split(',')
                        if len(elemetos) == 1:
                            institucionsalva = Institucion.objects.filter(id=elemetos[0])
                        elif len(elemetos) == 2:
                            institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                                id=elemetos[1])
                        elif len(elemetos) == 3:
                            institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                                id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2])
                        elif len(elemetos) == 4:
                            institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                                id=elemetos[1]) | Institucion.objects.filter(
                                id=elemetos[2]) | Institucion.objects.filter(id=elemetos[3])
                        elif len(elemetos) == 5:
                            institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                                id=elemetos[1]) | Institucion.objects.filter(
                                id=elemetos[2]) | Institucion.objects.filter(
                                id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4])
                        elif len(elemetos) == 6:
                            institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                                id=elemetos[1]) | Institucion.objects.filter(
                                id=elemetos[2]) | Institucion.objects.filter(
                                id=elemetos[3]) | Institucion.objects.filter(
                                id=elemetos[4]) | Institucion.objects.filter(id=elemetos[5])

                if len(partes[8]) == 0 or partes[8] == "null":
                    tiporsalva = None
                else:
                    if partes[8] != None:
                        elemetos = partes[8].split(',')
                        if len(elemetos) == 1:
                            tiporsalva = TipoProyecto.objects.filter(id=elemetos[0])
                        elif len(elemetos) == 2:
                            tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                id=elemetos[1])
                        elif len(elemetos) == 3:
                            tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2])
                        elif len(elemetos) == 4:
                            tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                id=elemetos[1]) | TipoProyecto.objects.filter(
                                id=elemetos[2]) | TipoProyecto.objects.filter(id=elemetos[3])
                        elif len(elemetos) == 5:
                            tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                id=elemetos[1]) | TipoProyecto.objects.filter(
                                id=elemetos[2]) | TipoProyecto.objects.filter(
                                id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4])
                        elif len(elemetos) == 6:
                            tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                id=elemetos[1]) | TipoProyecto.objects.filter(
                                id=elemetos[2]) | TipoProyecto.objects.filter(
                                id=elemetos[3]) | TipoProyecto.objects.filter(
                                id=elemetos[4]) | TipoProyecto.objects.filter(id=elemetos[5])

                if len(partes[9]) == 0 or partes[9] == "null":
                    responsablesalva = None
                else:
                    if partes[9] != None:
                        elemetos = partes[9].split(',')
                        if len(elemetos) == 1:
                            responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0])
                        elif len(elemetos) == 2:
                            responsablesalva = ResponsableInstitucional.objects.filter(
                                id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1])
                        elif len(elemetos) == 3:
                            responsablesalva = ResponsableInstitucional.objects.filter(
                                id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2])
                        elif len(elemetos) == 4:
                            responsablesalva = ResponsableInstitucional.objects.filter(
                                id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3])
                        elif len(elemetos) == 5:
                            responsablesalva = ResponsableInstitucional.objects.filter(
                                id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[3]) | ResponsableInstitucional.objects.filter(id=elemetos[4])
                        elif len(elemetos) == 6:
                            responsablesalva = ResponsableInstitucional.objects.filter(
                                id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[3]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[4]) | ResponsableInstitucional.objects.filter(id=elemetos[5])

                if len(partes[10]) == 0 or partes[10] == "null":
                    tutorsalva = None
                else:
                    if partes[10] != None:
                        elemetos = partes[10].split(',')
                        if len(elemetos) == 1:
                            tutorsalva = Tutor.objects.filter(id=elemetos[0])
                        elif len(elemetos) == 2:
                            tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1])
                        elif len(elemetos) == 3:
                            tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2])
                        elif len(elemetos) == 4:
                            tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                id=elemetos[3])
                        elif len(elemetos) == 5:
                            tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4])
                        elif len(elemetos) == 6:
                            tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4]) | Tutor.objects.filter(
                                id=elemetos[5])

                if len(partes[11]) == 0 or partes[11] == "null":
                    autorsalva = None
                else:
                    if partes[11] != None:
                        elemetos = partes[11].split(',')
                        if len(elemetos) == 1:
                            autorsalva = Autor.objects.filter(id=elemetos[0])
                        elif len(elemetos) == 2:
                            autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1])
                        elif len(elemetos) == 3:
                            autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                id=elemetos[1]) | Autor.objects.filter(id=elemetos[2])
                        elif len(elemetos) == 4:
                            autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                id=elemetos[3])
                        elif len(elemetos) == 5:
                            autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                id=elemetos[3]) | Autor.objects.filter(id=elemetos[4])
                        elif len(elemetos) == 6:
                            autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                id=elemetos[3]) | Autor.objects.filter(id=elemetos[4]) | Autor.objects.filter(
                                id=elemetos[5])

                if len(partes[12]) == 0 or partes[12] == "null":
                    areasalva = None
                else:
                    if partes[12] != None:
                        elemetos = partes[12].split(',')
                        if len(elemetos) == 1:
                            areasalva = AreaConocimiento.objects.filter(id=elemetos[0])
                        elif len(elemetos) == 2:
                            areasalva = AreaConocimiento.objects.filter(
                                id=elemetos[0]) | AreaConocimiento.objects.filter(id=elemetos[1])
                        elif len(elemetos) == 3:
                            areasalva = AreaConocimiento.objects.filter(
                                id=elemetos[0]) | AreaConocimiento.objects.filter(
                                id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2])
                        elif len(elemetos) == 4:
                            areasalva = AreaConocimiento.objects.filter(
                                id=elemetos[0]) | AreaConocimiento.objects.filter(
                                id=elemetos[1]) | AreaConocimiento.objects.filter(
                                id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3])
                        elif len(elemetos) == 5:
                            areasalva = AreaConocimiento.objects.filter(
                                id=elemetos[0]) | AreaConocimiento.objects.filter(
                                id=elemetos[1]) | AreaConocimiento.objects.filter(
                                id=elemetos[2]) | AreaConocimiento.objects.filter(
                                id=elemetos[3]) | AreaConocimiento.objects.filter(id=elemetos[4])
                        elif len(elemetos) == 6:
                            areasalva = AreaConocimiento.objects.filter(
                                id=elemetos[0]) | AreaConocimiento.objects.filter(
                                id=elemetos[1]) | AreaConocimiento.objects.filter(
                                id=elemetos[2]) | AreaConocimiento.objects.filter(
                                id=elemetos[3]) | AreaConocimiento.objects.filter(
                                id=elemetos[4]) | AreaConocimiento.objects.filter(id=elemetos[5])

                form = GuardarProyectoForm(data)
                formset = ImagenFormset(queryset=Imagenes.objects.none())
                formar = ArchivosFormset(queryset=Archivos.objects.none())
                formac = ActasFormset(queryset=Actas.objects.none())
                formi = GuardarInstitucionForm()
                formti = GuardarTipoForm()
                formre = GuardarResponsableForm()
                formt = GuardarTutorForm()
                forma = GuardarAutorForm(request.POST, request.FILES)
                formare = GuardarAreaForm()
                return render(request, 'proyecto/agregar_proyecto.html',
                              {'message': message, 'form': form, 'formset': formset, 'formar': formar,
                               'formac': formac,
                               'formi': formi, 'formti': formti, 'formre': formre, 'formt': formt, 'forma': forma,
                               'formare': formare,
                               'carreras': carreras, 'tipoproyectos': tipoproyectos, 'instituciones': instituciones,
                               'responsableinstitucionales': responsableinstitucionales, 'autores': autores,
                               'tutores': tutores,
                               'areaconocimientos': areaconocimientos,
                               'institucionsalva': institucionsalva, 'tiporsalva': tiporsalva,
                               'responsablesalva': responsablesalva,
                               'tutorsalva': tutorsalva, 'autorsalva': autorsalva, 'areasalva': areasalva
                               })

        elif formare.is_valid():
            formare.save()
            data = {'Titulo': partes[0],
                    'Proposito': partes[1],
                    'Estado_proyecto': partes[2],
                    'Poblacion_utiliza': partes[3],
                    'Numero_muestra_ninos': partes[4],
                    'Tiempo_inactividad': partes[5],
                    'Sugerencias': partes[6],
                    'Fecha_Donacion': partes[13],
                    }

            if len(partes[7]) == 0 or partes[7] == "null":
                institucionsalva = None
            else:
                if partes[7] != None:
                    elemetos = partes[7].split(',')
                    if len(elemetos)== 1:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4]) | Institucion.objects.filter(id=elemetos[5])

            if len(partes[8]) == 0 or partes[8] == "null":
                tiporsalva = None
            else:
                if partes[8] != None:
                    elemetos = partes[8].split(',')
                    if len(elemetos)== 1:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4]) | TipoProyecto.objects.filter(id=elemetos[5])

            if len(partes[9]) == 0 or partes[9] == "null":
                responsablesalva = None
            else:
                if partes[9] != None:
                    elemetos = partes[9].split(',')
                    if len(elemetos)== 1:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3]) | ResponsableInstitucional.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3]) | ResponsableInstitucional.objects.filter(id=elemetos[4]) | ResponsableInstitucional.objects.filter(id=elemetos[5])


            if len(partes[10]) == 0 or partes[10] == "null":
                tutorsalva = None
            else:
                if partes[10] != None:
                    elemetos = partes[10].split(',')
                    if len(elemetos)== 1:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4]) | Tutor.objects.filter(id=elemetos[5])

            if len(partes[11]) == 0 or partes[11] == "null":
                autorsalva = None
            else:
                if partes[11] != None:
                    elemetos = partes[11].split(',')
                    if len(elemetos)== 1:
                        autorsalva = Autor.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1]) | Autor.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(id=elemetos[3]) | Autor.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(id=elemetos[3]) | Autor.objects.filter(id=elemetos[4]) | Autor.objects.filter(id=elemetos[5])

            if len(partes[12]) == 0 or partes[12] == "null":
                areasalva = None
            else:
                if partes[12] != None:
                    elemetos = partes[12].split(',')
                    if len(elemetos)== 1:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3]) | AreaConocimiento.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3]) | AreaConocimiento.objects.filter(id=elemetos[4]) | AreaConocimiento.objects.filter(id=elemetos[5])

            form = GuardarProyectoForm(data)
            formset = ImagenFormset(queryset=Imagenes.objects.none())
            formar = ArchivosFormset(queryset=Archivos.objects.none())
            formac = ActasFormset(queryset=Actas.objects.none())
            formi = GuardarInstitucionForm()
            formti = GuardarTipoForm()
            formre = GuardarResponsableForm()
            formt = GuardarTutorForm()
            forma = GuardarAutorForm()
            formare = GuardarAreaForm()
            message1 = "El Área de Conocimiento a sido registrado con éxito."
            return render(request, 'proyecto/agregar_proyecto.html',
                          {'message': message, 'message1': message1, 'form': form, 'formset': formset, 'formar': formar, 'formac': formac,
                           'formi': formi, 'formti': formti, 'formre': formre, 'formt': formt, 'forma': forma,
                           'formare': formare,
                           'carreras': carreras, 'tipoproyectos': tipoproyectos, 'instituciones': instituciones,
                           'responsableinstitucionales': responsableinstitucionales, 'autores': autores, 'tutores': tutores,
                           'areaconocimientos': areaconocimientos,
                           'institucionsalva':institucionsalva,'tiporsalva':tiporsalva,'responsablesalva':responsablesalva,
                           'tutorsalva':tutorsalva,'autorsalva': autorsalva,'areasalva':areasalva})
        else:
            data = {'Titulo': partes[0],
                    'Proposito': partes[1],
                    'Estado_proyecto': partes[2],
                    'Poblacion_utiliza': partes[3],
                    'Numero_muestra_ninos': partes[4],
                    'Tiempo_inactividad': partes[5],
                    'Sugerencias': partes[6],
                    'Fecha_Donacion': partes[13],
                    }

            if len(partes[7]) == 0 or partes[7] == "null":
                institucionsalva = None
            else:
                if partes[7] != None:
                    elemetos = partes[7].split(',')
                    if len(elemetos)== 1:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4]) | Institucion.objects.filter(id=elemetos[5])

            if len(partes[8]) == 0 or partes[8] == "null":
                tiporsalva = None
            else:
                if partes[8] != None:
                    elemetos = partes[8].split(',')
                    if len(elemetos)== 1:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4]) | TipoProyecto.objects.filter(id=elemetos[5])

            if len(partes[9]) == 0 or partes[9] == "null":
                responsablesalva = None
            else:
                if partes[9] != None:
                    elemetos = partes[9].split(',')
                    if len(elemetos)== 1:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3]) | ResponsableInstitucional.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3]) | ResponsableInstitucional.objects.filter(id=elemetos[4]) | ResponsableInstitucional.objects.filter(id=elemetos[5])

            if len(partes[10]) == 0 or partes[10] == "null":
                tutorsalva = None
            else:
                if partes[10] != None:
                    elemetos = partes[10].split(',')
                    if len(elemetos)== 1:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4]) | Tutor.objects.filter(id=elemetos[5])

            if len(partes[11]) == 0 or partes[11] == "null":
                autorsalva = None
            else:
                if partes[11] != None:
                    elemetos = partes[11].split(',')
                    if len(elemetos)== 1:
                        autorsalva = Autor.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1]) | Autor.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(id=elemetos[3]) | Autor.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(id=elemetos[3]) | Autor.objects.filter(id=elemetos[4]) | Autor.objects.filter(id=elemetos[5])

            if len(partes[12]) == 0 or partes[12] == "null":
                areasalva = None
            else:
                if partes[12] != None:
                    elemetos = partes[12].split(',')
                    if len(elemetos)== 1:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3]) | AreaConocimiento.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3]) | AreaConocimiento.objects.filter(id=elemetos[4]) | AreaConocimiento.objects.filter(id=elemetos[5])


            form = GuardarProyectoForm(data)
            formset = ImagenFormset(queryset=Imagenes.objects.none())
            formar = ArchivosFormset(queryset=Archivos.objects.none())
            formac = ActasFormset(queryset=Actas.objects.none())
            formi = GuardarInstitucionForm()
            formti = GuardarTipoForm()
            formre = GuardarResponsableForm()
            formt = GuardarTutorForm()
            forma = GuardarAutorForm()
            formare = GuardarAreaForm()
            message = "Uno de los campos fueron erróneos o no se a agregado en el registro del Proyecto."
            return render(request, 'proyecto/agregar_proyecto.html',
                          {'message':message, 'form': form, 'formset': formset, 'formar': formar, 'formac': formac,
                           'formi': formi, 'formti': formti, 'formre': formre, 'formt': formt, 'forma': forma, 'formare': formare,
                           'carreras': carreras, 'tipoproyectos': tipoproyectos, 'instituciones': instituciones,
                           'responsableinstitucionales': responsableinstitucionales, 'autores': autores, 'tutores': tutores,
                           'areaconocimientos': areaconocimientos,
                           'institucionsalva':institucionsalva,'tiporsalva':tiporsalva,'responsablesalva':responsablesalva,
                           'tutorsalva':tutorsalva,'autorsalva': autorsalva,'areasalva':areasalva})


    else:
        form = GuardarProyectoForm()
        formset = ImagenFormset(queryset=Imagenes.objects.none())
        formar = ArchivosFormset(queryset=Archivos.objects.none())
        formac = ActasFormset(queryset=Actas.objects.none())
        formi = GuardarInstitucionForm()
        formti = GuardarTipoForm()
        formre = GuardarResponsableForm()
        formt = GuardarTutorForm()
        forma = GuardarAutorForm()
        formare = GuardarAreaForm()
    return render(request, 'proyecto/agregar_proyecto.html',
                  {'message': message, 'form': form, 'formset': formset, 'formar': formar, 'formac': formac,
                   'formi': formi, 'formti': formti, 'formre': formre, 'formt': formt, 'forma': forma, 'formare': formare,
                   'carreras': carreras, 'tipoproyectos': tipoproyectos, 'instituciones': instituciones,
                   'responsableinstitucionales': responsableinstitucionales, 'autores': autores, 'tutores': tutores,
                   'areaconocimientos': areaconocimientos})


@login_required
@permission_required('gestionproyecto.editar_proyecto',reverse_lazy('Proyecto'))
def editar_proyecto(request, proyecto_id):
    global partes
    message = None
    message1 = None
    imagena = None
    arcvhioa = None
    actaa = None
    instituciones = Institucion.objects.all()
    tipoproyectos = TipoProyecto.objects.all()
    responsableinstitucionales = ResponsableInstitucional.objects.all()
    autores = Autor.objects.all()
    tutores = Tutor.objects.all()
    carreras = Carrera.objects.all()
    areaconocimientos = AreaConocimiento.objects.all()
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    ImagenFormset = modelformset_factory(Imagenes, fields=('nombre_imagenes',),extra=1)
    ArchivosFormset = modelformset_factory(Archivos,fields=('nombre_archivos',),extra=1)
    ActasFormset = modelformset_factory(Actas,fields=('nombre_actas',),extra=1)
    autorsalva = proyecto.Autor.all()
    tutorsalva = proyecto.Tutor.all()
    institucionsalva = proyecto.Institucion.all()
    tiporsalva = proyecto.TipoProyecto.all()
    areasalva = proyecto.AreaConocimiento.all()
    responsablesalva = proyecto.ResponsableInstitucional.all()
    if request.method == 'POST':
        form = GuardarProyectoForm(request.POST, request.FILES, instance=proyecto)
        formset = ImagenFormset(request.POST,request.FILES)
        formar = ArchivosFormset(request.POST,request.FILES)
        formac = ActasFormset(request.POST,request.FILES)
        #
        formi = GuardarInstitucionForm(request.POST, request.FILES)
        formti = GuardarTipoForm(request.POST, request.FILES)
        formre = GuardarResponsableForm(request.POST, request.FILES)
        formt = GuardarTutorForm(request.POST, request.FILES)
        forma = GuardarAutorForm(request.POST, request.FILES)
        formare = GuardarAreaForm(request.POST, request.FILES)
        #
        form2 = GuardarForm(request.POST)
        form3 = GuardarForm1(request.POST)
        form4 = GuardarForm2(request.POST)
        form5 = GuardarForm3(request.POST)
        form6 = GuardarForm4(request.POST)
        form7 = GuardarForm5(request.POST)
        form8 = GuardarForm6(request.POST)
        form9 = GuardarForm7(request.POST)
        form10 = GuardarForm8(request.POST)
        form11 = GuardarForm9(request.POST)

        if form2.is_valid():
            nombre = form2.cleaned_data.get('nombre')
            partes = nombre.split(';')
        elif form3.is_valid():
            nombre = form3.cleaned_data.get('nombre1')
            partes = nombre.split(';')
        elif form4.is_valid():
            nombre = form4.cleaned_data.get('nombre2')
            partes = nombre.split(';')
        elif form5.is_valid():
            nombre = form5.cleaned_data.get('nombre3')
            partes = nombre.split(';')
        elif form6.is_valid():
            nombre = form6.cleaned_data.get('nombre4')
            partes = nombre.split(';')
        elif form7.is_valid():
            nombre = form7.cleaned_data.get('nombre5')
            partes = nombre.split(';')
        elif form8.is_valid():
            nombre = form8.cleaned_data.get('nombre6')
            arcvhioa = nombre
            partes = nombre.split(';')
        elif form9.is_valid():
            nombre = form9.cleaned_data.get('nombre7')
            actaa = nombre
            partes = nombre.split(';')
        elif form10.is_valid():
            nombre = form10.cleaned_data.get('nombre8')
            partes = nombre.split(';')
            imagena = nombre
        elif form11.is_valid():
            nombre = form11.cleaned_data.get('nombre9')
            partes = nombre.split(';')
            actaa = None
            imagena = None
            arcvhioa = None
            formset = ImagenFormset()
            formar = ArchivosFormset()
            formac = ActasFormset()
        else:
            partes =[]

        if len(partes) == 0 and not form.is_valid():
            form = GuardarProyectoForm(request.POST)
            formset = ImagenFormset(queryset=Imagenes.objects.none())
            formar = ArchivosFormset(queryset=Archivos.objects.none())
            formac = ActasFormset(queryset=Actas.objects.none())
            formi = GuardarInstitucionForm()
            formti = GuardarTipoForm()
            formre = GuardarResponsableForm()
            formt = GuardarTutorForm()
            forma = GuardarAutorForm()
            formare = GuardarAreaForm()
            message = "Se debe elegir (al menos uno) en cada espacio de selección."
            return render(request, 'proyecto/editar_proyecto.html',
                          {'message': message, 'message1': message1, 'form': form, 'formset': formset, 'formar': formar,
                           'formac': formac,
                           'formi': formi, 'formti': formti, 'formre': formre, 'formt': formt, 'forma': forma,
                           'formare': formare,
                           'carreras': carreras, 'tipoproyectos': tipoproyectos, 'instituciones': instituciones,
                           'responsableinstitucionales': responsableinstitucionales, 'autores': autores,
                           'tutores': tutores, 'proyecto': proyecto,
                           'areaconocimientos': areaconocimientos
                           })

        elif formi.is_valid():
            formi.save()
            data = {'Titulo': partes[0],
                    'Proposito': partes[1],
                    'Estado_proyecto': partes[2],
                    'Poblacion_utiliza': partes[3],
                    'Numero_muestra_ninos': partes[4],
                    'Tiempo_inactividad': partes[5],
                    'Sugerencias': partes[6],
                    'Fecha_Donacion': partes[13],
                    }

            if len(partes[7]) == 0 or partes[7] == "null":
                institucionsalva = None
            else:
                if partes[7] != None:
                    elemetos = partes[7].split(',')
                    if len(elemetos) == 1:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1])
                    elif len(elemetos) == 3:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(
                            id=elemetos[3])
                    elif len(elemetos) == 5:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(
                            id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(
                            id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4]) | Institucion.objects.filter(
                            id=elemetos[5])

            if len(partes[8]) == 0 or partes[8] == "null":
                tiporsalva = None
            else:
                if partes[8] != None:
                    elemetos = partes[8].split(',')
                    if len(elemetos) == 1:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1])
                    elif len(elemetos) == 3:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(
                            id=elemetos[3])
                    elif len(elemetos) == 5:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(
                            id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(
                            id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4]) | TipoProyecto.objects.filter(
                            id=elemetos[5])

            if len(partes[9]) == 0 or partes[9] == "null":
                responsablesalva = None
            else:
                if partes[9] != None:
                    elemetos = partes[9].split(',')
                    if len(elemetos) == 1:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[3]) | ResponsableInstitucional.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[3]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[4]) | ResponsableInstitucional.objects.filter(id=elemetos[5])

            if len(partes[10]) == 0 or partes[10] == "null":
                tutorsalva = None
            else:
                if partes[10] != None:
                    elemetos = partes[10].split(',')
                    if len(elemetos) == 1:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                            id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                            id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                            id=elemetos[3])
                    elif len(elemetos) == 5:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                            id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                            id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                            id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                            id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4]) | Tutor.objects.filter(
                            id=elemetos[5])

            if len(partes[11]) == 0 or partes[11] == "null":
                autorsalva = None
            else:
                if partes[11] != None:
                    elemetos = partes[11].split(',')
                    if len(elemetos) == 1:
                        autorsalva = Autor.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                            id=elemetos[1]) | Autor.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                            id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                            id=elemetos[3])
                    elif len(elemetos) == 5:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                            id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                            id=elemetos[3]) | Autor.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                            id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                            id=elemetos[3]) | Autor.objects.filter(id=elemetos[4]) | Autor.objects.filter(
                            id=elemetos[5])

            if len(partes[12]) == 0 or partes[12] == "null":
                areasalva = None
            else:
                if partes[12] != None:
                    elemetos = partes[12].split(',')
                    if len(elemetos) == 1:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1])
                    elif len(elemetos) == 3:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1]) | AreaConocimiento.objects.filter(
                            id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1]) | AreaConocimiento.objects.filter(
                            id=elemetos[2]) | AreaConocimiento.objects.filter(
                            id=elemetos[3]) | AreaConocimiento.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1]) | AreaConocimiento.objects.filter(
                            id=elemetos[2]) | AreaConocimiento.objects.filter(
                            id=elemetos[3]) | AreaConocimiento.objects.filter(
                            id=elemetos[4]) | AreaConocimiento.objects.filter(id=elemetos[5])

            form = GuardarProyectoForm(data)
            formset = ImagenFormset(queryset = Imagenes.objects.filter(proyecto=proyecto))
            formar = ArchivosFormset(queryset = Archivos.objects.filter(proyecto=proyecto))
            formac = ActasFormset(queryset = Actas.objects.filter(proyecto=proyecto))
            formi = GuardarInstitucionForm()
            formti = GuardarTipoForm()
            formre = GuardarResponsableForm()
            formt = GuardarTutorForm()
            forma = GuardarAutorForm()
            formare = GuardarAreaForm()
            message1 = "La Institución a sido registrada con éxito."
            return render(request, 'proyecto/editar_proyecto.html',
                          {'message': message, 'message1': message1, 'form': form, 'formset': formset, 'formar': formar, 'formac': formac,
                           'formi': formi, 'formti': formti, 'formre': formre, 'formt': formt, 'forma': forma,
                           'formare': formare,
                           'carreras': carreras, 'tipoproyectos': tipoproyectos, 'instituciones': instituciones,
                           'responsableinstitucionales': responsableinstitucionales, 'autores': autores,
                           'tutores': tutores, 'proyecto':proyecto,
                           'areaconocimientos': areaconocimientos,
                           'tipoproyecto': tiporsalva, 'institucion': institucionsalva,
                           'responsableinstitucional': responsablesalva, 'autor': autorsalva, 'tutor': tutorsalva,
                           'areaconocimiento': areasalva
                           })
        elif formti.is_valid():
            formti.save()
            data = {'Titulo': partes[0],
                    'Proposito': partes[1],
                    'Estado_proyecto': partes[2],
                    'Poblacion_utiliza': partes[3],
                    'Numero_muestra_ninos': partes[4],
                    'Tiempo_inactividad': partes[5],
                    'Sugerencias': partes[6],
                    'Fecha_Donacion': partes[13],
                    }

            if len(partes[7]) == 0 or partes[7] == "null":
                institucionsalva = None
            else:
                if partes[7] != None:
                    elemetos = partes[7].split(',')
                    if len(elemetos) == 1:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1])
                    elif len(elemetos) == 3:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(
                            id=elemetos[3])
                    elif len(elemetos) == 5:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(
                            id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(
                            id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4]) | Institucion.objects.filter(
                            id=elemetos[5])

            if len(partes[8]) == 0 or partes[8] == "null":
                tiporsalva = None
            else:
                if partes[8] != None:
                    elemetos = partes[8].split(',')
                    if len(elemetos) == 1:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1])
                    elif len(elemetos) == 3:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(
                            id=elemetos[3])
                    elif len(elemetos) == 5:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(
                            id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(
                            id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4]) | TipoProyecto.objects.filter(
                            id=elemetos[5])

            if len(partes[9]) == 0 or partes[9] == "null":
                responsablesalva = None
            else:
                if partes[9] != None:
                    elemetos = partes[9].split(',')
                    if len(elemetos) == 1:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[3]) | ResponsableInstitucional.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[3]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[4]) | ResponsableInstitucional.objects.filter(id=elemetos[5])

            if len(partes[10]) == 0 or partes[10] == "null":
                tutorsalva = None
            else:
                if partes[10] != None:
                    elemetos = partes[10].split(',')
                    if len(elemetos) == 1:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                            id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                            id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                            id=elemetos[3])
                    elif len(elemetos) == 5:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                            id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                            id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                            id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                            id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4]) | Tutor.objects.filter(
                            id=elemetos[5])

            if len(partes[11]) == 0 or partes[11] == "null":
                autorsalva = None
            else:
                if partes[11] != None:
                    elemetos = partes[11].split(',')
                    if len(elemetos) == 1:
                        autorsalva = Autor.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                            id=elemetos[1]) | Autor.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                            id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                            id=elemetos[3])
                    elif len(elemetos) == 5:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                            id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                            id=elemetos[3]) | Autor.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                            id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                            id=elemetos[3]) | Autor.objects.filter(id=elemetos[4]) | Autor.objects.filter(
                            id=elemetos[5])

            if len(partes[12]) == 0 or partes[12] == "null":
                areasalva = None
            else:
                if partes[12] != None:
                    elemetos = partes[12].split(',')
                    if len(elemetos) == 1:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1])
                    elif len(elemetos) == 3:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1]) | AreaConocimiento.objects.filter(
                            id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1]) | AreaConocimiento.objects.filter(
                            id=elemetos[2]) | AreaConocimiento.objects.filter(
                            id=elemetos[3]) | AreaConocimiento.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1]) | AreaConocimiento.objects.filter(
                            id=elemetos[2]) | AreaConocimiento.objects.filter(
                            id=elemetos[3]) | AreaConocimiento.objects.filter(
                            id=elemetos[4]) | AreaConocimiento.objects.filter(id=elemetos[5])

            form = GuardarProyectoForm(data)
            formset = ImagenFormset(queryset = Imagenes.objects.filter(proyecto=proyecto))
            formar = ArchivosFormset(queryset = Archivos.objects.filter(proyecto=proyecto))
            formac = ActasFormset(queryset = Actas.objects.filter(proyecto=proyecto))
            formi = GuardarInstitucionForm()
            formti = GuardarTipoForm()
            formre = GuardarResponsableForm()
            formt = GuardarTutorForm()
            forma = GuardarAutorForm()
            formare = GuardarAreaForm()
            message1 = "El Tipo de Proyecto a sido registrada con éxito."
            return render(request, 'proyecto/editar_proyecto.html',
                          {'message': message, 'message1': message1, 'form': form, 'formset': formset, 'formar': formar, 'formac': formac,
                           'formi': formi, 'formti': formti, 'formre': formre, 'formt': formt, 'forma': forma,
                           'formare': formare,
                           'carreras': carreras, 'tipoproyectos': tipoproyectos, 'instituciones': instituciones,
                           'responsableinstitucionales': responsableinstitucionales, 'autores': autores,
                           'tutores': tutores, 'proyecto':proyecto,
                           'areaconocimientos': areaconocimientos,
                           'tipoproyecto': tiporsalva, 'institucion': institucionsalva,
                           'responsableinstitucional': responsablesalva, 'autor': autorsalva, 'tutor': tutorsalva,
                           'areaconocimiento': areasalva
                           })
        elif formre.is_valid():
            formre.save()
            data = {'Titulo': partes[0],
                    'Proposito': partes[1],
                    'Estado_proyecto': partes[2],
                    'Poblacion_utiliza': partes[3],
                    'Numero_muestra_ninos': partes[4],
                    'Tiempo_inactividad': partes[5],
                    'Sugerencias': partes[6],
                    'Fecha_Donacion': partes[13],
                    }

            if len(partes[7]) == 0 or partes[8] == "null":
                institucionsalva = None
            else:
                if partes[7] != None:
                    elemetos = partes[7].split(',')
                    if len(elemetos) == 1:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1])
                    elif len(elemetos) == 3:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(
                            id=elemetos[3])
                    elif len(elemetos) == 5:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(
                            id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(
                            id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4]) | Institucion.objects.filter(
                            id=elemetos[5])

            if len(partes[8]) == 0 or partes[8] == "null":
                tiporsalva = None
            else:
                if partes[8] != None:
                    elemetos = partes[8].split(',')
                    if len(elemetos) == 1:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1])
                    elif len(elemetos) == 3:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(
                            id=elemetos[3])
                    elif len(elemetos) == 5:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(
                            id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(
                            id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4]) | TipoProyecto.objects.filter(
                            id=elemetos[5])

            if len(partes[9]) == 0 or partes[9] == "null":
                responsablesalva = None
            else:
                if partes[9] != None:
                    elemetos = partes[9].split(',')
                    if len(elemetos) == 1:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[3]) | ResponsableInstitucional.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[3]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[4]) | ResponsableInstitucional.objects.filter(id=elemetos[5])

            if len(partes[10]) == 0 or partes[10] == "null":
                tutorsalva = None
            else:
                if partes[10] != None:
                    elemetos = partes[10].split(',')
                    if len(elemetos) == 1:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                            id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                            id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                            id=elemetos[3])
                    elif len(elemetos) == 5:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                            id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                            id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                            id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                            id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4]) | Tutor.objects.filter(
                            id=elemetos[5])

            if len(partes[11]) == 0 or partes[11] == "null":
                autorsalva = None
            else:
                if partes[11] != None:
                    elemetos = partes[11].split(',')
                    if len(elemetos) == 1:
                        autorsalva = Autor.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                            id=elemetos[1]) | Autor.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                            id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                            id=elemetos[3])
                    elif len(elemetos) == 5:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                            id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                            id=elemetos[3]) | Autor.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                            id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                            id=elemetos[3]) | Autor.objects.filter(id=elemetos[4]) | Autor.objects.filter(
                            id=elemetos[5])

            if len(partes[12]) == 0 or partes[12] == "null":
                areasalva = None
            else:
                if partes[12] != None:
                    elemetos = partes[12].split(',')
                    if len(elemetos) == 1:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1])
                    elif len(elemetos) == 3:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1]) | AreaConocimiento.objects.filter(
                            id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1]) | AreaConocimiento.objects.filter(
                            id=elemetos[2]) | AreaConocimiento.objects.filter(
                            id=elemetos[3]) | AreaConocimiento.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1]) | AreaConocimiento.objects.filter(
                            id=elemetos[2]) | AreaConocimiento.objects.filter(
                            id=elemetos[3]) | AreaConocimiento.objects.filter(
                            id=elemetos[4]) | AreaConocimiento.objects.filter(id=elemetos[5])

            form = GuardarProyectoForm(data)
            formset = ImagenFormset(queryset = Imagenes.objects.filter(proyecto=proyecto))
            formar = ArchivosFormset(queryset = Archivos.objects.filter(proyecto=proyecto))
            formac = ActasFormset(queryset = Actas.objects.filter(proyecto=proyecto))
            formi = GuardarInstitucionForm()
            formti = GuardarTipoForm()
            formre = GuardarResponsableForm()
            formt = GuardarTutorForm()
            forma = GuardarAutorForm()
            formare = GuardarAreaForm()
            message1 = "El Responsable Institucional a sido registrada con éxito."
            return render(request, 'proyecto/editar_proyecto.html',
                          {'message': message, 'message1': message1, 'form': form, 'formset': formset, 'formar': formar, 'formac': formac,
                           'formi': formi, 'formti': formti, 'formre': formre, 'formt': formt, 'forma': forma,
                           'formare': formare,
                           'carreras': carreras, 'tipoproyectos': tipoproyectos, 'instituciones': instituciones,
                           'responsableinstitucionales': responsableinstitucionales, 'autores': autores,
                           'tutores': tutores, 'proyecto':proyecto,
                           'areaconocimientos': areaconocimientos,
                           'tipoproyecto': tiporsalva, 'institucion': institucionsalva,
                           'responsableinstitucional': responsablesalva, 'autor': autorsalva, 'tutor': tutorsalva,
                           'areaconocimiento': areasalva
                           })
        elif formt.is_valid():
            cedula = formt.cleaned_data.get('cedula_tutor')
            if len(cedula) == 10:
                if verificar(cedula) is not False:
                    formt.save()
                    data = {'Titulo': partes[0],
                            'Proposito': partes[1],
                            'Estado_proyecto': partes[2],
                            'Poblacion_utiliza': partes[3],
                            'Numero_muestra_ninos': partes[4],
                            'Tiempo_inactividad': partes[5],
                            'Sugerencias': partes[6],
                            'Fecha_Donacion': partes[13],
                            }

                    if len(partes[7]) == 0 or partes[7] == "null":
                        institucionsalva = None
                    else:
                        if partes[7] != None:
                            elemetos = partes[7].split(',')
                            if len(elemetos) == 1:
                                institucionsalva = Institucion.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1])
                            elif len(elemetos) == 3:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1]) | Institucion.objects.filter(
                                    id=elemetos[2]) | Institucion.objects.filter(
                                    id=elemetos[3])
                            elif len(elemetos) == 5:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1]) | Institucion.objects.filter(
                                    id=elemetos[2]) | Institucion.objects.filter(
                                    id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1]) | Institucion.objects.filter(
                                    id=elemetos[2]) | Institucion.objects.filter(
                                    id=elemetos[3]) | Institucion.objects.filter(
                                    id=elemetos[4]) | Institucion.objects.filter(
                                    id=elemetos[5])

                    if len(partes[8]) == 0 or partes[8] == "null":
                        tiporsalva = None
                    else:
                        if partes[8] != None:
                            elemetos = partes[8].split(',')
                            if len(elemetos) == 1:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1])
                            elif len(elemetos) == 3:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1]) | TipoProyecto.objects.filter(
                                    id=elemetos[2]) | TipoProyecto.objects.filter(
                                    id=elemetos[3])
                            elif len(elemetos) == 5:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1]) | TipoProyecto.objects.filter(
                                    id=elemetos[2]) | TipoProyecto.objects.filter(
                                    id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1]) | TipoProyecto.objects.filter(
                                    id=elemetos[2]) | TipoProyecto.objects.filter(
                                    id=elemetos[3]) | TipoProyecto.objects.filter(
                                    id=elemetos[4]) | TipoProyecto.objects.filter(
                                    id=elemetos[5])

                    if len(partes[9]) == 0 or partes[9] == "null":
                        responsablesalva = None
                    else:
                        if partes[9] != None:
                            elemetos = partes[9].split(',')
                            if len(elemetos) == 1:
                                responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1])
                            elif len(elemetos) == 3:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3])
                            elif len(elemetos) == 5:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[3]) | ResponsableInstitucional.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[3]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[4]) | ResponsableInstitucional.objects.filter(id=elemetos[5])

                    if len(partes[10]) == 0 or partes[10] == "null":
                        tutorsalva = None
                    else:
                        if partes[10] != None:
                            elemetos = partes[10].split(',')
                            if len(elemetos) == 1:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1])
                            elif len(elemetos) == 3:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                    id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                    id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                    id=elemetos[3])
                            elif len(elemetos) == 5:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                    id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                    id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                    id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                    id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4]) | Tutor.objects.filter(
                                    id=elemetos[5])

                    if len(partes[11]) == 0 or partes[11] == "null":
                        autorsalva = None
                    else:
                        if partes[11] != None:
                            elemetos = partes[11].split(',')
                            if len(elemetos) == 1:
                                autorsalva = Autor.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1])
                            elif len(elemetos) == 3:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                    id=elemetos[1]) | Autor.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                    id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                    id=elemetos[3])
                            elif len(elemetos) == 5:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                    id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                    id=elemetos[3]) | Autor.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                    id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                    id=elemetos[3]) | Autor.objects.filter(id=elemetos[4]) | Autor.objects.filter(
                                    id=elemetos[5])

                    if len(partes[12]) == 0 or partes[12] == "null":
                        areasalva = None
                    else:
                        if partes[12] != None:
                            elemetos = partes[12].split(',')
                            if len(elemetos) == 1:
                                areasalva = AreaConocimiento.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1])
                            elif len(elemetos) == 3:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1]) | AreaConocimiento.objects.filter(
                                    id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3])
                            elif len(elemetos) == 5:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1]) | AreaConocimiento.objects.filter(
                                    id=elemetos[2]) | AreaConocimiento.objects.filter(
                                    id=elemetos[3]) | AreaConocimiento.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1]) | AreaConocimiento.objects.filter(
                                    id=elemetos[2]) | AreaConocimiento.objects.filter(
                                    id=elemetos[3]) | AreaConocimiento.objects.filter(
                                    id=elemetos[4]) | AreaConocimiento.objects.filter(id=elemetos[5])

                    form = GuardarProyectoForm(data)
                    formset = ImagenFormset(queryset = Imagenes.objects.filter(proyecto=proyecto))
                    formar = ArchivosFormset(queryset = Archivos.objects.filter(proyecto=proyecto))
                    formac = ActasFormset(queryset = Actas.objects.filter(proyecto=proyecto))
                    formi = GuardarInstitucionForm()
                    formti = GuardarTipoForm()
                    formre = GuardarResponsableForm()
                    formt = GuardarTutorForm()
                    forma = GuardarAutorForm()
                    formare = GuardarAreaForm()
                    message1 = "El Tutor a sido registrada con éxito."
                    return render(request, 'proyecto/editar_proyecto.html',
                                  {'message': message, 'message1': message1, 'form': form, 'formset': formset, 'formar': formar,
                                   'formac': formac,
                                   'formi': formi, 'formti': formti, 'formre': formre, 'formt': formt, 'forma': forma,
                                   'formare': formare,
                                   'carreras': carreras, 'tipoproyectos': tipoproyectos, 'instituciones': instituciones,
                                   'responsableinstitucionales': responsableinstitucionales, 'autores': autores,
                                   'tutores': tutores, 'proyecto':proyecto,
                                   'areaconocimientos': areaconocimientos,
                                   'tipoproyecto': tiporsalva, 'institucion': institucionsalva,
                                   'responsableinstitucional': responsablesalva, 'autor': autorsalva, 'tutor': tutorsalva,
                                   'areaconocimiento': areasalva
                                   })
                else:
                    message = "El número de cédula del Tutor es invalido, verifique el número."
                    data = {'Titulo': partes[0],
                            'Proposito': partes[1],
                            'Estado_proyecto': partes[2],
                            'Poblacion_utiliza': partes[3],
                            'Numero_muestra_ninos': partes[4],
                            'Tiempo_inactividad': partes[5],
                            'Sugerencias': partes[6],
                            'Fecha_Donacion': partes[13],
                            }

                    if len(partes[7]) == 0 or partes[7] == "null":
                        institucionsalva = None
                    else:
                        if partes[7] != None:
                            elemetos = partes[7].split(',')
                            if len(elemetos) == 1:
                                institucionsalva = Institucion.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1])
                            elif len(elemetos) == 3:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1]) | Institucion.objects.filter(
                                    id=elemetos[2]) | Institucion.objects.filter(
                                    id=elemetos[3])
                            elif len(elemetos) == 5:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1]) | Institucion.objects.filter(
                                    id=elemetos[2]) | Institucion.objects.filter(
                                    id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1]) | Institucion.objects.filter(
                                    id=elemetos[2]) | Institucion.objects.filter(
                                    id=elemetos[3]) | Institucion.objects.filter(
                                    id=elemetos[4]) | Institucion.objects.filter(
                                    id=elemetos[5])

                    if len(partes[8]) == 0 or partes[8] == "null":
                        tiporsalva = None
                    else:
                        if partes[8] != None:
                            elemetos = partes[8].split(',')
                            if len(elemetos) == 1:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1])
                            elif len(elemetos) == 3:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1]) | TipoProyecto.objects.filter(
                                    id=elemetos[2]) | TipoProyecto.objects.filter(
                                    id=elemetos[3])
                            elif len(elemetos) == 5:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1]) | TipoProyecto.objects.filter(
                                    id=elemetos[2]) | TipoProyecto.objects.filter(
                                    id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1]) | TipoProyecto.objects.filter(
                                    id=elemetos[2]) | TipoProyecto.objects.filter(
                                    id=elemetos[3]) | TipoProyecto.objects.filter(
                                    id=elemetos[4]) | TipoProyecto.objects.filter(
                                    id=elemetos[5])

                    if len(partes[9]) == 0 or partes[9] == "null":
                        responsablesalva = None
                    else:
                        if partes[9] != None:
                            elemetos = partes[9].split(',')
                            if len(elemetos) == 1:
                                responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1])
                            elif len(elemetos) == 3:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3])
                            elif len(elemetos) == 5:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[3]) | ResponsableInstitucional.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[3]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[4]) | ResponsableInstitucional.objects.filter(id=elemetos[5])

                    if len(partes[10]) == 0 or partes[10] == "null":
                        tutorsalva = None
                    else:
                        if partes[10] != None:
                            elemetos = partes[10].split(',')
                            if len(elemetos) == 1:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1])
                            elif len(elemetos) == 3:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                    id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                    id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                    id=elemetos[3])
                            elif len(elemetos) == 5:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                    id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                    id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                    id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                    id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4]) | Tutor.objects.filter(
                                    id=elemetos[5])

                    if len(partes[11]) == 0 or partes[11] == "null":
                        autorsalva = None
                    else:
                        if partes[11] != None:
                            elemetos = partes[11].split(',')
                            if len(elemetos) == 1:
                                autorsalva = Autor.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1])
                            elif len(elemetos) == 3:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                    id=elemetos[1]) | Autor.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                    id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                    id=elemetos[3])
                            elif len(elemetos) == 5:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                    id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                    id=elemetos[3]) | Autor.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                    id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                    id=elemetos[3]) | Autor.objects.filter(id=elemetos[4]) | Autor.objects.filter(
                                    id=elemetos[5])

                    if len(partes[12]) == 0 or partes[12] == "null":
                        areasalva = None
                    else:
                        if partes[12] != None:
                            elemetos = partes[12].split(',')
                            if len(elemetos) == 1:
                                areasalva = AreaConocimiento.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1])
                            elif len(elemetos) == 3:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1]) | AreaConocimiento.objects.filter(
                                    id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3])
                            elif len(elemetos) == 5:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1]) | AreaConocimiento.objects.filter(
                                    id=elemetos[2]) | AreaConocimiento.objects.filter(
                                    id=elemetos[3]) | AreaConocimiento.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1]) | AreaConocimiento.objects.filter(
                                    id=elemetos[2]) | AreaConocimiento.objects.filter(
                                    id=elemetos[3]) | AreaConocimiento.objects.filter(
                                    id=elemetos[4]) | AreaConocimiento.objects.filter(id=elemetos[5])

                    form = GuardarProyectoForm(data)
                    formset = ImagenFormset(queryset = Imagenes.objects.filter(proyecto=proyecto))
                    formar = ArchivosFormset(queryset = Archivos.objects.filter(proyecto=proyecto))
                    formac = ActasFormset(queryset = Actas.objects.filter(proyecto=proyecto))
                    formi = GuardarInstitucionForm()
                    formti = GuardarTipoForm()
                    formre = GuardarResponsableForm()
                    formt = GuardarTutorForm(request.POST, request.FILES)
                    forma = GuardarAutorForm()
                    formare = GuardarAreaForm()
                    return render(request, 'proyecto/editar_proyecto.html',
                                  {'message': message, 'form': form, 'formset': formset, 'formar': formar,
                                   'formac': formac,
                                   'formi': formi, 'formti': formti, 'formre': formre, 'formt': formt, 'forma': forma,
                                   'formare': formare,
                                   'carreras': carreras, 'tipoproyectos': tipoproyectos, 'instituciones': instituciones,
                                   'responsableinstitucionales': responsableinstitucionales, 'autores': autores,
                                   'tutores': tutores, 'proyecto':proyecto,
                                   'areaconocimientos': areaconocimientos,
                                   'tipoproyecto': tiporsalva, 'institucion': institucionsalva,
                                   'responsableinstitucional': responsablesalva, 'autor': autorsalva, 'tutor': tutorsalva,
                                   'areaconocimiento': areasalva
                                   })
            else:
                message = "Ingrese los 10 dígitos de la cédula para registrar el Tutor."
                data = {'Titulo': partes[0],
                        'Proposito': partes[1],
                        'Estado_proyecto': partes[2],
                        'Poblacion_utiliza': partes[3],
                        'Numero_muestra_ninos': partes[4],
                        'Tiempo_inactividad': partes[5],
                        'Sugerencias': partes[6],
                        'Fecha_Donacion': partes[13],
                        }

                if len(partes[7]) == 0 or partes[7] == "null":
                    institucionsalva = None
                else:
                    if partes[7] != None:
                        elemetos = partes[7].split(',')
                        if len(elemetos) == 1:
                            institucionsalva = Institucion.objects.filter(id=elemetos[0])
                        elif len(elemetos) == 2:
                            institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                                id=elemetos[1])
                        elif len(elemetos) == 3:
                            institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                                id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2])
                        elif len(elemetos) == 4:
                            institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                                id=elemetos[1]) | Institucion.objects.filter(
                                id=elemetos[2]) | Institucion.objects.filter(
                                id=elemetos[3])
                        elif len(elemetos) == 5:
                            institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                                id=elemetos[1]) | Institucion.objects.filter(
                                id=elemetos[2]) | Institucion.objects.filter(
                                id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4])
                        elif len(elemetos) == 6:
                            institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                                id=elemetos[1]) | Institucion.objects.filter(
                                id=elemetos[2]) | Institucion.objects.filter(
                                id=elemetos[3]) | Institucion.objects.filter(
                                id=elemetos[4]) | Institucion.objects.filter(
                                id=elemetos[5])

                if len(partes[8]) == 0 or partes[8] == "null":
                    tiporsalva = None
                else:
                    if partes[8] != None:
                        elemetos = partes[8].split(',')
                        if len(elemetos) == 1:
                            tiporsalva = TipoProyecto.objects.filter(id=elemetos[0])
                        elif len(elemetos) == 2:
                            tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                id=elemetos[1])
                        elif len(elemetos) == 3:
                            tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2])
                        elif len(elemetos) == 4:
                            tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                id=elemetos[1]) | TipoProyecto.objects.filter(
                                id=elemetos[2]) | TipoProyecto.objects.filter(
                                id=elemetos[3])
                        elif len(elemetos) == 5:
                            tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                id=elemetos[1]) | TipoProyecto.objects.filter(
                                id=elemetos[2]) | TipoProyecto.objects.filter(
                                id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4])
                        elif len(elemetos) == 6:
                            tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                id=elemetos[1]) | TipoProyecto.objects.filter(
                                id=elemetos[2]) | TipoProyecto.objects.filter(
                                id=elemetos[3]) | TipoProyecto.objects.filter(
                                id=elemetos[4]) | TipoProyecto.objects.filter(
                                id=elemetos[5])

                if len(partes[9]) == 0 or partes[9] == "null":
                    responsablesalva = None
                else:
                    if partes[9] != None:
                        elemetos = partes[9].split(',')
                        if len(elemetos) == 1:
                            responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0])
                        elif len(elemetos) == 2:
                            responsablesalva = ResponsableInstitucional.objects.filter(
                                id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1])
                        elif len(elemetos) == 3:
                            responsablesalva = ResponsableInstitucional.objects.filter(
                                id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2])
                        elif len(elemetos) == 4:
                            responsablesalva = ResponsableInstitucional.objects.filter(
                                id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3])
                        elif len(elemetos) == 5:
                            responsablesalva = ResponsableInstitucional.objects.filter(
                                id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[3]) | ResponsableInstitucional.objects.filter(id=elemetos[4])
                        elif len(elemetos) == 6:
                            responsablesalva = ResponsableInstitucional.objects.filter(
                                id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[3]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[4]) | ResponsableInstitucional.objects.filter(id=elemetos[5])

                if len(partes[10]) == 0 or partes[10] == "null":
                    tutorsalva = None
                else:
                    if partes[10] != None:
                        elemetos = partes[10].split(',')
                        if len(elemetos) == 1:
                            tutorsalva = Tutor.objects.filter(id=elemetos[0])
                        elif len(elemetos) == 2:
                            tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1])
                        elif len(elemetos) == 3:
                            tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2])
                        elif len(elemetos) == 4:
                            tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                id=elemetos[3])
                        elif len(elemetos) == 5:
                            tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4])
                        elif len(elemetos) == 6:
                            tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4]) | Tutor.objects.filter(
                                id=elemetos[5])

                if len(partes[11]) == 0 or partes[11] == "null":
                    autorsalva = None
                else:
                    if partes[11] != None:
                        elemetos = partes[11].split(',')
                        if len(elemetos) == 1:
                            autorsalva = Autor.objects.filter(id=elemetos[0])
                        elif len(elemetos) == 2:
                            autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1])
                        elif len(elemetos) == 3:
                            autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                id=elemetos[1]) | Autor.objects.filter(id=elemetos[2])
                        elif len(elemetos) == 4:
                            autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                id=elemetos[3])
                        elif len(elemetos) == 5:
                            autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                id=elemetos[3]) | Autor.objects.filter(id=elemetos[4])
                        elif len(elemetos) == 6:
                            autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                id=elemetos[3]) | Autor.objects.filter(id=elemetos[4]) | Autor.objects.filter(
                                id=elemetos[5])

                if len(partes[12]) == 0 or partes[12] == "null":
                    areasalva = None
                else:
                    if partes[12] != None:
                        elemetos = partes[12].split(',')
                        if len(elemetos) == 1:
                            areasalva = AreaConocimiento.objects.filter(id=elemetos[0])
                        elif len(elemetos) == 2:
                            areasalva = AreaConocimiento.objects.filter(
                                id=elemetos[0]) | AreaConocimiento.objects.filter(
                                id=elemetos[1])
                        elif len(elemetos) == 3:
                            areasalva = AreaConocimiento.objects.filter(
                                id=elemetos[0]) | AreaConocimiento.objects.filter(
                                id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2])
                        elif len(elemetos) == 4:
                            areasalva = AreaConocimiento.objects.filter(
                                id=elemetos[0]) | AreaConocimiento.objects.filter(
                                id=elemetos[1]) | AreaConocimiento.objects.filter(
                                id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3])
                        elif len(elemetos) == 5:
                            areasalva = AreaConocimiento.objects.filter(
                                id=elemetos[0]) | AreaConocimiento.objects.filter(
                                id=elemetos[1]) | AreaConocimiento.objects.filter(
                                id=elemetos[2]) | AreaConocimiento.objects.filter(
                                id=elemetos[3]) | AreaConocimiento.objects.filter(id=elemetos[4])
                        elif len(elemetos) == 6:
                            areasalva = AreaConocimiento.objects.filter(
                                id=elemetos[0]) | AreaConocimiento.objects.filter(
                                id=elemetos[1]) | AreaConocimiento.objects.filter(
                                id=elemetos[2]) | AreaConocimiento.objects.filter(
                                id=elemetos[3]) | AreaConocimiento.objects.filter(
                                id=elemetos[4]) | AreaConocimiento.objects.filter(id=elemetos[5])

                form = GuardarProyectoForm(data)
                formset = ImagenFormset(queryset = Imagenes.objects.filter(proyecto=proyecto))
                formar = ArchivosFormset(queryset = Archivos.objects.filter(proyecto=proyecto))
                formac = ActasFormset(queryset = Actas.objects.filter(proyecto=proyecto))
                formi = GuardarInstitucionForm()
                formti = GuardarTipoForm()
                formre = GuardarResponsableForm()
                formt = GuardarTutorForm(request.POST, request.FILES)
                forma = GuardarAutorForm()
                formare = GuardarAreaForm()
                return render(request, 'proyecto/editar_proyecto.html',
                              {'message': message, 'form': form, 'formset': formset, 'formar': formar, 'formac': formac,
                               'formi': formi, 'formti': formti, 'formre': formre, 'formt': formt, 'forma': forma,
                               'formare': formare,
                               'carreras': carreras, 'tipoproyectos': tipoproyectos, 'instituciones': instituciones,
                               'responsableinstitucionales': responsableinstitucionales, 'autores': autores,
                               'tutores': tutores, 'proyecto':proyecto,
                               'areaconocimientos': areaconocimientos,
                               'tipoproyecto': tiporsalva, 'institucion': institucionsalva,
                               'responsableinstitucional': responsablesalva, 'autor': autorsalva, 'tutor': tutorsalva,
                               'areaconocimiento': areasalva
                               })


        elif forma.is_valid():
            cedula = forma.cleaned_data.get('cedula_autor')
            if len(cedula) == 10:
                if verificar(cedula) is not False:
                    forma.save()
                    data = {'Titulo': partes[0],
                            'Proposito': partes[1],
                            'Estado_proyecto': partes[2],
                            'Poblacion_utiliza': partes[3],
                            'Numero_muestra_ninos': partes[4],
                            'Tiempo_inactividad': partes[5],
                            'Sugerencias': partes[6],
                            'Fecha_Donacion': partes[13],
                            }

                    if len(partes[7]) == 0 or partes[7] == "null":
                        institucionsalva = None
                    else:
                        if partes[7] != None:
                            elemetos = partes[7].split(',')
                            if len(elemetos) == 1:
                                institucionsalva = Institucion.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1])
                            elif len(elemetos) == 3:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1]) | Institucion.objects.filter(
                                    id=elemetos[2]) | Institucion.objects.filter(
                                    id=elemetos[3])
                            elif len(elemetos) == 5:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1]) | Institucion.objects.filter(
                                    id=elemetos[2]) | Institucion.objects.filter(
                                    id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1]) | Institucion.objects.filter(
                                    id=elemetos[2]) | Institucion.objects.filter(
                                    id=elemetos[3]) | Institucion.objects.filter(
                                    id=elemetos[4]) | Institucion.objects.filter(
                                    id=elemetos[5])

                    if len(partes[8]) == 0 or partes[8] == "null":
                        tiporsalva = None
                    else:
                        if partes[8] != None:
                            elemetos = partes[8].split(',')
                            if len(elemetos) == 1:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1])
                            elif len(elemetos) == 3:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1]) | TipoProyecto.objects.filter(
                                    id=elemetos[2]) | TipoProyecto.objects.filter(
                                    id=elemetos[3])
                            elif len(elemetos) == 5:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1]) | TipoProyecto.objects.filter(
                                    id=elemetos[2]) | TipoProyecto.objects.filter(
                                    id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1]) | TipoProyecto.objects.filter(
                                    id=elemetos[2]) | TipoProyecto.objects.filter(
                                    id=elemetos[3]) | TipoProyecto.objects.filter(
                                    id=elemetos[4]) | TipoProyecto.objects.filter(
                                    id=elemetos[5])

                    if len(partes[9]) == 0 or partes[9] == "null":
                        responsablesalva = None
                    else:
                        if partes[9] != None:
                            elemetos = partes[9].split(',')
                            if len(elemetos) == 1:
                                responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1])
                            elif len(elemetos) == 3:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3])
                            elif len(elemetos) == 5:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[3]) | ResponsableInstitucional.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[3]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[4]) | ResponsableInstitucional.objects.filter(id=elemetos[5])

                    if len(partes[10]) == 0 or partes[10] == "null":
                        tutorsalva = None
                    else:
                        if partes[10] != None:
                            elemetos = partes[10].split(',')
                            if len(elemetos) == 1:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1])
                            elif len(elemetos) == 3:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                    id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                    id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                    id=elemetos[3])
                            elif len(elemetos) == 5:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                    id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                    id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                    id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                    id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4]) | Tutor.objects.filter(
                                    id=elemetos[5])

                    if len(partes[11]) == 0 or partes[11] == "null":
                        autorsalva = None
                    else:
                        if partes[11] != None:
                            elemetos = partes[11].split(',')
                            if len(elemetos) == 1:
                                autorsalva = Autor.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1])
                            elif len(elemetos) == 3:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                    id=elemetos[1]) | Autor.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                    id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                    id=elemetos[3])
                            elif len(elemetos) == 5:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                    id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                    id=elemetos[3]) | Autor.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                    id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                    id=elemetos[3]) | Autor.objects.filter(id=elemetos[4]) | Autor.objects.filter(
                                    id=elemetos[5])

                    if len(partes[12]) == 0 or partes[12] == "null":
                        areasalva = None
                    else:
                        if partes[12] != None:
                            elemetos = partes[12].split(',')
                            if len(elemetos) == 1:
                                areasalva = AreaConocimiento.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1])
                            elif len(elemetos) == 3:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1]) | AreaConocimiento.objects.filter(
                                    id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3])
                            elif len(elemetos) == 5:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1]) | AreaConocimiento.objects.filter(
                                    id=elemetos[2]) | AreaConocimiento.objects.filter(
                                    id=elemetos[3]) | AreaConocimiento.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1]) | AreaConocimiento.objects.filter(
                                    id=elemetos[2]) | AreaConocimiento.objects.filter(
                                    id=elemetos[3]) | AreaConocimiento.objects.filter(
                                    id=elemetos[4]) | AreaConocimiento.objects.filter(id=elemetos[5])

                    form = GuardarProyectoForm(data)
                    formset = ImagenFormset(queryset=Imagenes.objects.filter(proyecto=proyecto))
                    formar = ArchivosFormset(queryset=Archivos.objects.filter(proyecto=proyecto))
                    formac = ActasFormset(queryset=Actas.objects.filter(proyecto=proyecto))
                    formi = GuardarInstitucionForm()
                    formti = GuardarTipoForm()
                    formre = GuardarResponsableForm()
                    formt = GuardarTutorForm()
                    forma = GuardarAutorForm()
                    formare = GuardarAreaForm()
                    message1 = "El Autor a sido registrado con éxito."
                    return render(request, 'proyecto/editar_proyecto.html',
                                  {'message': message, 'message1': message1, 'form': form, 'formset': formset, 'formar': formar,
                                   'formac': formac,
                                   'formi': formi, 'formti': formti, 'formre': formre, 'formt': formt, 'forma': forma,
                                   'formare': formare,
                                   'carreras': carreras, 'tipoproyectos': tipoproyectos, 'instituciones': instituciones,
                                   'responsableinstitucionales': responsableinstitucionales, 'autores': autores,
                                   'tutores': tutores, 'proyecto':proyecto,
                                   'areaconocimientos': areaconocimientos,
                                   'tipoproyecto': tiporsalva, 'institucion': institucionsalva,
                                   'responsableinstitucional': responsablesalva, 'autor': autorsalva, 'tutor': tutorsalva,
                                   'areaconocimiento': areasalva
                                   })
                else:
                    message = "El número de cédula del Autor es invalido, verifique el número."
                    data = {'Titulo': partes[0],
                            'Proposito': partes[1],
                            'Estado_proyecto': partes[2],
                            'Poblacion_utiliza': partes[3],
                            'Numero_muestra_ninos': partes[4],
                            'Tiempo_inactividad': partes[5],
                            'Sugerencias': partes[6],
                            'Fecha_Donacion': partes[13],
                            }

                    if len(partes[7]) == 0 or partes[7] == "null":
                        institucionsalva = None
                    else:
                        if partes[7] != None:
                            elemetos = partes[7].split(',')
                            if len(elemetos) == 1:
                                institucionsalva = Institucion.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1])
                            elif len(elemetos) == 3:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1]) | Institucion.objects.filter(
                                    id=elemetos[2]) | Institucion.objects.filter(
                                    id=elemetos[3])
                            elif len(elemetos) == 5:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1]) | Institucion.objects.filter(
                                    id=elemetos[2]) | Institucion.objects.filter(
                                    id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                institucionsalva = Institucion.objects.filter(
                                    id=elemetos[0]) | Institucion.objects.filter(
                                    id=elemetos[1]) | Institucion.objects.filter(
                                    id=elemetos[2]) | Institucion.objects.filter(
                                    id=elemetos[3]) | Institucion.objects.filter(
                                    id=elemetos[4]) | Institucion.objects.filter(
                                    id=elemetos[5])

                    if len(partes[8]) == 0 or partes[8] == "null":
                        tiporsalva = None
                    else:
                        if partes[8] != None:
                            elemetos = partes[8].split(',')
                            if len(elemetos) == 1:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1])
                            elif len(elemetos) == 3:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1]) | TipoProyecto.objects.filter(
                                    id=elemetos[2]) | TipoProyecto.objects.filter(
                                    id=elemetos[3])
                            elif len(elemetos) == 5:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1]) | TipoProyecto.objects.filter(
                                    id=elemetos[2]) | TipoProyecto.objects.filter(
                                    id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                    id=elemetos[1]) | TipoProyecto.objects.filter(
                                    id=elemetos[2]) | TipoProyecto.objects.filter(
                                    id=elemetos[3]) | TipoProyecto.objects.filter(
                                    id=elemetos[4]) | TipoProyecto.objects.filter(
                                    id=elemetos[5])

                    if len(partes[9]) == 0 or partes[9] == "null":
                        responsablesalva = None
                    else:
                        if partes[9] != None:
                            elemetos = partes[9].split(',')
                            if len(elemetos) == 1:
                                responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1])
                            elif len(elemetos) == 3:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3])
                            elif len(elemetos) == 5:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[3]) | ResponsableInstitucional.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                responsablesalva = ResponsableInstitucional.objects.filter(
                                    id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[3]) | ResponsableInstitucional.objects.filter(
                                    id=elemetos[4]) | ResponsableInstitucional.objects.filter(id=elemetos[5])

                    if len(partes[10]) == 0 or partes[10] == "null":
                        tutorsalva = None
                    else:
                        if partes[10] != None:
                            elemetos = partes[10].split(',')
                            if len(elemetos) == 1:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1])
                            elif len(elemetos) == 3:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                    id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                    id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                    id=elemetos[3])
                            elif len(elemetos) == 5:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                    id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                    id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                    id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                    id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4]) | Tutor.objects.filter(
                                    id=elemetos[5])

                    if len(partes[11]) == 0 or partes[11] == "null":
                        autorsalva = None
                    else:
                        if partes[11] != None:
                            elemetos = partes[11].split(',')
                            if len(elemetos) == 1:
                                autorsalva = Autor.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1])
                            elif len(elemetos) == 3:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                    id=elemetos[1]) | Autor.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                    id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                    id=elemetos[3])
                            elif len(elemetos) == 5:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                    id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                    id=elemetos[3]) | Autor.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                    id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                    id=elemetos[3]) | Autor.objects.filter(id=elemetos[4]) | Autor.objects.filter(
                                    id=elemetos[5])

                    if len(partes[12]) == 0 or partes[12] == "null":
                        areasalva = None
                    else:
                        if partes[12] != None:
                            elemetos = partes[12].split(',')
                            if len(elemetos) == 1:
                                areasalva = AreaConocimiento.objects.filter(id=elemetos[0])
                            elif len(elemetos) == 2:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1])
                            elif len(elemetos) == 3:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2])
                            elif len(elemetos) == 4:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1]) | AreaConocimiento.objects.filter(
                                    id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3])
                            elif len(elemetos) == 5:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1]) | AreaConocimiento.objects.filter(
                                    id=elemetos[2]) | AreaConocimiento.objects.filter(
                                    id=elemetos[3]) | AreaConocimiento.objects.filter(id=elemetos[4])
                            elif len(elemetos) == 6:
                                areasalva = AreaConocimiento.objects.filter(
                                    id=elemetos[0]) | AreaConocimiento.objects.filter(
                                    id=elemetos[1]) | AreaConocimiento.objects.filter(
                                    id=elemetos[2]) | AreaConocimiento.objects.filter(
                                    id=elemetos[3]) | AreaConocimiento.objects.filter(
                                    id=elemetos[4]) | AreaConocimiento.objects.filter(id=elemetos[5])

                    form = GuardarProyectoForm(data)
                    formset = ImagenFormset(queryset=Imagenes.objects.filter(proyecto=proyecto))
                    formar = ArchivosFormset(queryset=Archivos.objects.filter(proyecto=proyecto))
                    formac = ActasFormset(queryset=Actas.objects.filter(proyecto=proyecto))
                    formi = GuardarInstitucionForm()
                    formti = GuardarTipoForm()
                    formre = GuardarResponsableForm()
                    formt = GuardarTutorForm()
                    forma = GuardarAutorForm(request.POST, request.FILES)
                    formare = GuardarAreaForm()
                    return render(request, 'proyecto/editar_proyecto.html',
                                  {'message': message, 'form': form, 'formset': formset, 'formar': formar,
                                   'formac': formac,
                                   'formi': formi, 'formti': formti, 'formre': formre, 'formt': formt, 'forma': forma,
                                   'formare': formare, 'proyecto':proyecto,
                                   'carreras': carreras, 'tipoproyectos': tipoproyectos, 'instituciones': instituciones,
                                   'responsableinstitucionales': responsableinstitucionales, 'autores': autores,
                                   'tutores': tutores,
                                   'areaconocimientos': areaconocimientos,
                                   'tipoproyecto': tiporsalva, 'institucion': institucionsalva,
                                   'responsableinstitucional': responsablesalva, 'autor': autorsalva, 'tutor': tutorsalva,
                                   'areaconocimiento': areasalva
                                   })
            else:
                message = "Ingrese los 10 dígitos de la cédula para registrar el Autor."
                data = {'Titulo': partes[0],
                        'Proposito': partes[1],
                        'Estado_proyecto': partes[2],
                        'Poblacion_utiliza': partes[3],
                        'Numero_muestra_ninos': partes[4],
                        'Tiempo_inactividad': partes[5],
                        'Sugerencias': partes[6],
                        'Fecha_Donacion': partes[13],
                        }

                if len(partes[7]) == 0 or partes[7] == "null":
                    institucionsalva = None
                else:
                    if partes[7] != None:
                        elemetos = partes[7].split(',')
                        if len(elemetos) == 1:
                            institucionsalva = Institucion.objects.filter(id=elemetos[0])
                        elif len(elemetos) == 2:
                            institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                                id=elemetos[1])
                        elif len(elemetos) == 3:
                            institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                                id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2])
                        elif len(elemetos) == 4:
                            institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                                id=elemetos[1]) | Institucion.objects.filter(
                                id=elemetos[2]) | Institucion.objects.filter(
                                id=elemetos[3])
                        elif len(elemetos) == 5:
                            institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                                id=elemetos[1]) | Institucion.objects.filter(
                                id=elemetos[2]) | Institucion.objects.filter(
                                id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4])
                        elif len(elemetos) == 6:
                            institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                                id=elemetos[1]) | Institucion.objects.filter(
                                id=elemetos[2]) | Institucion.objects.filter(
                                id=elemetos[3]) | Institucion.objects.filter(
                                id=elemetos[4]) | Institucion.objects.filter(
                                id=elemetos[5])

                if len(partes[8]) == 0 or partes[8] == "null":
                    tiporsalva = None
                else:
                    if partes[8] != None:
                        elemetos = partes[8].split(',')
                        if len(elemetos) == 1:
                            tiporsalva = TipoProyecto.objects.filter(id=elemetos[0])
                        elif len(elemetos) == 2:
                            tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                id=elemetos[1])
                        elif len(elemetos) == 3:
                            tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2])
                        elif len(elemetos) == 4:
                            tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                id=elemetos[1]) | TipoProyecto.objects.filter(
                                id=elemetos[2]) | TipoProyecto.objects.filter(
                                id=elemetos[3])
                        elif len(elemetos) == 5:
                            tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                id=elemetos[1]) | TipoProyecto.objects.filter(
                                id=elemetos[2]) | TipoProyecto.objects.filter(
                                id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4])
                        elif len(elemetos) == 6:
                            tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                                id=elemetos[1]) | TipoProyecto.objects.filter(
                                id=elemetos[2]) | TipoProyecto.objects.filter(
                                id=elemetos[3]) | TipoProyecto.objects.filter(
                                id=elemetos[4]) | TipoProyecto.objects.filter(
                                id=elemetos[5])

                if len(partes[9]) == 0 or partes[9] == "null":
                    responsablesalva = None
                else:
                    if partes[9] != None:
                        elemetos = partes[9].split(',')
                        if len(elemetos) == 1:
                            responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0])
                        elif len(elemetos) == 2:
                            responsablesalva = ResponsableInstitucional.objects.filter(
                                id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1])
                        elif len(elemetos) == 3:
                            responsablesalva = ResponsableInstitucional.objects.filter(
                                id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2])
                        elif len(elemetos) == 4:
                            responsablesalva = ResponsableInstitucional.objects.filter(
                                id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3])
                        elif len(elemetos) == 5:
                            responsablesalva = ResponsableInstitucional.objects.filter(
                                id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[3]) | ResponsableInstitucional.objects.filter(id=elemetos[4])
                        elif len(elemetos) == 6:
                            responsablesalva = ResponsableInstitucional.objects.filter(
                                id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[3]) | ResponsableInstitucional.objects.filter(
                                id=elemetos[4]) | ResponsableInstitucional.objects.filter(id=elemetos[5])

                if len(partes[10]) == 0 or partes[10] == "null":
                    tutorsalva = None
                else:
                    if partes[10] != None:
                        elemetos = partes[10].split(',')
                        if len(elemetos) == 1:
                            tutorsalva = Tutor.objects.filter(id=elemetos[0])
                        elif len(elemetos) == 2:
                            tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1])
                        elif len(elemetos) == 3:
                            tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2])
                        elif len(elemetos) == 4:
                            tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                id=elemetos[3])
                        elif len(elemetos) == 5:
                            tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4])
                        elif len(elemetos) == 6:
                            tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                                id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                                id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4]) | Tutor.objects.filter(
                                id=elemetos[5])

                if len(partes[11]) == 0 or partes[11] == "null":
                    autorsalva = None
                else:
                    if partes[11] != None:
                        elemetos = partes[11].split(',')
                        if len(elemetos) == 1:
                            autorsalva = Autor.objects.filter(id=elemetos[0])
                        elif len(elemetos) == 2:
                            autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1])
                        elif len(elemetos) == 3:
                            autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                id=elemetos[1]) | Autor.objects.filter(id=elemetos[2])
                        elif len(elemetos) == 4:
                            autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                id=elemetos[3])
                        elif len(elemetos) == 5:
                            autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                id=elemetos[3]) | Autor.objects.filter(id=elemetos[4])
                        elif len(elemetos) == 6:
                            autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                                id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                                id=elemetos[3]) | Autor.objects.filter(id=elemetos[4]) | Autor.objects.filter(
                                id=elemetos[5])

                if len(partes[12]) == 0 or partes[12] == "null":
                    areasalva = None
                else:
                    if partes[12] != None:
                        elemetos = partes[12].split(',')
                        if len(elemetos) == 1:
                            areasalva = AreaConocimiento.objects.filter(id=elemetos[0])
                        elif len(elemetos) == 2:
                            areasalva = AreaConocimiento.objects.filter(
                                id=elemetos[0]) | AreaConocimiento.objects.filter(
                                id=elemetos[1])
                        elif len(elemetos) == 3:
                            areasalva = AreaConocimiento.objects.filter(
                                id=elemetos[0]) | AreaConocimiento.objects.filter(
                                id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2])
                        elif len(elemetos) == 4:
                            areasalva = AreaConocimiento.objects.filter(
                                id=elemetos[0]) | AreaConocimiento.objects.filter(
                                id=elemetos[1]) | AreaConocimiento.objects.filter(
                                id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3])
                        elif len(elemetos) == 5:
                            areasalva = AreaConocimiento.objects.filter(
                                id=elemetos[0]) | AreaConocimiento.objects.filter(
                                id=elemetos[1]) | AreaConocimiento.objects.filter(
                                id=elemetos[2]) | AreaConocimiento.objects.filter(
                                id=elemetos[3]) | AreaConocimiento.objects.filter(id=elemetos[4])
                        elif len(elemetos) == 6:
                            areasalva = AreaConocimiento.objects.filter(
                                id=elemetos[0]) | AreaConocimiento.objects.filter(
                                id=elemetos[1]) | AreaConocimiento.objects.filter(
                                id=elemetos[2]) | AreaConocimiento.objects.filter(
                                id=elemetos[3]) | AreaConocimiento.objects.filter(
                                id=elemetos[4]) | AreaConocimiento.objects.filter(id=elemetos[5])

                form = GuardarProyectoForm(data)
                formset = ImagenFormset(queryset=Imagenes.objects.filter(proyecto=proyecto))
                formar = ArchivosFormset(queryset=Archivos.objects.filter(proyecto=proyecto))
                formac = ActasFormset(queryset=Actas.objects.filter(proyecto=proyecto))
                formi = GuardarInstitucionForm()
                formti = GuardarTipoForm()
                formre = GuardarResponsableForm()
                formt = GuardarTutorForm()
                forma = GuardarAutorForm(request.POST, request.FILES)
                formare = GuardarAreaForm()
                return render(request, 'proyecto/editar_proyecto.html',
                              {'message': message, 'form': form, 'formset': formset, 'formar': formar, 'formac': formac,
                               'formi': formi, 'formti': formti, 'formre': formre, 'formt': formt, 'forma': forma,
                               'formare': formare,
                               'carreras': carreras, 'tipoproyectos': tipoproyectos, 'instituciones': instituciones,
                               'responsableinstitucionales': responsableinstitucionales, 'autores': autores,
                               'tutores': tutores, 'proyecto':proyecto,
                               'areaconocimientos': areaconocimientos,
                               'tipoproyecto': tiporsalva, 'institucion': institucionsalva,
                               'responsableinstitucional': responsablesalva, 'autor': autorsalva, 'tutor': tutorsalva,
                               'areaconocimiento': areasalva
                               })


        elif formare.is_valid():
            formare.save()
            data = {'Titulo': partes[0],
                    'Proposito': partes[1],
                    'Estado_proyecto': partes[2],
                    'Poblacion_utiliza': partes[3],
                    'Numero_muestra_ninos': partes[4],
                    'Tiempo_inactividad': partes[5],
                    'Sugerencias': partes[6],
                    'Fecha_Donacion': partes[13],
                    }

            if len(partes[7]) == 0 or partes[7] == "null":
                institucionsalva = None
            else:
                if partes[7] != None:
                    elemetos = partes[7].split(',')
                    if len(elemetos) == 1:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1])
                    elif len(elemetos) == 3:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(
                            id=elemetos[3])
                    elif len(elemetos) == 5:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(
                            id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(
                            id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4]) | Institucion.objects.filter(
                            id=elemetos[5])

            if len(partes[8]) == 0 or partes[8] == "null":
                tiporsalva = None
            else:
                if partes[8] != None:
                    elemetos = partes[8].split(',')
                    if len(elemetos) == 1:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1])
                    elif len(elemetos) == 3:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(
                            id=elemetos[3])
                    elif len(elemetos) == 5:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(
                            id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(
                            id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4]) | TipoProyecto.objects.filter(
                            id=elemetos[5])

            if len(partes[9]) == 0 or partes[9] == "null":
                responsablesalva = None
            else:
                if partes[9] != None:
                    elemetos = partes[9].split(',')
                    if len(elemetos) == 1:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[3]) | ResponsableInstitucional.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[3]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[4]) | ResponsableInstitucional.objects.filter(id=elemetos[5])

            if len(partes[10]) == 0 or partes[10] == "null":
                tutorsalva = None
            else:
                if partes[10] != None:
                    elemetos = partes[10].split(',')
                    if len(elemetos) == 1:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                            id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                            id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                            id=elemetos[3])
                    elif len(elemetos) == 5:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                            id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                            id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                            id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                            id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4]) | Tutor.objects.filter(
                            id=elemetos[5])

            if len(partes[11]) == 0 or partes[11] == "null":
                autorsalva = None
            else:
                if partes[11] != None:
                    elemetos = partes[11].split(',')
                    if len(elemetos) == 1:
                        autorsalva = Autor.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                            id=elemetos[1]) | Autor.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                            id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                            id=elemetos[3])
                    elif len(elemetos) == 5:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                            id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                            id=elemetos[3]) | Autor.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                            id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                            id=elemetos[3]) | Autor.objects.filter(id=elemetos[4]) | Autor.objects.filter(
                            id=elemetos[5])

            if len(partes[12]) == 0 or partes[12] == "null":
                areasalva = None
            else:
                if partes[12] != None:
                    elemetos = partes[12].split(',')
                    if len(elemetos) == 1:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1])
                    elif len(elemetos) == 3:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1]) | AreaConocimiento.objects.filter(
                            id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1]) | AreaConocimiento.objects.filter(
                            id=elemetos[2]) | AreaConocimiento.objects.filter(
                            id=elemetos[3]) | AreaConocimiento.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1]) | AreaConocimiento.objects.filter(
                            id=elemetos[2]) | AreaConocimiento.objects.filter(
                            id=elemetos[3]) | AreaConocimiento.objects.filter(
                            id=elemetos[4]) | AreaConocimiento.objects.filter(id=elemetos[5])

            form = GuardarProyectoForm(data)
            formset = ImagenFormset(queryset=Imagenes.objects.filter(proyecto=proyecto))
            formar = ArchivosFormset(queryset=Archivos.objects.filter(proyecto=proyecto))
            formac = ActasFormset(queryset=Actas.objects.filter(proyecto=proyecto))
            formi = GuardarInstitucionForm()
            formti = GuardarTipoForm()
            formre = GuardarResponsableForm()
            formt = GuardarTutorForm()
            forma = GuardarAutorForm()
            formare = GuardarAreaForm()
            message1 = "El Área de Conocimiento a sido registrada con éxito."
            return render(request, 'proyecto/editar_proyecto.html',
                          {'message': message, 'message1': message1, 'form': form, 'formset': formset, 'formar': formar, 'formac': formac,
                           'formi': formi, 'formti': formti, 'formre': formre, 'formt': formt, 'forma': forma,
                           'formare': formare,
                           'carreras': carreras, 'tipoproyectos': tipoproyectos, 'instituciones': instituciones,
                           'responsableinstitucionales': responsableinstitucionales, 'autores': autores,
                           'tutores': tutores, 'proyecto':proyecto,
                           'areaconocimientos': areaconocimientos,
                           'tipoproyecto': tiporsalva, 'institucion': institucionsalva,
                           'responsableinstitucional': responsablesalva, 'autor': autorsalva, 'tutor': tutorsalva,
                           'areaconocimiento': areasalva
                           })
        elif form.is_valid():
            form.save()
            return redirect('Proyecto')

        elif formset.is_valid() and imagena != None and arcvhioa == None and actaa ==None:
            data = {'Titulo': partes[0],
                    'Proposito': partes[1],
                    'Estado_proyecto': partes[2],
                    'Poblacion_utiliza': partes[3],
                    'Numero_muestra_ninos': partes[4],
                    'Tiempo_inactividad': partes[5],
                    'Sugerencias': partes[6],
                    'Fecha_Donacion': partes[13],
                    }

            if len(partes[7]) == 0 or partes[7] == "null":
                institucionsalva = None
            else:
                if partes[7] != None:
                    elemetos = partes[7].split(',')
                    if len(elemetos) == 1:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1])
                    elif len(elemetos) == 3:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(
                            id=elemetos[3])
                    elif len(elemetos) == 5:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(
                            id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(
                            id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4]) | Institucion.objects.filter(
                            id=elemetos[5])

            if len(partes[8]) == 0 or partes[8] == "null":
                tiporsalva = None
            else:
                if partes[8] != None:
                    elemetos = partes[8].split(',')
                    if len(elemetos) == 1:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1])
                    elif len(elemetos) == 3:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(
                            id=elemetos[3])
                    elif len(elemetos) == 5:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(
                            id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(
                            id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4]) | TipoProyecto.objects.filter(
                            id=elemetos[5])

            if len(partes[9]) == 0 or partes[9] == "null":
                responsablesalva = None
            else:
                if partes[9] != None:
                    elemetos = partes[9].split(',')
                    if len(elemetos) == 1:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[3]) | ResponsableInstitucional.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[3]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[4]) | ResponsableInstitucional.objects.filter(id=elemetos[5])

            if len(partes[10]) == 0 or partes[10] == "null":
                tutorsalva = None
            else:
                if partes[10] != None:
                    elemetos = partes[10].split(',')
                    if len(elemetos) == 1:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                            id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                            id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                            id=elemetos[3])
                    elif len(elemetos) == 5:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                            id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                            id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                            id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                            id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4]) | Tutor.objects.filter(
                            id=elemetos[5])

            if len(partes[11]) == 0 or partes[11] == "null":
                autorsalva = None
            else:
                if partes[11] != None:
                    elemetos = partes[11].split(',')
                    if len(elemetos) == 1:
                        autorsalva = Autor.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                            id=elemetos[1]) | Autor.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                            id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                            id=elemetos[3])
                    elif len(elemetos) == 5:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                            id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                            id=elemetos[3]) | Autor.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                            id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                            id=elemetos[3]) | Autor.objects.filter(id=elemetos[4]) | Autor.objects.filter(
                            id=elemetos[5])

            if len(partes[12]) == 0 or partes[12] == "null":
                areasalva = None
            else:
                if partes[12] != None:
                    elemetos = partes[12].split(',')
                    if len(elemetos) == 1:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1])
                    elif len(elemetos) == 3:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1]) | AreaConocimiento.objects.filter(
                            id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1]) | AreaConocimiento.objects.filter(
                            id=elemetos[2]) | AreaConocimiento.objects.filter(
                            id=elemetos[3]) | AreaConocimiento.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1]) | AreaConocimiento.objects.filter(
                            id=elemetos[2]) | AreaConocimiento.objects.filter(
                            id=elemetos[3]) | AreaConocimiento.objects.filter(
                            id=elemetos[4]) | AreaConocimiento.objects.filter(id=elemetos[5])

            datos = Imagenes.objects.filter(proyecto=proyecto)
            for index, f in enumerate(formset):
                if f.cleaned_data:
                    if f.cleaned_data['id'] is None:
                        foto = Imagenes(proyecto=proyecto, nombre_imagenes=f.cleaned_data.get('nombre_imagenes'))
                        foto.save()
                    elif f.cleaned_data['nombre_imagenes'] is False:
                        foto = Imagenes.objects.get (id=request.POST.get('form-'+str(index) +'-id'))
                        foto.delete()
                        break
                    else:
                        foto = Imagenes(proyecto=proyecto, nombre_imagenes=f.cleaned_data.get('nombre_imagenes'))
                        d= Imagenes.objects.get(id=datos[index].id)
                        d.nombre_imagenes=foto.nombre_imagenes
                        d.save()

            form = GuardarProyectoForm(data)
            formset = ImagenFormset(queryset=Imagenes.objects.filter(proyecto=proyecto))
            formar = ArchivosFormset(queryset=Archivos.objects.filter(proyecto=proyecto))
            formac = ActasFormset(queryset=Actas.objects.filter(proyecto=proyecto))
            formi = GuardarInstitucionForm()
            formti = GuardarTipoForm()
            formre = GuardarResponsableForm()
            formt = GuardarTutorForm()
            forma = GuardarAutorForm()
            formare = GuardarAreaForm()
            message1 = "Las Imágenes han sido editadas con éxito."
            return render(request, 'proyecto/editar_proyecto.html',
                          {'message': message, 'message1': message1, 'form': form, 'formset': formset, 'formar': formar,
                           'formac': formac,
                           'formi': formi, 'formti': formti, 'formre': formre, 'formt': formt, 'forma': forma,
                           'formare': formare,
                           'carreras': carreras, 'tipoproyectos': tipoproyectos, 'instituciones': instituciones,
                           'responsableinstitucionales': responsableinstitucionales, 'autores': autores,
                           'tutores': tutores, 'proyecto': proyecto,
                           'areaconocimientos': areaconocimientos,
                           'tipoproyecto': tiporsalva, 'institucion': institucionsalva,
                           'responsableinstitucional': responsablesalva, 'autor': autorsalva, 'tutor': tutorsalva,
                           'areaconocimiento': areasalva
                           })

        elif formar.is_valid() and arcvhioa != None and imagena == None and actaa ==None:
            data = {'Titulo': partes[0],
                    'Proposito': partes[1],
                    'Estado_proyecto': partes[2],
                    'Poblacion_utiliza': partes[3],
                    'Numero_muestra_ninos': partes[4],
                    'Tiempo_inactividad': partes[5],
                    'Sugerencias': partes[6],
                    'Fecha_Donacion': partes[13],
                    }

            if len(partes[7]) == 0 or partes[7] == "null":
                institucionsalva = None
            else:
                if partes[7] != None:
                    elemetos = partes[7].split(',')
                    if len(elemetos) == 1:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1])
                    elif len(elemetos) == 3:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(
                            id=elemetos[3])
                    elif len(elemetos) == 5:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(
                            id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(
                            id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4]) | Institucion.objects.filter(
                            id=elemetos[5])

            if len(partes[8]) == 0 or partes[8] == "null":
                tiporsalva = None
            else:
                if partes[8] != None:
                    elemetos = partes[8].split(',')
                    if len(elemetos) == 1:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1])
                    elif len(elemetos) == 3:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(
                            id=elemetos[3])
                    elif len(elemetos) == 5:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(
                            id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(
                            id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4]) | TipoProyecto.objects.filter(
                            id=elemetos[5])

            if len(partes[9]) == 0 or partes[9] == "null":
                responsablesalva = None
            else:
                if partes[9] != None:
                    elemetos = partes[9].split(',')
                    if len(elemetos) == 1:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[3]) | ResponsableInstitucional.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[3]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[4]) | ResponsableInstitucional.objects.filter(id=elemetos[5])

            if len(partes[10]) == 0 or partes[10] == "null":
                tutorsalva = None
            else:
                if partes[10] != None:
                    elemetos = partes[10].split(',')
                    if len(elemetos) == 1:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                            id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                            id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                            id=elemetos[3])
                    elif len(elemetos) == 5:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                            id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                            id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                            id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                            id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4]) | Tutor.objects.filter(
                            id=elemetos[5])

            if len(partes[11]) == 0 or partes[11] == "null":
                autorsalva = None
            else:
                if partes[11] != None:
                    elemetos = partes[11].split(',')
                    if len(elemetos) == 1:
                        autorsalva = Autor.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                            id=elemetos[1]) | Autor.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                            id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                            id=elemetos[3])
                    elif len(elemetos) == 5:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                            id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                            id=elemetos[3]) | Autor.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                            id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                            id=elemetos[3]) | Autor.objects.filter(id=elemetos[4]) | Autor.objects.filter(
                            id=elemetos[5])

            if len(partes[12]) == 0 or partes[12] == "null":
                areasalva = None
            else:
                if partes[12] != None:
                    elemetos = partes[12].split(',')
                    if len(elemetos) == 1:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1])
                    elif len(elemetos) == 3:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1]) | AreaConocimiento.objects.filter(
                            id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1]) | AreaConocimiento.objects.filter(
                            id=elemetos[2]) | AreaConocimiento.objects.filter(
                            id=elemetos[3]) | AreaConocimiento.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1]) | AreaConocimiento.objects.filter(
                            id=elemetos[2]) | AreaConocimiento.objects.filter(
                            id=elemetos[3]) | AreaConocimiento.objects.filter(
                            id=elemetos[4]) | AreaConocimiento.objects.filter(id=elemetos[5])

            data1 = Archivos.objects.filter(proyecto=proyecto)
            for index1, f1 in enumerate(formar):
                if f1.cleaned_data:
                    if f1.cleaned_data['id'] is None:
                        arc = Archivos(proyecto=proyecto, nombre_archivos=f1.cleaned_data.get('nombre_archivos'))
                        arc.save()
                    elif f1.cleaned_data['nombre_archivos'] is False:
                        arce= Archivos.objects.get (id=request.POST.get('form-'+str(index1) +'-id'))
                        arce.delete()
                        break
                    else:
                        arc = Archivos(proyecto=proyecto, nombre_archivos=f1.cleaned_data.get('nombre_archivos'))
                        ar= Archivos.objects.get(id=data1[index1].id)
                        ar.nombre_archivos=arc.nombre_archivos
                        ar.save()

            form = GuardarProyectoForm(data)
            formset = ImagenFormset(queryset=Imagenes.objects.filter(proyecto=proyecto))
            formar = ArchivosFormset(queryset=Archivos.objects.filter(proyecto=proyecto))
            formac = ActasFormset(queryset=Actas.objects.filter(proyecto=proyecto))
            formi = GuardarInstitucionForm()
            formti = GuardarTipoForm()
            formre = GuardarResponsableForm()
            formt = GuardarTutorForm()
            forma = GuardarAutorForm()
            formare = GuardarAreaForm()
            message1 = "Los Archivos han sido editados con éxito."
            return render(request, 'proyecto/editar_proyecto.html',
                          {'message': message, 'message1': message1, 'form': form, 'formset': formset, 'formar': formar,
                           'formac': formac,
                           'formi': formi, 'formti': formti, 'formre': formre, 'formt': formt, 'forma': forma,
                           'formare': formare,
                           'carreras': carreras, 'tipoproyectos': tipoproyectos, 'instituciones': instituciones,
                           'responsableinstitucionales': responsableinstitucionales, 'autores': autores,
                           'tutores': tutores, 'proyecto': proyecto,
                           'areaconocimientos': areaconocimientos,
                           'tipoproyecto': tiporsalva, 'institucion': institucionsalva,
                           'responsableinstitucional': responsablesalva, 'autor': autorsalva, 'tutor': tutorsalva,
                           'areaconocimiento': areasalva
                           })

        elif formac.is_valid() and actaa != None and imagena == None and arcvhioa == None:
            data = {'Titulo': partes[0],
                    'Proposito': partes[1],
                    'Estado_proyecto': partes[2],
                    'Poblacion_utiliza': partes[3],
                    'Numero_muestra_ninos': partes[4],
                    'Tiempo_inactividad': partes[5],
                    'Sugerencias': partes[6],
                    'Fecha_Donacion': partes[13],
                    }

            if len(partes[7]) == 0 or partes[7] == "null":
                institucionsalva = None
            else:
                if partes[7] != None:
                    elemetos = partes[7].split(',')
                    if len(elemetos) == 1:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1])
                    elif len(elemetos) == 3:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(
                            id=elemetos[3])
                    elif len(elemetos) == 5:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(
                            id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(
                            id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4]) | Institucion.objects.filter(
                            id=elemetos[5])

            if len(partes[8]) == 0 or partes[8] == "null":
                tiporsalva = None
            else:
                if partes[8] != None:
                    elemetos = partes[8].split(',')
                    if len(elemetos) == 1:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1])
                    elif len(elemetos) == 3:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(
                            id=elemetos[3])
                    elif len(elemetos) == 5:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(
                            id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(
                            id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4]) | TipoProyecto.objects.filter(
                            id=elemetos[5])

            if len(partes[9]) == 0 or partes[9] == "null":
                responsablesalva = None
            else:
                if partes[9] != None:
                    elemetos = partes[9].split(',')
                    if len(elemetos) == 1:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[3]) | ResponsableInstitucional.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[3]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[4]) | ResponsableInstitucional.objects.filter(id=elemetos[5])

            if len(partes[10]) == 0 or partes[10] == "null":
                tutorsalva = None
            else:
                if partes[10] != None:
                    elemetos = partes[10].split(',')
                    if len(elemetos) == 1:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                            id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                            id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                            id=elemetos[3])
                    elif len(elemetos) == 5:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                            id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                            id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                            id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                            id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4]) | Tutor.objects.filter(
                            id=elemetos[5])

            if len(partes[11]) == 0 or partes[11] == "null":
                autorsalva = None
            else:
                if partes[11] != None:
                    elemetos = partes[11].split(',')
                    if len(elemetos) == 1:
                        autorsalva = Autor.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                            id=elemetos[1]) | Autor.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                            id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                            id=elemetos[3])
                    elif len(elemetos) == 5:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                            id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                            id=elemetos[3]) | Autor.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                            id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                            id=elemetos[3]) | Autor.objects.filter(id=elemetos[4]) | Autor.objects.filter(
                            id=elemetos[5])

            if len(partes[12]) == 0 or partes[12] == "null":
                areasalva = None
            else:
                if partes[12] != None:
                    elemetos = partes[12].split(',')
                    if len(elemetos) == 1:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1])
                    elif len(elemetos) == 3:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1]) | AreaConocimiento.objects.filter(
                            id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1]) | AreaConocimiento.objects.filter(
                            id=elemetos[2]) | AreaConocimiento.objects.filter(
                            id=elemetos[3]) | AreaConocimiento.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1]) | AreaConocimiento.objects.filter(
                            id=elemetos[2]) | AreaConocimiento.objects.filter(
                            id=elemetos[3]) | AreaConocimiento.objects.filter(
                            id=elemetos[4]) | AreaConocimiento.objects.filter(id=elemetos[5])

            data2 = Actas.objects.filter(proyecto=proyecto)
            for index2, f2 in enumerate(formac):
                if f2.cleaned_data:
                    if f2.cleaned_data['id'] is None:
                        act = Actas(proyecto=proyecto, nombre_actas=f2.cleaned_data.get('nombre_actas'))
                        act.save()
                    elif f2.cleaned_data['nombre_actas'] is False:
                        acte = Actas.objects.get (id=request.POST.get('form-'+str(index2) +'-id'))
                        acte.delete()
                        break
                    else:
                        act = Actas(proyecto=proyecto, nombre_actas=f2.cleaned_data.get('nombre_actas'))
                        ac= Actas.objects.get(id=data2[index2].id)
                        ac.nombre_actas=act.nombre_actas
                        ac.save()

            form = GuardarProyectoForm(data)
            formset = ImagenFormset(queryset=Imagenes.objects.filter(proyecto=proyecto))
            formar = ArchivosFormset(queryset=Archivos.objects.filter(proyecto=proyecto))
            formac = ActasFormset(queryset=Actas.objects.filter(proyecto=proyecto))
            formi = GuardarInstitucionForm()
            formti = GuardarTipoForm()
            formre = GuardarResponsableForm()
            formt = GuardarTutorForm()
            forma = GuardarAutorForm()
            formare = GuardarAreaForm()
            message1 = "Las Actas han sido editadas con éxito."
            return render(request, 'proyecto/editar_proyecto.html',
                          {'message': message, 'message1': message1, 'form': form, 'formset': formset, 'formar': formar,
                           'formac': formac,
                           'formi': formi, 'formti': formti, 'formre': formre, 'formt': formt, 'forma': forma,
                           'formare': formare,
                           'carreras': carreras, 'tipoproyectos': tipoproyectos, 'instituciones': instituciones,
                           'responsableinstitucionales': responsableinstitucionales, 'autores': autores,
                           'tutores': tutores, 'proyecto': proyecto,
                           'areaconocimientos': areaconocimientos,
                           'tipoproyecto': tiporsalva, 'institucion': institucionsalva,
                           'responsableinstitucional': responsablesalva, 'autor': autorsalva, 'tutor': tutorsalva,
                           'areaconocimiento': areasalva
                           })
        else:
            data = {'Titulo': partes[0],
                    'Proposito': partes[1],
                    'Estado_proyecto': partes[2],
                    'Poblacion_utiliza': partes[3],
                    'Numero_muestra_ninos': partes[4],
                    'Tiempo_inactividad': partes[5],
                    'Sugerencias': partes[6],
                    'Fecha_Donacion': partes[13],
                    }

            if len(partes[7]) == 0 or partes[7] == "null":
                institucionsalva = None
            else:
                if partes[7] != None:
                    elemetos = partes[7].split(',')
                    if len(elemetos) == 1:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1])
                    elif len(elemetos) == 3:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(
                            id=elemetos[3])
                    elif len(elemetos) == 5:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(
                            id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        institucionsalva = Institucion.objects.filter(id=elemetos[0]) | Institucion.objects.filter(
                            id=elemetos[1]) | Institucion.objects.filter(id=elemetos[2]) | Institucion.objects.filter(
                            id=elemetos[3]) | Institucion.objects.filter(id=elemetos[4]) | Institucion.objects.filter(
                            id=elemetos[5])

            if len(partes[8]) == 0 or partes[8] == "null":
                tiporsalva = None
            else:
                if partes[8] != None:
                    elemetos = partes[8].split(',')
                    if len(elemetos) == 1:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1])
                    elif len(elemetos) == 3:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(
                            id=elemetos[3])
                    elif len(elemetos) == 5:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(
                            id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        tiporsalva = TipoProyecto.objects.filter(id=elemetos[0]) | TipoProyecto.objects.filter(
                            id=elemetos[1]) | TipoProyecto.objects.filter(id=elemetos[2]) | TipoProyecto.objects.filter(
                            id=elemetos[3]) | TipoProyecto.objects.filter(id=elemetos[4]) | TipoProyecto.objects.filter(
                            id=elemetos[5])

            if len(partes[9]) == 0 or partes[9] == "null":
                responsablesalva = None
            else:
                if partes[9] != None:
                    elemetos = partes[9].split(',')
                    if len(elemetos) == 1:
                        responsablesalva = ResponsableInstitucional.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[1]) | ResponsableInstitucional.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[2]) | ResponsableInstitucional.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[3]) | ResponsableInstitucional.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        responsablesalva = ResponsableInstitucional.objects.filter(
                            id=elemetos[0]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[1]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[2]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[3]) | ResponsableInstitucional.objects.filter(
                            id=elemetos[4]) | ResponsableInstitucional.objects.filter(id=elemetos[5])

            if len(partes[10]) == 0 or partes[10] == "null":
                tutorsalva = None
            else:
                if partes[10] != None:
                    elemetos = partes[10].split(',')
                    if len(elemetos) == 1:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                            id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                            id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                            id=elemetos[3])
                    elif len(elemetos) == 5:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                            id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                            id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        tutorsalva = Tutor.objects.filter(id=elemetos[0]) | Tutor.objects.filter(
                            id=elemetos[1]) | Tutor.objects.filter(id=elemetos[2]) | Tutor.objects.filter(
                            id=elemetos[3]) | Tutor.objects.filter(id=elemetos[4]) | Tutor.objects.filter(
                            id=elemetos[5])

            if len(partes[11]) == 0 or partes[11] == "null":
                autorsalva = None
            else:
                if partes[11] != None:
                    elemetos = partes[11].split(',')
                    if len(elemetos) == 1:
                        autorsalva = Autor.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(id=elemetos[1])
                    elif len(elemetos) == 3:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                            id=elemetos[1]) | Autor.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                            id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                            id=elemetos[3])
                    elif len(elemetos) == 5:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                            id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                            id=elemetos[3]) | Autor.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        autorsalva = Autor.objects.filter(id=elemetos[0]) | Autor.objects.filter(
                            id=elemetos[1]) | Autor.objects.filter(id=elemetos[2]) | Autor.objects.filter(
                            id=elemetos[3]) | Autor.objects.filter(id=elemetos[4]) | Autor.objects.filter(
                            id=elemetos[5])

            if len(partes[12]) == 0 or partes[12] == "null":
                areasalva = None
            else:
                if partes[12] != None:
                    elemetos = partes[12].split(',')
                    if len(elemetos) == 1:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0])
                    elif len(elemetos) == 2:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1])
                    elif len(elemetos) == 3:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1]) | AreaConocimiento.objects.filter(id=elemetos[2])
                    elif len(elemetos) == 4:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1]) | AreaConocimiento.objects.filter(
                            id=elemetos[2]) | AreaConocimiento.objects.filter(id=elemetos[3])
                    elif len(elemetos) == 5:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1]) | AreaConocimiento.objects.filter(
                            id=elemetos[2]) | AreaConocimiento.objects.filter(
                            id=elemetos[3]) | AreaConocimiento.objects.filter(id=elemetos[4])
                    elif len(elemetos) == 6:
                        areasalva = AreaConocimiento.objects.filter(id=elemetos[0]) | AreaConocimiento.objects.filter(
                            id=elemetos[1]) | AreaConocimiento.objects.filter(
                            id=elemetos[2]) | AreaConocimiento.objects.filter(
                            id=elemetos[3]) | AreaConocimiento.objects.filter(
                            id=elemetos[4]) | AreaConocimiento.objects.filter(id=elemetos[5])
            form = GuardarProyectoForm(data)
            formset = ImagenFormset(queryset=Imagenes.objects.filter(proyecto=proyecto))
            formar = ArchivosFormset(queryset=Archivos.objects.filter(proyecto=proyecto))
            formac = ActasFormset(queryset=Actas.objects.filter(proyecto=proyecto))
            formi = GuardarInstitucionForm()
            formti = GuardarTipoForm()
            formre = GuardarResponsableForm()
            formt = GuardarTutorForm()
            forma = GuardarAutorForm()
            formare = GuardarAreaForm()
            message = "Uno de los campos fueron erróneos o no se a agregado en el registro del Proyecto."
            return render(request, 'proyecto/editar_proyecto.html',
                          {'message':message, 'form': form, 'formset': formset, 'formar': formar, 'formac': formac,
                           'formi': formi, 'formti': formti, 'formre': formre, 'formt': formt, 'forma': forma, 'formare': formare,
                           'carreras': carreras, 'tipoproyectos': tipoproyectos, 'instituciones': instituciones,
                           'responsableinstitucionales': responsableinstitucionales, 'autores': autores, 'tutores': tutores,
                           'areaconocimientos': areaconocimientos, 'proyecto':proyecto,
                           'tipoproyecto': tiporsalva, 'institucion': institucionsalva,
                           'responsableinstitucional': responsablesalva, 'autor': autorsalva, 'tutor': tutorsalva,
                           'areaconocimiento': areasalva
                           })
    else:
        form = GuardarProyectoForm(instance=proyecto)
        formset = ImagenFormset(queryset = Imagenes.objects.filter(proyecto=proyecto))
        formar = ArchivosFormset(queryset = Archivos.objects.filter(proyecto=proyecto))
        formac = ActasFormset(queryset = Actas.objects.filter(proyecto=proyecto))
        formi = GuardarInstitucionForm()
        formti = GuardarTipoForm()
        formre = GuardarResponsableForm()
        formt = GuardarTutorForm()
        forma = GuardarAutorForm()
        formare = GuardarAreaForm()
        estado = proyecto.Donado
        if estado == "Si":
            activa ="Si"
        else:
            activa = None
        fecha = proyecto.Fecha_Donacion
        if fecha is not None:
            factiva ="Si"
        else:
            factiva = None
        print(fecha)

    return render(request, 'proyecto/editar_proyecto.html',
                  {'message': message, 'form': form, 'formset': formset, 'formar': formar, 'formac': formac,
                   'formi': formi, 'formti': formti, 'formre': formre, 'formt': formt, 'forma': forma,
                   'formare': formare, 'proyecto':proyecto,
                   'carreras': carreras, 'tipoproyectos': tipoproyectos, 'instituciones': instituciones,
                   'responsableinstitucionales': responsableinstitucionales, 'autores': autores, 'tutores': tutores,
                   'areaconocimientos': areaconocimientos,
                   'tipoproyecto': tiporsalva, 'institucion': institucionsalva,
                   'responsableinstitucional': responsablesalva, 'autor': autorsalva, 'tutor': tutorsalva,
                   'areaconocimiento': areasalva, 'activa':activa, 'factiva':factiva
                   })


@login_required
@permission_required('gestionproyecto.eliminar_proyecto',reverse_lazy('Proyecto'))
def eliminar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    proyecto.delete()
    return redirect('Proyecto')


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