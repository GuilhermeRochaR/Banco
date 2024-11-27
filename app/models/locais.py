from configs.extensions import db
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey

# Modelo da tabela Locais
class Local(db.Model):
    __tablename__ = 'locais'
    id_local = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.Text, nullable=True)
    capacidade = db.Column(db.Integer, nullable=True)
    descricao = db.Column(db.Text, nullable=True)