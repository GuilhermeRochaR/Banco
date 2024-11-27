from configs.extensions import db
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey

# Modelo da tabela Membros
class Membro(db.Model):
    __tablename__ = 'membros'
    id_membro = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=True)
    telefone = db.Column(db.String(20), nullable=True)
    endereco = db.Column(db.Text, nullable=True)
    data_nascimento = db.Column(db.Date, nullable=True)
    data_entrada = db.Column(db.Date, nullable=True)