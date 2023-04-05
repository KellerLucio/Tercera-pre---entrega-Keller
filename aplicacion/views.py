from django.shortcuts import render
from django.views.generic import ListView
from aplicacion.models import Tarea,Persona,Gato
from aplicacion.forms import BuscarTareasForm,BuscarPersonasForm,BuscarGatosForm

def index (request):
	return render(request, "aplicacion/index.html")

class BuscarTarea(ListView):
	model = Tarea
	context_object_name = "tareas"

	def get_queryset(self):
		f = BuscarTareasForm(self.request.GET)
		if f.is_valid():
			return Tarea.objects.filter(nombre_icontains=f.data ["criterio_nombre"]) . all() 

		return Tarea.objects.none()

class BuscarPersonas(ListView):
	model = Persona
	context_object_name = "personas"
	
	def get_queryset(self):
		f = BuscarPersonasForm(self.request.GET)
		if f.is_valid():
			return Persona.objects.filter(nombre_icontains=f.data ["criterio_nombre"]) . all()  #Es para encontrar coincidencias el icontains

		return Persona.objects.none()

class BuscarGato(ListView):
	model = Gato
	context_object_name = "gatos"

	def get_queryset(self):
		f = BuscarGatosForm(self.request.GET)
		if f.is_valid():
			return Gato.objects.filter(nombre_icontains=f.data ["criterio_nombre"]) . all()  #Es para encontrar coincidencias el icontains

		return Gato.objects.none()
