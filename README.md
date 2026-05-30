Agente de Inteligencia Artificial para la detección de vulnerabilidades en código fuente utilizando arquitectura RAG (Retrieval-Augmented Generation).
Este proyecto combina embeddings, búsqueda vectorial y modelos de lenguaje para analizar código y detectar posibles problemas de seguridad.

Características:
- Análisis estático de código fuente
- Generación de embeddings con sentence-transformers
- Búsqueda eficiente 
- Integración con modelos de lenguaje (LLM)
- API REST con Flask
- Soporte para múltiples fuentes de conocimiento

Tecnologías utilizadas:
- Python 3.10
- Flask
- sentence-transformers
- PyTorch
- Transformers
- OpenAI API

Se requiere instalar las librerías con el comando:
- pip install -r requirements.txt

Y si da problemas es recomendable instalar por partes:
- pip install --upgrade pip
- pip install numpy==1.26.4
- pip install torch==2.2.2
- pip install -r requirements.txt

Para ejecutar:
- git clone ...
- docker build -t vucan-backend . 
- docker run -p 5000:5000 --env-file .env -v "RUTA_COMPLETA_DEL_PROYECTO_A_ANALIZAR" vucan-backend
