from flask import Blueprint, request, render_template
from flask_login import login_required
from models.eventos import Evento
from configs.extensions import db

eventos_router = Blueprint("eventos_router", __name__, template_folder="templates")

# Rota para listar todos os eventos
@eventos_router.get("/eventos")
@login_required
def listar_eventos():
    # Consulta todos os eventos no banco de dados
    eventos = Evento.query.all()
    return render_template("lista_eventos.html", eventos=eventos)

@eventos_router.get("/eventos")
@login_required
def abrir_eventos():
    return render_template("eventosNOVO.html")

# Rota para criar um novo evento
@eventos_router.post("/eventos")
@login_required
def create_evento():  
    nome=request.form.get("nome"),
    descricao=request.form.get("descricao"),
    data_inicio=request.form.get("data_inicio"),
    data_fim=request.form.get("data_fim"),
    id_local=request.form.get("id_local"),

    novo_evento = Evento(
        nome=nome,
        descricao=descricao,
        data_inicio=data_inicio,
        data_fim=data_fim,
        id_local=id_local
    )
    
    db.session.add(novo_evento)
    db.session.commit()

