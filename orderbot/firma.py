import base64
import hashlib
import hmac

from django.http import HttpResponse


@csrf_exempt
def whatsapp(request):
    if request.method == 'POST':
        # Token Twilio
        twilio_token = ''

        # Obtener la firma proporcionada por Twilio
        twilio = request.META.get('HTTP_X_TWILIO_SIGNATURE', '')

        # Request.body o Request.POST
        request_body = request.body.decode('utf-8')

        # Validar firma
        calculated_signature = base64.b64encode(
            hmac.new(twilio_token.encode('utf-8'),
                     request_body.encode('utf-8'), hashlib.sha1).digest()
        ).decode('utf-8')

        if twilio == calculated_signature:
            return True
        else:
            return HttpResponse('Firma no válida', status=403)
    else:
        return HttpResponse('Método no permitido', status=405)
