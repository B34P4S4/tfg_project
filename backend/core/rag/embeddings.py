# transformamos los datos en numeros con la libreria sentencetransformer

from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def embeber_texto(text):
    return model.encode([text])[0]
