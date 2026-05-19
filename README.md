# CRUD API built with Django REST Framework

[Go to the task of Django](#2-solución-tarea-1)

A complete CRUD API developed with Django REST Framework (DRF). Supports all standard operations for resource management.

## 🚀 Features

- Full CRUD operations (Create, Read, Update, Delete)
- RESTful API endpoints
- JSON request/response format
- Django Admin interface
- SQLite database (configurable to PostgreSQL/MySQL)
- CORS support (optional)

## 📋 Requirements

- Python 3.8 or higher
- pip package manager

## 🛠️ Installation

### 1. Clone the repository

```bash
- git clone https://github.com/Bootcamp-IA-MAD-P7/tarea-1-abel
- cd tarea-1-abel
- python -m venv .venv
- source venv/bin/activate  # On Windows: venv\Scripts\activate
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver
```

___

## 2. Solución tarea 1

### 1. ¿Qué es un CRUD y cuál es su propósito?
Es la forma básica de gestionar datos: Crear, Leer, Actualizar, Eliminar. Su propósito es manejar información de forma sencilla.
Ejemplo: Una agenda de contactos donde agregas, ves, editas o borras un número.

### 2. Patrones de arquitectura
Son plantillas para organizar el código de una aplicación.

- MVC (Modelo–Vista–Controlador): Separa los datos (Modelo), la pantalla (Vista) y la lógica que los une (Controlador).

- MVT (Modelo–Vista–Template): Similar, pero la Vista en Django responde a peticiones y el Template es la plantilla HTML.

- Diferencias: En MVC el Controlador maneja la entrada del usuario; en MVT la Vista hace esa función.

- ¿Cuál usa Django? MVT (Modelo–Vista–Template).

### 3. Estructura de un proyecto en Django

- Modelos: Definen cómo son los datos (ej: una tarea tiene título y fecha).

- Vistas: Reciben peticiones y deciden qué responder.

- Templates: Son las páginas HTML que ve el usuario.

- URLs: Asocian direcciones web con vistas (ej: /tareas/ lleva a la lista de tareas).

- ¿Para qué se usa %% en templates?
No es %%, es {% %} para instrucciones (ej: {% if %}) y {{ }} para mostrar variables.
Ejemplo: {{ nombre }} muestra el nombre del usuario.

### 4. Flujo de datos desde un formulario HTML a la BD

1.Usuario envía el formulario → 2. Vista recibe los datos → 3. Django valida y limpia la información → 4. Se guarda en la base de datos mediante el modelo.

### 5. Herramientas de Django para un CRUD

- startapp – Crea una nueva aplicación dentro del proyecto.

- makemigrations – Prepara los cambios en los modelos.

- migrate – Aplica esos cambios a la base de datos.

- runserver – Levanta el servidor web para probar.

- ModelForm – Crea formularios automáticos desde un modelo.

- admin – Panel de gestión listo para usar.

### 6. ¿Cómo funciona el Admin de Django?
Es un sitio web ya hecho donde puedes ver, agregar, editar y borrar datos de tus modelos sin escribir código extra. Solo lo registras y ya tienes un panel de control.

### 7. ¿Django usa arquitectura REST?
No directamente. Django es para páginas web tradicionales.
Django Rest Framework (DRF) es una librería externa que añade REST a Django, permitiendo crear APIs para aplicaciones móviles o de una sola página (SPA).