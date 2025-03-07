from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QFormLayout, QHBoxLayout, QLineEdit, QSpacerItem, QSizePolicy, QDateEdit, QComboBox, QPushButton, QMessageBox, QStackedWidget
from PySide6.QtGui import QIntValidator, QRegularExpressionValidator
from PySide6.QtCore import QDate, QRegularExpression

class MedicosEnfermeras(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        # Crear un QStackedWidget para contener los diferentes frames
        self.stacked_widget = QStackedWidget()
        self.medicos_frame = self.create_medicos_frame()
        self.stacked_widget.addWidget(self.medicos_frame)

        self.layout.addWidget(self.stacked_widget)
        self.setLayout(self.layout)

    def create_medicos_frame(self):
        frame = QWidget()
        layout = QFormLayout(frame)
        
        # Agrupar cédula, nombres, apellidos, fecha de nacimiento y edad en una fila
        row_layout1 = QHBoxLayout()
        row_layout1.setContentsMargins(0, 0, 0, 0)  # Ajustar márgenes
        self.cedula_entry_medico = QLineEdit()
        self.cedula_entry_medico.setValidator(QIntValidator(0, 99999999))
        self.cedula_entry_medico.setMaxLength(8)
        self.cedula_entry_medico.setFixedWidth(200)
        self.cedula_entry_medico.setStyleSheet("background-color: white;")
        row_layout1.addWidget(QLabel("Cédula:"))
        row_layout1.addSpacerItem(QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout1.addWidget(self.cedula_entry_medico)
        
        self.nombres_entry_medico = QLineEdit()
        self.nombres_entry_medico.setValidator(QRegularExpressionValidator(QRegularExpression("[A-Za-z ]{1,50}")))
        self.nombres_entry_medico.setMaxLength(50)
        self.nombres_entry_medico.setFixedWidth(200)
        self.nombres_entry_medico.setStyleSheet("background-color: white;")
        row_layout1.addWidget(QLabel("Nombres:"))
        row_layout1.addSpacerItem(QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout1.addWidget(self.nombres_entry_medico)
        
        self.apellidos_entry_medico = QLineEdit()
        self.apellidos_entry_medico.setValidator(QRegularExpressionValidator(QRegularExpression("[A-Za-z ]{1,50}")))
        self.apellidos_entry_medico.setMaxLength(50)
        self.apellidos_entry_medico.setFixedWidth(200)
        self.apellidos_entry_medico.setStyleSheet("background-color: white;")
        row_layout1.addWidget(QLabel("Apellidos:"))
        row_layout1.addSpacerItem(QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout1.addWidget(self.apellidos_entry_medico)
        
        self.birthdate_entry_medico = QDateEdit()
        self.birthdate_entry_medico.setCalendarPopup(True)
        self.birthdate_entry_medico.setFixedWidth(200)
        self.birthdate_entry_medico.setStyleSheet("""
            QDateEdit {
                background-color: white;
            }
            QCalendarWidget QToolButton {
                color: white;
                background-color: #2e2e2e;
            }
            QCalendarWidget QMenu {
                background-color: #2e2e2e;
                color: white;
            }
            QCalendarWidget QSpinBox {
                color: white;
                background-color: #2e2e2e;
            }
            QCalendarWidget QWidget#qt_calendar_navigationbar {
                background-color: #2e2e2e;
            }
            QCalendarWidget QAbstractItemView:enabled {
                color: white;
                background-color: #2e2e2e;
                selection-background-color: #4e4e4e;
                selection-color: white;
            }
        """)
        self.birthdate_entry_medico.dateChanged.connect(self.update_age_medico)
        row_layout1.addWidget(QLabel("Fecha de Nacimiento:"))
        row_layout1.addSpacerItem(QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout1.addWidget(self.birthdate_entry_medico)
        
        self.age_label_medico = QLabel("")
        self.age_label_medico.setFixedWidth(50)
        row_layout1.addWidget(QLabel("Edad:"))
        row_layout1.addSpacerItem(QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout1.addWidget(self.age_label_medico)
        
        layout.addRow(row_layout1)
        
        # Agrupar teléfono, género, estado civil y lugar de nacimiento en una fila (Médicos)
        row_layout2 = QHBoxLayout()
        self.telefono_entry_medico = QLineEdit()
        self.telefono_entry_medico.setInputMask("0000-0000000")  # Máscara de entrada para el formato (0000-0000000)
        self.telefono_entry_medico.setMaxLength(15)
        self.telefono_entry_medico.setFixedWidth(50)
        self.telefono_entry_medico.setStyleSheet("background-color: white;")
        self.telefono_entry_medico.setCursorPosition(0)  # Posicionar el cursor al inicio
        row_layout2.addWidget(QLabel("Teléfono:"))
        row_layout2.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout2.addWidget(self.telefono_entry_medico)

        self.genero_combobox_medico = QComboBox()
        self.genero_combobox_medico.addItems(["Masculino", "Femenino"])
        self.genero_combobox_medico.setFixedWidth(50)
        self.genero_combobox_medico.setStyleSheet("background-color: white;")
        row_layout2.addWidget(QLabel("Género:"))
        row_layout2.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout2.addWidget(self.genero_combobox_medico)

        self.estado_civil_combobox_medico = QComboBox()
        self.estado_civil_combobox_medico.addItems(["Soltero", "Casado", "Viudo", "Divorciado"])
        self.estado_civil_combobox_medico.setFixedWidth(50)
        self.estado_civil_combobox_medico.setStyleSheet("background-color: white;")
        row_layout2.addWidget(QLabel("Estado Civil:"))
        row_layout2.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout2.addWidget(self.estado_civil_combobox_medico)

        self.lugar_nacimiento_entry_medico = QLineEdit()
        self.lugar_nacimiento_entry_medico.setValidator(QRegularExpressionValidator(QRegularExpression("[A-Za-z ]{1,50}")))
        self.lugar_nacimiento_entry_medico.setMaxLength(50)
        self.lugar_nacimiento_entry_medico.setFixedWidth(50)
        self.lugar_nacimiento_entry_medico.setStyleSheet("background-color: white;")
        row_layout2.addWidget(QLabel("Lugar de Nacimiento:"))
        row_layout2.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout2.addWidget(self.lugar_nacimiento_entry_medico)

        layout.addRow(row_layout2)
        
        # Agrupar dirección y número de registro médico en una fila
        row_layout3 = QHBoxLayout()
        self.direccion_entry_medico = QLineEdit()
        self.direccion_entry_medico.setValidator(QRegularExpressionValidator(QRegularExpression(".{1,500}")))
        self.direccion_entry_medico.setMaxLength(200)
        self.direccion_entry_medico.setFixedWidth(200)
        self.direccion_entry_medico.setStyleSheet("background-color: white;")
        row_layout3.addWidget(QLabel("Dirección:"))
        row_layout3.addWidget(self.direccion_entry_medico)
        
        self.numero_registro_medico_entry = QLineEdit()
        self.numero_registro_medico_entry.setValidator(QRegularExpressionValidator(QRegularExpression(".{1,500}")))
        self.numero_registro_medico_entry.setMaxLength(20)
        self.numero_registro_medico_entry.setFixedWidth(20)
        self.numero_registro_medico_entry.setStyleSheet("background-color: white;")
        row_layout3.addWidget(QLabel("Número de Registro Médico:"))
        row_layout3.addWidget(self.numero_registro_medico_entry)
        
        layout.addRow(row_layout3)
        
        self.horario_guardia_entry = QLineEdit()
        self.horario_guardia_entry.setValidator(QRegularExpressionValidator(QRegularExpression(".{1,500}")))
        self.horario_guardia_entry.setMaxLength(30)
        self.horario_guardia_entry.setFixedWidth(30)
        self.horario_guardia_entry.setStyleSheet("background-color: white;")
        layout.addRow(QLabel("Horario de Guardia:"), self.horario_guardia_entry)
        
        self.save_button_medico = QPushButton("Guardar")
        self.save_button_medico.setFixedSize(150, 30)  # Establecer tamaño fijo
        self.save_button_medico.clicked.connect(self.save_medico)
        layout.addRow(self.save_button_medico)
        
        self.clear_button_medico = QPushButton("Limpiar Información")
        self.clear_button_medico.setFixedSize(150, 30)  # Establecer tamaño fijo
        self.clear_button_medico.clicked.connect(self.clear_medico_form)
        layout.addRow(self.clear_button_medico)
        
        frame.setLayout(layout)
        return frame

    def show_medicos_frame(self):
        self.stacked_widget.setCurrentWidget(self.medicos_frame)
    
    def calculate_age(self, birthdate):
        today = QDate.currentDate().toPython()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age

    def update_age_medico(self):
        birthdate = self.birthdate_entry_medico.date().toPython()
        age = self.calculate_age(birthdate)
        self.age_label_medico.setText(str(age))

    def save_medico(self):
        cedula = self.cedula_entry_medico.text()
        nombres = self.nombres_entry_medico.text()
        apellidos = self.apellidos_entry_medico.text()
        birthdate = self.birthdate_entry_medico.date().toPython()
        genero = self.genero_combobox_medico.currentText()
        estado_civil = self.estado_civil_combobox_medico.currentText()
        numero_registro_medico = self.numero_registro_medico_entry.text()
        horario_guardia = self.horario_guardia_entry.text()

        if not cedula or not nombres or not apellidos or not numero_registro_medico or not horario_guardia:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        # Aquí puedes agregar la lógica para guardar los datos en la base de datos
        QMessageBox.information(self, "Guardado", "Datos del médico guardados correctamente.")

    def clear_medico_form(self):
        self.cedula_entry_medico.clear()
        self.nombres_entry_medico.clear()
        self.apellidos_entry_medico.clear()
        self.birthdate_entry_medico.setDate(QDate.currentDate())
        self.age_label_medico.clear()
        self.genero_combobox_medico.setCurrentIndex(0)
        self.estado_civil_combobox_medico.setCurrentIndex(0)
        self.numero_registro_medico_entry.clear()
        self.horario_guardia_entry.clear()