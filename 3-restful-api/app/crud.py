from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from datetime import datetime

from . import models, schemas

# ========== UTILS ==========

def parse_and_validate_data(data: list[str]) -> list[list[int]]:
    parsed_data = []

    for row in data:
        try:
            numbers = list(map(int, row.strip().split()))
        except ValueError:
            raise ValueError(f"Valores no numéricos encontrados en: '{row}'")
        parsed_data.append(numbers)

    return parsed_data

def normalize_data(data: list[list[int]]) -> tuple[list[list[float]], float, float]:
    flat = [num for row in data for num in row]
    if not flat:
        raise ValueError("No hay datos para normalizar.")
    
    max_val = max(flat)
    if max_val == 0:
        raise ValueError("El valor máximo de los datos es cero; no se puede normalizar.")

    avg_before = sum(flat) / len(flat)
    normalized = [[round(x / max_val, 4) for x in row] for row in data]
    flat_norm = [num for row in normalized for num in row]
    avg_after = sum(flat_norm) / len(flat_norm)

    return normalized, avg_before, avg_after

# ========== CRUD ==========

def get_or_create_device(db: Session, name: str) -> models.Device:
    device = db.query(models.Device).filter(models.Device.name == name).first()
    if device:
        return device
    device = models.Device(name=name)
    db.add(device)
    db.commit()
    db.refresh(device)
    return device

def create_image_element(db: Session, element: schemas.ImageElementBase) -> models.ImageElement:
    try:
        parsed = parse_and_validate_data(element.data)
        normalized, avg_before, avg_after = normalize_data(parsed)
        data_size = sum(len(row) for row in parsed)

        device = get_or_create_device(db, element.device_name)

        db_element = models.ImageElement(
            id=element.id,
            device_id=device.id,
            average_before=avg_before,
            average_after=avg_after,
            data_size=data_size,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        db.add(db_element)
        db.commit()
        db.refresh(db_element)
        return db_element

    except IntegrityError:
        db.rollback()
        raise ValueError(f"Ya existe un elemento con id '{element.id}'")


def get_image_element(db: Session, id: str):
    return db.query(models.ImageElement).filter(models.ImageElement.id == id).first()

def get_all_elements(db: Session, filters: dict = {}):
    query = db.query(models.ImageElement)

    if 'created_from' in filters:
        query = query.filter(models.ImageElement.created_at >= filters['created_from'])
    if 'created_to' in filters:
        query = query.filter(models.ImageElement.created_at <= filters['created_to'])
    if 'updated_from' in filters:
        query = query.filter(models.ImageElement.updated_at >= filters['updated_from'])
    if 'updated_to' in filters:
        query = query.filter(models.ImageElement.updated_at <= filters['updated_to'])
    if 'avg_before_gt' in filters:
        query = query.filter(models.ImageElement.average_before > filters['avg_before_gt'])
    if 'avg_before_lt' in filters:
        query = query.filter(models.ImageElement.average_before < filters['avg_before_lt'])
    if 'avg_after_gt' in filters:
        query = query.filter(models.ImageElement.average_after > filters['avg_after_gt'])
    if 'avg_after_lt' in filters:
        query = query.filter(models.ImageElement.average_after < filters['avg_after_lt'])
    if 'data_size_gt' in filters:
        query = query.filter(models.ImageElement.data_size > filters['data_size_gt'])
    if 'data_size_lt' in filters:
        query = query.filter(models.ImageElement.data_size < filters['data_size_lt'])

    return query.all()

def update_image_element(db: Session, element_id: str, updates: schemas.ImageElementUpdate):
    db_element = get_image_element(db, element_id)
    if not db_element:
        return None

    if updates.device_name:
        device = get_or_create_device(db, updates.device_name)
        db_element.device_id = device.id
    if updates.new_id:
        db_element.id = updates.new_id

    db_element.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_element)
    return db_element

def delete_image_element(db: Session, element_id: str):
    element = get_image_element(db, element_id)
    if not element:
        return None
    db.delete(element)
    db.commit()
    return element
