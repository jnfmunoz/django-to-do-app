<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/7/75/Django_logo.svg" alt="Django Logo" width="200">
</p>
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white) 
![CSS](https://img.shields.io/badge/CSS-3-blue) ![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow) ![Python](https://img.shields.io/badge/Python-3.11.4-blue) ![Django](https://img.shields.io/badge/Django-4.2.16-green) ![SQLite3](https://img.shields.io/badge/SQLite-3.39-blue) ![django-bootstrap-v5](https://img.shields.io/badge/django--bootstrap--v5-1.0.11-blueviolet) ![sweetify](https://img.shields.io/badge/sweetify-2.3.1-yellow)   

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
	git clone 	https://github.com/jnfmunoz/django-to-do-app.git

2. Navega al directorio del repositorio:
    cd django-to-do-app

3. Crea y activa un entorno virtual:
    Para crear un entorno virtual:
        python -m venv venv-django-to-do-app
    Para activar tu entorno virtual:
        .\venv-django-to-do-app\Scripts\activate

4. Instala las dependencias:
        pip install -r requirements.txt

5. Realiza las migraciones:
        python manage.py migrate

6. Iniciar el servidor de desarrollo:
        python manage.py runserver

## Uso
1. Accede a `http://127.0.0.1:8000/`.
2. !Comienza a gestionar tus tareas!

## Capturas de Pantalla

#### Página de inicio
![Página de inicio](screenshots/index.PNG)

#### Listado de tareas
![Listado de tareas](screenshots/task-list.PNG)

#### Detalle de tarea
![Detalle Tarea](screenshots/task-detail.PNG)

#### Nueva tarea
![Nueva Tarea](screenshots/new-task.PNG)

#### Actualizar tarea
![Actualizar Tarea](screenshots/update-task.PNG)

## Filtros de búsqueda

### Búsqueda por id
![Buscar por id](screenshots/search-task-by-id.PNG)

### Búsqueda por prioridad
![Buscar por prioridad](screenshots/search-task-by-priority.PNG)

### Búsqueda por fecha límite
![Buscar por fecha límite](screenshots/search-task-by-deadline.PNG)

### Búsqueda por estado
![Buscar por estado](screenshots/search-task-by-status.PNG)

### Búsqueda por campos mixtos
![Buscar por múltiples filtros](screenshots/search-task-mixed.PNG)

### Buscar y no obtener resultados
![Sin resultados](screenshots/search-task-no-results.PNG)

## Mensajes de confirmación
### Antes de eliminar una tarea
[!Confirmar antes de eliminar una tarea](screenshots/delete-task-confirm-message.PNG)

### Antes de agregar una nueva tarea
[!Confirmar y agregar una tarea](screenshots/new-task-confirm-message.PNG)

### Antes de actualizar una tarea
![Confirmar y actualizar una tarea](screenshots/update-task-confirm-message.PNG)

## Tecnologías
- **Django 4.2.16** - Framework web de Python.
- **Bootstrap 5** - Framework CSS para diseño responsivo.
- **Sweetify 2.3.1** - Librería para mostrar alertas personalizadas.
- **Python 3.11.4** - Lenguaje de programación utilizado para desarrollar el backend.
- **JavaScript** - Lenguaje para interactividad en el frontend.
- **HTML5** - Lenguaje de marcado utilizado para estructurar la página web.
- **SQLite3** - Base de datos utilizada (por defecto en Django).