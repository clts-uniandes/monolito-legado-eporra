import unittest

from src.logica.eporra import EPorra
from src.modelo.declarative_base import Session

class CarreraTestCase(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        self.eporra = EPorra()

        

    def test_crearCarrera(self):
        competidoresPrueba = [{'Nombre':'Pepito Perez', 'Probabilidad':0.5},\
                        {'Nombre':'Pepa Perez', 'Probabilidad':0.5}]
        carrera = self.eporra.crearCarrera("Mi primera carrera", False, competidoresPrueba)
        self.assertEqual(carrera, True)
    
    def test_crearCarreraDuplicada(self):
        competidoresPrueba = [{'Nombre':'Pepito Perez', 'Probabilidad':0.5},\
                        {'Nombre':'Pepa Perez', 'Probabilidad':0.5}]
        carrera1 = self.eporra.crearCarrera("Mi primera carrera", False, competidoresPrueba)
        carrera2 = self.eporra.crearCarrera("Mi primera carrera", False, competidoresPrueba)
        self.assertEqual(carrera2, False)

