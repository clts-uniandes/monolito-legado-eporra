from tokenize import Double
from xmlrpc.client import Boolean
from sqlalchemy import Column, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .declarative_base import Base

class Competidor(Base):

    __tablename__ = 'competidor'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    probabilidad = Column(Float)
    carrera_id = Column(Integer, ForeignKey('carrera.id'))

    carrera = relationship("Carrera", back_populates="competidores")
    apuesta = relationship("Apuesta", back_populates="competidores")