from app import app, db
from flask import render_template, session
from .forms import MatForm
from .models import Dados

import pandas as pd
import plotly.express as px

@app.route('/',  methods=['GET', 'POST'])
def pagina_formulario():
    form = MatForm()

    if session.get('respondido'):
        return render_template('respondido.html')

    if form.validate_on_submit():
        session['respondido'] = True
        respostas = Dados(
            nome=form.nome.data,
            idade=form.idade.data,
            sexo=form.sexo.data,
            q4=form.q4.data,
            q5=form.q5.data,
            q6=form.q6.data,
            q7=form.q7.data,
            q8=form.q8.data,
            q9=form.q9.data,
            q10=form.q10.data,
            q11=form.q11.data
        )

        db.session.add(respostas)
        db.session.commit()

        return render_template('respondido.html')

    return render_template('formulario.html', form=form)

@app.route('/analise/')
def analise():

    df = pd.read_sql_table('dados', db.engine)

    info = {}

    info['num_respostas'] = df.index[-1]

    graficos = {}

    count_sexo = df['sexo'].value_counts().reset_index()
    count_sexo.columns = ['Sexo', 'Quantidade']
    graficos['sexo'] = px.pie(data_frame=count_sexo, names='Sexo', values='Quantidade', title='Respostas por gênero').to_html(full_html=False)


    #aqui ele cria outro dataframe, um filtro de idades com base nos valores de bins
    df['faixa'] = pd.cut(df['idade'], bins=[13, 14, 15, 16, 17, 18, 50], labels=['<=13', '14', '15', '16', '17', '>=18'])
    count_faixa = df['faixa'].value_counts().reset_index()
    count_faixa.columns = ['Faixa Etária', 'Quantidade']
    graficos['idade'] = px.pie(data_frame=count_faixa, names='Faixa Etária', values='Quantidade', title='Respostas por idade').to_html(full_html=False)

    titulos = {
        'q4':'Já sofreu ou presenciou algum tipo de preconceito?',
        'q5':'Você sabe o que é xenofobia?',
        'q6':'Na sua opinião, a xenofobia é um problema relevante no Brasil/mundo?',
        'q7':'Você acredita que a xenofobia está relacionada a:',
        'q8':'Você conhece alguém que sofreu ou sofre com a xenofobia?',
        'q9':'Você acredita que as punições atuais são suficientes?',
        'q10':'Onde você acredita que mais ocorrem casos de xenofobia?',
        'q11':'Você acredita que a mídia (TV, jornais, internet) reforça estereótipos que alimentam a xenofobia?'
    }

    for q in ['q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11']:
        contagem = df[q].value_counts().reset_index()
        contagem.columns = ['Resposta', 'Quantidade']
        graficos[q] = px.bar(data_frame=contagem, x='Resposta', y='Quantidade', tittle=titulos.get(q)).to_html(full_html=False)

    return render_template('analise.html', graficos=graficos, info=info)