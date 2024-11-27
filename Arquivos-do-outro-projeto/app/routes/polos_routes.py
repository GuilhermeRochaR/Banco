from flask import Blueprint, render_template, redirect, request
from flask_login import login_required
from models.polo import Polo


polos_router = Blueprint("polos_router", __name__, template_folder="templates")


@polos_router.get("/polos")
@login_required
def get_all_polos():
    list_polos = Polo.get_all_polos()
    return render_template("polos.html", list_polos=list_polos)


@polos_router.post("/polos")
def create_equipment():
    polo_name = request.json["name"]
    new_polo = Polo(polo_name)
    new_polo.create_polo()
    return {
        "id": new_polo.id,
        "name": new_polo.name
    }

