import unittest

from src.logica.eporra import EPorra
from src.modelo.declarative_base import Session

class ApostadorTestCase(unittest.TestCase):
    
    def setUp(self):
        self.session = Session()
        self.eporra = EPorra()
        
    def test_darListaApostadoresVacia(self):
        listaVacia = self.eporra.darListaApostadores()
        self.assertIsNotNone(listaVacia)
        self.assertEqual(len(listaVacia),0)
    