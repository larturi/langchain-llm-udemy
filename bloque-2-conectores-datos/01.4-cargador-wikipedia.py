from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate

# pip install wikipedia en una terminal
from langchain_community.document_loaders import WikipediaLoader

# Cargar variables de entorno
load_dotenv()

# Inicializar el modelo de chat
chat = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0
)


def responder_wikipedia(persona, pregunta_arg):
    # Obtener artículo de wikipedia
    # parámetros posibles en: https://python.langchain.com/v0.2/docs/integrations/document_loaders/wikipedia/
    docs = WikipediaLoader(query=persona, lang="es", load_max_docs=10)
    contexto_extra = "\n\n".join([doc.page_content for doc in docs.load()])

    # Pregunta de usuario
    human_prompt = HumanMessagePromptTemplate.from_template(
        'Responde a esta pregunta\n{pregunta}, aquí tienes contenido extra:\n{contenido}')

    # Construir prompt
    chat_prompt = ChatPromptTemplate.from_messages([human_prompt])

    # Resultado
    result = chat.invoke(chat_prompt.format_prompt(
        pregunta=pregunta_arg, contenido=contexto_extra
    ).to_messages())

    print(result.content)


responder_wikipedia("Lionel Messi", "¿Cuándo nació?")
