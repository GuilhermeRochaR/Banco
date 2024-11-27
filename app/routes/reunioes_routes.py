from flask import Blueprint, request, render_template
from flask_login import login_required
from models.reunioes import Reuniao
from configs.extensions import db

reunioes_router = Blueprint("reunioes_router", __name__, template_folder="templates")

# Rota para listar todas as reuniões
@reunioes_router.get("/reunioes")
@login_required
def get_all_reunioes():
    reunioes = Reuniao.query.all()
    return render_template("reunioes.html", reunioes=reunioes)

# Rota para criar uma nova reunião
@reunioes_router.post("/reunioes")
@login_required
def create_reuniao():
    data = request.json
    nova_reuniao = Reuniao(
        nome=data.get("nome"),
        descricao=data.get("descricao"),
        data_inicio=data.get("data_inicio"),
        data_fim=data.get("data_fim"),
        id_ministerio=data.get("id_ministerio"),
        id_local=data.get("id_local"),
    )
    db.session.add(nova_reuniao)
    db.session.commit()
    return {
        "id": nova_reuniao.id_reuniao,
        "nome": nova_reuniao.nome,
        "descricao": nova_reuniao.descricao
    }
