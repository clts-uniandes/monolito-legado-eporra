from src.modelo.declarative_base import engine, Base


class EPorra():

    def __init__(self):
        #Base.metadata.create_all(engine)
        self.descripcion = "Descipcion de la aplicaion"

    
    def darDescripcionAplicacion(self):
        return self.descripcion
    
    def darListaCarreras(self):# SI Interesa
        return None

    def crearCarrera(self, nombre, estaTerminada, competidores):# SI Interesa
        return None

    def darListaCompetidores(self, id): # SI Interesa
        return None
    
    def crearCompetidor(self, id, nombre, probabilidad):# SI Interesa
        return None



