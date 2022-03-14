import unittest
from unittest import result

from src.logica.eporra import EPorra
from src.modelo.declarative_base import Session
from src.modelo.carrera import Carrera
from src.modelo.competidor import Competidor
from src.modelo.apostador import Apostador
from src.modelo.apuesta import Apuesta

from faker import Faker

class CarreraTestCase(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        self.eporra = EPorra()
        self.dataFactory = Faker('es_MX')
        Faker.seed(1001)
        probabilidad = self.dataFactory.pyfloat(0,2)
        self.nombreCarrera = self.dataFactory.catch_phrase()
        nombreCompetidor1 = self.dataFactory.name()
        nombreCompetidor2 = self.dataFactory.name()
        self.competidoresPrueba = [{'Nombre': nombreCompetidor1, 'Probabilidad':probabilidad}, {'Nombre': nombreCompetidor2, 'Probabilidad':1-probabilidad}]
        self.competidoresPruebaProbabilidad = [{'Nombre': nombreCompetidor1, 'Probabilidad':0.8}, {'Nombre': nombreCompetidor2, 'Probabilidad':0.5}] 
        
        
    def test_crearCarrera(self):
        resultado = self.eporra.crearCarrera(self.nombreCarrera, self.competidoresPrueba)
        self.assertGreater(resultado, 0)
    
    def test_crearCarreraDuplicada(self):
        nombreCarreraDuplicada = self.dataFactory.catch_phrase()
        resultado1 = self.eporra.crearCarrera(nombreCarreraDuplicada, self.competidoresPrueba)
        resultado2 = self.eporra.crearCarrera(nombreCarreraDuplicada, self.competidoresPrueba)
        self.assertGreater(resultado1, 0)
        self.assertEqual(resultado2, 0)
    
    def test_crearCarreraNombreVacio(self):
        resultado = self.eporra.crearCarrera("", self.competidoresPrueba)
        self.assertEqual(resultado, 0)
    
    def test_crearCarreraValidarProbabilidad(self):
        resultado = self.eporra.crearCarrera(self.nombreCarrera, self.competidoresPruebaProbabilidad)
        self.assertEqual(resultado, 0)
    
    def test_darListaCarrerasVacia(self):
        listadoCarreras = self.eporra.darListaCarreras()
        self.assertIsNotNone(listadoCarreras)
        self.assertEqual(len(listadoCarreras),0)
    
    def test_darListaCarrerasUnaCarrera(self):
        self.eporra.crearCarrera(self.nombreCarrera, self.competidoresPrueba)
        listaUnaCarrera = self.eporra.darListaCarreras()
        self.assertEqual(len(listaUnaCarrera),1)
    
    def test_darListaCarrerasOrdenada(self):
        nombreCarrera2 = self.dataFactory.catch_phrase()
        carrerasPrueba = [self.nombreCarrera,nombreCarrera2]
        carrerasPrueba.sort()
        self.eporra.crearCarrera(self.nombreCarrera, self.competidoresPrueba)
        self.eporra.crearCarrera(nombreCarrera2, self.competidoresPrueba)
        listaCarrerasOrdenada = self.eporra.darListaCarreras()
        self.assertEqual(carrerasPrueba[0],listaCarrerasOrdenada[0]['nombre'])
        self.assertEqual(carrerasPrueba[1],listaCarrerasOrdenada[1]['nombre'])
    
    def test_terminarCarrera(self):
        idCarrera = self.eporra.crearCarrera(self.nombreCarrera, self.competidoresPrueba)
        resultado = self.eporra.terminarCarrera(idCarrera)
        self.assertTrue(resultado)
    
    def test_terminarCarreraIdInvalida(self):
        self.eporra.crearCarrera(self.nombreCarrera, self.competidoresPrueba)
        self.assertRaises(AttributeError, self.eporra.terminarCarrera, 0)
    
    def test_eliminarCarrera(self):
        idCarrera = self.eporra.crearCarrera(self.nombreCarrera, self.competidoresPrueba)
        resultado = self.eporra.eliminarCarrera(idCarrera)
        carreraEliminada = self.eporra.darCarrera(idCarrera)
        self.assertTrue(resultado)
        self.assertIsNone(carreraEliminada)
    
    def test_eliminarCarreraConApuestas(self):
        idCarrera = self.eporra.crearCarrera(self.nombreCarrera, self.competidoresPrueba)
        self.eporra.crearCompetidor(idCarrera, self.competidoresPrueba[0]['Nombre'], self.competidoresPrueba[0]['Probabilidad'])
        self.eporra.crearCompetidor(idCarrera, self.competidoresPrueba[1]['Nombre'], self.competidoresPrueba[1]['Probabilidad'])
        nombreApostador = self.dataFactory.name()
        self.eporra.crearApostador(nombreApostador)
        self.eporra.crearApuesta(nombreApostador, idCarrera, 5.00, self.competidoresPrueba[0]['Nombre'])
        resultado = self.eporra.eliminarCarrera(idCarrera)
        carreraEliminada = self.eporra.darCarrera(idCarrera)
        self.assertFalse(resultado)
        self.assertIsNotNone(carreraEliminada)
        self.session.query(Apuesta).delete()
        self.session.query(Apostador).delete()
        self.session.query(Competidor).delete()
        self.session.commit()
    
    def test_eliminarCarreraSinID(self):
        resultado = self.eporra.eliminarCarrera()
        self.assertFalse(resultado)

    def test_eliminarCarreraIdInvalido(self):
        resultado = self.eporra.eliminarCarrera(0)
        self.assertFalse(resultado)
    
    def tearDown(self):
        self.session.query(Carrera).delete()
        self.session.commit()
    