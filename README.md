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

Requisitos previos:
- Docker
- Docker Compose
- Claves de API (OpenAI / Gemini)

Configuración del entorno:
- Crear un archivo `.env` en la raíz del proyecto con la forma:
    OPENAI_API_KEY=tu_clave
    GEMINI_API_KEY=tu_clave

Para ejecutar:
- git clone https://github.com/B34P4S4/tfg_project
- cd vulcanai
- docker compose up --build
- http://localhost:3000 (o el puerto configurado)

Guía de usuario se encuentra en:
- docs/user_guide.md