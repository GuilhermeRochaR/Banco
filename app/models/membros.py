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

    def __init__(self, id_membro: int, nome: str, email: str, telefone: str, endereco: str, data_nascimento: Date, data_entrada: Date):
        self.id_membro = id_membro
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.data_nascimento = data_nascimento
        self.data_entrada = data_entrada

        @staticmethod
        def get_todos_membros():
            membros = Membro.query.all()

            for membro in membros:
                print(f"ID: {membro.id_membro}, Nome: {membro.nome}, Email: {membro.email}")