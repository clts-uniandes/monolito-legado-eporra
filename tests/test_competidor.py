import unittest

from src.logica.eporra import EPorra
from src.modelo.declarative_base import Session
from src.modelo.carrera import Carrera
from src.modelo.competidor import Competidor

class CompetidorTestCase(unittest.TestCase):
    
    def setUp(self):
        self.session = Session()
        self.eporra = EPorra()
        self.competidoresPrueba = [{'Nombre':'Pepito Perez', 'Probabilidad':0.5},\
                        {'Nombre':'Pepa Perez', 'Probabilidad':0.5}]
        self.idCarrera = self.eporra.crearCarrera("Mi carrera con competidores", self.competidoresPrueba)
    
    def test_crearCompetidor(self):
        resultado = self.eporra.crearCompetidor(self.idCarrera, "Competidor 1", 0.2)
        self.assertTrue(resultado)
    
    def test_crearCompetidorDatosVacios(self):
        resultado = self.eporra.crearCompetidor(self.idCarrera, "", None)
        self.assertFalse(resultado)

    def test_crearCompetidorDuplicado(self):
        resultado1 = self.eporra.crearCompetidor(self.idCarrera, "Competidor A", 0.2)
        resultado2 = self.eporra.crearCompetidor(self.idCarrera, "Competidor A", 0.2)
        self.assertTrue(resultado1)
        self.assertFalse(resultado2)
    
    def test_darListaCompetidores(self):
        listadoCompetidores = self.eporra.darListaCompetidores()
        self.assertIsNotNone(listadoCompetidores)
    
    def tearDown(self):
        self.session.query(Competidor).delete()
        self.session.query(Carrera).delete()
        self.session.commit()