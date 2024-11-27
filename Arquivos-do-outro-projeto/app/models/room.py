from configs.extensions import db
from sqlalchemy.orm import mapped_column, Mapped

class Room(db.Model):
    __tablename__ = 'rooms'

    id: Mapped[int] = mapped_column(primary_key=True)
    descricao: Mapped[str] = mapped_column(db.String(255), nullable=False)
    assentos: Mapped[int] = mapped_column(db.Integer, nullable=False)
    setor_id: Mapped[int] = mapped_column(db.ForeignKey('sector.id'), nullable=False)

    setor = db.relationship('Sector', backref=db.backref('rooms', lazy=True)) 

    def __init__(self, descricao: str, assentos: int, setor_id: int):
        self.descricao = descricao
        self.assentos = assentos
        self.setor_id = setor_id

    def create_room(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all_rooms():
        results = Room.query.all()
        return [
            {"id": room.id, "descricao": room.descricao, "assentos": room.assentos, "setor_id": room.setor_id}
            for room in results
        ]