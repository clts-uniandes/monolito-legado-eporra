import unittest

from src.logica.eporra import EPorra
from src.modelo.declarative_base import Session

class AplicacionTestCase(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        self.eporra = EPorra()

    def test_darAplicacion(self):
        resultadoEsperado = self.eporra.darDescripcionAplicacion()
        self.assertEqual(resultadoEsperado, "Descripción de la aplicación")