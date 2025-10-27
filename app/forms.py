from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange

class MatForm(FlaskForm):
    nome = StringField('Nome: (opcional)')
    idade = IntegerField('Idade:', validators=[DataRequired(), NumberRange(min=1, max=100)])
    sexo = SelectField('Sexo:', choices=[(0, "Masculino"), 
                                        (1, "Feminino"), 
                                        (2, "Prefiro não dizer")], 
                                        validators=[DataRequired()])
    q4 = SelectField('Já sofreu ou presenciou algum tipo de preconceito:', choices=[(0, "Sim, já sofri"),
                                                                                    (1, "Sim, já presenciei"),
                                                                                    (2, "Não")],
                                                                                    validators=[DataRequired()])
    q5 = SelectField('Você sabe o que é xenofobia:', choices=[(0, "Não"),
                                                             (1, "Sim")],
                                                             validators=[DataRequired(), NumberRange(min=0, max=1)])
    q6 = SelectField('Na sua opinião, a xenofobia é um problema relevante no Brasil/mundo:', choices=[(0, "Sim, muito relevante"),
                                                                                                     (1, "Sim, porém pouco relevante"),
                                                                                                     (2, "Não")],
                                                                                                     validators=[DataRequired()])
    q7 = SelectField('Você acredita que a xenofobia está relacionada a:', choices=[(0, "Medo"),
                                                                                   (1, "Preconceito cultural"),
                                                                                   (2, "Caráter"),
                                                                                   (3, "Questões econômicas"),
                                                                                   (4, "Falta de conhecimento/educação")],
                                                                                   validators=[DataRequired(), NumberRange(min=0, max=4)])
    q8 = SelectField('Você conhece alguém que sofreu ou sofre com a xenofobia:', choices=[(0, "Não"), 
                                                                                          (1, "Sim")],
                                                                                          validators=[DataRequired()])
    q9 = SelectField('Você acredita que as punições atuais são suficientes:', choices=[(0, "Sim, acredito que as leis atuais sejam suficientes"),
                                                                                       (1, "Sim, porém acredito que ainda haja coisas para melhorar"),
                                                                                       (2, "Não, porém está no caminho certo"),
                                                                                       (4, "Não, acredito que estamos longe de leis justas")],
                                                                                       validators=[DataRequired()])
    q10 = SelectField('Onde você acredita que mais ocorrem casos de xenofobia:', choices=[(0, "Mídias (TV, jornais, internet)"),
                                                                                          (1, "Escolas"),
                                                                                          (2, "Ambientes profissionais")],
                                                                                          validators=[DataRequired()])
    q11 = SelectField('Você acredita que a mídia (TV, jornais, internet) reforça estereótipos que alimentam a xenofobia:', choices=[(0, "Sim, acredito plenamente"),
                                                                                                                                    (1, "Sim, porém não é o principal"),
                                                                                                                                    (2, "Não")],
                                                                                                                                    validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')