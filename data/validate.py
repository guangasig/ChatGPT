
def question(pregunta, contexto):
    palabras_contexto = contexto.lower().split()
    return any(palabra in pregunta.lower() for palabra in palabras_contexto)

# Funcion trabajando


def answer(pregunta, contexto):
    palabras_contexto = contexto.lower().split()
    return any(palabra in pregunta.lower() for palabra in palabras_contexto)
