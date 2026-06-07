from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, String, Float

class Base(DeclarativeBase):
    pass

class Audit(Base):
    __tablename__ = 'audits'

    id = Column(String, primary_key=True)
    domain = Column(String, nullable=False)
    pvs_score = Column(Float, default=0)
