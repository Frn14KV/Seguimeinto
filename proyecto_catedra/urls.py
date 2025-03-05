from django.contrib import admin

admin.autodiscover()
from django.urls import include, path, re_path
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

import gestioninstitucion.views
import gestionresponsableinstitucional.views
import gestionautor.views
import gestiontutor.views
import gestiontipoproyecto.views
import gestionareaconocimiento.views
import gestioncarrera.views
import proyecto_catedra.views
import gestionproyecto.views

from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/doc', include('django.contrib.admindocs.urls')),

    #inicio y opciones usuario
    path('', proyecto_catedra.views.homepage, name="homepage"),
    path('usuarios', proyecto_catedra.views.usuarios, name="usuarios"),
    path('usuarios/agregar', proyecto_catedra.views.agregar_usuario, name='agregar_usuario'),
    re_path(r'^usuarios/eliminar/(?P<usuario_id>\d+)/$', proyecto_catedra.views.eliminar, name='eliminar_usuario'),
    re_path(r'^usuarios/editar/(?P<usuario_id>\d+)/$', proyecto_catedra.views.editar_usuario, name='editar_usuario'),
    re_path(r'^usuarios/editar/clave/(?P<usuario_id>\d+)/$', proyecto_catedra.views.cambiar_clave, name="editar_clave"),

    #inicion y registro
    path('login', proyecto_catedra.views.login_page, name="login"),
    path('loginv', proyecto_catedra.views.login_view, name="loginv"),
    path('logout', proyecto_catedra.views.logout_view, name="logout"),
    path('registro', proyecto_catedra.views.registro, name='registro'),
    path('registroad', proyecto_catedra.views.registroad, name='registroad'),
    path('registrosp', proyecto_catedra.views.registrosp, name='registrosp'),
    re_path(r'^oauth/', include('social_django.urls', namespace="social")),

    #recuperar password
    re_path(r'^password-reset/$',auth_views.PasswordResetView.as_view(template_name='registro/password_reset_form.html'), name="password_reset"),
    re_path(r'^password-reset/done/$',auth_views.PasswordResetDoneView.as_view(template_name='registro/password_reset_done.html'), name="password_reset_done"),
    re_path(r'^password-reset/complete/$',auth_views.PasswordResetCompleteView.as_view(template_name='registro/password_reset_complete.html'), name="password_reset_complete"),
    re_path(r'^password-reset/confirm/(?P<uidb64>[\w-]+)/(?P<token>[\w-]+)/$',auth_views.PasswordResetConfirmView.as_view(template_name='registro/password_reset_confirm.html'), name="password_reset_confirm"),

    #institucion
    path('institucion/', gestioninstitucion.views.index, name='Institucion'),
    path('institucion/guardar/', gestioninstitucion.views.guardar_institucion, name='guardar_institucion'),
    re_path(r'^institucion/editar/(?P<institucion_id>\d+)/$', gestioninstitucion.views.editar_institucion, name='editar_institucion'),
    re_path(r'^institucion/eliminar/(?P<institucion_id>\d+)/', gestioninstitucion.views.eliminar_institucion, name='eliminar_institucion'),
    re_path(r'^institucion/infor/(?P<institucion_id>\d+)/$', gestioninstitucion.views.institucion_detallada, name='institucion_detallada'),

    #responsable
    path('responsableinstitucional', gestionresponsableinstitucional.views.index, name='ResponsableInstitucional'),
    path('responsableinstitucional/guardar', gestionresponsableinstitucional.views.guardar_responsableinstitucional, name='guardar_responsableinstitucional'),
    re_path(r'^responsableinstitucional/editar/(?P<responsableinstitucional_id>\d+)/$', gestionresponsableinstitucional.views.editar_responsableinstitucional, name='editar_responsableinstitucional'),
    re_path(r'^responsableinstitucional/infor/(?P<responsableinstitucional_id>\d+)/$', gestionresponsableinstitucional.views.responsableinstitucional_detalle, name='responsableinstitucional_detalle'),
    re_path(r'^responsableinstitucional/eliminar/(?P<responsableinstitucional_id>\d+)/$', gestionresponsableinstitucional.views.eliminar_responsableinstitucional, name='eliminar_responsableinstitucional'),

    #autor
    path('autor', gestionautor.views.index, name='Autor'),
    path('autor/guardar', gestionautor.views.guardar_autor, name='guardar_autor'),
    re_path(r'^autor/editar/(?P<autor_id>\d+)/$', gestionautor.views.editar_autor, name='editar_autor'),
    re_path(r'^autor/infor/(?P<autor_id>\d+)/$', gestionautor.views.autor_detallado, name='autor_detallado'),
    re_path(r'^autor/eliminar/(?P<autor_id>\d+)/$', gestionautor.views.eliminar_autor, name='eliminar_autor'),

    #tutor
    path('tutor', gestiontutor.views.index, name='Tutor'),
    path('tutor/guardar', gestiontutor.views.guardar_tutor, name='guardar_tutor'),
    re_path(r'^tutor/editar/(?P<tutor_id>\d+)/$', gestiontutor.views.editar_tutor, name='editar_tutor'),
    re_path(r'^tutor/infor/(?P<tutor_id>\d+)/$', gestiontutor.views.tutor_detallado, name='tutor_detallado'),
    re_path(r'^tutor/eliminar/(?P<tutor_id>\d+)/$', gestiontutor.views.eliminar_tutor, name='eliminar_tutor'),

    #tipo de Proyecto
    path('tipoproyecto', gestiontipoproyecto.views.index, name='TipoProyecto'),
    path('tipoproyecto/guardar', gestiontipoproyecto.views.guardar_tipoproyecto, name='guardar_tipoproyecto'),
    re_path(r'^tipoproyecto/editar/(?P<tipoproyecto_id>\d+)/$', gestiontipoproyecto.views.editar_tipoproyecto, name='editar_tipoproyecto'),
    re_path(r'^tipoproyecto/eliminar/(?P<tipoproyecto_id>\d+)/$', gestiontipoproyecto.views.eliminar_tipoproyecto, name='eliminar_tipoproyecto'),

    #area de conocimiento
    path('areaconocimiento', gestionareaconocimiento.views.index, name='AreaConocimiento'),
    path('areaconocimiento/guardar', gestionareaconocimiento.views.guardar_areaconocimiento, name='guardar_areaconocimiento'),
    re_path(r'^areaconocimiento/editar/(?P<areaconocimiento_id>\d+)/$', gestionareaconocimiento.views.editar_areaconocimiento, name='editar_areaconocimiento'),
    re_path(r'^areaconocimiento/eliminar/(?P<areaconocimiento_id>\d+)/$', gestionareaconocimiento.views.eliminar_areaconocimiento, name='eliminar_areaconocimiento'),

    #carreras
    path('carrera', gestioncarrera.views.index, name='Carrera'),
    path('carrera/guardar', gestioncarrera.views.guardar_carrera, name='guardar_carrera'),
    re_path(r'^carrera/editar/(?P<carrera_id>\d+)/$', gestioncarrera.views.editar_carrera, name='editar_carrera'),
    re_path(r'^carrera/eliminar/(?P<carrera_id>\d+)/$', gestioncarrera.views.eliminar_carrera, name='eliminar_carrera'),

    #proyecto
    path('proyecto', gestionproyecto.views.index, name='Proyecto'),
    re_path(r'^proyecto/infor/(?P<proyecto_id>\d+)/$', gestionproyecto.views.proyecto_detalle, name='proyecto_detalle'),
    path('proyecto/guardar', gestionproyecto.views.guardar_proyecto, name='guardar_proyecto'),
    re_path(r'^proyecto/editar/(?P<proyecto_id>\d+)/$', gestionproyecto.views.editar_proyecto, name='editar_proyecto'),
    re_path(r'^proyecto/eliminar/(?P<proyecto_id>\d+)/$', gestionproyecto.views.eliminar_proyecto, name='eliminar_proyecto'),

]
#Archivos
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

