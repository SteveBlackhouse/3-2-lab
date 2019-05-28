from models import db


class AccountModel(db.Model):
    __tablename__ = 'account'

    account_number = db.Column(db.String(34), primary_key=True)
    money = db.Column(db.Float, nullable=False)
    active_to = db.Column(db.DATE, nullable=False)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

    owner_id = db.Column(
        db.Integer,
        db.ForeignKey('user.user_id', onupdate='cascade', ondelete='restrict'),
        nullable=False
    )

    owner = db.relationship('UserModel', foreign_keys=owner_id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
