from flask import Blueprint, render_template, request, redirect, make_response, flash, session
from models.membros import Membro
from flask_login import login_required, login_user, logout_user, current_user
from validation.validation_utils import validate_login_data

membros_router = Blueprint("membros_router", __name__, template_folder="templates")

# Rota para listar todos os membros
@membros_router.get("/")
@login_required
def render_index():
    membro_name = current_user.name
    return render_template("membros.html", membro_name=membro_name)

@membros_router.get("/login")
def index():
    return render_template("login.html")

@membros_router.get("/register")
def render_register():
    return render_template("cadastro.html")

@membros_router.post("/register")
def register():
    nome = request.form["nome"]
    email = request.form["email"]
    telefone = request.form["telefone"]
    endereco = request.form["endereço"]
    senha = request.form["senha"]
    confirma_senha = request.form["confirmarsenha"]
    datadenascimento = request.form
    ["datadenascimento"]
    ministerio = request.form["ministerio"]
    
    if senha == confirma_senha:
        exist_user = Membro.find_user_by_email(email=email)
        if exist_user == None:
            newUser = Membro(nome, email, senha)
            newUser.set_password(senha)
            newUser.create_user()
            return make_response(redirect("/login"),302)
        return make_response("<h1>Erro 400 - campos invalidos</h1>",400)
    else:
        return make_response("<h1>Senha não confirmada</h1>",400)

@membros_router.post("/login")
def login():
    # Obtém os dados do formulário
    data = {
        'usuario': request.form.get("email"),  # assumindo que email é o campo usado para login
        'senha': request.form.get("senha")
    }

    # Chama a função de validação para verificar os dados de login
    is_valid, error_message = validate_login_data(data)
    if not is_valid:
        flash(error_message, "Danger!")
        return redirect("/login")

    user = Membro.query.filter_by(email=data['usuario']).first()
    if user is not None and user.check_password(data['senha']):
        login_user(user, remember=True)
        return redirect("/")

    flash("Email ou senha inválidos", "Danger!")
    return redirect("/login")

@membros_router.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")




