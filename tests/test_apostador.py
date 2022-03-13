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
        
    def test_darListaApostadoresVacia(self):
        listaVacia = self.eporra.darListaApostadores()
        self.assertIsNotNone(listaVacia)
        self.assertEqual(len(listaVacia),0)
    
    def test_darListaApostadoresUnApostador(self):
        apostador1 = Apostador(nombre="Pepe Perez")
        self.session.add(apostador1)
        self.session.commit()
        listaUnApostador = self.eporra.darListaApostadores()
        self.assertEqual(len(listaUnApostador),1)
    
    def test_darListaApostadoresOrdenada(self):
        self.apostadoresPrueba = [{'Nombre':'Marta Conchita'},{'Nombre':'Pablo Puebla'}]
        apostador2 = Apostador(nombre="Pablo Puebla")
        apostador3 = Apostador(nombre="Marta Conchita")
        self.session.add(apostador2)
        self.session.add(apostador3)
        self.session.commit()
        listaApostadoresOrdenada = self.eporra.darListaApostadores()
        self.assertEqual(self.apostadoresPrueba[0]['Nombre'],listaApostadoresOrdenada[0]['Nombre'])
        self.assertEqual(self.apostadoresPrueba[1]['Nombre'],listaApostadoresOrdenada[1]['Nombre'])
    
    def tearDown(self):
        self.session.query(Apostador).delete()
        self.session.commit()
    