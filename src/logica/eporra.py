from src.modelo.carrera import Carrera
from src.modelo.competidor import Competidor
from src.modelo.apostador import Apostador
from src.modelo.apostador import Apuesta
from src.modelo.declarative_base import engine, Base, session


class EPorra():

    def __init__(self):
        Base.metadata.create_all(engine)
        self.descripcion = "Descripción de la aplicación"
        self.competidores = []
    
    def darDescripcionAplicacion(self):
        return self.descripcion
    
    def darListaCarreras(self):
        listaCarrreras = [elem.__dict__ for elem in session.query(Carrera).order_by(Carrera.nombre).all()]
        return listaCarrreras
    
    def darCarrera(self, id_carrera):
        carrera = session.query(Carrera).get(id_carrera)
        return carrera
        
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

    def eliminarCarrera(self, idCarrera = 0):
        if idCarrera == 0:
            return False
        carreraAEliminar = self.darCarrera(idCarrera)
        if carreraAEliminar is None:
            return False
        carreraC = self.darApuestasCarrera(idCarrera)
        if len(carreraC) > 0:
            return False
        session.delete(carreraAEliminar)
        session.commit()
        return True

    def darListaCompetidores(self, idCarrera = 0):
        listaCompetidores = session.query(Competidor.id.label("id"), Competidor.nombre.label("Nombre"), Competidor.probabilidad.label("Probabilidad"), Competidor.carrera_id.label("idCarrera")).filter(Competidor.carrera_id == idCarrera).all() 
        return [dict(zip(v.keys(), v)) for v in listaCompetidores]
    
    def crearCompetidor(self, carrera_actual, nombree, probabilidadd):
        if not nombree or not probabilidadd:
            return False
        competidorExistente = session.query(Competidor).filter(Competidor.nombre == nombree, Competidor.carrera_id == carrera_actual).all()
        if len(competidorExistente) > 0:
            return False
        carreraPadre = session.query(Carrera).filter(Carrera.id == carrera_actual).first()
        carreraPadre.competidores.append(Competidor(nombre=nombree, probabilidad=probabilidadd))
        session.commit()
        return True
    
    def crearApostador(self, nombreApostador):
        if not nombreApostador:
            return False
        apostadorExistente = session.query(Apostador).filter(Apostador.nombre == nombreApostador).all()
        if len(apostadorExistente) > 0:
            return False
        nuevoApostador=Apostador(nombre=nombreApostador)
        session.add(nuevoApostador)
        session.commit()
        return True
    
    def darListaApostadores(self):
        listaApostadores = session.query(Apostador.nombre.label("Nombre")).order_by(Apostador.nombre)
        
        return [dict(zip(v.keys(), v)) for v in listaApostadores]
    
    def validarApuesta(self, apostador, idCarrera, valorApuesta, Competidor): 
        if valorApuesta is None:
            return False
        if valorApuesta < 1:
            return False
        if not apostador:
            return False
        if not Competidor:
            return False
        return True

    def crearApuesta(self, nombre_apostador, id_carrera, valor_apuesta, nombre_competidor):
        validar = self.validarApuesta(nombre_apostador, id_carrera, valor_apuesta, nombre_competidor)
        if validar == False:
            return False
        apostador = session.query(Apostador).filter(Apostador.nombre == nombre_apostador).first()
        competidor = session.query(Competidor).filter(Competidor.nombre == nombre_competidor, Competidor.carrera_id == id_carrera).first()
        apuesta = Apuesta(valor=valor_apuesta, apostador_id=apostador.id, carrera_id=id_carrera, competidor_id=competidor.id)
        session.add(apuesta)
        session.commit()
        return True

    def darApuesta (self, idCarrera, idApuesta = 0):
        apuesta = session.query(Apostador.nombre.label("Apostador"), Apuesta.valor.label("Valor"), Competidor.nombre.label("Competidor")).filter(Apuesta.id == idApuesta, Carrera.id == idCarrera).join(Carrera, Apuesta.carrera_id == Carrera.id).join(Competidor, Competidor.id == Apuesta.competidor_id).join(Apostador, Apostador.id == Apuesta.apostador_id).first()
        if(apuesta == None):
            return False
        return dict(zip(apuesta.keys(), apuesta))
    
    def editarApuesta (self, idApuesta, apostador, nombreCarrera, valor, competidor):
        validar = self.validarApuesta(apostador, idApuesta, valor, competidor)
        if validar == False:
            return False
        apostador = session.query(Apostador).filter(Apostador.nombre == apostador).first()
        if apostador == None:
            return False
        competidor = session.query(Competidor).filter(Competidor.nombre == competidor).first()
        if competidor == None:
            return False
        resultadoEdicion = session.query(Apuesta).filter(Apuesta.id == idApuesta).update({"competidor_id": competidor.id, "valor": valor, "apostador_id": apostador.id})
        session.commit()
        if resultadoEdicion == None:
            return False
        return resultadoEdicion

    def darApuestasCarrera(self, idCarrera):
        listaApuestas = session.query(Apuesta.id.label("Id"), Competidor.id.label("CompetidorId"),Competidor.nombre.label("Competidor"), Apuesta.valor.label("Valor"), Apostador.id.label("ApostadorId"), Apostador.nombre.label("Apostador")).filter(Carrera.id == idCarrera).join(Carrera, Apuesta.carrera_id == Carrera.id).join(Competidor, Competidor.id == Apuesta.competidor_id).join(Apostador, Apostador.id == Apuesta.apostador_id).all()

        return [dict(zip(v.keys(), v)) for v in listaApuestas]

    def calcularCuota(self, probabilidad):
        cuota = probabilidad / (1 - probabilidad)
        return cuota

    def calcularGanancia(self, valorApostado, probabilidad):
        ganancia = valorApostado + (valorApostado / self.calcularCuota(probabilidad))
        return ganancia 

    def darCompetidor(self, idCompetidor):
        competidor = session.query(Competidor).get(idCompetidor)
        return competidor

    def darReporteGanancias(self, carrera_actual, id_ganador):
        gananciasApostadores = []
        gananciasCasa = 0.0
        if not id_ganador or id_ganador < 1 or not carrera_actual or carrera_actual < 1:
            return False
        apostadoresCarrera = session.query(Apuesta.apostador_id,Apostador.nombre).filter(Apuesta.carrera_id == carrera_actual).distinct().join(Apostador, Apuesta.apostador_id == Apostador.id).order_by(Apostador.nombre).all()
        apuestasCarrera = self.darApuestasCarrera(carrera_actual)
        ganador = self.darCompetidor(id_ganador)
        for apostador in apostadoresCarrera:
            apostadorGana = 0
            for apuesta in apuestasCarrera:
                if apostador[0] == apuesta["ApostadorId"] and apuesta["CompetidorId"] == id_ganador:
                    probabilidad = ganador.probabilidad
                    apostadorGana += self.calcularGanancia(apuesta["Valor"],probabilidad)
            gananciasApostadores.append((apostador[1],apostadorGana))
        for apuesta in apuestasCarrera:
            if apuesta["ApostadorId"] != id_ganador:
                gananciasCasa += apuesta["Valor"]
            else:
                probabilidad = ganador.probabilidad
                gananciasCasa -= self.calcularGanancia(apuesta["Valor"], probabilidad)

        return gananciasApostadores, gananciasCasa
    
    def terminarCarrera(self, idCarrera):
        carrera = self.darCarrera(idCarrera)
        carrera.estaTerminada = True
        session.commit()
        return True

