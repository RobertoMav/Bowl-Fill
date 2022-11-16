from sqlalchemy.orm import Session

from . import models, schemas

def get_data(db: Session, image_name: str):
    return db.query(models.Data).filter(models.Data.image == image_name).first()

def get_all_data(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Data).offset(skip).limit(limit).all()

def create_data(db: Session, data: schemas.DataCreate):
    db_data = models.Data(image=data.image, output=data.output)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data