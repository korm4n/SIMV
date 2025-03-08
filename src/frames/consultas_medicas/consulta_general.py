from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFormLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QDateEdit, QSpacerItem, QSizePolicy
from PySide6.QtGui import QIntValidator, QRegularExpressionValidator, QIcon
from PySide6.QtCore import QRegularExpression, QSize, Qt
from utils import calculate_age  # Importar la función desde utils.py

class ConsultaGeneral(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Crear botón de "Atrás"
        self.back_button = QPushButton("Atrás")
        self.back_button.setIcon(QIcon("ruta/a/tu/imagen.png"))  # Establecer la imagen del botón
        self.back_button.setIconSize(QSize(24, 24))  # Ajustar el tamaño de la imagen
        self.back_button.setFixedSize(100, 40)  # Ajustar el tamaño del botón
        self.back_button.clicked.connect(self.go_back)
        layout.addWidget(self.back_button, alignment=Qt.AlignLeft)  # Ajustar la ubicación del botón

        # Crear el formulario de paciente
        form_layout = QFormLayout()
        layout.addLayout(form_layout)

        # Agrupar cédula, nombres, apellidos, fecha de nacimiento y edad en una fila
        row_layout1 = QHBoxLayout()
        row_layout1.setContentsMargins(0, 0, 0, 0)  # Ajustar márgenes
        self.cedula_entry_paciente = QLineEdit()
        self.cedula_entry_paciente.setValidator(QIntValidator(0, 99999999))
        self.cedula_entry_paciente.setMaxLength(8)
        self.cedula_entry_paciente.setFixedWidth(100)
        self.cedula_entry_paciente.setStyleSheet("background-color: white;")
        row_layout1.addWidget(QLabel("Cédula:"))
        row_layout1.addSpacerItem(QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout1.addWidget(self.cedula_entry_paciente)
        
        self.nombres_entry_paciente = QLineEdit()
        self.nombres_entry_paciente.setValidator(QRegularExpressionValidator(QRegularExpression("[A-Za-z ]{1,50}")))
        self.nombres_entry_paciente.setMaxLength(50)
        self.nombres_entry_paciente.setFixedWidth(150)
        self.nombres_entry_paciente.setStyleSheet("background-color: white;")
        row_layout1.addWidget(QLabel("Nombres:"))
        row_layout1.addSpacerItem(QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout1.addWidget(self.nombres_entry_paciente)
        
        self.apellidos_entry_paciente = QLineEdit()
        self.apellidos_entry_paciente.setValidator(QRegularExpressionValidator(QRegularExpression("[A-Za-z ]{1,50}")))
        self.apellidos_entry_paciente.setMaxLength(50)
        self.apellidos_entry_paciente.setFixedWidth(150)
        self.apellidos_entry_paciente.setStyleSheet("background-color: white;")
        row_layout1.addWidget(QLabel("Apellidos:"))
        row_layout1.addSpacerItem(QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout1.addWidget(self.apellidos_entry_paciente)
        
        self.birthdate_entry_paciente = QDateEdit()
        self.birthdate_entry_paciente.setCalendarPopup(True)
        self.birthdate_entry_paciente.setFixedWidth(120)
        self.birthdate_entry_paciente.setStyleSheet("""
            QDateEdit {
                background-color: white;
            }
            QCalendarWidget QToolButton {
                color: white;
                background-color: #2c3e50;
            }
            QCalendarWidget QMenu {
                color: white;
                background-color: #2c3e50;
            }
            QCalendarWidget QSpinBox {
                color: white;
                background-color: #2c3e50;
            }
            QCalendarWidget QWidget#qt_calendar_navigationbar {
                background-color: #2c3e50;
            }
            QCalendarWidget QAbstractItemView:enabled {
                color: white;
                background-color: #34495e;
                selection-background-color: #1abc9c;
                selection-color: black;
            }
        """)
        self.birthdate_entry_paciente.dateChanged.connect(self.update_age_paciente)
        row_layout1.addWidget(QLabel("Fecha de Nacimiento:"))
        row_layout1.addSpacerItem(QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout1.addWidget(self.birthdate_entry_paciente)
        
        self.age_label_paciente = QLabel("")
        self.age_label_paciente.setFixedWidth(50)
        row_layout1.addWidget(QLabel("Edad:"))
        row_layout1.addSpacerItem(QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout1.addWidget(self.age_label_paciente)
        
        form_layout.addRow(row_layout1)

        # Otros campos del formulario pueden ser agregados aquí de manera similar...

    def go_back(self):
        self.parent.show_main_menu()

    def update_age_paciente(self):
        birthdate = self.birthdate_entry_paciente.date().toPython()
        age = calculate_age(birthdate)
        self.age_label_paciente.setText(str(age))