import openai
from decouple import config
from openai.error import OpenAIError

from models.OpenAIModels import OpenAIModels


class Openia:
    def __init__(self, input_text=None):
        self.input_text = input_text
        self.api_key = config('OPENAI_TOKEN', default='DEFAULT')

    def response(self):
        print('input_text=', self.input_text)
        print('self.input_text=', self.input_text)
        try:
            openai.api_key = self.api_key
            response = openai.ChatCompletion.create(
                model=OpenAIModels.TURBO,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": self.input_text}
                ]
            )
            return response['choices'][0]['message']['content']
        except OpenAIError as e:
            print(f"Error de  OpenAI: {e}")
            return "Lo siento, no puedo proporcionar una respuesta en este momento."
