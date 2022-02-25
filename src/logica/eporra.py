from src.modelo.declarative_base import engine, Base


class EPorra():

    def __init__(self):
        Base.metadata.create_all(engine)
    
    def darDescripcionAplicacion(self):
        return None
    
    def darListaCarreras(self):
        return None

    def crearCarrera(self, nombre, listaCompetidores):
        return None
    
    def crearCompetidor(self, nombre, probabilidad):
        return None

