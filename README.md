# [DJANGO](https://www.djangoproject.com)  
## Bot Whatsapp ISTE

### Módulos y versiones
| Módulo | Código | Descripción | 
| --- | --- | --- |
| python 3.10 | descargar | ['Ver documentación'](https://www.python.org/downloads) |
| django 4.2 | pip install django | Framework de desarrollo web de código abierto más utilizado |
| Openai 0.27 | pip install openai | ['Ver documentación'](https://pypi.org/project/openai/ ) |

### Instrucciones para iniciar el proyecto
1. Instalacion de Python en el host
    * Instalar segun el sistema operativo con la documentación del [Python](https://www.python.org/downloads/)
2. Instalación de recursos
    * Primero crear un entorno virtual 
    * `python -m venv venv`
    * Segundo activar el entonro virtual
    * `.\venv\Scripts\activate`
    * Para finalizar ejecutar la instrucción para instalar los paques necesarios
    * `pip install -r requirements.txt`
3. Levantar proyecto en el host
    * Para iniciar un proyecto ejecutar `python manage.py runserver 127.0.0.1:83`
    * Recordar que se trabajará con las versiones indicadas, por recomendación del framework hasta junio 2023
4. Configurar Twilio webhook WhatsApp
    * Primero crear una cuenta Twilio
    * Luego, conectar WhatsApp Personal o Empresarial a la zona de pruebas de Twilio [Ver configuración Sanbox](https://www.twilio.com/es-mx/docs/whatsapp/sandbox)
    * Por último, configurar una URL pública para envió de sms de salida [Ver configuración Sanbox Settings](https://www.twilio.com/es-mx/docs/whatsapp/sandbox)
5. Probar el bot
    * Abrir la aplicación de WhatsApp y enviar un mensaje al número de pruebas de Twilio configurada