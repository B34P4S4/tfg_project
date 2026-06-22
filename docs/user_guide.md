# Guía de usuario - VulcanAI

## 1. Introducción

**VulcanAI** es una herramienta de análisis de seguridad que utiliza inteligencia artificial agéntica multimodelo para identificar vulnerabilidades en código fuente de diferentes lenguajes de programación.

La plataforma combina modelos de IA especializados, técnicas de *Retrieval-Augmented Generation (RAG)* y una arquitectura basada en agentes para mejorar la precisión y la calidad de los resultados obtenidos en el análisis de seguridad del software.

Su objetivo es facilitar la detección temprana de vulnerabilidades y apoyar las tareas de auditoría de seguridad en entornos de desarrollo.

---

## 2. Funcionalidades principales

### 2.1 Análisis de código fuente

- Permite cargar archivos o proyectos de software para su análisis.
- Detecta vulnerabilidades de seguridad presentes en el código mediante modelos de IA.
- Soporta múltiples lenguajes de programación: Javascript, Typescript, PHP, Python, SQL.

---

### 2.2 Detección multimodelo

- Emplea varios modelos de inteligencia artificial de forma coordinada: Gemini y OpenAI.
- Fusiona los resultados obtenidos para mejorar la cobertura.
- Reduce errores de clasificación mediante consenso entre modelos.

---

### 2.3 Enriquecimiento mediante RAG

- Consulta una base de conocimiento especializada en ciberseguridad.
- Complementa el análisis con información contextual.
- Proporciona detalles sobre vulnerabilidades, impacto y mitigación.

---

### 2.4 Generación de informes

- Presenta los resultados de forma estructurada e intuitiva.
- Incluye:
  - Descripción de la vulnerabilidad.
  - Nivel de severidad.
  - Evidencias detectadas.
  - Recomendaciones de mitigación.

---

### 2.5 Gestión del histórico de análisis

- Almacena los análisis realizados en una base de datos.
- Permite consultar análisis anteriores.
- Facilita la reutilización y comparación de resultados.

---

### 2.6 Estadísticas y métricas

- Proporciona información agregada sobre los análisis realizados.
- Incluye:
  - Número total de vulnerabilidades detectadas.
  - Distribución por severidad.
  - Métricas de detección por lenguaje.

---

## 3. Flujo básico de uso

1. Acceder a la interfaz web de VulcanAI.
2. Introduce la ruta del proyecto que se desea analizar.
3. Iniciar el proceso de análisis.
4. Revisar los resultados generados por la plataforma.
5. Consultar las vulnerabilidades detectadas y recomendaciones asociadas.
6. Acceder al histórico o a las estadísticas para realizar seguimiento de los análisis.

---

## 4. Descripción general del sistema

VulcanAI implementa una arquitectura basada en agentes de inteligencia artificial que trabajan de forma coordinada para analizar código fuente desde distintas perspectivas.

El sistema combina:

- Modelos de lenguaje especializados.
- Un módulo de RAG para enriquecimiento contextual.
- Un sistema de fusión de resultados multimodelo.
- Persistencia de resultados para análisis histórico.
- Visualización de métricas y resultados.

---

## 5. Conclusión

Esta solución proporciona un mecanismo automatizado de apoyo a la auditoría de seguridad del software, facilitando la identificación temprana de vulnerabilidades y la adopción de medidas correctivas durante el ciclo de desarrollo.