from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime

# ======================
# Esquemas para Device
# ======================

class DeviceBase(BaseModel):
    name: str

class DeviceCreate(DeviceBase):
    pass

class Device(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

# ======================
# Esquemas para ImageElement
# ======================

class ImageElementBase(BaseModel):
    id: str
    data: List[str]  # Aceptamos lista de strings (filas con números separados por espacio)
    device_name: str = Field(..., alias="deviceName")  # Permitimos recibir "deviceName"

    class Config:
        from_attributes = True
        populate_by_name = True  # Esto permite que FastAPI use los aliases al deserializar

class ImageElementCreate(ImageElementBase):
    pass

class ImageElementUpdate(BaseModel):
    device_name: Optional[str] = None
    new_id: Optional[str] = None

class ImageElementOut(BaseModel):
    id: str
    average_before: float
    average_after: float
    data_size: int
    created_at: datetime
    updated_at: datetime
    device_id: int  # o podrías hacer que devuelva el nombre también si haces join

    class Config:
        from_attributes = True

class CreateElementResponse(BaseModel):
    created: List[ImageElementOut]
    errors: Dict[str, str]