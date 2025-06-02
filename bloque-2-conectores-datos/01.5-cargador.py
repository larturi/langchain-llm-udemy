
import os
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Inicializar el modelo de chat
chat = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0
)

print("Directorio actual:", os.getcwd())

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "fuentes_datos", "historia_espania.txt")

with open(file_path, encoding="utf8") as file:
    texto_completo = file.read()

    print("Cantidad de caracteres del archvivo:")
    print(len(texto_completo))

    print("Número de palabras")
    len(texto_completo.split())

# Indicamos que divida cuando se encuentra 1 salto de línea y trate de hacer fragmentos
# de 1000 caracteres
text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000)

# Creamos documentos gracias al transformador
texts = text_splitter.create_documents([texto_completo])

# Verificamos el tipo del objeto obtenido
print(type(texts))
print('\n')

# Verificamos el tipo de cada elemento
print(type(texts[0]))
print('\n')
print(texts[0])
print(texts[1])
