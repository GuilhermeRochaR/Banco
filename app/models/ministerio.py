from configs.extensions import db
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey, String, Text, Integer

# Modelo da tabela Ministerio
class Ministerio(db.Model):
    __tablename__ = 'ministerio'
    id_ministerio: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    descricao: Mapped[str | None] = mapped_column(Text, nullable=True)
    id_membro: Mapped[int] = mapped_column(Integer, ForeignKey('membros.id_membro'), nullable=False)

    membro = db.relationship('Membro', backref=db.backref('ministerio', lazy=True))

    def __init__(self, nome: str, descricao: str | None, id_membro: int):
        self.nome = nome
        self.descricao = descricao
        self.id_membro = id_membro

    @staticmethod
    def get_todos_ministerios():
        ministerios = Ministerio.query.all()
        for ministerio in ministerios:
            print(f"ID: {ministerio.id_ministerio}, Nome: {ministerio.nome}")