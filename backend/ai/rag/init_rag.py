# inicializamos el RAG
from backend.ai.rag.embeddings import embeber_texto
from backend.ai.rag.vector_store import VectorStore
from backend.ai.rag.knowledge_base import KNOWLEDGE_BASE

vector_store = None

def init_vector_store():
    vector_store = VectorStore(dim=384)

    for item in KNOWLEDGE_BASE:
        text = f"""
        Tipo: {item['1.2']}
        Descripción: {item['1.3']}
        CWE: CWE-{item['3.4']}
        OWASP Top 10: A{item['3.1']}:2025
        """
        vector = embeber_texto(text)
        vector_store.add(vector, item)

    return vector_store


