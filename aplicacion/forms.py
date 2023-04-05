from django import forms 

class BuscarTareasForm(forms.Form):
	criterio_nombre_tarea = forms.CharField(max_length=100)
	
class BuscarPersonasForm(forms.Form):
	criterio_nombre_persona = forms.CharField(max_length=100)

class BuscarGatosForm(forms.Form):
	criterio_nombre_gato = forms.CharField(max_length=100)
	