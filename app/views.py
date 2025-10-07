from app import app
from flask import render_template, url_for, request, redirect

@app.route('/',  methods=['GET', 'POST'])
def pagina_formulario():
    nome = "Pedro"
    return render_template('formulario.html', nome=nome)