from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel


class Category(BaseModel):
    """
    Category model definition.
    """
    __tablename__ = 'categories'
    name = Column(String(64), nullable=False)
    slug = Column(String(64), nullable=False, unique=True)
    image_url = Column(String(64), nullable=False)

    # *Many
    merchants = relationship('Merchant', back_populates='category', lazy='dynamic')