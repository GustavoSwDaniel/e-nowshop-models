from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import func

from enowshop_models.base import Base


class EmployeesPermissions(Base):
    __tablename__ = 'employees_permissions'
    
    id = Column(Integer, primary_key=True)
    uuid = Column(String(36))
    employee_id = Column(Integer)
    permission_id = Column(Integer)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    employee_id = relationship('Employees')
    permission_id = relationship('Permissions')
