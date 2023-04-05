from django.contrib import admin
from django.urls import path
from aplicacion.views import crear_tarea,crear_persona,crear_gato
from aplicacion.views import index,BuscarTarea,BuscarPersonas,BuscarGato

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('tareas/create', crear_tarea, name="tareas-create"),
    path('personas/create', crear_persona, name="personas-create"),
    path('gatos/create', crear_gato, name="gatos-create"),
    path('tareas/list', BuscarTarea.as_view(), name="tarea-list"),
    path('personas/list', BuscarPersonas.as_view(), name="personas-list"),
    path('gatos/list', BuscarGato.as_view(), name="gato-list"),
]
