from sqlalchemy.orm import mapped_column, Mapped
from configs.extensions import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    matricula: Mapped[str] = mapped_column(db.String(15), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(db.String(100), nullable=False)
    email: Mapped[str] = mapped_column(db.String(150), unique=True)
    password: Mapped[str] = mapped_column(db.String(100), nullable=False)
    active: Mapped[bool] = mapped_column(db.Boolean, default=True)
    foto: Mapped[str] = mapped_column(db.String(255), nullable=True)


    def __init__(self, matricula, name, email, password, foto=None, active = True):
        self.matricula = matricula
        self.name = name
        self.email = email
        self.password = password
        self.foto = foto
        self.active = active


    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    @classmethod
    def find_user_by_email(cls,email):
        return User.query.filter_by(email = email).first()
    
    def create_user(self):
        db.session.add(self)
        db.session.commit()

    def get_id(self):
        return str(self.id)


    def user_to_dict(self):
        return {
            "id": self.id,
            "email": self.email
        }
    

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    

