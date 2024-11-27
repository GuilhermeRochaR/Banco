from flask import Blueprint, render_template, redirect, request
from flask_login import login_required
from models.equipment import Equipment


equipment_router = Blueprint("equipment_router", __name__, template_folder="templates")


@equipment_router.get("/equipments")
@login_required
def get_all_equipments():
    list_equipments = Equipment.get_all_equipments()
    return render_template("equipments.html", list_equipments=list_equipments)


@equipment_router.post("/equipments")
def create_equipment():
    equipment_name = request.json["name"]
    new_equipment = Equipment(equipment_name)
    new_equipment.create_equipment()
    return {
        "id": new_equipment.id,
        "name": new_equipment.name
    }

