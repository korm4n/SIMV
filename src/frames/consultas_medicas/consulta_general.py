from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFormLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QDateEdit, QTextEdit, QCheckBox, QSpacerItem, QSizePolicy
from PySide6.QtGui import QIntValidator, QDoubleValidator, QIcon
from PySide6.QtCore import QSize, Qt, QDate, QTime
from utils import calculate_age  # Importar la función desde utils.py
from frames.consultas_medicas.Historia_Clinica.Historia_clinica_p import MainWindow  # Importar la clase MainWindow

class ConsultaGeneral(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Crear el formulario de paciente
        form_layout = QFormLayout()
        layout.addLayout(form_layout)

        # Crear un layout horizontal para los campos en una misma línea
        h_layout1 = QHBoxLayout()

        self.cedula_entry = QLineEdit()
        self.cedula_entry.setMaxLength(20)
        self.cedula_entry.setFixedWidth(100)
        h_layout1.addWidget(QLabel("Cédula:"))
        h_layout1.addWidget(self.cedula_entry)

        self.primer_nombre_entry = QLineEdit()
        self.primer_nombre_entry.setMaxLength(255)
        self.primer_nombre_entry.setFixedWidth(120)
        h_layout1.addWidget(QLabel("Primer Nombre:"))
        h_layout1.addWidget(self.primer_nombre_entry)

        self.segundo_nombre_entry = QLineEdit()
        self.segundo_nombre_entry.setMaxLength(255)
        self.segundo_nombre_entry.setFixedWidth(100)
        h_layout1.addWidget(QLabel("Segundo Nombre:"))
        h_layout1.addWidget(self.segundo_nombre_entry)

        self.primer_apellido_entry = QLineEdit()
        self.primer_apellido_entry.setMaxLength(255)
        self.primer_apellido_entry.setFixedWidth(120)
        h_layout1.addWidget(QLabel("Primer Apellido:"))
        h_layout1.addWidget(self.primer_apellido_entry)

        self.segundo_apellido_entry = QLineEdit()
        self.segundo_apellido_entry.setMaxLength(255)
        self.segundo_apellido_entry.setFixedWidth(100)
        h_layout1.addWidget(QLabel("Segundo Apellido:"))
        h_layout1.addWidget(self.segundo_apellido_entry)

        self.age_label_paciente = QLabel()
        self.age_label_paciente.setFixedWidth(30)
        h_layout1.addWidget(QLabel("Edad:"))
        h_layout1.addWidget(self.age_label_paciente)

        form_layout.addRow(h_layout1)

        # Crear un layout horizontal para los campos en una misma línea
        h_layout2 = QHBoxLayout()

        self.fecha_nacimiento_entry = QDateEdit()
        self.fecha_nacimiento_entry.setCalendarPopup(True)
        self.fecha_nacimiento_entry.setFixedWidth(100)
        self.fecha_nacimiento_entry.dateChanged.connect(self.update_age_paciente)
        h_layout2.addWidget(QLabel("Fecha de Nacimiento:"))
        h_layout2.addWidget(self.fecha_nacimiento_entry)

        self.genero_entry = QComboBox()
        self.genero_entry.addItems(["Masculino", "Femenino"])
        self.genero_entry.setFixedWidth(100)
        h_layout2.addWidget(QLabel("Género:"))
        h_layout2.addWidget(self.genero_entry)

        self.estado_civil_entry = QComboBox()
        self.estado_civil_entry.addItems(["Soltero", "Casado", "Viudo", "Divorciado"])
        self.estado_civil_entry.setFixedWidth(100)
        h_layout2.addWidget(QLabel("Estado Civil:"))
        h_layout2.addWidget(self.estado_civil_entry)

        self.nacionalidad_entry = QLineEdit()
        self.nacionalidad_entry.setMaxLength(20)
        self.nacionalidad_entry.setFixedWidth(110)
        h_layout2.addWidget(QLabel("Nacionalidad:"))
        h_layout2.addWidget(self.nacionalidad_entry)

        self.profesion_ocupacion_entry = QLineEdit()
        self.profesion_ocupacion_entry.setMaxLength(100)
        self.profesion_ocupacion_entry.setFixedWidth(180)
        h_layout2.addWidget(QLabel("Profesión/Ocupación:"))
        h_layout2.addWidget(self.profesion_ocupacion_entry)

        form_layout.addRow(h_layout2)

        # Crear un layout horizontal para los campos en una misma línea
        h_layout3 = QHBoxLayout()

        self.lugar_nacimiento_entry = QLineEdit()
        self.lugar_nacimiento_entry.setMaxLength(255)
        self.lugar_nacimiento_entry.setFixedWidth(100)
        h_layout3.addWidget(QLabel("Lugar de Nacimiento:"))
        h_layout3.addWidget(self.lugar_nacimiento_entry)

        self.religion_entry = QLineEdit()
        self.religion_entry.setMaxLength(20)
        self.religion_entry.setFixedWidth(100)
        h_layout3.addWidget(QLabel("Religión:"))
        h_layout3.addWidget(self.religion_entry)

        self.nombre_apellido_emergencia_entry = QLineEdit()
        self.nombre_apellido_emergencia_entry.setMaxLength(255)
        self.nombre_apellido_emergencia_entry.setFixedWidth(150)
        h_layout3.addWidget(QLabel("Familiar de Emergencia:"))
        h_layout3.addWidget(self.nombre_apellido_emergencia_entry)

        self.telefono_emergencia_entry = QLineEdit()
        self.telefono_emergencia_entry.setMaxLength(20)
        self.telefono_emergencia_entry.setFixedWidth(100)
        h_layout3.addWidget(QLabel("Teléfono de Emergencia:"))
        h_layout3.addWidget(self.telefono_emergencia_entry)

        self.parentesco_entry = QLineEdit()
        self.parentesco_entry.setMaxLength(20)
        self.parentesco_entry.setFixedWidth(100)
        h_layout3.addWidget(QLabel("Parentesco:"))
        h_layout3.addWidget(self.parentesco_entry)

        form_layout.addRow(h_layout3)

        # Crear un layout horizontal para los campos en una misma línea
        h_layout4 = QHBoxLayout()

        self.direccion_entry = QLineEdit()
        self.direccion_entry.setMaxLength(255)
        self.direccion_entry.setFixedWidth(280)
        h_layout4.addWidget(QLabel("Dirección:"))
        h_layout4.addWidget(self.direccion_entry)

        self.temperatura_entry = QLineEdit()
        self.temperatura_entry.setValidator(QDoubleValidator(0, 100, 2))
        self.temperatura_entry.setFixedWidth(50)
        self.temperatura_entry.setPlaceholderText("Temp")
        h_layout4.addWidget(self.temperatura_entry)

        self.pulso_entry = QLineEdit()
        self.pulso_entry.setValidator(QIntValidator(0, 300))
        self.pulso_entry.setFixedWidth(50)
        self.pulso_entry.setPlaceholderText("Pulso")
        h_layout4.addWidget(self.pulso_entry)

        self.respiracion_entry = QLineEdit()
        self.respiracion_entry.setValidator(QIntValidator(0, 100))
        self.respiracion_entry.setFixedWidth(80)
        self.respiracion_entry.setPlaceholderText("Respiración")
        h_layout4.addWidget(self.respiracion_entry)

        self.frecuencia_cardiaca_entry = QLineEdit()
        self.frecuencia_cardiaca_entry.setValidator(QIntValidator(0, 300))
        self.frecuencia_cardiaca_entry.setFixedWidth(90)
        self.frecuencia_cardiaca_entry.setPlaceholderText("Ritmo Cardíaco")
        h_layout4.addWidget(self.frecuencia_cardiaca_entry)

        self.tension_arterial_maxima_entry = QLineEdit()
        self.tension_arterial_maxima_entry.setValidator(QIntValidator(0, 300))
        self.tension_arterial_maxima_entry.setFixedWidth(100)
        self.tension_arterial_maxima_entry.setPlaceholderText("Tensión Máxima")
        h_layout4.addWidget(self.tension_arterial_maxima_entry)

        self.tension_arterial_minima_entry = QLineEdit()
        self.tension_arterial_minima_entry.setValidator(QIntValidator(0, 300))
        self.tension_arterial_minima_entry.setFixedWidth(100)
        self.tension_arterial_minima_entry.setPlaceholderText("Tensión Mínima")
        h_layout4.addWidget(self.tension_arterial_minima_entry)

        self.peso_entry = QLineEdit()
        self.peso_entry.setValidator(QDoubleValidator(0, 500, 2))
        self.peso_entry.setFixedWidth(45)
        self.peso_entry.setPlaceholderText("Peso")
        h_layout4.addWidget(self.peso_entry)

        self.talla_entry = QLineEdit()
        self.talla_entry.setValidator(QDoubleValidator(0, 3, 2))
        self.talla_entry.setFixedWidth(40)
        self.talla_entry.setPlaceholderText("Talla")
        h_layout4.addWidget(self.talla_entry)

        self.grasa_corporal_entry = QLineEdit()
        self.grasa_corporal_entry.setValidator(QDoubleValidator(0, 100, 2))
        self.grasa_corporal_entry.setFixedWidth(95)
        self.grasa_corporal_entry.setPlaceholderText("Grasa Corporal")
        h_layout4.addWidget(self.grasa_corporal_entry)

        self.indice_masa_corporal_entry = QLineEdit()
        self.indice_masa_corporal_entry.setValidator(QDoubleValidator(0, 100, 2))
        self.indice_masa_corporal_entry.setFixedWidth(95)
        self.indice_masa_corporal_entry.setPlaceholderText("Masa Corporal")
        h_layout4.addWidget(self.indice_masa_corporal_entry)

        form_layout.addRow(h_layout4)

        self.motivo_consulta_entry = QTextEdit()
        self.motivo_consulta_entry.setFixedWidth(1020)
        form_layout.addRow(QLabel("Motivo de Consulta:"), self.motivo_consulta_entry)

        self.enfermedad_actual_entry = QTextEdit()
        self.enfermedad_actual_entry.setFixedWidth(1020)
        form_layout.addRow(QLabel("Enfermedad Actual:"), self.enfermedad_actual_entry)

        self.diagnostico_admision_entry = QTextEdit()
        self.diagnostico_admision_entry.setFixedWidth(1020)
        form_layout.addRow(QLabel("Diagnóstico de<br>Admisión:"), self.diagnostico_admision_entry)

        self.intervencion_tratamiento_entry = QTextEdit()
        self.intervencion_tratamiento_entry.setFixedWidth(1020)
        form_layout.addRow(QLabel("Intervención y/o <br>Tratamiento:"), self.intervencion_tratamiento_entry)

        self.diagnostico_final_entry = QTextEdit()
        self.diagnostico_final_entry.setFixedWidth(1020)
        form_layout.addRow(QLabel("Diagnóstico Final:"), self.diagnostico_final_entry)

        h_layout5 = QHBoxLayout()

        self.estado_actual_entry = QComboBox()
        self.estado_actual_entry.addItems(["Seleccione", "Mejora", "Ingreso", "Muerte"])
        self.estado_actual_entry.setFixedWidth(100)
        self.estado_actual_entry.currentIndexChanged.connect(self.update_autopsia_state)  # Conectar la señal
        h_layout5.addWidget(QLabel("Estado Actual:"))
        h_layout5.addWidget(self.estado_actual_entry)

        self.autopsia_entry = QComboBox()
        self.autopsia_entry.addItems(["Seleccione", "Si", "No"])
        self.autopsia_entry.setFixedWidth(100)
        self.autopsia_entry.setEnabled(False)  # Deshabilitar inicialmente
        h_layout5.addWidget(QLabel("Autopsia Pedida:"))
        h_layout5.addWidget(self.autopsia_entry)

        self.fecha_alta_entry = QDateEdit(QDate.currentDate())  # Establecer la fecha actual
        self.fecha_alta_entry.setCalendarPopup(True)
        self.fecha_alta_entry.setFixedWidth(100)
        h_layout5.addWidget(QLabel("Fecha de Alta:"))
        h_layout5.addWidget(self.fecha_alta_entry)

        self.hora_alta_entry = QLineEdit(QTime.currentTime().toString("HH:mm"))  # Establecer la hora actual
        self.hora_alta_entry.setFixedWidth(100)
        h_layout5.addWidget(QLabel("Hora de Alta:"))
        h_layout5.addWidget(self.hora_alta_entry)

          # Agregar un espaciador para empujar la hora a la izquierda
        h_layout5.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        form_layout.addRow(h_layout5)

        # Crear un layout horizontal para los botones en la parte inferior
        button_layout = QHBoxLayout()

        # Botón "Historia Clínica" en la esquina inferior izquierda
        self.historia_clinica_button = QPushButton("Historia Clínica")
        self.historia_clinica_button.setIcon(QIcon("iconos/historial.png"))  # Establecer la imagen del botón
        self.historia_clinica_button.setIconSize(QSize(24, 24))  # Ajustar el tamaño de la imagen
        self.historia_clinica_button.setFixedSize(150, 40)  # Ajustar el tamaño del botón
        self.historia_clinica_button.clicked.connect(self.open_historia_clinica)  # Conectar la señal
        button_layout.addWidget(self.historia_clinica_button, alignment=Qt.AlignLeft)

        # Espaciador para empujar los botones hacia las esquinas
        button_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Botón "Atrás" en la esquina inferior derecha
        self.back_button = QPushButton("Atrás")
        self.back_button.setIcon(QIcon("iconos/atras.png"))  # Establecer la imagen del botón
        self.back_button.setIconSize(QSize(24, 24))  # Ajustar el tamaño de la imagen
        self.back_button.setFixedSize(100, 40)  # Ajustar el tamaño del botón
        self.back_button.clicked.connect(self.go_back)
        button_layout.addWidget(self.back_button, alignment=Qt.AlignRight)

        # Botón "Guardar" en la esquina inferior derecha
        self.save_button = QPushButton("Guardar")
        self.save_button.setIcon(QIcon("iconos/guardar.png"))  # Establecer la imagen del botón
        self.save_button.setIconSize(QSize(24, 24))  # Ajustar el tamaño de la imagen
        self.save_button.setFixedSize(100, 40)  # Ajustar el tamaño del botón
        button_layout.addWidget(self.save_button, alignment=Qt.AlignRight)

        layout.addLayout(button_layout)

    def go_back(self):
        self.parent.show_main_menu()

    def update_age_paciente(self):
        birthdate = self.fecha_nacimiento_entry.date().toPython()
        age = calculate_age(birthdate)
        self.age_label_paciente.setText(str(age))

    def update_autopsia_state(self):
        if self.estado_actual_entry.currentText() == "Muerte":
            self.autopsia_entry.setEnabled(True)
        else:
            self.autopsia_entry.setEnabled(False)

    def open_historia_clinica(self):
        self.historia_clinica_window = MainWindow()
        self.historia_clinica_window.show()