from configs.extensions import db
from sqlalchemy.orm import mapped_column, Mapped


class Polo(db.Model):
    __tablename__ = 'polos'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(120), nullable=False)

    def __init__(self, name: str):
        self.name = name

    def create_polo(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all_polos():
        polo_list = list()
        results = Polo.query.all()
        for row in results:
            r = {
                "name": row.name
            }
            polo_list.append(r)

        return polo_list
