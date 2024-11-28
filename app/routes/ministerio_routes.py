from flask import Blueprint, request, render_template
from flask_login import login_required
from models.ministerio import Ministerio
from configs.extensions import db
from sqlalchemy import text


ministerios_router = Blueprint("ministerio_router", __name__, template_folder="templates")

# Rota para listar todos os ministérios
@ministerios_router.get("/ministerio")
@login_required
def cadastro_ministerio():
    membros = db.session.execute(text("SELECT id_membro, nome FROM Membros")).fetchall()
    print(membros)
    return render_template('ministerioNOVO.html', membros=membros)


# Rota para criar um novo ministério
@ministerios_router.post("/ministerio")
@login_required
def create_ministerio():
    # Usando request.form para pegar os dados do formulário
    nome = request.form.get("nome")
    descricao = request.form.get("descricao")
    id_membro = request.form.get("id_membro")
    
    # Criando o novo ministério
    novo_ministerio = Ministerio(
        nome=nome,
        descricao=descricao,
        id_membro=id_membro
    )

    db.session.add(novo_ministerio)
    db.session.commit()

