import sys
from PyQt5.QtWidgets import QApplication
from src.logica.eporra import EPorra
from src.vista.InterfazEPorra import App_EPorra
from src.logica.Logica_mock import Logica_mock
if __name__ == '__main__':
    # Punto inicial de la aplicación

    #logica = Logica_mock()
    logica = EPorra()
    app = App_EPorra(sys.argv, logica)
    sys.exit(app.exec_())