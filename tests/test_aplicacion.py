import unittest

from src.logica.eporra import EPorra
from src.modelo.declarative_base import Session

from faker import Faker

class AplicacionTestCase(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        self.eporra = EPorra()
        self.dataFactory = Faker('es_MX')
        Faker.seed(1991)
        descripcion = self.dataFactory.unique.catch_phrase()
    
    def test_darAplicacion(self):
        resultadoEsperado = self.eporra.darDescripcionAplicacion()
        self.assertEqual(resultadoEsperado, "Descripción de la aplicación")
    
