from PySide6.QtWidgets import QApplication, QMainWindow
import sys
from ventana import Ventana

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.setWindowTitle("Sistema de Información Médica")
    ventana.show()
    sys.exit(app.exec())