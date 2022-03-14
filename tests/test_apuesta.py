import unittest

from src.logica.eporra import EPorra
from src.modelo.declarative_base import Session
from src.modelo.apostador import Apostador
from src.modelo.carrera import Carrera
from src.modelo.competidor import Competidor
from src.modelo.apuesta import Apuesta

from faker import Faker

class ApuestaTestCase(unittest.TestCase):
    
    def setUp(self):
        self.session = Session()
        self.eporra = EPorra()
        self.dataFactory = Faker('es_MX')
        Faker.seed(1001)
        self.nombreApostador = self.dataFactory.unique.name()
        apostadorApuesta = Apostador(nombre=self.nombreApostador)
        self.session.add(apostadorApuesta)
        self.session.commit()
        self.competidoresPrueba = []
        for _ in range(2):
            comp = {
                "Nombre": self.dataFactory.unique.name(),
                "Probabilidad": 0.5
            }
            self.competidoresPrueba.append(comp)
        self.idCarreraPrueba = self.eporra.crearCarrera(self.dataFactory.unique.name(), self.competidoresPrueba)
        for comp in self.competidoresPrueba:
            self.eporra.crearCompetidor(self.idCarreraPrueba, comp["Nombre"], comp["Probabilidad"])
        self.valorApuetaRandom = self.dataFactory.pyint(min_value=1, max_value=1000)
        self.apuestasPrueba = {'Apostador': self.nombreApostador, 'Valor': self.valorApuetaRandom, 'Competidor': self.competidoresPrueba[0]["Nombre"]}
        self.apuestasPruebaLista = [{"Id": 1, "Apostador": self.nombreApostador, 'ApostadorId': 1, 'CompetidorId': 1, "Valor": self.valorApuetaRandom, "Competidor": self.competidoresPrueba[0]["Nombre"]}]
    
    def test_crearApuesta(self):
        exito = self.eporra.crearApuesta(self.nombreApostador, self.idCarreraPrueba, 5.00, self.competidoresPrueba[0]["Nombre"])
        self.assertTrue(exito)
    
    def test_crearApuestaSinValor(self):
        valorApuestaPrueba = None
        fracaso = self.eporra.crearApuesta(self.nombreApostador, self.idCarreraPrueba, valorApuestaPrueba, self.competidoresPrueba[0]["Nombre"])
        self.assertFalse(fracaso)
    
    def test_crearApuestaMenorAMontoMinimo(self):
        valorApuestaPrueba = self.dataFactory.pyfloat(min_value=0, max_value=1)
        fracaso = self.eporra.crearApuesta(self.nombreApostador, self.idCarreraPrueba, valorApuestaPrueba, self.competidoresPrueba[0]["Nombre"])
        self.assertFalse(fracaso)
    
    def test_crearApuestaApostadorVacio(self):
        nombreApostador = ""
        fracaso = self.eporra.crearApuesta(nombreApostador, self.idCarreraPrueba, 1.0, self.competidoresPrueba[0]["Nombre"])
        self.assertFalse(fracaso)
    
    def test_crearApuestaCompetidorVacio(self):
        nombreCompetidor = ""
        fracaso = self.eporra.crearApuesta(self.nombreApostador, self.idCarreraPrueba, 1.0, nombreCompetidor)
        self.assertFalse(fracaso)
    
    def test_darApuestasCarrerasVacio(self):
        resultado = self.eporra.darApuestasCarrera(self.idCarreraPrueba)
        self.assertListEqual([], resultado)

    def test_darApuestasCarrerasConCarreras(self):
        self.eporra.crearApuesta(self.nombreApostador, self.idCarreraPrueba, self.valorApuetaRandom, self.competidoresPrueba[0]["Nombre"])
        resultado = self.eporra.darApuestasCarrera(self.idCarreraPrueba)
        self.assertListEqual(self.apuestasPruebaLista, resultado)
    
    def test_darApuesta(self):
        idApuesta = 1
        resultadoCrearApuesta = self.eporra.crearApuesta(self.nombreApostador, self.idCarreraPrueba, self.valorApuetaRandom, self.competidoresPrueba[0]["Nombre"])
        resultadoDarApuesta = self.eporra.darApuesta(self.idCarreraPrueba,idApuesta)
        self.assertTrue(resultadoCrearApuesta)
        self.assertEqual(self.apuestasPrueba, resultadoDarApuesta)

    def test_darApuestaIdInvalido(self):
        idApuesta = 100
        resultadoCrearApuesta = self.eporra.crearApuesta(self.nombreApostador, self.idCarreraPrueba, self.valorApuetaRandom, self.competidoresPrueba[0]["Nombre"])
        resultadoDarApuesta = self.eporra.darApuesta(idApuesta)
        self.assertTrue(resultadoCrearApuesta)
        self.assertEqual(False, resultadoDarApuesta)
    
    def test_editarApuesta(self):
        idApuesta = 1
        apuestaEditada = {"Apostador": self.nombreApostador, "Valor": 6.00, "Competidor": self.competidoresPrueba[1]["Nombre"]}
        resultadoCrearApuesta = self.eporra.crearApuesta(self.nombreApostador, self.idCarreraPrueba, self.valorApuetaRandom, self.competidoresPrueba[0]["Nombre"])
        editarApuesta = self.eporra.editarApuesta(idApuesta, apuestaEditada["Apostador"], self.idCarreraPrueba, apuestaEditada["Valor"], apuestaEditada["Competidor"])
        resultadoEdicion = self.eporra.darApuesta(self.idCarreraPrueba, idApuesta)
        self.assertTrue(resultadoCrearApuesta)
        self.assertTrue(editarApuesta)
        self.assertEqual(apuestaEditada, resultadoEdicion)

    def test_editarApuestaIdInvalido(self):
        idApuesta = 200
        apuestaEditada = {"Apostador": self.nombreApostador, "Valor": 6.00, "Competidor": self.competidoresPrueba[1]["Nombre"]}
        resultadoCrearApuesta = self.eporra.crearApuesta(self.nombreApostador, self.idCarreraPrueba, self.valorApuetaRandom, self.competidoresPrueba[0]["Nombre"])
        editarApuesta = self.eporra.editarApuesta(idApuesta, apuestaEditada["Apostador"], self.idCarreraPrueba, apuestaEditada["Valor"], apuestaEditada["Competidor"])
        resultadoEdicion = self.eporra.darApuesta(idApuesta, self.idCarreraPrueba)
        self.assertTrue(resultadoCrearApuesta)
        self.assertFalse(editarApuesta)
        self.assertEqual(False, resultadoEdicion)

    def test_editarApuestaConDatosInvalido(self):
        idApuesta = 200
        apuestaEditada = {"Apostador": self.nombreApostador, "Valor": 6.00, "Competidor": self.competidoresPrueba[1]["Nombre"]}
        resultadoCrearApuesta = self.eporra.crearApuesta(self.nombreApostador, self.idCarreraPrueba, self.valorApuetaRandom, self.competidoresPrueba[0]["Nombre"])
        editarApuesta = self.eporra.editarApuesta(idApuesta, apuestaEditada["Apostador"], self.idCarreraPrueba, apuestaEditada["Valor"], apuestaEditada["Competidor"])
        resultadoEdicion = self.eporra.darApuesta(idApuesta)
        self.assertTrue(resultadoCrearApuesta)
        self.assertFalse(editarApuesta)
        self.assertEqual(False, resultadoEdicion)
    
    def tearDown(self):
        self.competidoresPrueba = []
        self.session.query(Carrera).delete()
        self.session.query(Apuesta).delete()
        self.session.query(Competidor).delete()
        self.session.query(Apostador).delete()
        self.session.commit()