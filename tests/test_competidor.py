import unittest

from src.logica.eporra import EPorra
from src.modelo.declarative_base import Session

class CompetidorTestCasde(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        self.eporra = EPorra()
    
    def test_crearCompetidor(self):
        dictCompetidor = {"Nombre": "Competidor 1", "Probabilidad": 0.2}
        competidor = self.eporra.crearCompetidor(dictCompetidor)
        self.assertTrue(competidor)
    
    def test_crearCompetidorDatosVacios(self):
        competidorSinDatos = {"Nombre": "", "Probabilidad": None}
        competidor = self.eporra.crearCompetidor(competidorSinDatos)
        self.assertFalse(competidor)

    def test_crearCompetidorDuplicado(self):
        dictCompetidor1 = {"Nombre": "Competidor 1", "Probabilidad": 0.2}
        dictCompetidor2 = {"Nombre": "Competidor 1", "Probabilidad": 0.2}
        competidor1 = self.eporra.crearCompetidor(dictCompetidor1)
        competidor2 = self.eporra.crearCompetidor(dictCompetidor2)
        self.assertFalse(competidor2)
    
    def test_darListaCompetidores(self):
        listadoCompetidores = self.eporra.darListaCompetidores()
        self.assertIsNotNone(listadoCompetidores)