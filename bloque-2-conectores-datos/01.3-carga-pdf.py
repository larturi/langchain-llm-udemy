import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate

# Cargar variables de entorno
load_dotenv()

# Inicializar el modelo de chat
chat = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.7
)

# Definir path del PDF
base_dir = os.path.dirname(__file__)
pdf_path = os.path.join(base_dir, "fuentes_datos", "tecnologías_emergentes.pdf")

if not os.path.exists(pdf_path):
    raise FileNotFoundError(f"⚠️ El archivo no existe: {pdf_path}")

print("📄 Cargando y dividiendo el PDF...")

loader = PyPDFLoader(pdf_path)
pages = loader.load_and_split()

if not pages:
    raise ValueError("⚠️ El PDF está vacío o no se pudo leer correctamente.")

print(f"✅ PDF cargado con {len(pages)} página(s).\n")

print("📝 Contenido de la primera página:")
print("-" * 50)
print(pages[0].page_content)
print("-" * 50 + "\n")

# Plantilla para resumir contenido
human_template = "Necesito que hagas un resumen del siguiente texto:\n\n{contenido}"
human_prompt = HumanMessagePromptTemplate.from_template(human_template)
chat_prompt = ChatPromptTemplate.from_messages([human_prompt])

# Resumir la primera página
print("🤖 Resumen de la primera página:\n")
solicitud_pagina1 = chat_prompt.format_prompt(contenido=pages[0].page_content).to_messages()
respuesta_pagina1 = chat.invoke(solicitud_pagina1)
print(respuesta_pagina1.content)
print("\n" + "=" * 60 + "\n")

# Concatenar y resumir todo el documento
print("📚 Generando resumen del documento completo...\n")

documento_completo = "\n".join([page.page_content for page in pages])

solicitud_completa = chat_prompt.format_prompt(contenido=documento_completo).to_messages()
respuesta_completa = chat.invoke(solicitud_completa)

print("🧾 Resumen del documento completo:")
print("-" * 50)
print(respuesta_completa.content)
print("-" * 50)
