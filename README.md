# API de Gestión de Adopción y Cuidado de Gatos

## Descripción

Esta es una API desarrollada con FastAPI para gestionar el registro y la adopción de gatos en un refugio. Incluye funcionalidades para crear perfiles de gatos, registrar sus cuidados médicos y gestionar adoptantes.

## Instalación

1. Clona el repositorio:


2. Crea y activa un entorno virtual:

   ```bash
   python -m venv env
   source env/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Ejecuta el servidor:

   ```bash
   uvicorn main:app --reload
   ```

2. Accede a la documentación de la API en `http://127.0.0.1:8000/docs`.

## Estructura del Proyecto
