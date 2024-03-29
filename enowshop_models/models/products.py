from sqlalchemy import Column, Integer, String, DateTime, Date, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy import func, event
from sqlalchemy.orm import relationship

from enowshop_models.base import Base
from enowshop_models.helpers.helpers import generate_data, generate_uuid


class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    uuid = Column(String(36))
    name = Column(String(255))
    description = Column(String(100))
    price = Column(Integer())
    market = Column(Integer())
    unity = Column(Integer())
    image_url = Column(String(200))
    is_active = Column(Boolean, default=True)
    infos = Column(JSON)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    physical_characteristics = Column(MutableDict.as_mutable(JSON))
    promotion_id = Column(Integer, ForeignKey('promotion.id'), nullable=True)
    category_products = relationship('CategoryProducts', back_populates='product')
    promotion = relationship('Promotion', back_populates='products')

event.listen(Products, 'before_insert', generate_data)
event.listen(Products, 'before_insert', generate_uuid)
