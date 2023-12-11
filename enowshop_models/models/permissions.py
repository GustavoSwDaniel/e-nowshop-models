from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import func, event

from enowshop_models.base import Base
from enowshop_models.helpers.helpers import generate_uuid, generate_data

class Permissions(Base):
    __tablename__ = 'permissions'
    
    id = Column(Integer, primary_key=True)
    uuid = Column(String(36))
    name = Column(String(50))
    description = Column(String(100))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
