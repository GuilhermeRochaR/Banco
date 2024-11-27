from flask import Blueprint, render_template, redirect, request
from flask_login import login_required
from models.sector import Sector

sector_router = Blueprint("sector_router", __name__, template_folder="templates")


@sector_router.get("/sectors")
@login_required
def get_all_sectors():
    list_sectors = Sector.get_all_sectors()
    return render_template("sector.html", list_sectors=list_sectors)


@sector_router.post("/sectors")
def create_sector():
    data = request.json
    sector_name = data.get("nome")
    sector_amigable_name = data.get("nomeAmigavel")

    new_sector = Sector(nome=sector_name, nomeAmigavel=sector_amigable_name)
    new_sector.create_sector()

    return{
        "id": new_sector.id,
        "nome": new_sector.nome,
        "nomeAmigavel": new_sector.nomeAmigavel
    }