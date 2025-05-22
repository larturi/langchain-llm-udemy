import os

from langchain_openai import ChatOpenAI

from langchain_community.document_loaders import BSHTMLLoader

from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Inicializar el modelo de chat
chat = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.7
)

base_dir = os.path.dirname(__file__)

# Carga datos HTML
print("Cargando datos HTML")

html_path = os.path.join(base_dir, "fuentes_datos", "ejemplo_web.html")
loader = BSHTMLLoader(html_path)

data = loader.load()

print(data[0].page_content)