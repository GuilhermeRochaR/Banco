from flask import Blueprint, request, render_template
from flask_login import login_required
from models.locais import Local
from configs.extensions import db

locais_router = Blueprint("locais_router", __name__, template_folder="templates")

# Rota para listar todos os locais
@locais_router.get("/locais")
@login_required
def get_all_locais():
    locais = Local.query.all()
    return render_template("locais.html", locais=locais)

# Rota para criar um novo local
@locais_router.post("/locais")
@login_required
def create_local():
    data = request.json
    novo_local = Local(
        nome=data.get("nome"),
        endereco=data.get("endereco"),
        capacidade=data.get("capacidade"),
        descricao=data.get("descricao"),
    )
    db.session.add(novo_local)
    db.session.commit()
    return {
        "id": novo_local.id_local,
        "nome": novo_local.nome,
        "descricao": novo_local.descricao
    }
