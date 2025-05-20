from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Inicializar el modelo de chat
chat = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.7
)


def ejemplo_basico():
    resultado = chat.invoke([
        HumanMessage(content="¿Puedes decirme dónde se encuentra Madrid?")
    ])
    print("Respuesta simple:")
    print(resultado.content)
    print("\n" + "-"*50 + "\n")


def ejemplo_con_system_message():
    resultado = chat.invoke([
        SystemMessage(
            content="Eres un historiador experto en ciudades españolas"),
        HumanMessage(content="¿Puedes decirme dónde se encuentra Madrid?")
    ])
    print("Respuesta con personalidad de historiador:")
    print(resultado.content)
    print("\n" + "-"*50 + "\n")


def ejemplo_multiple_respuestas():
    resultado = chat.batch([
        [
            SystemMessage(
                content="Eres un historiador experto en ciudades españolas"),
            HumanMessage(content="¿Puedes decirme dónde se encuentra Madrid?")
        ],
        [
            SystemMessage(content="Eres un guía turístico entusiasta"),
            HumanMessage(content="¿Puedes decirme dónde se encuentra Madrid?")
        ]
    ])
    print("Respuesta del historiador:")
    print(resultado[0].content)
    print("\nRespuesta del guía turístico:")
    print(resultado[1].content)


if __name__ == "__main__":
    print("Ejemplo 1: Respuesta básica")
    ejemplo_basico()

    print("Ejemplo 2: Respuesta con personalidad")
    ejemplo_con_system_message()

    print("Ejemplo 3: Múltiples respuestas con diferentes personalidades")
    ejemplo_multiple_respuestas()
