import unittest

from src.logica.eporra import EPorra
from src.modelo.declarative_base import Session
from src.modelo.apostador import Apostador
from src.modelo.carrera import Carrera
from src.modelo.competidor import Competidor
from src.modelo.apuesta import Apuesta

class ApuestaTestCase(unittest.TestCase):
    
    def setUp(self):
        self.session = Session()
        self.eporra = EPorra()
    
    def test_crearApuesta(self):
        apostadorApuesta = Apostador(nombre="Marco Martin")
        self.session.add(apostadorApuesta)
        self.session.commit()
        competidoresPrueba = [{'Nombre':'Carlos Casas', 'Probabilidad':0.5},\
                        {'Nombre':'Carla Cueva', 'Probabilidad':0.5}]
        idCarreraPrueba = self.eporra.crearCarrera("Mi carrera de apuesta", competidoresPrueba)
        valorApuestaPrueba = 5.00
        self.eporra.crearCompetidor(idCarreraPrueba, "Carlos Casas", 0.5)
        self.eporra.crearCompetidor(idCarreraPrueba, "Carla Cueva", 0.5)
        exito = self.eporra.crearApuesta("Marco Martin", idCarreraPrueba, valorApuestaPrueba, "Carlos Casas")
        self.assertTrue(exito)
    
    def test_crearApuestaSinValor(self):
        apostadorApuesta = Apostador(nombre="Marco Martin")
        self.session.add(apostadorApuesta)
        self.session.commit()
        competidoresPrueba = [{'Nombre':'Carlos Casas', 'Probabilidad':0.5},\
                        {'Nombre':'Carla Cueva', 'Probabilidad':0.5}]
        idCarreraPrueba = self.eporra.crearCarrera("Mi carrera de apuesta", competidoresPrueba)
        valorApuestaPrueba = None
        self.eporra.crearCompetidor(idCarreraPrueba, "Carlos Casas", 0.5)
        self.eporra.crearCompetidor(idCarreraPrueba, "Carla Cueva", 0.5)
        fracaso = self.eporra.crearApuesta("Marco Martin", idCarreraPrueba, valorApuestaPrueba, "Carlos Casas")
        self.assertFalse(fracaso)

    
    def tearDown(self):
        self.session.query(Apuesta).delete()
        self.session.query(Competidor).delete()
        self.session.query(Carrera).delete()
        self.session.query(Apostador).delete()
        self.session.commit()
    