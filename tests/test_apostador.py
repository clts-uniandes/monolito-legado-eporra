import unittest

from src.logica.eporra import EPorra
from src.modelo.declarative_base import Session
from src.modelo.apostador import Apostador

from faker import Faker
class ApostadorTestCase(unittest.TestCase):
    
    def setUp(self):
        self.session = Session()
        self.eporra = EPorra()
        self.dataFactory = Faker('es_MX')
        Faker.seed(1001)
        self.nombreApostador1 = self.dataFactory.unique.name()
        self.nombreApostador2 = self.dataFactory.unique.name()

    def test_crearApostador(self):
        resultado = self.eporra.crearApostador(self.nombreApostador1 )
        self.assertTrue(resultado)
    
    def test_crearApostadorNombreVacio(self):
        resultado = self.eporra.crearApostador("")
        self.assertFalse(resultado)
    
    def test_crearApostadorNombreRepetido(self):
        resultado1 = self.eporra.crearApostador(self.nombreApostador1)
        resultado2 = self.eporra.crearApostador(self.nombreApostador1)
        self.assertTrue(resultado1)
        self.assertFalse(resultado2)
        
    def test_darListaApostadoresVacia(self):
        listaVacia = self.eporra.darListaApostadores()
        self.assertIsNotNone(listaVacia)
        self.assertEqual(len(listaVacia),0)
    
    def test_darListaApostadoresUnApostador(self):
        self.eporra.crearApostador(self.nombreApostador1)
        listaUnApostador = self.eporra.darListaApostadores()
        self.assertEqual(len(listaUnApostador),1)
    
    def test_darListaApostadoresOrdenada(self):
        self.apostadoresPrueba = [self.nombreApostador1, self.nombreApostador2]
        self.apostadoresPrueba.sort()
        self.eporra.crearApostador(self.nombreApostador1)
        self.eporra.crearApostador(self.nombreApostador2)
        listaApostadoresOrdenada = self.eporra.darListaApostadores()
        self.assertEqual(self.apostadoresPrueba[0],listaApostadoresOrdenada[0]['Nombre'])
        self.assertEqual(self.apostadoresPrueba[1],listaApostadoresOrdenada[1]['Nombre'])
    
    def tearDown(self):
        self.session.query(Apostador).delete()
        self.session.commit()
    