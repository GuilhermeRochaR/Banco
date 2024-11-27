from flask import Blueprint, request, render_template
from flask_login import login_required
from models.ministerio import Ministerio
from configs.extensions import db

ministerios_router = Blueprint("ministerios_router", __name__, template_folder="templates")

# Rota para listar todos os ministérios
@ministerios_router.get("/ministerios")
@login_required
def get_all_ministerios():
    ministerios = Ministerio.query.all()
    return render_template("ministerios.html", ministerios=ministerios)

# Rota para criar um novo ministério
@ministerios_router.post("/ministerios")
@login_required
def create_ministerio():
    data = request.json
    novo_ministerio = Ministerio(
        nome=data.get("nome"),
        descricao=data.get("descricao"),
        id_membro=data.get("id_membro"),
    )
    db.session.add(novo_ministerio)
    db.session.commit()
    return {
        "id": novo_ministerio.id_ministerio,
        "nome": novo_ministerio.nome,
        "descricao": novo_ministerio.descricao
    }
