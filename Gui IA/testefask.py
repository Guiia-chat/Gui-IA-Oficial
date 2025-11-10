from flask import Flask
from flask import request, jsonify

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import modelo
import fine_tuning


app = Flask(__name__)

modelo.inicializar_banco_de_dados(
    host='localhost',
    user='root',
    password='9532',
    database='Chat_bot_Guiia'
)



from views import *


if  __name__ == "__main__":
 app.run(debug=True)