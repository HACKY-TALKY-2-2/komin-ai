from pydantic import BaseModel


class News(BaseModel):
    title: str
    content: str
    url: str

    class Config:
        orm_mode = True


class Entity(BaseModel):
    name: str
    kpi_1: str | None = None  # TODO: enum으로 변경
    kpi_2: str | None = None
    kpi_3: str | None = None

    news: list[News] = []

    class Config:
        orm_mode = True


class EntityCreate(BaseModel):
    name: str
    kpi_1: str | None = None  # TODO: enum으로 변경
    kpi_2: str | None = None
    kpi_3: str | None = None

    class Config:
        orm_mode = True

class Dashboard(BaseModel):
    dashboard_queue: list[Entity] = []
