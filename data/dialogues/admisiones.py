from PyPDF2 import PdfReader


def informacion(archivo):
    texto = ""
    with open(archivo, "rb") as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        for page in pdf_reader.pages:
            texto += page.extract_text()
    return texto
