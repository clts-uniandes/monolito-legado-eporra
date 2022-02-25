from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .declarative_base import Base

class Aplicacion(Base):

    __tablename__ = 'aplicacion'

    id = Column(Integer, primary_key=True)
    descripcion = Column(String)

    carrera = relationship('Carrera', cascade='all, delete')