# inicializamos el RAG

from core.rag.embeddings import embeber_texto
from core.rag.vector_store import VectorStore
from core.rag.knowledge_base import KNOWLEDGE_BASE

vector_store = None

def init_vector_store():
    vector_store = VectorStore(dim=384)

    for item in KNOWLEDGE_BASE:
        text = f"""
        Tipo: {item['1.2']}
        Descripción: {item['1.3']}
        CWE: CWE-{item['3.4']}
        Categoría OWASP: A{item['3.1']}
        """
        vector = embeber_texto(text)
        vector_store.add(vector, item)

    return vector_store


