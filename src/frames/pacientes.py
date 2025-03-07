from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from consultas_medicas.consulta_general import ConsultaGeneral
from consultas_medicas.consulta_pediatrica import ConsultaPediatrica
from consultas_medicas.consulta_ginecologica import ConsultaGinecologica
from consultas_medicas.emergencia import Emergencia
from datetime import date

def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

class Pacientes(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Información Médica")
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # Crear botones
        self.consulta_general_button = QPushButton("Consulta General")
        self.consulta_pediatrica_button = QPushButton("Consulta Pediátrica")
        self.consulta_ginecologica_button = QPushButton("Consulta Ginecológica")
        self.emergencia_button = QPushButton("Emergencia")

        # Conectar botones a sus acciones
        self.consulta_general_button.clicked.connect(self.show_consulta_general)
        self.consulta_pediatrica_button.clicked.connect(self.show_consulta_pediatrica)
        self.consulta_ginecologica_button.clicked.connect(self.show_consulta_ginecologica)
        self.emergencia_button.clicked.connect(self.show_emergencia)

        # Agregar botones al layout
        self.main_layout.addWidget(self.consulta_general_button)
        self.main_layout.addWidget(self.consulta_pediatrica_button)
        self.main_layout.addWidget(self.consulta_ginecologica_button)
        self.main_layout.addWidget(self.emergencia_button)

    def show_main_menu(self):
        self.clear_layout(self.main_layout)
        self.main_layout.addWidget(self.consulta_general_button)
        self.main_layout.addWidget(self.consulta_pediatrica_button)
        self.main_layout.addWidget(self.consulta_ginecologica_button)
        self.main_layout.addWidget(self.emergencia_button)

    def show_consulta_general(self):
        self.clear_layout(self.main_layout)
        self.consulta_general_frame = ConsultaGeneral(self)
        self.main_layout.addWidget(self.consulta_general_frame)

    def show_consulta_pediatrica(self):
        self.clear_layout(self.main_layout)
        self.consulta_pediatrica_frame = ConsultaPediatrica(self)
        self.main_layout.addWidget(self.consulta_pediatrica_frame)

    def show_consulta_ginecologica(self):
        self.clear_layout(self.main_layout)
        self.consulta_ginecologica_frame = ConsultaGinecologica(self)
        self.main_layout.addWidget(self.consulta_ginecologica_frame)

    def show_emergencia(self):
        self.clear_layout(self.main_layout)
        self.emergencia_frame = Emergencia(self)
        self.main_layout.addWidget(self.emergencia_frame)

    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def calculate_age(self, birthdate):
        return calculate_age(birthdate)