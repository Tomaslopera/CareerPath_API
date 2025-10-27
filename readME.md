### Trabajo IA agentes 

El proyecto incluye la api donde se tiene acceso al modelo, correr con estos comandos en diferentes terminales   

uvicorn main:app --host 0.0.0.0 --port 8000  
ngrok 8000  

En la carpeta N8N se encuentran los dos JSON del proyecto  
- Rag: Workflow para vectorizar la info de maestrías 
- Agent: Agente de ia con acceso a todas las herramientas necesarias para recomedar 