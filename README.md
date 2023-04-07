# Entregable 3

## 1. Herencia de HTML
aplicacion -> templates -> aplicacion -> base.html
Ahi se encuentra el html 'padre'.
Arme el bloque y lo pegue en las herencias 'hijas'

## 2. Models
aplicacion -> models
3 clases de models: 'Tarea', 'Persona' y 'Gato'

## 3. Formulario para insertar a BD
web -> urls.py
URLS: 
Model Tarea: tareas/create
Model Persona: personas/create
Model Gato: gatos/create

## 4. Formulario de busqueda en BD
web -> urls.py
URLS: 
Model Tarea: tareas/list
Model Persona: personas/list
Model Gato: gatos/list


# ERRORES QUE NO PUDE SOLUCIONAR
Cuando se intenta cargar en los formularios para insertar a BD salta un error: ('django template source does not exist')
Busque en todos lados pero no encontre porque no funciona, ya que el template de tarea.html, persona.html y gato.html estan, a mi parecer, bien hechos
No detecte donde esta el error
Pero si vamos a '/admin/' vamos a poder agregar a la BD de los distintos models

