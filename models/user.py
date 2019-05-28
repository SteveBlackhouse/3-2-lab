from models import db


class UserModel(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    money = db.Column(db.Float, nullable=False, default=0.0)
    birth_date = db.Column(db.DATE)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
