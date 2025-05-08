#!/usr/bin/env python3
from app.models.base_model import BaseModel
from sqlalchemy import Column, String, DateTime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship


class Consumer(BaseModel):
    """
    Consumer model definition.
    """
    __tablename__ = 'consumers'
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    school = Column(String(128), nullable=True, default=None)
    profile_picture = Column(String(128), nullable=True, default=None)
    verified_at = Column(DateTime, nullable=True, default=None)
    _password = Column(String(128), nullable=False)

    #*Many
    coupons = relationship('Coupon', back_populates='consumer', lazy='dynamic')

    @property
    def password(self) -> str:
        """
        Getter for the password attribute.
        """
        raise AttributeError("password is not accessible")

    @password.setter
    def password(self, value: Column[str]) -> None:
        """
        Setter for the password attribute.
        """
        if not isinstance(value, str):
            raise TypeError("Password must be a string")
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        self._password = generate_password_hash(value)

    @property
    def verified(self) -> bool:
        """
        Getter for the verified attribute.
        """
        return self.verified_at is not None

    def verify_password(self, password: str) -> bool:
        """
        Verify the provided password against the stored hashed password.
        """
        if not isinstance(password, str):
            raise TypeError("Password must be a string")
        return check_password_hash(str(self._password), password)
