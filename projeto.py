from flask import Flask
from flask import render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root@localhost/agenda'
db = SQLAlchemy(app)

class agenda(db.Model):
    __tablename__ = 'contato'
    _id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome = db.Column(db.String(50))
    telefone = db.Column(db.String(20))
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class time(db.Model):
    __tablename__ = 'times'
    _id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nometime = db.Column(db.String(50))
    historia = db.Column(db.String(20000))
    tecnico = db.Column(db.String(50))
    armador = db.Column(db.String(50))
    ala = db.Column(db.String(50))
    pivo = db.Column(db.String(50))
    def __init__(self, nome, historia,tecnico,armador,ala,pivo):
        self.nome = nome
        self.historia = historia
        self.tecnico=tecnico
        self.armador=armador
        self.ala=ala
        self.pivo=pivo

class placar(db.Model):
    __tablename__ = 'resultado'
    _id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nometime1 = db.Column(db.String(50))
    placartime1 = db.Column(db.String(5))
    nometime2 = db.Column(db.String(50))
    placartime2 = db.Column(db.String(5))
    def __init__(self, nometime1, placartime1,nometime2,placartime2):
        self.nometime1 = nometime1
        self.placartime1 = placartime1
        self.nometime2 = nometime2
        self.placartime2 = placartime2

db.create_all()

@app.route("/teste")
def teste():
    return 'Olá Mundo'

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/cadastrosms")
def cadastrosms():
    return render_template("cadastrosms.html")

@app.route("/cadastrartime")
def cadastrartime():
    return render_template("cadastrartime.html")

@app.route("/cadastroplacar")
def cadastroplacar():
    return render_template("cadastroplacar.html")

@app.route("/mensagem")
def mensagem():
    return render_template("mensagem.html")

@app.route("/cadastrar",methods=['GET', 'POST'])
def cadastrar():
    if request.method =="POST":
        nome = (request.form.get("nome"))
        telefone = (request.form.get("telefone"))
        if nome:
            f = agenda(nome,telefone)
            db.session.add(f)
            db.session.commit()
    return redirect(url_for("mensagem"))

@app.route("/cadastrartimes",methods=['GET', 'POST'])
def cadastrartimes():
    if request.method =="POST":
        nometime = (request.form.get("nometime"))
        historia = (request.form.get("historia"))
        if nometime:
            f = time(nometime,historia)
            db.session.add(f)
            db.session.commit()
    return redirect(url_for("mensagem"))

@app.route("/cadastrarplacar",methods=['GET', 'POST'])
def cadastrarplacar():
    if request.method =="POST":
        nometime1 = (request.form.get("nometime1"))
        placartime1 = (request.form.get("placartime1"))
        if nometime1:
            f = placar(nometime1, placartime1,nometime2,placartime2)
            db.session.add(f)
            db.session.commit()
    return redirect(url_for("mensagem"))

@app.route("/listar")
def listar():
    agendas = agenda.query.all()
    return render_template("listar.html", agenda=agendas)


if __name__ == "__main__":
    app.run(debug=True)

