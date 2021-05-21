from flask import Flask
from flask_wtf.file import FileField, FileAllowed
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flaskext.mysql import MySQL
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer
from flask_wtf  import  FlaskForm 
from  wtforms  import  StringField, PasswordField, TextAreaField, SubmitField, IntegerField, SelectField, FloatField, DecimalField
from wtforms.validators import InputRequired, Length, AnyOf, DataRequired
from flask_login import LoginManager
from sqlalchemy.sql import select
from decimal import ROUND_UP

app = Flask(__name__)
app.config.from_object('config')
mysql = MySQL(app)
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

lm = LoginManager(app)
lm.init_app(app)


from .models import tables

class Status(FlaskForm):
    status = SelectField(u'Status', choices=[('finalizado', 'finalizado')])
    submit= SubmitField('Confirmar')

class Unit(FlaskForm):
    unit= StringField('Quantidade', validators=[InputRequired(message='Um titulo é exigido'), Length(min=1, max=20, message= 'Máximo de 20 caracteres.')])
    submit= SubmitField('Fazer pedido')
    
class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(message='deu ruim')])
    password = PasswordField("password", validators=[DataRequired(message='deu ruim')])
    submit= SubmitField('Realizar login')

class CreateProductForm(FlaskForm):
    title = StringField('Titulo', validators=[InputRequired(message='Um titulo é exigido'), Length(min=1, max=20, message= 'Máximo de 20 caracteres.')])
    description = TextAreaField('Descrição', validators=[InputRequired('Um subtitulo é exigido')])
    picture = FileField('Upload da imagem', validators=[FileAllowed(['jpg', 'png'])])
    price = DecimalField('Preço (Somente duas casas após o ponto final)', places=1, rounding=ROUND_UP, validators=[InputRequired('Um preço é exigido')])
    submit= SubmitField('Finalizar')

class UpdateAccount1(FlaskForm):
    username = StringField('Nome de usuário', validators=[InputRequired(message='Um usuário é exigido'), Length(min=1, max=30, message= 'Máximo de 30 caracteres.')])
    password = StringField('Senha', validators=[InputRequired(message='Um usuário é exigido'), Length(min=1, max=30, message= 'Máximo de 30 caracteres.')])
    contato = StringField('Contato', validators=[InputRequired(message='Um contato é exigido'), Length(min=1, max=60, message= 'Máximo de 60 caracteres.')])
    city = StringField('Cidade', validators=[InputRequired(message='Um contato é exigido'), Length(min=1, max=60, message= 'Máximo de 60 caracteres.')])
    street = StringField('Rua', validators=[InputRequired(message='Um contato é exigido'), Length(min=1, max=60, message= 'Máximo de 60 caracteres.')])
    number = IntegerField('Numero')
    submit= SubmitField('Finalizar')


    
# from app import admin
# admin.init_app(app)
from app.controllers import index


