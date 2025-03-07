from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

class ConsultaPediatrica(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Crear botón de "Atrás"
        self.back_button = QPushButton("Atrás")
        self.back_button.clicked.connect(self.go_back)
        layout.addWidget(self.back_button)

        # Aquí puedes agregar los campos específicos para la consulta pediátrica
        layout.addWidget(QLabel("Consulta Pediátrica"))

    def go_back(self):
        self.parent.show_main_menu()