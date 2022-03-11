
import unittest

from src.logica.eporra import EPorra
from src.modelo.declarative_base import Session
from src.modelo.apostador import Apostador
from src.modelo.carrera import Carrera
from src.modelo.competidor import Competidor
from src.modelo.apuesta import Apuesta

class ReporteGananciasTestCase(unittest.TestCase):
    
    def setUp(self):
        self.session = Session()
        self.eporra = EPorra()
        apostadorApuesta1 = Apostador(nombre="Marco Martin")
        apostadorApuesta2 = Apostador(nombre="Pepe P")
        self.session.add(apostadorApuesta1)
        self.session.add(apostadorApuesta2)
        self.session.commit()
        competidoresPrueba = [{'Nombre':'Carlos Casas', 'Probabilidad':0.5}, {'Nombre':'Carla Cueva', 'Probabilidad':0.5}]
        self.idCarreraPrueba = self.eporra.crearCarrera("Mi carrera de apuesta", competidoresPrueba)
        self.eporra.crearCompetidor(self.idCarreraPrueba, "Carlos Casas", 0.5)
        self.eporra.crearCompetidor(self.idCarreraPrueba, "Carla Cueva", 0.5)
        self.eporra.crearApuesta("Pepe P", self.idCarreraPrueba, 5.00, "Carlos Casas")
        self.eporra.crearApuesta("Marco Martin", self.idCarreraPrueba, 5.00, "Carla Cueva")
        self.eporra.crearApuesta("Pepe P", self.idCarreraPrueba, 5.00, "Carlos Casas")
        self.eporra.crearApuesta("Marco Martin", self.idCarreraPrueba, 5.00, "Carla Cueva")
    
    def test_mostrarReporteGanancias(self):
        competidorGanador = self.session.query(Competidor.id).filter(Competidor.nombre == "Carlos Casas").first()[0]
        listaApostadoresGanancias, gananciasCasa = self.eporra.darReporteGanancias(self.idCarreraPrueba,competidorGanador)
        self.assertIsNotNone(listaApostadoresGanancias)
        self.assertEqual(-10.0,gananciasCasa)    

    def test_mostrarReporteGananciasCompetidorInvalido(self):
        resultado = self.eporra.darReporteGanancias(self.idCarreraPrueba, 0)
        self.assertEqual(resultado, False) 

    def tearDown(self):
        self.session.query(Apuesta).delete()
        self.session.query(Competidor).delete()
        self.session.query(Carrera).delete()
        self.session.query(Apostador).delete()
        self.session.commit()