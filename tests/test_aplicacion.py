import unittest

from src.logica.eporra import EPorra
from src.modelo.aplicacion import Applicacion
from src.modelo.declarative_base import Session

class AplicacionTestCase(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        self.eporra = EPorra()

    def darAplicacion(self):
        resultadoEsperado = self.eporra.darDescripcionAplicacion()
        self.assertEqual(resultadoEsperado, "Descipcion de la aplicaion")