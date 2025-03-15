import sys
from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Historia Clínica")
        self.setGeometry(100, 100, 820, 560)  # Establece las dimensiones de la ventana
        self.setStyleSheet("background-color: white;")  # Establece el color de fondo a blanco

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()