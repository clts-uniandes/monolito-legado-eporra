import unittest

from src.logica.eporra import EPorra
from src.modelo.declarative_base import Session
from src.modelo.apostador import Apostador

class ApostadorTestCase(unittest.TestCase):
    
    def setUp(self):
        self.session = Session()
        self.eporra = EPorra()
        
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
    