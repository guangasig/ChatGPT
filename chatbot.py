import openai
from decouple import config

from data.dialogues.dialog_uno import informacion
from data.validate import question
from models.OpenAIModels import OpenAIModels

openai.api_key = config('OPENAI_TOKEN', default='DEFAULT')


def obtener_respuesta(input_text, contexto):
    print('engine', OpenAIModels.TURBO)
    try:
        if question(input_text, contexto):
            response = openai.ChatCompletion.create(
                model=OpenAIModels.TURBO,
                messages=[
                    {"role": "system", "content": contexto},
                    {"role": "user", "content": input_text}
                ]
            )
            return response['choices'][0]['message']['content']
        else:
            return "Esta pregunta no parece estar relacionada con el contexto proporcionado."
    except Exception as e:
        print(f"Error: {e}")
        return "Lo siento, no puedo proporcionar una respuesta en este momento."


if __name__ == "__main__":

    context = informacion('./data/dialogues/Brochure_uno.pdf')
    print("¡Hola! Soy s-manuel. ¿Cómo puedo ayudarte?")

    while True:
        user_input = input("Tú: ")
        if user_input.lower() in ['exit', 'quit', 'salir']:
            print("Es un placer poder ayudarte. ¡Adiós!")
            break
        response = obtener_respuesta(user_input, context)
        print("Asistente:", response)
