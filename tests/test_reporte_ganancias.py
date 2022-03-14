import unittest

from src.logica.eporra import EPorra
from src.modelo.declarative_base import Session
from src.modelo.apostador import Apostador
from src.modelo.carrera import Carrera
from src.modelo.competidor import Competidor
from src.modelo.apuesta import Apuesta

from faker import Faker

class ReporteGananciasTestCase(unittest.TestCase):
    
    def setUp(self):
        self.session = Session()
        self.eporra = EPorra()
        self.dataFactory = Faker('es_MX')
        Faker.seed(1001)
        self.nombreApostador1 = self.dataFactory.name()
        self.nombreApostador2 = self.dataFactory.name()
        nombreCarrera = self.dataFactory.catch_phrase()
        self.eporra.crearApostador(self.nombreApostador1)
        self.eporra.crearApostador(self.nombreApostador2)
        self.nombreCompetidor1 = self.dataFactory.name()
        self.nombreCompetidor2 = self.dataFactory.name()
        competidoresPrueba = [{'Nombre':self.nombreCompetidor1, 'Probabilidad':0.5}, {'Nombre':self.nombreCompetidor2, 'Probabilidad':0.5}]
        self.idCarreraPrueba = self.eporra.crearCarrera(nombreCarrera, competidoresPrueba)
        self.eporra.crearCompetidor(self.idCarreraPrueba, self.nombreCompetidor1, 0.5)
        self.eporra.crearCompetidor(self.idCarreraPrueba, self.nombreCompetidor2, 0.5)
        self.eporra.crearApuesta(self.nombreApostador1, self.idCarreraPrueba, 5.00, self.nombreCompetidor1)
        self.eporra.crearApuesta(self.nombreApostador1, self.idCarreraPrueba, 5.00, self.nombreCompetidor2)
        self.competidorGanador = self.session.query(Competidor.id).filter(Competidor.nombre == self.nombreCompetidor1).first()[0]
    
    def test_mostrarReporteGanancias(self):
        self.eporra.crearApuesta(self.nombreApostador2, self.idCarreraPrueba, 5.00, self.nombreCompetidor1)
        self.eporra.crearApuesta(self.nombreApostador2, self.idCarreraPrueba, 5.00, self.nombreCompetidor2)
        listaApostadoresGanancias, gananciasCasa = self.eporra.darReporteGanancias(self.idCarreraPrueba,self.competidorGanador)
        self.assertIsNotNone(listaApostadoresGanancias)
        self.assertEqual(len(listaApostadoresGanancias),2)
        self.assertEqual(-10.0,gananciasCasa)
    
    def test_mostrarReporteGananciasUnSoloApostador(self):
        listaApostadoresGanancias, gananciasCasa = self.eporra.darReporteGanancias(self.idCarreraPrueba,self.competidorGanador)
        self.assertIsNotNone(listaApostadoresGanancias)
        self.assertEqual(len(listaApostadoresGanancias),1)
        self.assertEqual(-20.0,gananciasCasa)
    
    def test_test_mostrarReporteGananciasOrdenado(self):
        self.eporra.crearApuesta(self.nombreApostador2, self.idCarreraPrueba, 5.00, self.nombreCompetidor1)
        self.eporra.crearApuesta(self.nombreApostador2, self.idCarreraPrueba, 5.00, self.nombreCompetidor2)
        apostadoresCarrera = [self.nombreApostador1,self.nombreApostador2]
        apostadoresCarrera.sort()
        listaApostadoresGanancias = self.eporra.darReporteGanancias(self.idCarreraPrueba,self.competidorGanador)
        self.assertEqual(apostadoresCarrera[0],listaApostadoresGanancias[0][0][0])
        self.assertEqual(apostadoresCarrera[1],listaApostadoresGanancias[0][1][0])
    
    def test_mostrarReporteGananciasCompetidorInvalido(self):
        resultado = self.eporra.darReporteGanancias(self.idCarreraPrueba, 0)
        self.assertEqual(resultado, False)
    
    def test_mostrarReporteGananciasCarreraInvalida(self):
        competidorGanador = self.session.query(Competidor.id).filter(Competidor.nombre == self.nombreCompetidor1).first()[0]
        resultado = self.eporra.darReporteGanancias(0, competidorGanador)
        self.assertEqual(resultado, False)
    
    def tearDown(self):
        self.session.query(Apuesta).delete()
        self.session.query(Competidor).delete()
        self.session.query(Carrera).delete()
        self.session.query(Apostador).delete()
        self.session.commit()
    