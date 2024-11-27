from configs.extensions import db
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, String, DateTime, Integer, ForeignKey

# Modelo da tabela Eventos
class Evento(db.Model):
    __tablename__ = 'eventos'
    id_evento: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    descricao: Mapped[str | None] = mapped_column(Text, nullable=True)  # Tipo pode ser str ou None
    tipo: Mapped[str] = mapped_column(String(100), nullable=True)
    data_inicio: Mapped[DateTime] = mapped_column(nullable=False)
    data_fim: Mapped[DateTime | None] = mapped_column(nullable=True)  # Pode ser None
    id_local: Mapped[int | None] = mapped_column(Integer, ForeignKey('locais.id_local'), nullable=True)
   
    local = db.relationship('Local', backref=db.backref('eventos', lazy=True))

    def __init__(self, nome: str, descricao: str, tipo: str, data_inicio: DateTime, data_fim: DateTime | None, id_local: int | None):
        self.nome = nome
        self.descricao = descricao
        self.tipo = tipo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.id_local = id_local

    @staticmethod
    def get_todos_eventos():
        eventos = Evento.query.all()
        for evento in eventos:
            print(f"ID: {evento.id_evento}, Nome: {evento.nome}, Tipo: {evento.tipo}, Data Início: {evento.data_inicio}")