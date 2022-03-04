from sqlalchemy import Column, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .declarative_base import Base

class Apuesta(Base):

    __tablename__ = "apuesta"

    id = Column(Integer, primary_key=True)
    valor = Column(Float)
    apostador_id = Column(Integer, ForeignKey('apostador.id'))
    carrera_id = Column(Integer, ForeignKey('carrera.id'))
    competidor_id = Column(Integer, ForeignKey('competidor.id'))

    apostador = relationship("Apostador", back_populates="apuestas")
    carrera = relationship("Carrera", back_populates="apuestas")
    competidores = relationship("Competidor")

