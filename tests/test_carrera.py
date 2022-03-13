import unittest

from src.logica.eporra import EPorra
from src.modelo.declarative_base import Session
from src.modelo.apostador import Apostador
from src.modelo.carrera import Carrera
from src.modelo.competidor import Competidor
from src.modelo.apuesta import Apuesta

class CarreraTestCase(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        self.eporra = EPorra()
        self.competidoresPrueba = [{'Nombre':'Pepito Perez', 'Probabilidad':0.5},\
                        {'Nombre':'Pepa Perez', 'Probabilidad':0.5}]
        self.competidoresPruebaProbabilidad = [{'Nombre':'Pepito Perez', 'Probabilidad':0.8},\
                        {'Nombre':'Pepa Perez', 'Probabilidad':0.5}]

        apostadorApuesta = Apostador(nombre="Marco Martin")
        self.session.add(apostadorApuesta)
        self.session.commit()
        competidoresPrueba2 = [{'Nombre':'Carlos Casas', 'Probabilidad':0.5}, {'Nombre':'Carla Cueva', 'Probabilidad':0.5}]
        self.idCarreraPrueba = self.eporra.crearCarrera("Mi carrera de apuesta", competidoresPrueba2)
        self.eporra.crearCompetidor(self.idCarreraPrueba, "Carlos Casas", 0.5)
        self.eporra.crearCompetidor(self.idCarreraPrueba, "Carla Cueva", 0.5)
        
    
    def test_crearCarrera(self):
        resultado = self.eporra.crearCarrera("Mi primera carrera", self.competidoresPrueba)
        self.assertGreater(resultado, 0)
    
    def test_crearCarreraDuplicada(self):
        resultado1 = self.eporra.crearCarrera("Mi segunda carrera", self.competidoresPrueba)
        resultado2 = self.eporra.crearCarrera("Mi segunda carrera", self.competidoresPrueba)
        self.assertGreater(resultado1, 0)
        self.assertEqual(resultado2, 0)
    
    def test_crearCarreraNombreVacio(self):
        resultado = self.eporra.crearCarrera("", self.competidoresPrueba)
        self.assertEqual(resultado, 0)

    def test_crearCarreraValidadProbabilidad(self):
        resultado = self.eporra.crearCarrera("Mi carrera", self.competidoresPruebaProbabilidad)
        self.assertEqual(resultado, 0)
    
    def test_darListaCarreras(self):
        listadoCarreras = self.eporra.darListaCarreras()
        self.assertIsNotNone(listadoCarreras)
    
    def test_terminarCarrera(self):
        idCarrera = self.eporra.crearCarrera("Mi carrera a terminar", self.competidoresPrueba)
        resultado = self.eporra.terminarCarrera(idCarrera)
        self.assertTrue(resultado)
    
    def test_terminarCarreraIdInvalida(self):
        idCarrera = self.eporra.crearCarrera("Mi carrera a terminar", self.competidoresPrueba)
        self.assertRaises(AttributeError, self.eporra.terminarCarrera, idCarrera+1)

    def test_eliminarCarrera(self):
        resultado = self.eporra.eliminarCarrera(self.idCarreraPrueba)
        carreraEliminada = self.eporra.darCarrera(self.idCarreraPrueba)
        self.assertTrue(resultado)
        self.assertIsNone(carreraEliminada)
    
    def test_eliminarCarreraConApuestas(self):
        self.eporra.crearApuesta("Marco Martin", self.idCarreraPrueba, 5.00, "Carlos Casas")
        resultado = self.eporra.eliminarCarrera(self.idCarreraPrueba)
        carreraEliminada = self.eporra.darCarrera(self.idCarreraPrueba)
        self.assertFalse(resultado)
        self.assertIsNotNone(carreraEliminada)
    
    def tearDown(self):
        self.session.query(Carrera).delete()
        self.session.query(Apuesta).delete()
        self.session.query(Competidor).delete()
        self.session.query(Apostador).delete()
        self.session.commit()
    