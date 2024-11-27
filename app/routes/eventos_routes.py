from flask import Blueprint, request, render_template
from flask_login import login_required
from models.eventos import Evento
from configs.extensions import db

eventos_router = Blueprint("eventos_router", __name__, template_folder="templates")

# Rota para listar todos os eventos
@eventos_router.get("/eventos")
@login_required
def get_all_eventos():
    eventos = Evento.query.all()
    return render_template("eventos.html", eventos=eventos)

# Rota para criar um novo evento
@eventos_router.post("/eventos")
@login_required
def create_evento():
    data = request.json
    novo_evento = Evento(
        nome=data.get("nome"),
        descricao=data.get("descricao"),
        data_inicio=data.get("data_inicio"),
        data_fim=data.get("data_fim"),
        id_local=data.get("id_local"),
    )
    db.session.add(novo_evento)
    db.session.commit()
    return {
        "id": novo_evento.id_evento,
        "nome": novo_evento.nome,
        "descricao": novo_evento.descricao
    }
