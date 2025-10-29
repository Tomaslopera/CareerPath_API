# n8n Career Path - Agent

Este repositorio contiene dos flujos de **n8n** que implementan un **agente académico inteligente** capaz de recomendar programas de maestría para estudiantes de ingeniería de sistemas o áreas tecnológicas, combinando técnicas de **RAG (Retrieval-Augmented Generation)** y **modelos de lenguaje**.

## Autores
> Tomás Lopera

> Pedro Sierra

## Descripción General

El sistema está compuesto por dos flujos principales:

1. **Agent** → Agente conversacional inteligente que interactúa con el usuario, analiza sus intereses y genera recomendaciones personalizadas.
2. **RAG** → Flujo de ingestión y vectorización de documentos de maestrías desde Google Drive hacia un índice en Pinecone, utilizado por el agente para enriquecer las recomendaciones.

## Tecnologías utilizadas

- **n8n** – Orquestador del flujo de datos e integración de herramientas de IA.  
- **FastAPI** – API backend para procesar solicitudes y servir predicciones.  
- **Hugging Face (BERT)** – Modelo preentrenado para predecir programas de maestría relevantes según el perfil del usuario.  
- **Pinecone** – Vector database utilizada como base de conocimiento semántica.  
- **OpenAI Embeddings** – Para generar representaciones vectoriales de los textos de maestrías.  
- **Google Drive API** – Fuente de datos para cargar y actualizar la información de los programas académicos.

## Flujo 1: AI Agent (Asesor Académico)

Este flujo gestiona la conversación con el usuario, recopila sus intereses y genera una recomendación personalizada.
Integra:

- Un modelo de chat (OpenAI) para la interacción.
- Una memoria de contexto para mantener coherencia.
- Un HTTP Request Tool conectado a la API de FastAPI.
- Una VectorStore Pinecone para enriquecer las recomendaciones con información detallada.

## Flujo 2: RAG Loader (Carga y Embeddings)

Este flujo se ejecuta automáticamente cuando se carga un nuevo archivo con información de programas en Google Drive.
Procesa los documentos en los siguientes pasos:

- Trigger de Google Drive (nuevo archivo detectado).
- Descarga del documento.
- División del texto en fragmentos (Text Splitter).
- Generación de embeddings (OpenAI).
- Inserción en Pinecone como base de conocimiento vectorial.

## API del modelo

El modelo BERT se aloja mediante FastAPI, expuesto localmente o vía ngrok.
Se encarga de recibir el resumen de preferencias del usuario y devolver las tres maestrías más adecuadas.

> [Modelo Utilizado](https://huggingface.co/fazni/distilbert-base-uncased-career-path-prediction)

**Endpoint**
```bash
POST /predict
{
  "text": "Me gusta la ciberseguridad y el análisis de datos"
}

```
