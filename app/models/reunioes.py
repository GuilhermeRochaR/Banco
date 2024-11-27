from configs.extensions import db
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey

# Modelo da tabela Reunioes
class Reuniao(db.Model):
    __tablename__ = 'reunioes'
    id_reuniao = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    tipo = db.Column(db.String(100), nullable= False)
    data_inicio = db.Column(db.DateTime, nullable=False)
    data_fim = db.Column(db.DateTime, nullable=True)
    id_ministerio = db.Column(db.Integer, db.ForeignKey('ministerio.id_ministerio'), nullable=True)
    id_local = db.Column(db.Integer, db.ForeignKey('locais.id_local'), nullable=True)
    ministerio = db.relationship('Ministerio', backref=db.backref('reunioes', lazy=True))
    local = db.relationship('Local', backref=db.backref('reunioes', lazy=True))