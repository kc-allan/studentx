from sqlalchemy import Column, Integer, String, ForeignKey, Text, Enum, DateTime, CheckConstraint
from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel

DISCOUNT_TYPES = {
    "PERCENTAGE": "percentage",
    "FIXED_AMOUNT": "fixed_amount",
    "BUY_ONE_GET_ONE": "buy_one_get_one",
    "FREE_ITEM": "free_item"
}

OFFER_STATUS = {
    "ACTIVE": "active",
    "INACTIVE": "inactive",
    "EXPIRED": "expired",
    "SOLD_OUT": "sold_out"
}


class Offer(BaseModel):
    """
    CouponDeal model definition.
    """
    __tablename__ = 'offers'
    # Foreign Keys
    merchant_id = ForeignKey('merchants.id', nullable=False)

    # Attributes
    title = Column(String(64), nullable=False)
    description = Column(String(256), nullable=False)
    slug = Column(String(64), nullable=False, unique=True)
    discount_type: Column[Enum] = Column(
        Enum(*DISCOUNT_TYPES.values()), nullable=False)
    discount_value = Column(Integer, nullable=False)
    currency = Column(String(3), nullable=False)
    status: Column[Enum] = Column(
        Enum(*OFFER_STATUS.values()),
        nullable=False, default=OFFER_STATUS["ACTIVE"])
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    terms_and_conditions = Column(Text, nullable=True)
    featured_until = Column(DateTime, nullable=True, default=None)
    highlighted_until = Column(DateTime, nullable=True, default=None)

    # *One
    merchant = relationship('Merchant', back_populates='offers')

    # *Many
    coupons = relationship('Coupon', back_populates='offer', lazy='dynamic')

    # Constraints
    __table_args__ = (
        CheckConstraint('end_date > start_date', name='check_end_after_start'),
        CheckConstraint('featured_until > start_date',
                        name='check_featured_after_start'),
        CheckConstraint('highlighted_until > start_date',
                        name='check_highlighted_after_start'),
        CheckConstraint('end_date > featured_until',
                        name='check_end_after_featured'),
        CheckConstraint('end_date > highlighted_until',
                        name='check_end_after_highlighted'),
        CheckConstraint('featured_until > highlighted_until',
                        name='check_featured_after_highlighted'),
        CheckConstraint(
            "(status != 'active') OR (start_date <= CURRENT_TIMESTAMP)",
            name='check_start_for_active'),
    )

    @property
    def featured(self):
        """
        Getter for the featured status attribute.
        """
        return self.featured_until is not None

    @property
    def highlighted(self):
        """
        Getter for the highlighted status attribute.
        """
        return self.highlighted_until is not None
