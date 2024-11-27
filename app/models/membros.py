from configs.extensions import db
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, Text, Date

# Modelo da tabela Membros
class Membro(db.Model):
    __tablename__ = 'membros'
    id_membro: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str | None] = mapped_column(String(100), unique=True, nullable=True)  # Email único e opcional
    telefone: Mapped[str | None] = mapped_column(String(20), nullable=True)  # Telefone opcional
    endereco: Mapped[str | None] = mapped_column(Text, nullable=True)  # Endereço opcional
    data_nascimento: Mapped[Date | None] = mapped_column(nullable=True)  # Data de nascimento opcional
    data_entrada: Mapped[Date | None] = mapped_column(nullable=True)  # Data de entrada opcional