from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Device(Base):
    __tablename__ = "devices"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)

    elements = relationship("ImageElement", back_populates="device")

class ImageElement(Base):
    __tablename__ = "image_elements"
    
    id = Column(String, primary_key=True, index=True)  # ID externo tipo "aabbcc1"
    device_id = Column(Integer, ForeignKey("devices.id"), nullable=False)

    average_before = Column(Float, nullable=False)
    average_after = Column(Float, nullable=False)
    data_size = Column(Integer, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    device = relationship("Device", back_populates="elements")
