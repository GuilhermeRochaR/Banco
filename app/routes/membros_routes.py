from flask import Blueprint, request, render_template, request, redirect
from flask_login import login_required
from models.membros import Membro
from configs.extensions import db

membros_router = Blueprint("membros_router", __name__, template_folder="templates")

# Rota para listar todos os membros
@membros_router.get("/")
@login_required
def get_all_membros():
    membros = Membro.query.all()
    return render_template("membros.html", membros=membros)

# Rota para criar um novo membro
@membros_router.post("/membros")
@login_required
def create_membro():
    data = request.json
    novo_membro = Membro(
        nome=data.get("nome"),
        email=data.get("email"),
        telefone=data.get("telefone"),
        endereco=data.get("endereco"),
        data_nascimento=data.get("data_nascimento"),
        data_entrada=data.get("data_entrada"),
    )
    db.session.add(novo_membro)
    db.session.commit()
    return {
        "id": novo_membro.id_membro,
        "nome": novo_membro.nome,
        "email": novo_membro.email
    }
