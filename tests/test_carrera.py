import unittest
from unittest import result

from src.logica.eporra import EPorra
from src.modelo.declarative_base import Session
from src.modelo.carrera import Carrera

class CarreraTestCase(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        self.eporra = EPorra()
        self.competidoresPrueba = [{'Nombre':'Pepito Perez', 'Probabilidad':0.5},\
                        {'Nombre':'Pepa Perez', 'Probabilidad':0.5}]
        self.competidoresPruebaProbabilidad = [{'Nombre':'Pepito Perez', 'Probabilidad':0.8},\
                        {'Nombre':'Pepa Perez', 'Probabilidad':0.5}]
        
    
    def test_crearCarrera(self):
        resultado = self.eporra.crearCarrera("Mi primera carrera", self.competidoresPrueba)
        self.assertGreater(resultado, 0)
    
    def test_crearCarreraDuplicada(self):
        resultado1 = self.eporra.crearCarrera("Mi segunda carrera", self.competidoresPrueba)
        resultado2 = self.eporra.crearCarrera("Mi segunda carrera", self.competidoresPrueba)
        self.assertGreater(resultado1, 0)
        self.assertEqual(resultado2, 0)
    
    def test_crearCarreraNombreVacio(self):
        resultado = self.eporra.crearCarrera("", self.competidoresPrueba)
        self.assertEqual(resultado, 0)

    def test_crearCarreraValidadProbabilidad(self):
        resultado = self.eporra.crearCarrera("Mi carrera", self.competidoresPruebaProbabilidad)
        self.assertEqual(resultado, 0)
    
    def test_darListaCarreras(self):
        listadoCarreras = self.eporra.darListaCarreras()
        self.assertIsNotNone(listadoCarreras)
    
    def test_terminarCarrera(self):
        idCarrera = self.eporra.crearCarrera("Mi carrera a terminar", self.competidoresPrueba)
        resultado = self.eporra.terminarCarrera(idCarrera)
        self.assertTrue(resultado)
    
    def test_terminarCarreraIdInvalida(self):
        idCarrera = self.eporra.crearCarrera("Mi carrera a terminar", self.competidoresPrueba)
        self.assertRaises(AttributeError, self.eporra.terminarCarrera, idCarrera+1)
    
    def tearDown(self):
        self.session.query(Carrera).delete()
        self.session.commit()
    