from models import db


class DepositModel(db.Model):
    __tablename__ = 'deposit'

    deposit_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    amount = db.Column(db.Float, nullable=False)
    month_number = db.Column(db.SmallInteger, nullable=False)
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
