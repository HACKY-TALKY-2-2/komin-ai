from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from data.database import Base


class Entity(Base):
    __tablename__ = "entity"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    kpi_1 = Column(String, nullable=True)
    kpi_2 = Column(String, nullable=True)
    kpi_3 = Column(String, nullable=True)


class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    url = Column(String, nullable=False)

    entity_id = Column(Integer, ForeignKey('entity.id'))
    entity = relationship("Entity", backref="news")

