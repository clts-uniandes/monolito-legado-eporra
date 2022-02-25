from xmlrpc.client import Boolean
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .declarative_base import Base

class Carrera(Base):

    __tablename__ = 'aplicacion'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    estaTerminada = Column(Boolean)

    competidores = relationship('Competidor', cascade='all, delete, delete-orphan')