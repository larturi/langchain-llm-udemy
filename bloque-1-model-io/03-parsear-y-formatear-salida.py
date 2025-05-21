from langchain_openai import ChatOpenAI
from langchain.output_parsers import CommaSeparatedListOutputParser, DatetimeOutputParser
from langchain_core.messages import HumanMessage
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate

from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Inicializar el modelo de chat
chat = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.7
)

##### Parsear una lista de elementos separados por coma #####
output_parser = CommaSeparatedListOutputParser()

# Nos devuelve las instrucciones que va a pasar al LLM en función del parseador concreto
format_instructions = output_parser.get_format_instructions() 

# Creamos la plantilla de usuario (human_template) con la concatenación de la variable "request" 
# (la solicitud) y la variable "format_instructions" con las instrucciones adicionales 
# que le pasaremos al LLM
human_template = '{request}\n{format_instructions}'
human_prompt = HumanMessagePromptTemplate.from_template(human_template)

#Creamos el prompt y le damos formato a las variables
chat_prompt = ChatPromptTemplate.from_messages([human_prompt])

# Las instrucciones son las que proporciona el propio parseador
chat_prompt.format_prompt(
    request="dime 5 características de los coches americanos", 
    format_instructions = output_parser.get_format_instructions()
) 

# Transformamos el objeto prompt a una lista de mensajes y lo guardamos en "solicitud_completa" 
# que es lo que pasaremos al LLM finalmente
solicitud_completa = chat_prompt.format_prompt(
    request="dime 5 características de los coches americanos",
    format_instructions = output_parser.get_format_instructions()
).to_messages()

result = chat.invoke(solicitud_completa)

print(result.content)

output_parser.parse(result.content)


##### Parsear formatos de fecha #####

output_parser = DatetimeOutputParser()
print(output_parser.get_format_instructions())

template_text = "{request}\n{format_instructions}"
human_prompt=HumanMessagePromptTemplate.from_template(template_text)

chat_prompt = ChatPromptTemplate.from_messages([human_prompt])

print(chat_prompt.format(
    request="¿Cuándo es el día de la declaración de independencia de los EEUU?",
    format_instructions=output_parser.get_format_instructions()
))

solicitud_completa = chat_prompt.format_prompt(
    request="¿Cuándo es el día de la declaración de independencia de los EEUU?",
    format_instructions=output_parser.get_format_instructions()
).to_messages()

result = chat.invoke(solicitud_completa)

result.content

output_parser.parse(result.content)