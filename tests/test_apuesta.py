import unittest

from src.logica.eporra import EPorra
from src.modelo.declarative_base import Session
from src.modelo.apostador import Apostador

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
        