from app import app
from flask import render_template, url_for, request, redirect
from app.forms import MatForm

@app.route('/',  methods=['GET', 'POST'])
def pagina_formulario():
    form = MatForm()

    if form.validate_on_submit():
        return render_template('resposta.html')

    return render_template('formulario.html', form=form)