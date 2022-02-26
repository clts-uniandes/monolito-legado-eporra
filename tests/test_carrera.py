import unittest
from unittest import result

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
        resultado = self.eporra.crearCarrera("Mi primera carrera", self.competidoresPrueba, False)
        self.assertEqual(resultado, True)
    
    def test_crearCarreraDuplicada(self):
        resultado1 = self.eporra.crearCarrera("Mi primera carrera", self.competidoresPrueba)
        resultado2 = self.eporra.crearCarrera("Mi primera carrera", self.competidoresPrueba)
        self.assertEqual(resultado1, True)
        self.assertEqual(resultado2, False)
    
    def test_crearCarreraNombreVacio(self):
        resultado = self.eporra.crearCarrera("", self.competidoresPrueba)
        self.assertFalse(resultado)

    def test_crearCarreraValidadProbabilidad(self):
        resultado = self.eporra.crearCarrera("Mi carrera", self.competidoresPruebaProbabilidad)
        self.assertFalse(resultado)
    
    def test_darListaCarreras(self):
        listadoCarreras = self.eporra.darListaCarreras()
        self.assertTrue(listadoCarreras)
