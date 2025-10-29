from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange

class MatForm(FlaskForm):
    nome = StringField('Nome: (opcional)')
    
    idade = IntegerField(
        'Idade:',
        validators=[
            DataRequired(message="Por favor, insira sua idade."),
            NumberRange(min=13, max=50, message="A idade deve estar entre 13 e 50 anos.")
        ]
    )

    sexo = SelectField(
        'Sexo:',
        choices=[("", "Selecione"), ("0", "Masculino"), ("1", "Feminino"), ("2", "Prefiro não dizer")],
        validators=[DataRequired()],
        coerce=str
    )

    q4 = SelectField(
        'Já sofreu ou presenciou algum tipo de preconceito?',
        choices=[("", "Selecione"), ("0", "Sim, já sofri"), ("1", "Sim, já presenciei"), ("2", "Não")],
        validators=[DataRequired()],
        coerce=str
    )

    q5 = SelectField(
        'Você sabe o que é xenofobia?',
        choices=[("", "Selecione"), ("0", "Não"), ("1", "Sim")],
        validators=[DataRequired()],
        coerce=str
    )

    q6 = SelectField(
        'Na sua opinião, a xenofobia é um problema relevante no Brasil/mundo?',
        choices=[("", "Selecione"), ("0", "Sim, muito relevante"), ("1", "Sim, porém pouco relevante"), ("2", "Não")],
        validators=[DataRequired()],
        coerce=str
    )

    q7 = SelectField(
        'Você acredita que a xenofobia está relacionada a:',
        choices=[
            ("", "Selecione"),
            ("0", "Medo"),
            ("1", "Preconceito cultural"),
            ("2", "Caráter"),
            ("3", "Questões econômicas"),
            ("4", "Falta de conhecimento/educação")
        ],
        validators=[DataRequired()],
        coerce=str
    )

    q8 = SelectField(
        'Você conhece alguém que sofreu ou sofre com a xenofobia?',
        choices=[("", "Selecione"), ("0", "Não"), ("1", "Sim")],
        validators=[DataRequired()],
        coerce=str
    )

    q9 = SelectField(
        'Você acredita que as punições atuais são suficientes?',
        choices=[
            ("", "Selecione"),
            ("0", "Sim, acredito que as leis atuais sejam suficientes"),
            ("1", "Sim, porém acredito que ainda haja coisas para melhorar"),
            ("2", "Não, porém está no caminho certo"),
            ("4", "Não, acredito que estamos longe de leis justas")
        ],
        validators=[DataRequired()],
        coerce=str
    )

    q10 = SelectField(
        'Onde você acredita que mais ocorrem casos de xenofobia?',
        choices=[
            ("", "Selecione"),
            ("0", "Mídias (TV, jornais, internet)"),
            ("1", "Escolas"),
            ("2", "Ambientes profissionais")
        ],
        validators=[DataRequired()],
        coerce=str
    )

    q11 = SelectField(
        'Você acredita que a mídia (TV, jornais, internet) reforça estereótipos que alimentam a xenofobia?',
        choices=[
            ("", "Selecione"),
            ("0", "Sim, acredito plenamente"),
            ("1", "Sim, porém não é o principal"),
            ("2", "Não")
        ],
        validators=[DataRequired()],
        coerce=str
    )

    btnSubmit = SubmitField('Enviar')