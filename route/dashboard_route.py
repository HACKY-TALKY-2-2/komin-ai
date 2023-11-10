from fastapi import APIRouter, Depends
from data.database import get_db
from data.models import Entity, News
from sqlalchemy.orm import Session
from entity.dashboard_entity import Dashboard, Entity, EntityCreate, News


router = APIRouter(prefix='dashboard')


@router.get("/", summary='', response_model=list[Entity])
def get_entity_list(db: Session = Depends(get_db)):
    entity_list = db.query(Entity).order_by(Entity.id).all()
    return entity_list


@router.get("/config", summary='')
def get_dashboard_config():
    return {"message": "Hello World"}


@router.post("/config", summary='')
def create_dashboard_config():
    return {"message": "Hello World"}


@router.put("/config", summary='')
def update_dashboard_config():
    return {"message": "Hello World"}


@router.get("/{id}", summary='')
def get_dashboard(id: int):
    return {"message": "Hello World"}


@router.post("{id}", summary='')
def create_entity(entity_create: EntityCreate, db: Session = Depends(get_db)):   # TODO: KPI들 받기
    new_entity = Entity(name=entity_create.name)
    db.add(new_entity)
    db.commit()
    return {"message": "Hello World"}


@router.put("{id}", summary='')
def update_dashboard(id: int):
    return {"message": "Hello World"}


@router.delete("{id}", summary='')
def delete_dashboard(id: int):
    return {"message": "Hello World"}
