import mysql.connector
import google.generativeai as guiia
from dotenv import load_dotenv
import os
import json

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
    contexto = "\n".join([f"Pergunta: {pergunta}\nResposta: {resposta}" for pergunta, resposta in dados])
    return contexto



guiia.configure(api_key=api_key)
model = guiia.GenerativeModel("gemini-2.5-flash")
def gerar_resposta(pergunta_usuario):
    contexto = get_database_connection()
    
    prompt = f"""
    Você é um assistente útil. Use o seguinte contexto para responder às perguntas dos usuários.

    Contexto:
    {contexto}

    pergunta do usuário: {pergunta_usuario}
    Instruções:
   1. Use o contexto abaixo para formular respostas detalhadas e explicativas.
2. Sempre que possível, conecte informações relacionadas dentro do contexto.
3. Evite respostas curtas ou vagas; forneça explicações completas.
4. Mantenha um tom natural e informativo, como se estivesse explicando para um colega.

    """
    
    response = model.generate_content(prompt)
    return response.text
       


