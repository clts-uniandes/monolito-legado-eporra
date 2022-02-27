import unittest

from src.logica.eporra import EPorra
from src.modelo.declarative_base import Session

class CompetidorTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.session = Session()
        cls.eporra = EPorra()
        cls.competidoresPrueba = [{'Nombre':'Pepito Perez', 'Probabilidad':0.5},\
                        {'Nombre':'Pepa Perez', 'Probabilidad':0.5}]
        cls.idCarrera = cls.eporra.crearCarrera("Mi primera carrera", cls.competidoresPrueba)
    
    def test_crearCompetidor(cls):
        resultado = cls.eporra.crearCompetidor(cls.idCarrera, "Competidor 1", 0.2)
        cls.assertTrue(resultado)
    
    def test_crearCompetidorDatosVacios(cls):
        resultado = cls.eporra.crearCompetidor(cls.idCarrera, "", None)
        cls.assertFalse(resultado)

    def test_crearCompetidorDuplicado(cls):
        resultado1 = cls.eporra.crearCompetidor(cls.idCarrera, "Competidor A", 0.2)
        resultado2 = cls.eporra.crearCompetidor(cls.idCarrera, "Competidor A", 0.2)
        cls.assertTrue(resultado1)
        cls.assertFalse(resultado2)
    
    def test_darListaCompetidores(self):
        listadoCompetidores = self.eporra.darListaCompetidores()
        self.assertIsNotNone(listadoCompetidores)