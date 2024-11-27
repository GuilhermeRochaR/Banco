from configs.extensions import db
from sqlalchemy.orm import mapped_column, Mapped

class Sector(db.Model):
    __tablename__ = 'sector'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(db.String(120), nullable=False)
    nomeAmigavel: Mapped[str] = mapped_column(db.String(120), nullable=False)
    polo_id: Mapped[int] = mapped_column(db.ForeignKey('polos.id'), nullable=False)

    polo = db.relationship('Polo', backref=db.backref('sectors', lazy=True))

    def __init__(self, nome: str, nomeAmigavel: str):
        self.nome = nome
        self.nomeAmigavel = nomeAmigavel

    def create_sector(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all_sectors():
        results = Sector.query.all()
        return [
            {"id": sector.id, "nome": sector.nome, "nomeAmigavel": sector.nomeAmigavel}
            for sector in results
        ]
