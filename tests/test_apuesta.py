import unittest

from src.logica.eporra import EPorra
from src.modelo.declarative_base import Session
from src.modelo.apostador import Apostador
from src.modelo.carrera import Carrera
from src.modelo.competidor import Competidor
from src.modelo.apuesta import Apuesta

class ApuestaTestCase(unittest.TestCase):
    
    def setUp(self):
        self.session = Session()
        self.eporra = EPorra()
        apostadorApuesta = Apostador(nombre="Marco Martin")
        self.session.add(apostadorApuesta)
        self.session.commit()
        competidoresPrueba = [{'Nombre':'Carlos Casas', 'Probabilidad':0.5}, {'Nombre':'Carla Cueva', 'Probabilidad':0.5}]
        self.idCarreraPrueba = self.eporra.crearCarrera("Mi carrera de apuesta", competidoresPrueba)
        self.eporra.crearCompetidor(self.idCarreraPrueba, "Carlos Casas", 0.5)
        self.eporra.crearCompetidor(self.idCarreraPrueba, "Carla Cueva", 0.5)
        self.apuestasPrueba = {'Apostador': 'Marco Martin', 'Valor': 5.0, 'Competidor': 'Carlos Casas'}
        self.apuestasPruebaLista = [{"Id": 1, "Apostador": "Marco Martin", 'ApostadorId': 1, 'CompetidorId': 1, "Valor": 5.00, "Competidor": "Carlos Casas"}]
    
    def test_crearApuesta(self):
        exito = self.eporra.crearApuesta("Marco Martin", self.idCarreraPrueba, 5.00, "Carlos Casas")
        self.assertTrue(exito)
    
    def test_crearApuestaSinValor(self):
        valorApuestaPrueba = None
        fracaso = self.eporra.crearApuesta("Marco Martin", self.idCarreraPrueba, valorApuestaPrueba, "Carlos Casas")
        self.assertFalse(fracaso)
    
    def test_crearApuestaMenorAMontoMinimo(self):
        valorApuestaPrueba = 0.3
        fracaso = self.eporra.crearApuesta("Marco Martin", self.idCarreraPrueba, valorApuestaPrueba, "Carlos Casas")
        self.assertFalse(fracaso)
    
    def test_crearApuestaApostadorVacio(self):
        nombreApostador = ""
        fracaso = self.eporra.crearApuesta(nombreApostador, self.idCarreraPrueba, 1.0, "Carlos Casas")
        self.assertFalse(fracaso)
    
    def test_crearApuestaCompetidorVacio(self):
        nombreCompetidor = ""
        fracaso = self.eporra.crearApuesta("Marco Martin", self.idCarreraPrueba, 1.0, nombreCompetidor)
        self.assertFalse(fracaso)
    
    def test_darApuestasCarrerasVacio(self):
        resultado = self.eporra.darApuestasCarrera(self.idCarreraPrueba)
        self.assertListEqual([], resultado)

    def test_darApuestasCarrerasConCarreras(self):
        self.eporra.crearApuesta("Marco Martin", self.idCarreraPrueba, 5.00, "Carlos Casas")
        resultado = self.eporra.darApuestasCarrera(self.idCarreraPrueba)
        self.assertListEqual(self.apuestasPruebaLista, resultado)
    
    def test_darApuesta(self):
        valorApuestaPrueba = 5.00
        idApuesta = 1
        resultadoCrearApuesta = self.eporra.crearApuesta("Marco Martin", self.idCarreraPrueba, valorApuestaPrueba, "Carlos Casas")
        resultadoDarApuesta = self.eporra.darApuesta(self.idCarreraPrueba,idApuesta)
        self.assertTrue(resultadoCrearApuesta)
        self.assertEqual(self.apuestasPrueba, resultadoDarApuesta)

    def test_darApuestaIdInvalido(self):
        valorApuestaPrueba = 5.00
        idApuesta = 100
        resultadoCrearApuesta = self.eporra.crearApuesta("Marco Martin", self.idCarreraPrueba, valorApuestaPrueba, "Carlos Casas")
        resultadoDarApuesta = self.eporra.darApuesta(idApuesta)
        self.assertTrue(resultadoCrearApuesta)
        self.assertEqual(False, resultadoDarApuesta)
    
    def test_editarApuesta(self):
        valorApuestaPrueba = 5.00
        idApuesta = 1
        apuestaEditada = {"Apostador": "Marco Martin", "Valor": 6.00, "Competidor": "Carla Cueva"}
        resultadoCrearApuesta = self.eporra.crearApuesta("Marco Martin", self.idCarreraPrueba, valorApuestaPrueba, "Carlos Casas")
        editarApuesta = self.eporra.editarApuesta(idApuesta, apuestaEditada["Apostador"], self.idCarreraPrueba, apuestaEditada["Valor"], apuestaEditada["Competidor"])
        resultadoEdicion = self.eporra.darApuesta(self.idCarreraPrueba, idApuesta)
        self.assertTrue(resultadoCrearApuesta)
        self.assertTrue(editarApuesta)
        self.assertEqual(apuestaEditada, resultadoEdicion)

    def test_editarApuestaIdInvalido(self):
        valorApuestaPrueba = 5.00
        idApuesta = 200
        apuestaEditada = {"Apostador": "Marco Martin", "Valor": 6.00, "Competidor": "Carla Cueva"}
        resultadoCrearApuesta = self.eporra.crearApuesta("Marco Martin", self.idCarreraPrueba, valorApuestaPrueba, "Carlos Casas")
        editarApuesta = self.eporra.editarApuesta(idApuesta, apuestaEditada["Apostador"], self.idCarreraPrueba, apuestaEditada["Valor"], apuestaEditada["Competidor"])
        resultadoEdicion = self.eporra.darApuesta(idApuesta, self.idCarreraPrueba)
        self.assertTrue(resultadoCrearApuesta)
        self.assertFalse(editarApuesta)
        self.assertEqual(False, resultadoEdicion)

    def test_editarApuestaConDatosInvalido(self):
        valorApuestaPrueba = 5.00
        idApuesta = 200
        apuestaEditada = {"Apostador": "Marco Martin", "Valor": 6.00, "Competidor": "Carla Cueva"}
        resultadoCrearApuesta = self.eporra.crearApuesta("Marco Martin", self.idCarreraPrueba, valorApuestaPrueba, "Carlos Casas")
        editarApuesta = self.eporra.editarApuesta(idApuesta, apuestaEditada["Apostador"], self.idCarreraPrueba, apuestaEditada["Valor"], apuestaEditada["Competidor"])
        resultadoEdicion = self.eporra.darApuesta(idApuesta)
        self.assertTrue(resultadoCrearApuesta)
        self.assertFalse(editarApuesta)
        self.assertEqual(False, resultadoEdicion)
    
    def tearDown(self):
        self.session.query(Carrera).delete()
        self.session.query(Apuesta).delete()
        self.session.query(Competidor).delete()
        self.session.query(Apostador).delete()
        self.session.commit()