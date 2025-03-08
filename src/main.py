from PySide6.QtWidgets import QApplication, QMainWindow
import sys
from ventana import Ventana

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.setWindowTitle("Sistema de Información Médica")
    
    # Aplicar hoja de estilo para cambiar el color del fondo, marco y cuadros de texto
    app.setStyleSheet(ventana.get_stylesheet())
    
    ventana.show()
    sys.exit(app.exec())