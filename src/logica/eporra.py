from src.modelo.carrera import Carrera
from src.modelo.competidor import Competidor
from src.modelo.declarative_base import engine, Base, session


class EPorra():

    def __init__(self):
        Base.metadata.create_all(engine)
        #self.descripcion = "Descipcion de la aplicaion"
        self.competidores = []

    
    def darDescripcionAplicacion(self):
        return self.descripcion
    
    def darListaCarreras(self):
        listaCarrreras = [elem.__dict__ for elem in session.query(Carrera).all()]
        return listaCarrreras
    
    def darCarrera(self, tets):
        carrera = session.query(Carrera).order_by(Carrera.id.desc()).first()
        return carrera.__dict__

    def darUltimaCarrera(self):
        carrera = session.query(Carrera).order_by(Carrera.id.desc()).first()
        return carrera

    def crearCarrera(self, nombre, competidores = [], estaTerminada = False):
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
            if totalProbabilidades > 1:
                return False

        if nombre == -1:
            ultimaCarrera = self.darUltimaCarrera()
            ultimaCarrera.competidores = listaCompetidores
            session.commit()
            return True
        
        carrera = Carrera(nombre=nombre, estaTerminada=estaTerminada)
        carrera.competidores = listaCompetidores
        session.add(carrera)
        session.commit()
        if carrera.id != None:
            return True
        return False

    def darListaCompetidores(self, id = ""):
        competidores = [elem.__dict__ for elem in session.query(Competidor).filter(Carrera.id.in_([id])).all()] 
        return competidores
    
    def crearCompetidor(self, carrera_actual, nombre, probabilidad):
        if not nombre or not probabilidad:
            return False
        for competidorExistente in self.competidores:
            if competidorExistente["Nombre"] == nombre:
                return False
        self.competidores.append({"Nombre": nombre, "Probabilidad": probabilidad})
        self.crearCarrera(carrera_actual, self.competidores)
        return True



