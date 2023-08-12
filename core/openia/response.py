import openai
from decouple import config
from openai.error import OpenAIError

from data.dialogues.admisiones import informacion
from data.validate import question
from models.OpenAIModels import OpenAIModels


class Openia:
    def __init__(self, input_text=None):
        self.input_text = input_text
        self.api_key = config('OPENAI_TOKEN', default='DEFAULT')
        self.context = informacion('./data/dialogues/Brouchure.pdf')

    def response(self):
        print('sms=', self.input_text)
        try:
            if question(self.input_text, self.context):
                openai.api_key = self.api_key
                response = openai.ChatCompletion.create(
                    model=OpenAIModels.TURBO,
                    messages=[
                        {"role": "system", "content": self.context},
                        {"role": "user", "content": self.input_text}
                    ]
                )
                return response['choices'][0]['message']['content']
            else:
                return "Esta pregunta no parece estar relacionada con la información del ISTE."

        except OpenAIError as e:
            print(f"Error de  OpenAI: {e}")
            return "Lo siento, no puedo proporcionar una respuesta en este momento."
