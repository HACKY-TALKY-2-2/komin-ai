from fastapi import APIRouter, Depends
from data.database import get_db
from data.models import Entity, News
from starlette import status
from sqlalchemy.orm import Session
from entity.dashboard_entity import Dashboard, EntityCreate, News


router = APIRouter(prefix='/dashboard')
dashboard = Dashboard(dashboard_queue=[])


@router.get("/config", summary='', response_model=Dashboard)
def get_dashboard_config():
    return dashboard


@router.put("/config", summary='', status_code=status.HTTP_204_NO_CONTENT)
def update_dashboard_config(dashboard_update: Dashboard):
    dashboard = dashboard_update


@router.get("/entity", summary='', response_model=list[EntityCreate])
def get_entity_list(db: Session = Depends(get_db)):
    entity_list = db.query(Entity).order_by(Entity.id).all()
    return entity_list


@router.get("/entity/{name}", summary='', response_model=EntityCreate)
def get_dashboard(name: str, db: Session = Depends(get_db)):
    entity = db.query(Entity).filter(Entity.name == name).first()
    return entity


@router.post("/entity", summary='', status_code=status.HTTP_204_NO_CONTENT)
def create_entity(entity_create: EntityCreate, db: Session = Depends(get_db)):   # TODO: KPI들 받기
    new_entity = Entity(name=entity_create.name,
                        kpi_1=entity_create.kpi_1, kpi_2=entity_create.kpi_2, kpi_3=entity_create.kpi_3)
    db.add(new_entity)
    db.commit()


@router.put("/entity", summary="", status_code=status.HTTP_204_NO_CONTENT)
def update_dashboard(entity_update: EntityCreate, db: Session = Depends(get_db)):
    entity = db.query(Entity).filter(Entity.id == entity_update.id).first()
    entity.kpi_1 = entity_update.kpi_1
    entity.kpi_2 = entity_update.kpi_2
    entity.kpi_3 = entity_update.kpi_3
    db.add(entity)
    db.commit()


@router.delete("entity/{name}", summary='', status_code=status.HTTP_204_NO_CONTENT)
def delete_dashboard(name: str, db: Session = Depends(get_db)):
    db.query(Entity).filter(Entity.name == name).delete()
    db.commit()
