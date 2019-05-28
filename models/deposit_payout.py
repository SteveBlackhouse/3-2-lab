from models import db


class DepositPayoutModel(db.Model):
    __tablename__ = 'deposit_payout'

    payment_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

    deposit_id = db.Column(
        db.BigInteger,
        db.ForeignKey('deposit.deposit_id', onupdate='cascade', ondelete='restrict'),
        nullable=False
    )
    deposit = db.relationship('DepositModel', foreign_keys=deposit_id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
