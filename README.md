# PoC LangChain con OpenAI

Este es un proyecto de prueba de concepto (PoC) que utiliza LangChain con el modelo GPT-3.5 de OpenAI.

## Requisitos

- Python 3.11.12
- Una API key de OpenAI

## Instalación

1. Clona este repositorio
2. Crea un archivo `.env` en la raíz del proyecto y añade tu API key de OpenAI
3. Instalar la version de python con pyenv: `pyenv install 3.11.12`
4. Elegir esa versión para este proyecto `pyenv local 3.11.12`
5. Crear el entorno virtual: `python -m venv venv`
6. Activar el entorno: `source venv/bin/activate`
7. Pip upgrade `pip install --upgrade pip`
8. Instalar dependencias: `pip install -r requirements.txt`

## Uso

Para ejecutar los ejemplos:

```bash
# Ejemplo 1: Interacción básica con LangChain y LLM
python3 bloque-1-model-io/01-interaccion-langchain-llm.py

# Ejemplo 2: Plantillas de prompts
python3 bloque-1-model-io/02-plantillas-de-prompts.py

```

## Estructura del Proyecto

- `main.py`: Contiene el código principal con un ejemplo básico de uso de LangChain
- `requirements.txt`: Lista de dependencias del proyecto
- `.env`: Archivo para las variables de entorno (no incluido en el repositorio)

## Características

- Uso de LangChain con GPT-3.5
- Implementación de prompts templates
- Manejo de variables de entorno
- Ejemplo básico de cadena de LLM

## Notas

- Asegúrate de mantener tu API key segura y nunca la compartas
- El archivo `.env` debe estar en el `.gitignore` para no exponer tus credenciales 