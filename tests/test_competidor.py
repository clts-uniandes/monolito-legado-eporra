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