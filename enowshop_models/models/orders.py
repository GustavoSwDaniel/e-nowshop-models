from sqlalchemy import Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy import func, event
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSON, ENUM
from sqlalchemy.ext.mutable import MutableDict
from enowshop_models.base import Base


from enowshop_models.helpers.helpers import generate_data

class Orders(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    uuid = Column(String(36))
    total_amount = Column(Integer())
    installments = Column(Integer, nullable=True)
    payment_method = Column(ENUM('credit_card', 'pix', 'boleto', name='payment_methods_enum'))
    meta_data = Column(MutableDict.as_mutable(JSON))
    status = Column(ENUM('approved', 'pending', 'denied', 'canceled', 'refunded', name='status_enum'), default='pending')
    payment_date = Column(DateTime, nullable=True)
    payment_id = Column(String(), nullable=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    order_items = relationship('OrderItems')
    user_id = Column(Integer, ForeignKey('users.id'))
    address_id = Column(Integer, ForeignKey('users_address.id'))
    address = relationship('UserAddress')


event.listen(Orders, 'before_insert', generate_data)
