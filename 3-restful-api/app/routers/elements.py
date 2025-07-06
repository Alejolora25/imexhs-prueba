from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional

from .. import models, schemas, crud
from ..database import get_db

from datetime import datetime


router = APIRouter(prefix="/api/elements", tags=["Image Elements"])

# === CREATE ===
@router.post("/", response_model=schemas.CreateElementResponse)
def create_element(payload: dict, db: Session = Depends(get_db)):
    created_items = []
    errors = {}

    for key, item in payload.items():
        try:
            element_data = schemas.ImageElementBase(**item)
            new_element = crud.create_image_element(db, element_data)
            created_items.append(new_element)
        except ValueError as ve:
            errors[key] = f"Validation error: {str(ve)}"
        except HTTPException as he:
            errors[key] = f"HTTP error: {str(he.detail)}"
        except Exception as e:
            errors[key] = f"Internal error: {str(e)}"

    return {"created": created_items, "errors": errors}


# === GET ALL ===
@router.get("/", response_model=list[schemas.ImageElementOut])
def get_elements(
    created_from: Optional[datetime] = Query(None),
    created_to: Optional[datetime] = Query(None),
    updated_from: Optional[datetime] = Query(None),
    updated_to: Optional[datetime] = Query(None),
    avg_before_gt: Optional[float] = Query(None),
    avg_before_lt: Optional[float] = Query(None),
    avg_after_gt: Optional[float] = Query(None),
    avg_after_lt: Optional[float] = Query(None),
    data_size_gt: Optional[int] = Query(None),
    data_size_lt: Optional[int] = Query(None),
    db: Session = Depends(get_db)
):
    filters = {k: v for k, v in  {
        "created_from": created_from,
        "created_to": created_to,
        "updated_from": updated_from,
        "updated_to": updated_to,
        "avg_before_gt": avg_before_gt,
        "avg_before_lt": avg_before_lt,
        "avg_after_gt": avg_after_gt,
        "avg_after_lt": avg_after_lt,
        "data_size_gt": data_size_gt,
        "data_size_lt": data_size_lt
    }.items() if v is not None}
    elements = crud.get_all_elements(db, filters)
    return elements

# === GET ONE ===
@router.get("/{element_id}", response_model=schemas.ImageElementOut)
def get_element_by_id(element_id: str, db: Session = Depends(get_db)):
    element = crud.get_image_element(db, element_id)
    if not element:
        raise HTTPException(status_code=404, detail="Elemento no encontrado.")
    return element

# === UPDATE ===
@router.put("/{element_id}", response_model=schemas.ImageElementOut)
def update_element(element_id: str, updates: schemas.ImageElementUpdate, db: Session = Depends(get_db)):
    updated = crud.update_image_element(db, element_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail="Elemento no encontrado.")
    return updated

# === DELETE ===
@router.delete("/{element_id}")
def delete_element(element_id: str, db: Session = Depends(get_db)):
    deleted = crud.delete_image_element(db, element_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Elemento no encontrado.")
    return {"detail": f"Elemento {element_id} eliminado correctamente."}
