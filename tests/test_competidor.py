import unittest

from src.logica.eporra import EPorra
from src.modelo.declarative_base import Session
from src.modelo.carrera import Carrera
from src.modelo.competidor import Competidor

from faker import Faker
class CompetidorTestCase(unittest.TestCase):
    
    def setUp(self):
        self.session = Session()
        self.eporra = EPorra()
        self.dataFactory = Faker('es_MX')
        Faker.seed(1001)
        self.competidoresPrueba = []
        for _ in range(2):
            comp = {
                "Nombre": self.dataFactory.unique.name(),
                "Probabilidad": 0.5
            }
            self.competidoresPrueba.append(comp)
        self.idCarreraPrueba = self.eporra.crearCarrera(self.dataFactory.unique.name(), self.competidoresPrueba)
        self.idCarreraPrueba2 = self.eporra.crearCarrera(self.dataFactory.unique.name(), self.competidoresPrueba)
    
    def test_crearCompetidor(self):
        resultado = self.eporra.crearCompetidor(self.idCarreraPrueba, self.competidoresPrueba[0]["Nombre"], self.competidoresPrueba[0]["Probabilidad"])
        self.assertTrue(resultado)
    
    def test_crearCompetidorDatosVacios(self):
        resultado = self.eporra.crearCompetidor(self.idCarreraPrueba, "", None)
        self.assertFalse(resultado)

    def test_crearCompetidorDuplicado(self):
        resultado1 = self.eporra.crearCompetidor(self.idCarreraPrueba, self.competidoresPrueba[0]["Nombre"], self.competidoresPrueba[0]["Probabilidad"])
        resultado2 = self.eporra.crearCompetidor(self.idCarreraPrueba, self.competidoresPrueba[0]["Nombre"], self.competidoresPrueba[0]["Probabilidad"])
        self.assertTrue(resultado1)
        self.assertFalse(resultado2)
    
    def test_darListaCompetidores(self):
        listadoCompetidores = self.eporra.darListaCompetidores()
        self.assertIsNotNone(listadoCompetidores)

    def test_darListaCompetidoresCarrera(self):
        for comp in self.competidoresPrueba:
            self.eporra.crearCompetidor(self.idCarreraPrueba, comp["Nombre"], comp["Probabilidad"])
        for comp in self.competidoresPrueba:
            self.eporra.crearCompetidor(self.idCarreraPrueba2, comp["Nombre"], comp["Probabilidad"])
        listadoCompetidores = self.eporra.darListaCompetidores(self.idCarreraPrueba2)
        self.assertEquals(2, len(listadoCompetidores))
    
    def tearDown(self):
        self.session.query(Competidor).delete()
        self.session.query(Carrera).delete()
        self.session.commit()