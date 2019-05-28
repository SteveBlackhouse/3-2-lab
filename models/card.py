from models import db


class CardModel(db.Model):
    __tablename__ = 'card'

    card_number = db.Column(db.String(17), primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    active_to = db.Column(db.DATE, nullable=False)
    cvv = db.Column(db.SmallInteger, nullable=False)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

    owner_id = db.Column(
        db.Integer,
        db.ForeignKey('user.user_id', onupdate='cascade', ondelete='restrict'),
        nullable=False
    )
    account_number = db.Column(
        db.String(34),
        db.ForeignKey('account.account_number', onupdate='cascade', ondelete='restrict'),
        nullable=False
    )

    owner = db.relationship('UserModel', foreign_keys=owner_id)
    account = db.relationship('AccountModel', foreign_keys=account_number)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
