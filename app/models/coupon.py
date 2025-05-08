from sqlalchemy import Column, Integer, String, Text, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel

COUPON_STATUS = {
    "ACTIVE": "active",
    "EXPIRED": "expired",
    "REDEEMED": "redeemed"
}


class Coupon(BaseModel):
    """
    Coupon model definition.
    """
    __tablename__ = 'coupons'
    offer_id = ForeignKey('offers.id', nullable=False)
    consumer_id = ForeignKey('consumers.id', nullable=False)

    coupon_code = Column(String(64), nullable=False, unique=True)
    redeemed_at = Column(DateTime, nullable=True, default=None)
    expiry_date = Column(DateTime, nullable=False)
    status: Column[Enum] = Column(Enum(*COUPON_STATUS.values()),
                    nullable=False, default=COUPON_STATUS['ACTIVE'])
    qr_code = Column(String(128), nullable=True, default=None)

    consumer = relationship('Consumer', back_populates='coupons')
    offer = relationship('Offer', back_populates='coupons')

    @property
    def expired(self):
        """
        Getter for the expired status attribute.
        """
        return self.status == COUPON_STATUS['EXPIRED']

    @property
    def redeemed(self):
        """
        Getter for the redeemed status attribute.
        """
        return self.status == COUPON_STATUS['REDEEMED']

    @property
    def active(self):
        """
        Getter for the active status attribute.
        """
        return self.status == COUPON_STATUS['ACTIVE']
