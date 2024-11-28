from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_required
from models.reunioes import Reuniao
from configs.extensions import db
from models.ministerio import Ministerio
from models.locais import Local 

reunioes_router = Blueprint("reunioes_router", __name__, template_folder="templates")

# Rota para listar todas as reuniões
@reunioes_router.get("/reunioes")
@login_required
def get_all_reunioes():
    reunioes = Reuniao.query.all()
    return render_template("reunioes_lista.html", reunioes=reunioes)

# Rota para criar uma nova reunião
@reunioes_router.get("/reunioes/cadastro")
@login_required
def entrar_cadastro():
    ministerios = Ministerio.query.all()  # Pegando todos os ministérios
    locais = Local.query.all()  # Pegando todos os locais
    return render_template('reunioesNOVO.html', ministerios=ministerios, locais=locais)
    


@reunioes_router.post("/reunioes/cadastro")
@login_required
def create_reuniao():
    nome = request.form.get("nome")
    descricao = request.form.get("descricao")
    tipo = request.form.get("tipo")
    data_inicio = request.form.get("data_inicio")
    data_fim = request.form.get("data_fim")
    id_ministerio = request.form.get("id_ministerio")
    id_local = request.form.get("id_local")

    # Validação para `id_ministerio` e `id_local`
    if not id_ministerio or id_ministerio == "":
        return "Erro: Ministério inválido.", 400

    if not id_local or id_local == "":
        return "Erro: Local inválido.", 400

    try:
        id_ministerio = int(id_ministerio)  # Converte o valor para inteiro
        id_local = int(id_local)
    except ValueError:
        return "Erro: Valores inválidos para ministério ou local.", 400

    # Criação da nova reunião
    nova_reuniao = Reuniao(
        nome=nome,
        descricao=descricao,
        tipo=tipo,
        data_inicio=data_inicio,
        data_fim=data_fim,
        id_ministerio=id_ministerio,
        id_local=id_local
    )

    # Adiciona e salva no banco de dados
    db.session.add(nova_reuniao)
    db.session.commit()

    return redirect(url_for("reunioes_router.get_all_reunioes"))


    
    