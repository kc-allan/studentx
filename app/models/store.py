from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel


class Store(BaseModel):
    __tablename__ = 'stores'
    # Foreign Keys
    merchant_id = ForeignKey('merchants.id', nullable=False)

    # Attributes
    name = Column(String(32), nullable=False)
    location = Column(String(64), nullable=False)
    contact_email = Column(String(128), nullable=False)
    contact_phone = Column(String(16), nullable=True)

    # *One
    merchant = relationship(
        'Merchant', back_populates='stores', lazy='dynamic')
