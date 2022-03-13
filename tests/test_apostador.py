import unittest

from src.logica.eporra import EPorra
from src.modelo.declarative_base import Session
from src.modelo.apostador import Apostador

class ApostadorTestCase(unittest.TestCase):
    
    def setUp(self):
        self.session = Session()
        self.eporra = EPorra()

    def test_crearApostador(self):
        nombre = "Pepe Perez"
        resultado = self.eporra.crearApostador(nombre)
        self.assertTrue(resultado)
    
    def test_crearApostadorNombreVacio(self):
        resultado = self.eporra.crearApostador("")
        self.assertFalse(resultado)
    
    def test_crearApostadorNombreRepetido(self):
        nombre = "Pepe Perez"
        resultado1 = self.eporra.crearApostador(nombre)
        resultado2 = self.eporra.crearApostador(nombre)
        self.assertTrue(resultado1)
        self.assertFalse(resultado2)
        
    def test_darListaApostadoresVacia(self):
        listaVacia = self.eporra.darListaApostadores()
        self.assertIsNotNone(listaVacia)
        self.assertEqual(len(listaVacia),0)
    
    def test_darListaApostadoresUnApostador(self):
        nombre = "Pepe Perez"
        self.eporra.crearApostador(nombre)
        listaUnApostador = self.eporra.darListaApostadores()
        self.assertEqual(len(listaUnApostador),1)
    
    def test_darListaApostadoresOrdenada(self):
        nombre1 = 'Pablo Puebla'
        nombre2 = 'Marta Conchita'
        self.apostadoresPrueba = [nombre1,nombre2]
        self.apostadoresPrueba.sort()
        self.eporra.crearApostador(nombre1)
        self.eporra.crearApostador(nombre2)
        listaApostadoresOrdenada = self.eporra.darListaApostadores()
        self.assertEqual(self.apostadoresPrueba[0],listaApostadoresOrdenada[0]['Nombre'])
        self.assertEqual(self.apostadoresPrueba[1],listaApostadoresOrdenada[1]['Nombre'])
    
    def tearDown(self):
        self.session.query(Apostador).delete()
        self.session.commit()
    