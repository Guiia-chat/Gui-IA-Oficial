import mysql.connector
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

def get_database_connection():   
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="9532",
        database="Chat_bot_Guiia"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT pergunta,resposta FROM Chat_bot")
    dados = cursor.fetchall()
    cursor.close()
    connection.close()    
    
    contexto = "\n".join([
        f"Pergunta: {pergunta}\nResposta: {resposta}"
        for pergunta, resposta in dados
    ])
    return contexto


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=api_key,
    temperature=0.0
)

prompt_template = ChatPromptTemplate.from_messages([
    ("system",
     """
Você é um assistente útil. Use o contexto para responder detalhadamente:

Instruções:
1. Use o contexto abaixo para formular respostas explicativas.
2. Conecte informações relacionadas sempre que possível.
3. Evite respostas curtas; seja completo e claro.
4. Tome um tom natural e informativo.

Contexto:
{contexto}
     """
    ),
    ("human", "{pergunta_usuario}")
])

def gerar_resposta(pergunta_usuario):
    contexto = get_database_connection()
    chain = prompt_template | llm
    response = chain.invoke({
        "contexto": contexto,
        "pergunta_usuario": pergunta_usuario
    })
    return response.content
