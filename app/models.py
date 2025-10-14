from app import db

class Dados(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=True)
    idade = db.Column(db.Integer)
    sexo = db.Column(db.Integer) #0 masculino; 1 feminino; 2 prefiro não dizer
    q4 = db.Column(db.Integer) #0 sim, já sofri; 1 sim, já presenciei; 2 não;
    q5 = db.Column(db.Integer) #0 não; 1 sim
    q6 = db.Column(db.Integer) #0 sim, muito relevante; 1 sim, porém pouco relevante; 2 não
    q7 = db.Column(db.Integer) #0 medo; 1 preconceito cultural; 2 caráter; 3 questões econômicas; 4 falta de conhecimento/educação
    q8 = db.Column(db.Integer) #0 não; 1 sim
    q9 = db.Column(db.Integer) #0 sim, acredito que as leis atuais sejam suficientes; 1 sim, porém acredito que ainda haja coisas para melhorar; 2 não, porém está no caminho certo; 3 não, acredito que estamos longe de leis justas
    q10 = db.Column(db.Integer) #0 mídias; 1 escolas; 2 ambientes profissionais
    q11 = db.Column(db.Integer) #0 sim, acredito plenamente; 1 sim, porém não é o principal; 2 não