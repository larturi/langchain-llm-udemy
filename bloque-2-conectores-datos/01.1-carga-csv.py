import os

from langchain_openai import ChatOpenAI

from langchain_community.document_loaders import CSVLoader

from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Inicializar el modelo de chat
chat = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.7
)

base_dir = os.path.dirname(__file__)

# Carga datos CSV

# Cargamos el fichero CSV
csv_path = os.path.join(base_dir, "fuentes_datos", "datos_ventas_small.csv")
loader = CSVLoader(csv_path, csv_args={'delimiter': ';'})

# Creamos el objeto "data" con los datos desde el cargador "loader"
data = loader.load()

print(data[0].page_content)
print("\n" + "-"*50 + "\n")
print(data[1].page_content)
