from flask import Blueprint, request, render_template
from flask_login import login_required
from models.request import Request
from datetime import datetime

request_router = Blueprint("request_router", __name__, template_folder="templates")

# Rota para listar todas as solicitações
@request_router.get("/requests")
@login_required
def get_all_requests():
    """
    Rota para listar todas as solicitações e renderizar no template request.html.
    """
    all_requests = Request.get_all_requests()
    return render_template("request.html", list_requests=all_requests)


# Rota para criar uma nova solicitação
@request_router.post("/requests")
@login_required
def create_request():
    """
    Rota para criar uma nova solicitação e renderizar no template request.html.
    """
    data = request.json

    # Extraindo os dados do JSON
    usuarioId = data.get("usuarioId")
    lugares = data.get("lugares")
    motivo = data.get("motivo")
    status = data.get("status", "Pending")  # Valor padrão "Pending"
    permanente = data.get("permanente", False)  # Valor padrão False
    idSetor = data.get("idSetor")
    data_solicitacao = data.get("data")
    inicio = data.get("inicio")
    fim = data.get("fim")

    # Convertendo strings para objetos de data e hora
    try:
        data_solicitacao = datetime.strptime(data_solicitacao, "%Y-%m-%d").date()
        inicio = datetime.strptime(inicio, "%H:%M:%S").time()
        fim = datetime.strptime(fim, "%H:%M:%S").time()
    except ValueError as e:
        return render_template("request.html", error="Data ou hora em formato inválido.", message=str(e))

    # Criando nova instância de Request
    new_request = Request(
        usuarioId=usuarioId,
        lugares=lugares,
        motivo=motivo,
        status=status,
        permanente=permanente,
        idSetor=idSetor,
        data=data_solicitacao,
        inicio=inicio,
        fim=fim
    )

    # Salvando no banco de dados
    new_request.create_request()

    # Recuperando a lista atualizada de solicitações para exibir no template
    all_requests = Request.get_all_requests()
    return render_template("request.html", list_requests=all_requests)
