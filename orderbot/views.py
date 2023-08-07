import openai
from decouple import config
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse

from models.OpenAIModels import OpenAIModels

openai.api_key = config('OPENAI_TOKEN', default='DEFAULT')


@csrf_exempt
def recibir_mensaje(request):
    if request.method == 'POST':
        numero_de_telefono = request.POST.get('From')
        mensaje_recibido = request.POST.get('Body')

        respuesta_generada = obtener_respuesta_gpt(mensaje_recibido)

        response = MessagingResponse()
        response.message(respuesta_generada)

        return HttpResponse(str(response))
    else:
        return HttpResponse('Método no permitido', status=405)


def obtener_respuesta_gpt(mensaje):
    try:
        response = openai.ChatCompletion.create(
            model=OpenAIModels.TURBO,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": mensaje}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error: {e}")
        return "Lo siento, no puedo proporcionar una respuesta en este momento."
