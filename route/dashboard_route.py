from fastapi import APIRouter, Depends
from data.database import get_db
from data.models import Entity, News
from starlette import status
from sqlalchemy.orm import Session
from entity.dashboard_entity import Dashboard, EntityCreate, News
import openai, os


router = APIRouter(prefix='/dashboard')
dashboard = []

openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_response(prompt, model="gpt-4-1106-preview"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content

@router.get("/config", summary='')
def get_dashboard_config():
    return dashboard


@router.put("/config", summary='', status_code=status.HTTP_204_NO_CONTENT)
def update_dashboard_config(dashboard_update: str):
    prompt = """
  당신은 똑똑한 비서입니다.
%% %% 사이는 당신에게 주어진 명령입니다.
당신은 여러 회사들의 순서를 나열하고, 이를 형식화하는 임무를 수행할 것입니다.
예를 들어, "대시보드를 영풍제지, 남양유업, 에코프로 순으로 정렬해 줘" 라는 명령을 받았을 때 당신은 영풍제지, 남양유업, 에코프로의 순서로 정렬해야 합니다.   단어, 콤마 외에 아무 것도 작성하지 마십시오
%%
{0}
%%
"""
    result = generate_response(prompt.format(dashboard_update), model="gpt-4-1106-preview")
    global dashboard
    dashboard = [x.strip() for x in result.split(",")]


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


@router.delete("/entity/{name}", summary='', status_code=status.HTTP_204_NO_CONTENT)
def delete_dashboard(name: str, db: Session = Depends(get_db)):
    db.query(Entity).filter(Entity.name == name).delete()
    db.commit()
