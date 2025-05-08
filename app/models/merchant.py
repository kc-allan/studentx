from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel


class Merchant(BaseModel):
    """
    Vendor model definition.
    """
    __tablename__ = 'merchants'
    # Foreign keys
    category_id = ForeignKey('categories.id', nullable=False)

    # Attributes
    email = Column(String(128), nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    logo = Column(String(128), nullable=True, default=None)
    website = Column(String(128), nullable=True, default=None)
    preferred_currency = Column(String(8), nullable=True, default=None)
    approved_on = Column(DateTime, nullable=True, default=None)

    # *One
    category = relationship('Category', back_populates='merchants')

    # *Many
    stores = relationship('Store', back_populates='merchant', lazy='dynamic')
    offers = relationship(
        'Offer', back_populates='merchant', lazy='dynamic')

    @property
    def approved(self) -> bool:
        """
        Getter for the approved attribute.
        """
        return self.approved_on is not None
