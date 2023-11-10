from fastapi import APIRouter, Depends
from data.database import get_db
from data.models import Entity, News
from starlette import status
from sqlalchemy.orm import Session
from entity.dashboard_entity import Dashboard, EntityCreate, News


router = APIRouter(prefix='/chatbot')


@router.post("/{token}", summary='')
def post_user_chat(token: str, body: dict):

    return {
        "result": body
    }
