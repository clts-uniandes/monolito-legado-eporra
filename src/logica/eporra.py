from src.modelo.carrera import Carrera
from src.modelo.competidor import Competidor
from src.modelo.apostador import Apostador
from src.modelo.declarative_base import engine, Base, session


class EPorra():

    def __init__(self):
        Base.metadata.create_all(engine)
        self.descripcion = "Descripción de la aplicación"
        self.competidores = []
    
    def darDescripcionAplicacion(self):
        return self.descripcion
    
    def darListaCarreras(self):
        listaCarrreras = [elem.__dict__ for elem in session.query(Carrera).all()]
        return listaCarrreras
    
    def darCarrera(self, id_carrera):
        return session.query(Carrera).get(id_carrera).__dict__

    def darUltimaCarrera(self):
        carrera = session.query(Carrera).order_by(Carrera.id.desc()).first()
        return carrera

    def crearCarrera(self, nombre, competidores):#crea nueva carrera en db solo si la data provista en pantalla es valida, crearCompetidor lo dispara la interfaz por aparte!
        carreraExistente = session.query(Carrera).filter(Carrera.nombre == nombre).all()
        if len(carreraExistente) > 0:
            return 0
        if nombre == "" or nombre == None:
            return 0
        probabilidadTotal = 0.0
        for competidor in competidores:
            probabilidadTotal += competidor["Probabilidad"]
        if probabilidadTotal != 1:
            return 0
        carrera = Carrera(nombre=nombre, estaTerminada=False)
        session.add(carrera)
        session.flush()#genera id de carrera pero sin persistir en db
        session.refresh(carrera)
        session.commit()
        return carrera.id

    def darListaCompetidores(self, id = ""):
        competidores = [elem.__dict__ for elem in session.query(Competidor).filter(Carrera.id.in_([id])).all()] 
        return competidores
    
    def crearCompetidor(self, carrera_actual, nombree, probabilidadd):
        if not nombree or not probabilidadd:
            return False
        competidorExistente = session.query(Competidor).filter(Competidor.nombre == nombree).all()
        if len(competidorExistente) > 0:
            return False
        carreraPadre = session.query(Carrera).filter(Carrera.id == carrera_actual).first()
        carreraPadre.competidores.append(Competidor(nombre=nombree, probabilidad=probabilidadd))
        session.commit()
        return True
    
    def darListaApostadores(self):
        listaApostadores = [elem.__dict__ for elem in session.query(Apostador).all()]
        return listaApostadores



