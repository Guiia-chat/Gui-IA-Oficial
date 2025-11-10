
from testefask import app
from flask import render_template, request, jsonify
from fine_tuning import gerar_resposta

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/Login')
def Login():
    return render_template('Login.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')
    
@app.route('/sobre_gui')
def sobre_gui():
    return render_template('sobre_gui.html')

@app.route('/sobre_nos')
def sobre_nos():
    return render_template('sobre_nos.html')    

   

@app.route('/buscar', methods=['POST'])
def buscar():
    data = request.get_json()
    pergunta = data.get('pergunta')

    if not pergunta:
        return jsonify({'resposta': 'Pergunta vazia'})

    resposta = gerar_resposta(pergunta)
    return jsonify({'resposta': resposta})

