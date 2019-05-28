from models import db


class CreditPaymentModel(db.Model):
    __tablename__ = 'credit_payment'

    payment_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

    credit_id = db.Column(
        db.BigInteger,
        db.ForeignKey('credit.credit_id', onupdate='cascade', ondelete='restrict'),
        nullable=False
    )
    credit = db.relationship('CreditModel', foreign_keys=credit_id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
