import PyPDF2


def informacion(archivo):
    texto = ""
    with open(archivo, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            texto += page.extractText()
    return texto
