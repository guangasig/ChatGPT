# Bot Whatsapp
![Badge en Desarollo](https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green)

### Módulos y versiones
| Módulo | Código | Descripción | 
| --- | --- | --- |
| python 3.10 | descargar | ['Documentación'](https://www.python.org/downloads) |
| django 4.2 | pip install django | ['Documentación'](https://www.djangoproject.com/) |
| Openai 0.27 | pip install openai | ['Documentación'](https://pypi.org/project/openai/) |
| twilio 8.5.0 | pip install twilio | ['Documentación'](https://pypi.org/project/twilio/) |

### Estructura del proyecto
- [core](./core): Archivos principales de Django
  - [utils](./core/utils): Herramientas validaciones y mas
  - [openia](./core/openia): Script's response.py en base a modelos de Openia

- [data](./data): Acceso a bases de datos
  - [utils](./data/dialgues): Script's .py para acceder a información para configurar del context de los modelos de Openia

- [models](./models): Modelos Openia
  - [models.py](./models/models.py): Class de modelos de Openia

- [results](./models): Registros de mensajes del usuario y respuestas de Openia
  - [result.py](./models/result.py): Script's para registrar las preguntas y respuestas dependiendo del modelo de Openia

- [chatbot.py](./chatbot.py): Codificación para hacer pruebas

- [manage.py](./chatbot.py): Script para ejecutar tareas relacionadas con el proyecto Django

- [README.md](./README.md): ¡Estás aquí!