from app import app
from flask import render_template, url_for, request, redirect

@app.route('/',  methods=['GET', 'POST'])
def pagina_inicial():
    nome = "Pedro"
    return render_template('index.html', nome=nome)