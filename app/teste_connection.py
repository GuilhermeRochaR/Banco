from app import app, db
from models.membros import Membro

# Testando a conexão com o banco de dados
with app.app_context():  # Garante que o contexto da aplicação Flask está ativo
    membro = Membro.query.first()
    if membro:
        print(f"Membro encontrado: {membro.nome}")
    else:
        print("Nenhum membro encontrado.")
