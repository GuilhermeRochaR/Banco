from configs.extensions import db
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey

from datetime import time, date
class Request(db.Model):
    __tablename__ = 'requests'

    id: Mapped[str] = mapped_column(primary_key=True)
    usuarioId: Mapped[str] =  mapped_column(db.String(255), ForeignKey('user.id'), nullable=False)
    lugares: Mapped[int] =  mapped_column(db.Integer, nullable=False)
    motivo: Mapped[str] =  mapped_column(db.String(255), nullable=False)
    status: Mapped[str] =  mapped_column(db.String(255), nullable=False)
    permanente: Mapped[bool] =  mapped_column(db.Boolean, nullable=False)
    idSetor: Mapped[str] =  mapped_column(db.String(255), ForeignKey('sector.id'), nullable=False)
    data: Mapped[date] =  mapped_column(db.Date, nullable=False)
    inicio: Mapped[time] =  mapped_column(db.Time, nullable=False)
    fim: Mapped[time] =  mapped_column(db.Time, nullable=False)

    usuario = db.relationship('User', backref=db.backref('requests', lazy=True))
    setor = db.relationship('Sector', backref=db.backref('requests', lazy=True))

    def __init__(self, usuarioId: str, lugares: int, motivo: str, status: str, permanente: bool, idSetor: str, data: date, inicio: time, fim: time):
        self.usuarioId = usuarioId
        self.lugares = lugares
        self.motivo = motivo
        self.status = status
        self.permanente = permanente
        self.idSetor = idSetor
        self.data = data
        self.inicio = inicio
        self.fim = fim

    @staticmethod
    def get_all_requests():
        """
        Retorna uma lista de todas as solicitações no formato de dicionário.
        """
        requests = Request.query.all()
        return [
            {
                "id": request.id,
                "usuarioId": request.usuarioId,
                "lugares": request.lugares,
                "motivo": request.motivo,
                "status": request.status,
                "permanente": request.permanente,
                "idSetor": request.idSetor,
                "data": str(request.data),
                "inicio": str(request.inicio),
                "fim": str(request.fim),
                "usuario": request.usuario.name if request.usuario else None,
                "setor": request.setor.nome if request.setor else None,
            }
            for request in requests
        ]
