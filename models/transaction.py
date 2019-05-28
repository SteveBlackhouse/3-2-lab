from models import db


class TransactionModel(db.Model):
    __tablename__ = 'transaction'

    transaction_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

    author_account = db.Column(
        db.String(34),
        db.ForeignKey('account.account_number', onupdate='cascade', ondelete='restrict'),
        nullable=False
    )
    receiver_account = db.Column(
        db.String(34),
        db.ForeignKey('account.account_number', onupdate='cascade', ondelete='restrict'),
        nullable=False
    )

    author = db.relationship('AccountModel', foreign_keys=author_account)
    receiver = db.relationship('AccountModel', foreign_keys=receiver_account)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
