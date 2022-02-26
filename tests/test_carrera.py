import unittest

from src.logica.eporra import EPorra
from src.modelo.declarative_base import Session

class CarreraTestCase(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        self.eporra = EPorra()
        self.competidoresPrueba = [{'Nombre':'Pepito Perez', 'Probabilidad':0.5},\
                        {'Nombre':'Pepa Perez', 'Probabilidad':0.5}]
        self.competidoresPruebaProbabilidad = [{'Nombre':'Pepito Perez', 'Probabilidad':0.8},\
                        {'Nombre':'Pepa Perez', 'Probabilidad':0.5}]

        

    def test_crearCarrera(self):
        carrera = self.eporra.crearCarrera("Mi primera carrera", False, self.competidoresPrueba)
        self.assertEqual(carrera, True)
    
    def test_crearCarreraDuplicada(self):
        carrera1 = self.eporra.crearCarrera("Mi primera carrera", False, self.competidoresPrueba)
        carrera2 = self.eporra.crearCarrera("Mi primera carrera", False, self.competidoresPrueba)
        self.assertEqual(carrera2, False)
    
    def test_crearCarreraNombreVacio(self):
        carrera1 = self.eporra.crearCarrera("", False, self.competidoresPrueba)
        self.assertFalse(carrera1)

    def test_crearCarreraValidadProbabilidad(self):
        carrera1 = self.eporra.crearCarrera("Mi carrera", False, self.competidoresPruebaProbabilidad)
        self.assertFalse(carrera1)

