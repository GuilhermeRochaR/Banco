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
    return render_template("reunioesNOVO.html", reunioes=reunioes)

# Rota para criar uma nova reunião
@reunioes_router.post("/reunioes")
@login_required
def create_reuniao():
    
    nome=request.form.get("nome")
    descricao=request.form.get("descricao")
    data_inicio=request.form.get("data_inicio")
    data_fim=request.form.get("data_fim")
    id_ministerio=request.form.get("id_ministerio")
    id_local=request.form.get("id_local")
    
    nova_reuniao = Reuniao(
        nome=nome,
        descricao=descricao,
        data_inicio=data_inicio,
        data_fim=data_fim,
        id_local=id_local
    )
    db.session.add(nova_reuniao)
    db.session.commit()
    