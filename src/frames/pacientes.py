from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize  # Importar QSize desde QtCore
from .consultas_medicas.consulta_general import ConsultaGeneral
from .consultas_medicas.consulta_pediatrica import ConsultaPediatrica
from .consultas_medicas.consulta_ginecologica import ConsultaGinecologica
from .consultas_medicas.emergencia import Emergencia

class Pacientes(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Información Médica")
        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)

        # Crear botones con iconos
        self.consulta_general_button = QPushButton("Consulta General")
        self.consulta_general_button.setIcon(QIcon("C:\\Users\\kervinfb\\OneDrive\\Documents\\Sistema de Informacion Medica\\sistema-informacion-medica\\src\\iconos\\medicopaciente.png"))
        self.consulta_general_button.setFixedSize(200, 50)  # Establecer tamaño del botón
        self.consulta_general_button.setIconSize(QSize(32, 32))  # Establecer tamaño del icono

        self.consulta_pediatrica_button = QPushButton("Consulta Pediátrica")
        self.consulta_pediatrica_button.setIcon(QIcon("C:\\Users\\kervinfb\\OneDrive\\Documents\\Sistema de Informacion Medica\\sistema-informacion-medica\\src\\iconos\\pediatria.png"))
        self.consulta_pediatrica_button.setFixedSize(200, 50)  # Establecer tamaño del botón
        self.consulta_pediatrica_button.setIconSize(QSize(32, 32))  # Establecer tamaño del icono

        self.consulta_ginecologica_button = QPushButton("Consulta Ginecológica")
        self.consulta_ginecologica_button.setIcon(QIcon("C:\\Users\\kervinfb\\OneDrive\\Documents\\Sistema de Informacion Medica\\sistema-informacion-medica\\src\\iconos\\ginecologia.png"))
        self.consulta_ginecologica_button.setFixedSize(200, 50)  # Establecer tamaño del botón
        self.consulta_ginecologica_button.setIconSize(QSize(32, 32))  # Establecer tamaño del icono

        self.emergencia_button = QPushButton("Emergencia")
        self.emergencia_button.setIcon(QIcon("iconos\\emergencia.png"))
        self.emergencia_button.setFixedSize(200, 50)  # Establecer tamaño del botón
        self.emergencia_button.setIconSize(QSize(32, 32))  # Establecer tamaño del icono

        # Conectar botones a sus acciones
        self.consulta_general_button.clicked.connect(self.show_consulta_general)
        self.consulta_pediatrica_button.clicked.connect(self.show_consulta_pediatrica)
        self.consulta_ginecologica_button.clicked.connect(self.show_consulta_ginecologica)
        self.emergencia_button.clicked.connect(self.show_emergencia)

        # Agregar botones al layout en posiciones específicas
        self.main_layout.addWidget(self.consulta_general_button, 0, 0)  # Fila 0, Columna 0
        self.main_layout.addWidget(self.consulta_pediatrica_button, 0, 1)  # Fila 0, Columna 1
        self.main_layout.addWidget(self.consulta_ginecologica_button, 1, 0)  # Fila 1, Columna 0
        self.main_layout.addWidget(self.emergencia_button, 1, 1)  # Fila 1, Columna 1

    def show_main_menu(self):
        self.clear_layout(self.main_layout)
        self.main_layout.addWidget(self.consulta_general_button, 0, 0)
        self.main_layout.addWidget(self.consulta_pediatrica_button, 0, 1)
        self.main_layout.addWidget(self.consulta_ginecologica_button, 1, 0)
        self.main_layout.addWidget(self.emergencia_button, 1, 1)

    def show_consulta_general(self):
        self.clear_layout(self.main_layout)
        self.consulta_general_frame = ConsultaGeneral(self)
        self.main_layout.addWidget(self.consulta_general_frame, 0, 0, 1, 2)  # Ocupa dos columnas

    def show_consulta_pediatrica(self):
        self.clear_layout(self.main_layout)
        self.consulta_pediatrica_frame = ConsultaPediatrica(self)
        self.main_layout.addWidget(self.consulta_pediatrica_frame, 0, 0, 1, 2)  # Ocupa dos columnas

    def show_consulta_ginecologica(self):
        self.clear_layout(self.main_layout)
        self.consulta_ginecologica_frame = ConsultaGinecologica(self)
        self.main_layout.addWidget(self.consulta_ginecologica_frame, 0, 0, 1, 2)  # Ocupa dos columnas

    def show_emergencia(self):
        self.clear_layout(self.main_layout)
        self.emergencia_frame = Emergencia(self)
        self.main_layout.addWidget(self.emergencia_frame, 0, 0, 1, 2)  # Ocupa dos columnas

    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().setParent(None)