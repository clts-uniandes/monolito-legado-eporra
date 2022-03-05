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
        apostadorApuesta = Apostador(nombre="Marco Martin")
        self.session.add(apostadorApuesta)
        self.session.commit()
        competidoresPrueba = [{'Nombre':'Carlos Casas', 'Probabilidad':0.5},\
                         {'Nombre':'Carla Cueva', 'Probabilidad':0.5}]
        self.idCarreraPrueba = self.eporra.crearCarrera("Mi carrera de apuesta", competidoresPrueba)
        self.eporra.crearCompetidor(self.idCarreraPrueba, "Carlos Casas", 0.5)
        self.eporra.crearCompetidor(self.idCarreraPrueba, "Carla Cueva", 0.5)
    
    def test_crearApuesta(self):
        valorApuestaPrueba = 5.00
        exito = self.eporra.crearApuesta("Marco Martin", self.idCarreraPrueba, valorApuestaPrueba, "Carlos Casas")
        self.assertTrue(exito)
    
    def test_crearApuestaSinValor(self):
        valorApuestaPrueba = None
        fracaso = self.eporra.crearApuesta("Marco Martin", self.idCarreraPrueba, valorApuestaPrueba, "Carlos Casas")
        self.assertFalse(fracaso)
    
    def test_crearApuestaMenorAMontoMinimo(self):
        valorApuestaPrueba = 0.3
        fracaso = self.eporra.crearApuesta("Marco Martin", self.idCarreraPrueba, valorApuestaPrueba, "Carlos Casas")
        self.assertFalse(fracaso)
    
    def test_crearApuestaApostadorVacio(self):
        valorApuestaPrueba = 1.0
        fracaso = self.eporra.crearApuesta("", self.idCarreraPrueba, valorApuestaPrueba, "Carlos Casas")
        self.assertFalse(fracaso)

    
    def tearDown(self):
        self.session.query(Apuesta).delete()
        self.session.query(Competidor).delete()
        self.session.query(Carrera).delete()
        self.session.query(Apostador).delete()
        self.session.commit()
    