from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


# Configuração do Banco de Dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:senha123@localhost/seu_banco'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria todas as tabelas no banco de dados

@app.route("/")
def home():
    return render_template("index.html")  # Página inicial

@app.route("/about")
def about():
    return render_template("about.html")  # Página "Sobre"

@app.route("/api/data", methods=["GET"])
def get_data():
    return jsonify({"message": "Bem-vindo à API!", "status": "sucesso"})

@app.route("/api/data", methods=["POST"])
def post_data():
    data = request.json
    return jsonify({"message": "Dados recebidos!", "data": data}), 201







if __name__ == "__main__":
    app.run(debug=True)
