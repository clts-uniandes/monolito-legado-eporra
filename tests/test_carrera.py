import unittest

from src.logica.eporra import EPorra
from src.modelo.declarative_base import Session

class CarreraTestCase(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        self.eporra = EPorra()