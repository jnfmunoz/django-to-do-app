<p align="center">
  <img src="screenshots/django-logo.png" alt="Django Logo" width="200">
</p>

<div align="center">
		
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white) ![CSS](https://img.shields.io/badge/CSS-3-blue) ![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow) ![Python](https://img.shields.io/badge/Python-3.11.4-blue) ![Django](https://img.shields.io/badge/Django-4.2.16-green) ![SQLite3](https://img.shields.io/badge/SQLite-3.39-blue) ![django-bootstrap-v5](https://img.shields.io/badge/django--bootstrap--v5-1.0.11-blueviolet) ![sweetify](https://img.shields.io/badge/sweetify-2.3.1-yellow)   
 
</div> 

# Gestión de Tareas con Django
Una aplicación web para gestionar tareas personales, diseñada para simplificar la organización y la productividad.
## Tabla de Contenidos
- [Descripción](#descripción)
- [Características](#características)
- [Instalación](#instalación)
- [Uso](#uso)
- [Capturas de Pantalla](#capturas-de-pantalla)
- [Tecnologías](#tecnologías)

## Descripción
Esta aplicación permite a los usuarios crear, editar, buscar y eliminar tareas, estableciendo prioridades y plazos. Ideal para estudiantes, profesionales o cualquier persona que busque optimizar su tiempo.

## Características
- Crear, editar, buscar y eliminar tareas.
- Establecer prioridades y fecha límite.
- Filtro de búsqueda de tareas a través del n° de tarea, prioridad, fecha límite y estado.
- Interfaz moderna y responsiva con Bootstrap.
- Alertas y confirmaciones con Sweetify.

## Instalación
1. Clona este repositorio
	```bash
	git clone https://github.com/jnfmunoz/django-to-do-app.git
 	```

2. Navega al directorio del repositorio:
	``` bash
   	cd django-to-do-app
	```     
3. Crea un entorno virtual:
	```bash
	python -m venv venv-django-to-do-app
 	```    
4. Para activar tu entorno virtual:
	```bash
	.\venv-django-to-do-app\Scripts\activate
	```	
5. Instala las dependencias:
	```bash
	pip install -r requirements.txt
	```
6. Realiza las migraciones:
	```bash
   	python manage.py migrate
	```
7. Iniciar el servidor de desarrollo:
	```bash
	python manage.py runserver
	```
## Uso
1. Accede a `http://127.0.0.1:8000/`.
2. !Comienza a gestionar tus tareas!

## Capturas de Pantalla

#### Página de inicio
<p align="center">
  <img src="screenshots\index.PNG">
</p>

#### Listado de tareas
<p align="center">
  <img src="screenshots\task-list.PNG">
</p>

#### Detalle de tarea
<p align="center">
  <img src="screenshots\task-detail.PNG">
</p>

#### Nueva tarea
<p align="center">
  <img src="screenshots\new-task.PNG">
</p>

#### Actualizar tarea
<p align="center">
  <img src="screenshots\update-task.PNG">
</p>

## Filtros de búsqueda

### Búsqueda por id
<p align="center">
  <img src="screenshots\search-task-by-id.PNG">
</p>

### Búsqueda por prioridad
<p align="center">
  <img src="screenshots\search-task-by-priority.PNG">
</p>

### Búsqueda por fecha límite
<p align="center">
  <img src="screenshots\search-task-by-deadline.PNG">
</p>

### Búsqueda por estado
<p align="center">
  <img src="screenshots\search-task-by-status.PNG">
</p>

### Búsqueda por campos mixtos
<p align="center">
  <img src="screenshots\search-task-mixed.PNG">
</p>

### Buscar y no obtener resultados
<p align="center">
  <img src="screenshots\search-task-no-results.PNG">
</p>

## Mensajes de confirmación
### Antes de eliminar una tarea
<p align="center">
  <img src="screenshots\delete-task-confirm-message.PNG">
</p>

### Antes de agregar una nueva tarea
<p align="center">
  <img src="screenshots\new-task-confirm-message.PNG">
</p>

### Antes de actualizar una tarea
<p align="center">
  <img src="screenshots\update-task-confirm-message.PNG">
</p>

## Tecnologías
- **Django 4.2.16** - Framework web de Python.
- **Bootstrap 5** - Framework CSS para diseño responsivo.
- **Sweetify 2.3.1** - Librería para mostrar alertas personalizadas.
- **Python 3.11.4** - Lenguaje de programación utilizado para desarrollar el backend.
- **JavaScript** - Lenguaje para interactividad en el frontend.
- **HTML5** - Lenguaje de marcado utilizado para estructurar la página web.
- **SQLite3** - Base de datos utilizada (por defecto en Django).
