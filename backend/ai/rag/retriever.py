from backend.ai.rag.knowledge_base import KNOWLEDGE_BASE
from backend.ai.rag.embeddings import embeber_texto
from backend.ai.rag.init_rag import vector_store

# obtenemos contexto del RAG automáticamente
def recuperar_contexto(chunk, vector_store):
    query_vector = embeber_texto(chunk)    
    return vector_store.search(query_vector, k=2)

# obtenemos el contexto manualmente
def recuperar_contexto_manual(code):
    context = []

    # extraemos el texto
    if isinstance(code, dict):
        code = code.get("code", "")

    # unificamos pasandolo todo a minusculas
    code_lower = code.lower()

    # A01: Broken Access Control
    if (
        "user_id" in code_lower or
        "account_id" in code_lower or
        "getuser" in code_lower or
        "request.get" in code_lower or
        "params" in code_lower
    ):
        context.append(KNOWLEDGE_BASE[0]) 
    
    # A04: Cryptographic Failures
    if (
        "md5" in code_lower or
        "sha1" in code_lower or
        "password" in code_lower or
        "hash" in code_lower or
        "encrypt" in code_lower
    ):
        context.append(KNOWLEDGE_BASE[1]) 

    # A05: Injection (SQL, command, etc.)
    if (
        "select" in code_lower or
        "insert" in code_lower or
        "update" in code_lower or
        "delete" in code_lower or
        "query" in code_lower or
        "execute" in code_lower
    ):
        context.append(KNOWLEDGE_BASE[2])

    # A07: Authentication Failures
    if (
        "login" in code_lower or
        "signin" in code_lower or
        "auth" in code_lower or
        "password" in code_lower
    ):
        context.append(KNOWLEDGE_BASE[3])  

    return context
