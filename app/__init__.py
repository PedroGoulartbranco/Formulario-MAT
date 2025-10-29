from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

database_url = os.environ.get('DATABASE_URL')

# Render às vezes fornece a URL com "postgres://" (antigo),
# então substituímos por "postgresql://" para compatibilidade com SQLAlchemy
if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

# Define a URI do banco
app.config['SQLALCHEMY_DATABASE_URI'] = database_url or 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'hfjsdsdksk!!dfhdksfhdjdhjks'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

db.create_all()

from app.views import pagina_formulario
