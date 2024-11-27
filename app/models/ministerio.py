from configs.extensions import db
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey

# Modelo da tabela Ministerio
class Ministerio(db.Model):
    __tablename__ = 'ministerio'
    id_ministerio = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    id_membro = db.Column(db.Integer, db.ForeignKey('membros.id_membro'), nullable=False)
    membro = db.relationship('Membro', backref=db.backref('ministerios', lazy=True))