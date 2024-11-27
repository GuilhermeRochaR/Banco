from configs.extensions import db
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey, String, Text, DateTime

# Modelo da tabela Reunioes
class Reuniao(db.Model):
    __tablename__ = 'reunioes'
    id_reuniao: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    descricao: Mapped[str | None] = mapped_column(Text, nullable=True)
    tipo: Mapped[str] = mapped_column(String(100), nullable=False)
    data_inicio: Mapped[DateTime] = mapped_column(nullable=False)
    data_fim: Mapped[DateTime | None] = mapped_column(nullable=True)
    id_ministerio: Mapped[int | None] = mapped_column(ForeignKey('ministerios.id_ministerio'), nullable=True)
    id_local: Mapped[int | None] = mapped_column(ForeignKey('locais.id_local'), nullable=True)

    
    ministerio = db.relationship('Ministerio', backref=db.backref('reunioes', lazy=True))
    local = db.relationship('Local', backref=db.backref('reunioes', lazy=True))