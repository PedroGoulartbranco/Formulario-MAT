from app import app
from flask import render_template, url_for, request, redirect
from app.forms import MatForm

@app.route('/',  methods=['GET', 'POST'])
def pagina_formulario():
    form = MatForm()
    return render_template('formulario.html', form=form)