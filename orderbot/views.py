from decouple import config
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse

from core.openia.response import Openia


@csrf_exempt
def whatsapp(request):
    if request.method == 'POST':
        numero_de_telefono = request.POST.get('From')
        mensaje_recibido = request.POST.get('Body')

        try:

            respuesta_generada = Openia(input_text=mensaje_recibido).response()
            response = MessagingResponse()
            response.message(respuesta_generada)
            return HttpResponse(str(response))

        except Exception as e:
            print(f"Error: {e}")
            return HttpResponse('Error interno OpenIA', status=500)
    else:
        return HttpResponse('Método no permitido', status=405)
