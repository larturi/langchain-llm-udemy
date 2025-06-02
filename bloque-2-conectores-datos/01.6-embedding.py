
import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import CSVLoader

# Cargar variables de entorno
load_dotenv()

# Inicializar el modelo de chat
chat = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0
)

embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"))

texto = "Esto es un texto enviado a OpenAI para ser incrustado en un vector n-dimensional"

embedded_text = embeddings.embed_query(texto)

print("Texto incrustado:", embedded_text)
print("Dimensiones del vector:", len(embedded_text))

# Cargamos el fichero CSV
base_dir = os.path.dirname(__file__)
csv_path = os.path.join(base_dir, "fuentes_datos", "datos_ventas_small.csv")
loader = CSVLoader(csv_path, csv_args={'delimiter': ';'})

data = loader.load()

# Creamos una comprensión de listas concatenando el campo "page_content"
# de todos los documentos existentes en la lista "data"
[elemento.page_content for elemento in data]

embedded_docs = embeddings.embed_documents(
    [elemento.page_content for elemento in data])

# Verificamos cuántos vectores a creado (1 por cada registro del fichero CSV con datos)
print("Número de vectores creados:", len(embedded_docs))
len(embedded_docs)

# Vemos un ejemplo del vector creado para el primer registro
print("Vector del primer registro:", embedded_docs[0])
embedded_docs[1]
