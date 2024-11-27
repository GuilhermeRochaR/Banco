from flask import Blueprint, render_template, request, redirect, make_response, flash, session
from models.user import User
from flask_login import login_required, login_user, logout_user, current_user
from validation.validation_utils import validate_login_data

user_router = Blueprint("user_router", __name__, template_folder="templates")


@user_router.get("/")
@login_required
def render_index():
    user_name = current_user.name
    return render_template("menu.html", user_name=user_name)


@user_router.get("/login")
def index():
    return render_template("login.html")


@user_router.get("/register")
def render_register():
    return render_template("cadastro.html")


@user_router.post("/register")
def register():
    matricula = request.form["matricula"]
    email = request.form["email"]
    name = request.form["name"]
    password = request.form["password"]
    password_confirm = request.form["confirmPassword"]

    if password == password_confirm:
        exist_user = User.find_user_by_email(email=email)
        if exist_user == None:
            newUser = User(matricula, name, email, password)
            newUser.set_password(password)
            newUser.create_user()
            return make_response(redirect("/login"),302)
        return make_response("<h1>Erro 400 - campos invalidos</h1>",400)
    else:
        return make_response("<h1>Senha não confirmada</h1>",400)



@user_router.post("/login")
def login():
    # Obtém os dados do formulário
    data = {
        'username': request.form.get("email"),  # assumindo que email é o campo usado para login
        'password': request.form.get("password")
    }

    # Chama a função de validação para verificar os dados de login
    is_valid, error_message = validate_login_data(data)
    if not is_valid:
        flash(error_message, "Danger!")
        return redirect("/login")

    # Continua com o processo de autenticação
    user = User.query.filter_by(email=data['username']).first()
    if user is not None and user.check_password(data['password']):
        login_user(user, remember=True)
        return redirect("/")

    flash("Email ou senha inválidos", "Danger!")
    return redirect("/login")


@user_router.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")