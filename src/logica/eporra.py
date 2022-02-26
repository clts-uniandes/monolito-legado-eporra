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
        listaCarrreras = session.query(Carrera).all()
        return listaCarrreras

    def crearCarrera(self, nombre, estaTerminada, competidores):
        carreraExistente = session.query(Carrera).filter(Carrera.nombre == nombre).all()
        if len(carreraExistente) > 0:
            return False
        if nombre == "" or nombre == None:
            return False
        listaCompetidores = []
        totalProbabilidades = 0.0
        for item in competidores:
            competidor = Competidor(nombre=item["Nombre"], probabilidad=item["Probabilidad"])
            session.add(competidor)
            listaCompetidores.append(competidor)
            totalProbabilidades = totalProbabilidades + item["Probabilidad"]
            if totalProbabilidades > 1.0:
                return False
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



