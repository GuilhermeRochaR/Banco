from configs.extensions import db
from sqlalchemy.orm import mapped_column, Mapped


class Equipment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(120), nullable=False)

    def __init__(self, name: str):
        self.name = name

    def create_equipment(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all_equipments():
        equipment_list = list()
        results = Equipment.query.all()
        for row in results:
            r = {
                "name": row.name
            }
            equipment_list.append(r)

        return equipment_list
    
