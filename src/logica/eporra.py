from src.modelo.carrera import Carrera
from src.modelo.competidor import Competidor
from src.modelo.declarative_base import engine, Base, session


class EPorra():

    def __init__(self):
        Base.metadata.create_all(engine)
        self.descripcion = "Descipcion de la aplicaion"

    
    def darDescripcionAplicacion(self):
        return self.descripcion
    
    def darListaCarreras(self):# SI Interesa
        return None

    def crearCarrera(self, nombre, estaTerminada, competidores):
        listaCompetidores = [] 
        for item in competidores:
            competidor = Competidor(nombre=item["Nombre"], probabilidad=item["Probabilidad"])
            session.add(competidor)
            listaCompetidores.append(competidor)
        carrera = Carrera(nombre=nombre, estaTerminada=estaTerminada)
        carrera.competidores = listaCompetidores
        session.add(carrera)
        session.commit()
        if carrera.id != None:
            return True
        return False

    def darListaCompetidores(self, id): # SI Interesa
        return None
    
    def crearCompetidor(self, id, nombre, probabilidad):# SI Interesa
        return None



