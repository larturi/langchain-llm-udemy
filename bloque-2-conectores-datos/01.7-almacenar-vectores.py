
import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader

from langchain_community.vectorstores import SKLearnVectorStore

# Cargar variables de entorno
load_dotenv()

# Inicializar el modelo de chat
chat = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0
)

# Abre el archivo de texto y carga su contenido
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "fuentes_datos", "historia_espania.txt")
loader = TextLoader(file_path, encoding="utf8")
documents = loader.load()

# Dividir en chunks
text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=500)  # Otro método de split basándose en tokens
docs = text_splitter.split_documents(documents)

# Inicializar las embeddings de OpenAI
funcion_embedding = OpenAIEmbeddings(
    openai_api_key=os.environ.get("OPENAI_API_KEY"))

# Alternativa con SKLearn Vector Store
# ruta donde se guardará la BBDD vectorizada
persist_path = "./ejemplosk_embedding_db"

# Creamos la BBDD de vectores a partir de los documentos y la función embeddings
vector_store = SKLearnVectorStore.from_documents(
    documents=docs,
    embedding=funcion_embedding,
    persist_path=persist_path,
    serializer="parquet",  # el serializador o formato de la BD lo definimos como parquet
)

# Fuerza a guardar los nuevos embeddings en el disco
vector_store.persist()

# Creamos un nuevo documento que será nuestra "consulta" para buscar el
# de mayor similitud en nuestra Base de Datos de Vectores y devolverlo
consulta = "dame información de la Primera Guerra Mundial"
docs = vector_store.similarity_search(consulta)
print(docs[0].page_content)

# Cargar la BD de vectores (uso posterior una vez tenemos creada ya la BD)
vector_store_connection = SKLearnVectorStore(
    embedding=funcion_embedding, persist_path=persist_path, serializer="parquet"
)
print("Una instancia de la BBDD de vectores se ha cargado desde ", persist_path)

nueva_consulta = "¿Qué paso en el siglo de Oro?"
docs = vector_store_connection.similarity_search(nueva_consulta)
print(docs[0].page_content)
