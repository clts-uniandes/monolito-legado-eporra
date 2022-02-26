import unittest

from src.logica.eporra import EPorra
from src.modelo.declarative_base import Session

class CompetidorTestCasde(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        self.eporra = EPorra()
    
    def test_crearCompetidor(self):
        resultado = self.eporra.crearCompetidor(-1, "Competidor 1", 0.2)
        self.assertTrue(resultado)
    
    def test_crearCompetidorDatosVacios(self):
        resultado = self.eporra.crearCompetidor(-1, "", None)
        self.assertFalse(resultado)

    def test_crearCompetidorDuplicado(self):
        resultado1 = self.eporra.crearCompetidor(-1, "Competidor 1", 0.2)
        resultado2 = self.eporra.crearCompetidor(-1, "Competidor 1", 0.2)
        self.assertTrue(resultado1)
        self.assertFalse(resultado2)
    
    def test_darListaCompetidores(self):
        listadoCompetidores = self.eporra.darListaCompetidores()
        self.assertIsNotNone(listadoCompetidores)