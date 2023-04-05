from django.shortcuts import render
from django.views.generic import ListView
from aplicacion.models import Tarea,Persona,Gato
from aplicacion.forms import TareaForm,PersonaForm,GatoForm
from aplicacion.forms import BuscarTareasForm,BuscarPersonasForm,BuscarGatosForm

def index (request):
	return render(request, "aplicacion/index.html")

#Creacion
def crear_tarea(request):

	Tareas = Tarea.objects.all()
	total_tarea = len(Tareas)
	context = {
		"tarea" : Tareas,
		"total_tarea" : total_tarea,
		"form": TareaForm(),
	}
	return render (request, "aplicacion/tareas.html", context)

def cargar_tarea(request):
	f = TareaForm(request.POST)
	Tareas = Tarea.objects.all()
	total_tarea = len(Tareas)

	context = {
		"tarea":Tareas,
		"total_tarea":total_tarea,
		"form":f,
	}

	if f.is_valid():
		Tarea(nombre = f.data["nombre"], estado = f.data["estado"], creado_el = f.data["creado_el"]).save()
		return render(request, "aplicacion/tareas.html", context)
	
def crear_persona(request):

	personas = Persona.objects.all()
	total_personas = len(personas)
	context = {
		"personas" : personas,
		"total_personas" : total_personas,
		"form": PersonaForm(),
	}
	return render (request, "aplicacion/personas.html",context)

def cargar_persona(request):
	f = PersonaForm(request.POST)
	personas = Persona.objects.all()
	total_personas = len(personas)

	context = {
		"personas":personas,
		"total_personas":total_personas,
		"form":f,
	}

	if f.is_valid():
		Persona(nombre = f.data["nombre"], apellido = f.data["apellido"], fecha_nacimiento = f.data["fecha_nacimiento"]).save()
		return render(request, "aplicacion/personas.html", context)

def crear_gato(request):

	gatos = Gato.objects.all()
	total_gatos = len(gatos)
	context = {
		"gatos" : gatos,
		"total_gatos" : total_gatos,
		"form": GatoForm(),
	}
	return render (request, "aplicacion/gatos.html",context)

def cargar_gato(request):
	f = GatoForm(request.POST)
	gatos = Gato.objects.all()
	total_gatos = len(gatos)

	context = {
		"gatos":gatos,
		"total_gatos":total_gatos,
		"form":f,
	}

	if f.is_valid():
		Persona(nombre = f.data["nombre"], raza = f.data["raza"], edad = f.data["edad"]).save()
		return render(request, "aplicacion/gatos.html", context)

#Busqueda
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
