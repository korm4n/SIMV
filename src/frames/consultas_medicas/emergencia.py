from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QFormLayout, QHBoxLayout, QLineEdit, QDateEdit, QComboBox, QTextEdit, QMessageBox
from PySide6.QtGui import QIcon, QDoubleValidator, QIntValidator
from PySide6.QtCore import QDate, QTime, QSize, Qt
from PySide6.QtWidgets import QSpacerItem, QSizePolicy
from datetime import date
from servicios import CreateConnection  # Importar la clase para la conexión a la base de datos
from mysql.connector import Error

class Emergencia(QWidget):
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
        self.cedula_entry.setInputMask("000000000")  # Máscara de entrada para el formato (00000000)
        self.cedula_entry.setMaxLength(8)
        self.cedula_entry.setFixedWidth(100)
        self.cedula_entry.setCursorPosition(0)  # Asegurar que el cursor esté a la izquierda
        self.cedula_entry.editingFinished.connect(self.check_cedula)  # Conectar el evento de edición terminada
        self.cedula_entry.textChanged.connect(self.mover_cursor_al_inicio)  # Conectar para mover el cursor al inicio
        h_layout1.addWidget(QLabel("Cédula:"))
        h_layout1.addWidget(self.cedula_entry)

        self.primer_nombre_entry = QLineEdit()
        self.primer_nombre_entry.setMaxLength(255)
        self.primer_nombre_entry.setFixedWidth(120)
        self.primer_nombre_entry.textChanged.connect(self.convert_to_uppercase)
        h_layout1.addWidget(QLabel("Primer Nombre:"))
        h_layout1.addWidget(self.primer_nombre_entry)

        self.segundo_nombre_entry = QLineEdit()
        self.segundo_nombre_entry.setMaxLength(255)
        self.segundo_nombre_entry.setFixedWidth(100)
        self.segundo_nombre_entry.textChanged.connect(self.convert_to_uppercase)
        h_layout1.addWidget(QLabel("Segundo Nombre:"))
        h_layout1.addWidget(self.segundo_nombre_entry)

        self.primer_apellido_entry = QLineEdit()
        self.primer_apellido_entry.setMaxLength(255)
        self.primer_apellido_entry.setFixedWidth(120)
        self.primer_apellido_entry.textChanged.connect(self.convert_to_uppercase)
        h_layout1.addWidget(QLabel("Primer Apellido:"))
        h_layout1.addWidget(self.primer_apellido_entry)

        self.segundo_apellido_entry = QLineEdit()
        self.segundo_apellido_entry.setMaxLength(255)
        self.segundo_apellido_entry.setFixedWidth(100)
        self.segundo_apellido_entry.textChanged.connect(self.convert_to_uppercase)
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

        # Nuevo campo de teléfono
        self.telefono_entry = QLineEdit()
        self.telefono_entry.setInputMask("0000-0000000")  # Máscara de entrada para el formato (0000-0000000)
        self.telefono_entry.setMaxLength(12)
        self.telefono_entry.setFixedWidth(110)
        h_layout2.addWidget(QLabel("Teléfono:"))
        h_layout2.addWidget(self.telefono_entry)

        self.genero_entry = QComboBox()
        self.genero_entry.addItems(["Seleccione", "Masculino", "Femenino", "Otro"])
        self.genero_entry.setFixedWidth(80)
        h_layout2.addWidget(QLabel("Género:"))
        h_layout2.addWidget(self.genero_entry)

        self.estado_civil_entry = QComboBox()
        self.estado_civil_entry.addItems(["Seleccione", "Soltero", "Casado", "Viudo", "Divorciado"])
        self.estado_civil_entry.setFixedWidth(80)
        h_layout2.addWidget(QLabel("Estado Civil:"))
        h_layout2.addWidget(self.estado_civil_entry)

        self.nacionalidad_entry = QComboBox()
        self.nacionalidad_entry.addItems(["Seleccione", "Venezolana", "Extranjera"])
        self.nacionalidad_entry.setFixedWidth(90)
        h_layout2.addWidget(QLabel("Nacionalidad:"))
        h_layout2.addWidget(self.nacionalidad_entry)

        self.profesion_ocupacion_entry = QLineEdit()
        self.profesion_ocupacion_entry.setMaxLength(100)
        self.profesion_ocupacion_entry.setFixedWidth(110)
        self.profesion_ocupacion_entry.textChanged.connect(self.convert_to_uppercase)
        h_layout2.addWidget(QLabel("Profesión/Ocupación:"))
        h_layout2.addWidget(self.profesion_ocupacion_entry)

        form_layout.addRow(h_layout2)

        # Crear un layout horizontal para los campos en una misma línea
        h_layout3 = QHBoxLayout()

        self.lugar_nacimiento_entry = QLineEdit()
        self.lugar_nacimiento_entry.setMaxLength(255)
        self.lugar_nacimiento_entry.setFixedWidth(100)
        self.lugar_nacimiento_entry.textChanged.connect(self.convert_to_uppercase)
        h_layout3.addWidget(QLabel("Lugar de Nacimiento:"))
        h_layout3.addWidget(self.lugar_nacimiento_entry)

        self.religion_entry = QLineEdit()
        self.religion_entry.setMaxLength(20)
        self.religion_entry.setFixedWidth(100)
        self.religion_entry.textChanged.connect(self.convert_to_uppercase)
        h_layout3.addWidget(QLabel("Religión:"))
        h_layout3.addWidget(self.religion_entry)

        self.nombre_apellido_emergencia_entry = QLineEdit()
        self.nombre_apellido_emergencia_entry.setMaxLength(255)
        self.nombre_apellido_emergencia_entry.setFixedWidth(150)
        self.nombre_apellido_emergencia_entry.textChanged.connect(self.convert_to_uppercase)
        h_layout3.addWidget(QLabel("Familiar de Emergencia:"))
        h_layout3.addWidget(self.nombre_apellido_emergencia_entry)

        self.telefono_emergencia_entry = QLineEdit()
        self.telefono_emergencia_entry.setInputMask("0000-0000000")  # Máscara de entrada para el formato (0000-0000000)
        self.telefono_emergencia_entry.setMaxLength(12)
        self.telefono_emergencia_entry.setFixedWidth(110)
        h_layout3.addWidget(QLabel("Teléfono de Emergencia:"))
        h_layout3.addWidget(self.telefono_emergencia_entry)

        self.parentesco_entry = QLineEdit()
        self.parentesco_entry.setMaxLength(20)
        self.parentesco_entry.setFixedWidth(100)
        self.parentesco_entry.textChanged.connect(self.convert_to_uppercase)
        h_layout3.addWidget(QLabel("Parentesco:"))
        h_layout3.addWidget(self.parentesco_entry)

        form_layout.addRow(h_layout3)

        # Crear un layout horizontal para los campos en una misma línea
        h_layout4 = QHBoxLayout()

        self.direccion_entry = QLineEdit()
        self.direccion_entry.setMaxLength(255)
        self.direccion_entry.setFixedWidth(280)
        self.direccion_entry.textChanged.connect(self.convert_to_uppercase)
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

        self.hora_alta_entry = QLineEdit(QTime.currentTime().toString("HH:mm:ss"))  # Establecer la hora actual
        self.hora_alta_entry.setFixedWidth(100)
        h_layout5.addWidget(QLabel("Hora de Alta:"))
        h_layout5.addWidget(self.hora_alta_entry)

          # Agregar un espaciador para empujar la hora a la izquierda
        h_layout5.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        form_layout.addRow(h_layout5)

        # Crear un layout horizontal para los botones en la parte inferior
        button_layout = QHBoxLayout()

        # Espaciador para empujar los botones hacia las esquinas
        button_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Botón "Atrás" en la esquina inferior derecha
        self.back_button = QPushButton("Atrás")
        self.back_button.setIcon(QIcon("iconos/atras.png"))  # Establecer la imagen del botón
        self.back_button.setIconSize(QSize(24, 24))  # Ajustar el tamaño de la imagen
        self.back_button.setFixedSize(100, 40)  # Ajustar el tamaño del botón
        self.back_button.clicked.connect(self.go_back)
        button_layout.addWidget(self.back_button, alignment=Qt.AlignRight)

        # Botón "Limpiar" en la esquina inferior derecha
        self.clear_button = QPushButton("Limpiar")
        self.clear_button.setIcon(QIcon("iconos/limpiar.png"))  # Establecer la imagen del botón
        self.clear_button.setIconSize(QSize(24, 24))  # Ajustar el tamaño de la imagen
        self.clear_button.setFixedSize(100, 40)  # Ajustar el tamaño del botón
        self.clear_button.clicked.connect(self.clear_all_fields)  # Conectar la señal
        button_layout.addWidget(self.clear_button, alignment=Qt.AlignRight)

        # Botón "Guardar" en la esquina inferior derecha
        self.save_button = QPushButton("Guardar")
        self.save_button.setIcon(QIcon("iconos/guardar.png"))  # Establecer la imagen del botón
        self.save_button.setIconSize(QSize(24, 24))  # Ajustar el tamaño de la imagen
        self.save_button.setFixedSize(100, 40)  # Ajustar el tamaño del botón
        self.save_button.clicked.connect(self.save_data)
        button_layout.addWidget(self.save_button, alignment=Qt.AlignRight)

        layout.addLayout(button_layout)


    def go_back(self):
        self.parent.show_main_menu()

    def check_cedula(self):
        cedula = self.cedula_entry.text()
        if (len(cedula) == 8 or len(cedula) == 9) and cedula.isdigit():
            db = CreateConnection()
            connection = db.create_connection()
            if connection:
                try:
                    cursor = connection.cursor()
                    query = "SELECT * FROM pacientes WHERE cedula = %s"
                    cursor.execute(query, (cedula,))
                    data = cursor.fetchone()
                    if data:
                        # Cargar los datos en el formulario
                        self.cedula_entry.setText(data[0])
                        self.primer_nombre_entry.setText(data[1])
                        self.segundo_nombre_entry.setText(data[2])
                        self.primer_apellido_entry.setText(data[3])
                        self.segundo_apellido_entry.setText(data[4])
                        self.fecha_nacimiento_entry.setDate(QDate.fromString(str(data[5]), "yyyy-MM-dd"))
                        self.telefono_entry.setText(data[6])
                        self.genero_entry.setCurrentText(data[8])
                        self.estado_civil_entry.setCurrentText(data[9])
                        self.nacionalidad_entry.setCurrentText(data[11])
                        self.profesion_ocupacion_entry.setText(data[12])
                        self.lugar_nacimiento_entry.setText(data[7])
                        self.religion_entry.setText(data[13])
                        self.nombre_apellido_emergencia_entry.setText(data[14])
                        self.telefono_emergencia_entry.setText(data[15])
                        self.parentesco_entry.setText(data[16])
                        self.direccion_entry.setText(data[10])
                    # No hacer nada si no se encuentra la cédula
                except Error as e:
                    QMessageBox.critical(self, "Error", f"Error al buscar la cédula: {e}")
                finally:
                    cursor.close()
                    connection.close()
            else:
                QMessageBox.critical(self, "Error", "No se pudo establecer la conexión con la base de datos.")
        else:
            QMessageBox.warning(self, "Cédula", "Cédula inválida. Debe contener 9 dígitos maximo.")
            self.cedula_entry.clear()
            self.cedula_entry.setFocus()

    def mover_cursor_al_inicio(self):
        if not self.cedula_entry.text():
            self.cedula_entry.setCursorPosition(0)

    def convert_to_uppercase(self):
        sender = self.sender()
        if sender:
            sender.setText(sender.text().upper())

    def update_age_paciente(self):
        fecha_nacimiento = self.fecha_nacimiento_entry.date().toPython()
        today = date.today()
        age = today.year - fecha_nacimiento.year - ((today.month, today.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        self.age_label_paciente.setText(str(age))

    def update_autopsia_state(self, index):
        if self.estado_actual_entry.itemText(index) == "Muerte":
            self.autopsia_entry.setEnabled(True)
        else:
            self.autopsia_entry.setEnabled(False)
            self.autopsia_entry.setCurrentIndex(0)  # Restablecer a "Seleccione"

    def clear_all_fields(self):
        self.cedula_entry.clear()
        self.primer_nombre_entry.clear()
        self.segundo_nombre_entry.clear()
        self.primer_apellido_entry.clear()
        self.segundo_apellido_entry.clear()
        self.fecha_nacimiento_entry.setDate(QDate.currentDate())
        self.age_label_paciente.clear()
        self.telefono_entry.clear()
        self.genero_entry.setCurrentIndex(0)
        self.estado_civil_entry.setCurrentIndex(0)
        self.nacionalidad_entry.setCurrentIndex(0)
        self.profesion_ocupacion_entry.clear()
        self.lugar_nacimiento_entry.clear()
        self.religion_entry.clear()
        self.nombre_apellido_emergencia_entry.clear()
        self.telefono_emergencia_entry.clear()
        self.parentesco_entry.clear()
        self.direccion_entry.clear()
        self.temperatura_entry.clear()
        self.pulso_entry.clear()
        self.respiracion_entry.clear()
        self.frecuencia_cardiaca_entry.clear()
        self.tension_arterial_maxima_entry.clear()
        self.tension_arterial_minima_entry.clear()
        self.peso_entry.clear()
        self.talla_entry.clear()
        self.grasa_corporal_entry.clear()
        self.indice_masa_corporal_entry.clear()
        self.motivo_consulta_entry.clear()
        self.enfermedad_actual_entry.clear()
        self.diagnostico_admision_entry.clear()
        self.intervencion_tratamiento_entry.clear()
        self.diagnostico_final_entry.clear()
        self.estado_actual_entry.setCurrentIndex(0)
        self.autopsia_entry.setCurrentIndex(0)
        self.fecha_alta_entry.setDate(QDate.currentDate())
        self.hora_alta_entry.setText(QTime.currentTime().toString("HH:mm:ss"))

    def save_data(self):
        # Obtener los datos del formulario
        if self.estado_actual_entry.currentText() == "Seleccione":
            QMessageBox.warning(self, "Campo Obligatorio", "Por favor seleccione un estado actual.")
            return

        # Recopilar datos del formulario y convertir a mayúsculas
        paciente_data = {
            "cedula": self.cedula_entry.text().upper(),
            "primer_nombre": self.primer_nombre_entry.text().upper(),
            "segundo_nombre": self.segundo_nombre_entry.text().upper(),
            "primer_apellido": self.primer_apellido_entry.text().upper(),
            "segundo_apellido": self.segundo_apellido_entry.text().upper(),
            "fecha_nacimiento": self.fecha_nacimiento_entry.date().toString("yyyy-MM-dd"),
            "telefono": self.telefono_entry.text().upper(),
            "genero": self.genero_entry.currentText() if self.genero_entry.currentText() != "Seleccione" else "",
            "estado_civil": self.estado_civil_entry.currentText() if self.estado_civil_entry.currentText() != "Seleccione" else "",
            "nacionalidad": self.nacionalidad_entry.currentText() if self.nacionalidad_entry.currentText() != "Seleccione" else "",
            "profesion_ocupacion": self.profesion_ocupacion_entry.text().upper(),
            "lugar_nacimiento": self.lugar_nacimiento_entry.text().upper(),
            "religion": self.religion_entry.text().upper(),
            "nombre_apellido_emergencia": self.nombre_apellido_emergencia_entry.text().upper(),
            "telefono_emergencia": self.telefono_emergencia_entry.text().upper(),
            "parentesco": self.parentesco_entry.text().upper(),
            "direccion": self.direccion_entry.text().upper()  # Agregar el campo direccion
        }

        # Verificar campos obligatorios
        campos_obligatorios = ["cedula", "primer_nombre", "primer_apellido", "fecha_nacimiento", "telefono", "genero", "estado_civil", "nacionalidad", "profesion_ocupacion", "lugar_nacimiento", "nombre_apellido_emergencia", "telefono_emergencia", "parentesco", "direccion"]
        campos_faltantes = [campo for campo in campos_obligatorios if not paciente_data[campo]]

        if campos_faltantes:
            QMessageBox.warning(self, "Campos Obligatorios Faltantes", f"Por favor complete los siguientes campos obligatorios: {', '.join(campos_faltantes)}")
            return

        paciente_cedula = paciente_data["cedula"]

        historia_clinica_personal_data = {
            "temperatura": self.temperatura_entry.text(),
            "pulso": self.pulso_entry.text(),
            "respiracion": self.respiracion_entry.text(),
            "frecuencia_cardiaca": self.frecuencia_cardiaca_entry.text(),
            "tension_arterial_maxima": self.tension_arterial_maxima_entry.text(),
            "tension_arterial_minima": self.tension_arterial_minima_entry.text(),
            "peso": self.peso_entry.text(),
            "talla": self.talla_entry.text(),
            "grasa_corporal": self.grasa_corporal_entry.text(),
            "indice_masa_corporal": self.indice_masa_corporal_entry.text(),
            "motivo_consulta": self.motivo_consulta_entry.toPlainText(),
            "enfermedad_actual": self.enfermedad_actual_entry.toPlainText(),
            "diagnostico_admision": self.diagnostico_admision_entry.toPlainText(),
            "intervencion_tratamiento": self.intervencion_tratamiento_entry.toPlainText(),
            "diagnostico_final": self.diagnostico_final_entry.toPlainText(),
            "estado_actual": self.estado_actual_entry.currentText() if self.estado_actual_entry.currentText() != "Seleccione" else "",
            "autopsia_pedida": self.autopsia_entry.currentText() if self.autopsia_entry.currentText() != "Seleccione" else "",
            "fecha_alta": self.fecha_alta_entry.date().toString("yyyy-MM-dd"),
            "hora_alta": self.hora_alta_entry.text()
        }

        db = CreateConnection()
        connection = db.create_connection()
        if connection:
            try:
                cursor = connection.cursor()

                # Verificar si la cédula ya existe
                query_check = "SELECT COUNT(*) FROM pacientes WHERE cedula = %s"
                cursor.execute(query_check, (paciente_cedula,))
                exists = cursor.fetchone()[0]

                if exists:
                    # Actualizar datos del paciente existente
                    query_update = """
                        UPDATE pacientes SET primer_nombre = %s, segundo_nombre = %s, primer_apellido = %s, segundo_apellido = %s, fecha_nacimiento = %s, telefono = %s, genero = %s, estado_civil = %s, nacionalidad = %s, profesion_ocupacion = %s, lugar_nacimiento = %s, religion = %s, nombre_apellido_emergencia = %s, telefono_emergencia = %s, parentesco = %s, direccion = %s
                        WHERE cedula = %s
                    """
                    values_update = (
                        paciente_data["primer_nombre"], paciente_data["segundo_nombre"], paciente_data["primer_apellido"], paciente_data["segundo_apellido"], paciente_data["fecha_nacimiento"], paciente_data["telefono"], paciente_data["genero"], paciente_data["estado_civil"], paciente_data["nacionalidad"], paciente_data["profesion_ocupacion"], paciente_data["lugar_nacimiento"], paciente_data["religion"], paciente_data["nombre_apellido_emergencia"], paciente_data["telefono_emergencia"], paciente_data["parentesco"], paciente_data["direccion"], paciente_cedula
                    )
                    cursor.execute(query_update, values_update)
                else:
                    # Insertar nuevo registro
                    query_insert = """
                        INSERT INTO pacientes (cedula, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, fecha_nacimiento, telefono, genero, estado_civil, nacionalidad, profesion_ocupacion, lugar_nacimiento, religion, nombre_apellido_emergencia, telefono_emergencia, parentesco, direccion)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    values_insert = (
                        paciente_data["cedula"], paciente_data["primer_nombre"], paciente_data["segundo_nombre"], paciente_data["primer_apellido"], paciente_data["segundo_apellido"], paciente_data["fecha_nacimiento"], paciente_data["telefono"], paciente_data["genero"], paciente_data["estado_civil"], paciente_data["nacionalidad"], paciente_data["profesion_ocupacion"], paciente_data["lugar_nacimiento"], paciente_data["religion"], paciente_data["nombre_apellido_emergencia"], paciente_data["telefono_emergencia"], paciente_data["parentesco"], paciente_data["direccion"]
                    )
                    cursor.execute(query_insert, values_insert)

                # Guardar datos en la tabla HistoriaClinicaPersonal
                query_historia_clinica_personal = """
                    INSERT INTO historia_clinica_personal (paciente_cedula, temperatura, pulso, respiracion, frecuencia_cardiaca, tension_arterial_maxima, tension_arterial_minima, peso, talla, grasa_corporal, indice_masa_corporal, motivo_consulta, enfermedad_actual, diagnostico_admision, intervencion_tratamiento, diagnostico_final, estado_actual, autopsia_pedida, fecha_alta, hora_alta)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                values_historia_clinica_personal = (
                    paciente_cedula, historia_clinica_personal_data["temperatura"], historia_clinica_personal_data["pulso"], historia_clinica_personal_data["respiracion"], historia_clinica_personal_data["frecuencia_cardiaca"], historia_clinica_personal_data["tension_arterial_maxima"],
                    historia_clinica_personal_data["tension_arterial_minima"], historia_clinica_personal_data["peso"], historia_clinica_personal_data["talla"], historia_clinica_personal_data["grasa_corporal"], historia_clinica_personal_data["indice_masa_corporal"],
                    historia_clinica_personal_data["motivo_consulta"], historia_clinica_personal_data["enfermedad_actual"], historia_clinica_personal_data["diagnostico_admision"], historia_clinica_personal_data["intervencion_tratamiento"], historia_clinica_personal_data["diagnostico_final"],
                    historia_clinica_personal_data["estado_actual"], historia_clinica_personal_data["autopsia_pedida"], historia_clinica_personal_data["fecha_alta"], historia_clinica_personal_data["hora_alta"]
                )
                cursor.execute(query_historia_clinica_personal, values_historia_clinica_personal)
                connection.commit()
                QMessageBox.information(self, "Guardar", "Datos guardados exitosamente.")
                self.clear_all_fields()  # Limpiar los campos después de guardar
            except Error as e:
                QMessageBox.critical(self, "Error", f"Error al guardar los datos: {e}")
            finally:
                cursor.close()
                connection.close()
        else:
            QMessageBox.critical(self, "Error", "No se pudo establecer la conexión con la base de datos.")