from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
from .views import exit
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('contacto', views.contacto, name='contacto'),
    path('login', views.login, name='login'),
    path('logout/', exit, name='exit'),
    path('inventario', views.inventbomber, name='inventario'), 
    path('crear', views.crear, name='crear'), 
    path('listado', views.listado, name='listado'),
    path('editar', views.editar, name='editar'), 
    path('eliminar/<int:id>', views.eliminar, name='eliminar'), 
    path('editar/<int:id>', views.editar, name='editar'), 
    path('mensaje', views.mensaje, name='mensaje'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)