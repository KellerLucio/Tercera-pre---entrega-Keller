from django import forms 

#Formularios
class TareaForm(forms.Form):
	nombre = forms.CharField(max_length=100)
	estado = forms.CharField(max_length=100)
	
class PersonaForm(forms.Form):
	nombre = forms.CharField(max_length=100)
	apellido = forms.CharField(max_length=100)
	fecha_nacimiento = forms.DateField()

class GatoForm(forms.Form):
	nombre = forms.CharField(max_length=100)
	raza = forms.CharField(max_length=100)
	edad = forms.CharField(max_length=100)     

#Form Para busqueda
class BuscarTareasForm(forms.Form):
	criterio_nombre_tarea = forms.CharField(max_length=100)
	
class BuscarPersonasForm(forms.Form):
	criterio_nombre_persona = forms.CharField(max_length=100)

class BuscarGatosForm(forms.Form):
	criterio_nombre_gato = forms.CharField(max_length=100)
	