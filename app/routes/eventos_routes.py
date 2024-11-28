from flask import Blueprint, request, render_template
from flask_login import login_required
from models.eventos import Evento
from configs.extensions import db
from flask import flash, redirect, url_for

eventos_router = Blueprint("eventos_router", __name__, template_folder="templates")

# Rota para listar todos os eventos
@eventos_router.get("/eventos")
@login_required
def listar_eventos():
    # Consulta todos os eventos no banco de dados
    eventos = Evento.query.all()

    # Locais e tipos de eventos são usados em outro contexto, mas podem ser passados também
    locais = [
        {"id_local": 1, "nome": "Igreja Central"},
        {"id_local": 2, "nome": "Igreja Filial"},
        {"id_local": 3, "nome": "Auditório"},
    ]
    tiposEventos = ["Culto de Adoração", "Seminário de Liderança", "Palestra sobre Família"]

    return render_template("eventosNOVO.html", eventos=eventos, locais=locais, tiposEventos=tiposEventos)


@eventos_router.post("/eventos")
@login_required
def cadastrar_evento():
    try:
        # Coleta os dados enviados pelo formulário
        nome = request.form.get("nome")
        descricao = request.form.get("descricao")
        data_inicio = request.form.get("data_inicio")
        data_fim = request.form.get("data_fim")
        id_local = request.form.get("id_local")
        tipo = request.form.get("tipo")

        # Cria o objeto Evento
        novo_evento = Evento(
            nome=nome,
            descricao=descricao,
            tipo=tipo,
            data_inicio=data_inicio,
            data_fim=data_fim,
            id_local=id_local
        )

        # Adiciona e confirma a transação no banco de dados
        db.session.add(novo_evento)
        db.session.commit()

        return "Evento cadastrado com sucesso!", 201  # Sucesso
    except Exception as e:
        db.session.rollback()  # Reverte caso haja erro
        return f"Erro ao cadastrar evento: {str(e)}", 400
