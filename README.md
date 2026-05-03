Agente de Inteligencia Artificial para la detección de vulnerabilidades en código fuente utilizando arquitectura RAG (Retrieval-Augmented Generation).
Este proyecto combina embeddings, búsqueda vectorial con FAISS y modelos de lenguaje para analizar código y detectar posibles problemas de seguridad.

Características:
- Análisis estático de código fuente
- Generación de embeddings con sentence-transformers
- Búsqueda eficiente con FAISS
- Integración con modelos de lenguaje (LLM)
- API REST con Flask
- Soporte para múltiples fuentes de conocimiento

Tecnologías utilizadas
- Python 3.10
- Flask
- sentence-transformers
- FAISS
- PyTorch
- Transformers
- OpenAI API

Se requiere instalar las librerías con el comando:
pip install -r requirements.txt

Si da problemas es recomendable instalar por partes:
pip install --upgrade pip
pip install numpy==1.26.4
pip install torch==2.2.2
pip install -r requirements.txt
