from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QFormLayout, QHBoxLayout, QLineEdit, QSpacerItem, QSizePolicy, QDateEdit, QComboBox, QPushButton, QMessageBox, QStackedWidget, QTableWidget, QTableWidgetItem
from PySide6.QtGui import QIntValidator, QRegularExpressionValidator, QColor, QIcon
from PySide6.QtCore import QDate, QRegularExpression, Qt
from mysql.connector import Error
from servicios import CreateConnection  # Importar la clase para crear la conexión

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
        layout = QVBoxLayout(frame)
        
        form_layout = QFormLayout()
        
        # Agrupar tipo, cédula, primer nombre, segundo nombre, primer apellido y segundo apellido en una fila
        row_layout1 = QHBoxLayout()
        row_layout1.setContentsMargins(0, 0, 0, 0)  # Ajustar márgenes

        self.tipo_combobox = QComboBox()
        self.tipo_combobox.addItems(["Seleccione", "Medico", "Enfermero"])
        self.tipo_combobox.setFixedWidth(80)
        self.tipo_combobox.setStyleSheet("background-color: white;")
        row_layout1.addWidget(QLabel("Medico/Enfermero:"))
        row_layout1.addSpacerItem(QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout1.addWidget(self.tipo_combobox)

        self.cedula_entry = QLineEdit()
        self.cedula_entry.setValidator(QIntValidator(0, 99999999))
        self.cedula_entry.setMaxLength(20)
        self.cedula_entry.setFixedWidth(80)
        self.cedula_entry.setStyleSheet("background-color: white;")
        self.cedula_entry.editingFinished.connect(self.verificar_cedula)  # Conectar al evento editingFinished
        row_layout1.addWidget(QLabel("Cédula:"))
        row_layout1.addSpacerItem(QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout1.addWidget(self.cedula_entry)

        self.primer_nombre_entry = QLineEdit()
        self.primer_nombre_entry.setValidator(QRegularExpressionValidator(QRegularExpression("[A-Za-z ]{1,255}")))
        self.primer_nombre_entry.setMaxLength(255)
        self.primer_nombre_entry.setFixedWidth(80)
        self.primer_nombre_entry.setStyleSheet("background-color: white;")
        self.primer_nombre_entry.textChanged.connect(self.convert_to_uppercase)
        row_layout1.addWidget(QLabel("Primer Nombre:"))
        row_layout1.addSpacerItem(QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout1.addWidget(self.primer_nombre_entry)

        self.segundo_nombre_entry = QLineEdit()
        self.segundo_nombre_entry.setValidator(QRegularExpressionValidator(QRegularExpression("[A-Za-z ]{1,255}")))
        self.segundo_nombre_entry.setMaxLength(255)
        self.segundo_nombre_entry.setFixedWidth(80)
        self.segundo_nombre_entry.setStyleSheet("background-color: white;")
        self.segundo_nombre_entry.textChanged.connect(self.convert_to_uppercase)
        row_layout1.addWidget(QLabel("Segundo Nombre:"))
        row_layout1.addSpacerItem(QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout1.addWidget(self.segundo_nombre_entry)

        self.primer_apellido_entry = QLineEdit()
        self.primer_apellido_entry.setValidator(QRegularExpressionValidator(QRegularExpression("[A-Za-z ]{1,255}")))
        self.primer_apellido_entry.setMaxLength(255)
        self.primer_apellido_entry.setFixedWidth(80)
        self.primer_apellido_entry.setStyleSheet("background-color: white;")
        self.primer_apellido_entry.textChanged.connect(self.convert_to_uppercase)
        row_layout1.addWidget(QLabel("Primer Apellido:"))
        row_layout1.addSpacerItem(QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout1.addWidget(self.primer_apellido_entry)

        self.segundo_apellido_entry = QLineEdit()
        self.segundo_apellido_entry.setValidator(QRegularExpressionValidator(QRegularExpression("[A-Za-z ]{1,255}")))
        self.segundo_apellido_entry.setMaxLength(255)
        self.segundo_apellido_entry.setFixedWidth(80)
        self.segundo_apellido_entry.setStyleSheet("background-color: white;")
        self.segundo_apellido_entry.textChanged.connect(self.convert_to_uppercase)
        row_layout1.addWidget(QLabel("Segundo Apellido:"))
        row_layout1.addSpacerItem(QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout1.addWidget(self.segundo_apellido_entry)

        form_layout.addRow(row_layout1)

        # Agrupar fecha de nacimiento, edad, teléfono, género y estado civil en una fila
        row_layout2 = QHBoxLayout()
        self.birthdate_entry = QDateEdit()
        self.birthdate_entry.setCalendarPopup(True)
        self.birthdate_entry.setFixedWidth(100)
        self.birthdate_entry.setStyleSheet("""
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
        self.birthdate_entry.dateChanged.connect(self.update_age)
        row_layout2.addWidget(QLabel("Fecha de Nacimiento:"))
        row_layout2.addSpacerItem(QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout2.addWidget(self.birthdate_entry)

        self.age_label = QLabel("")
        self.age_label.setFixedWidth(40)
        row_layout2.addWidget(QLabel("Edad:"))
        row_layout2.addSpacerItem(QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout2.addWidget(self.age_label)

        self.telefono_entry = QLineEdit()
        self.telefono_entry.setInputMask("0000-0000000")  # Máscara de entrada para el formato (0000-0000000)
        self.telefono_entry.setMaxLength(20)
        self.telefono_entry.setFixedWidth(100)
        self.telefono_entry.setStyleSheet("background-color: white;")
        self.telefono_entry.setCursorPosition(0)  # Posicionar el cursor al inicio
        row_layout2.addWidget(QLabel("Teléfono:"))
        row_layout2.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout2.addWidget(self.telefono_entry)

        self.genero_combobox = QComboBox()
        self.genero_combobox.addItems(["Seleccione", "Masculino", "Femenino", "Otros"])
        self.genero_combobox.setFixedWidth(100)
        self.genero_combobox.setStyleSheet("background-color: white;")
        row_layout2.addWidget(QLabel("Género:"))
        row_layout2.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout2.addWidget(self.genero_combobox)

        self.estado_civil_combobox = QComboBox()
        self.estado_civil_combobox.addItems(["Seleccione", "Soltero", "Casado", "Viudo", "Divorciado"])
        self.estado_civil_combobox.setFixedWidth(100)
        self.estado_civil_combobox.setStyleSheet("background-color: white;")
        row_layout2.addWidget(QLabel("Estado Civil:"))
        row_layout2.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout2.addWidget(self.estado_civil_combobox)

        self.numero_registro_medico_entry = QLineEdit()
        self.numero_registro_medico_entry.setValidator(QRegularExpressionValidator(QRegularExpression(".{1,20}")))
        self.numero_registro_medico_entry.setMaxLength(20)
        self.numero_registro_medico_entry.setFixedWidth(100)
        self.numero_registro_medico_entry.setStyleSheet("background-color: white;")
        row_layout2.addWidget(QLabel("Registro MPPPS:"))
        row_layout2.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout2.addWidget(self.numero_registro_medico_entry)

        form_layout.addRow(row_layout2)

        # Agrupar dirección en una fila
        row_layout3 = QHBoxLayout()
        row_layout3.setAlignment(Qt.AlignLeft)  # Alinear a la izquierda
        self.direccion_entry = QLineEdit()
        self.direccion_entry.setValidator(QRegularExpressionValidator(QRegularExpression(".{1,255}")))
        self.direccion_entry.setMaxLength(255)
        self.direccion_entry.setFixedWidth(320)
        self.direccion_entry.setStyleSheet("background-color: white;")
        row_layout3.addWidget(QLabel("Dirección:"))
        row_layout3.addWidget(self.direccion_entry)
        row_layout3.addSpacerItem(QSpacerItem(800, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))  # Añadir espacio

        form_layout.addRow(row_layout3)

        # Añadir el título "Horario de Guardia:"
        form_layout.addRow(QLabel("Horario de Guardia:"))

        # Añadir la tabla de horarios
        row_layout4 = QHBoxLayout()  # Alinear al centro
        self.horario_guardia_table = QTableWidget(7, 24)
        self.horario_guardia_table.setFixedSize(1200, 450) 
        self.horario_guardia_table.setHorizontalHeaderLabels([f"{i}:00" for i in range(24)])
        self.horario_guardia_table.setVerticalHeaderLabels(["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])
        self.horario_guardia_table.horizontalHeader().setDefaultSectionSize(40)
        self.horario_guardia_table.verticalHeader().setDefaultSectionSize(35)
        self.horario_guardia_table.setSelectionMode(QTableWidget.MultiSelection)
        self.horario_guardia_table.setSelectionBehavior(QTableWidget.SelectItems)
        self.horario_guardia_table.setEditTriggers(QTableWidget.NoEditTriggers)  # Deshabilitar edición de celdas
        self.horario_guardia_table.setStyleSheet("""
            QTableWidget {
                background-color: white;
            }
            QTableWidget::item:selected {
                background-color: blue;
            }
        """)

        # Inicializar las celdas de la tabla
        for row in range(self.horario_guardia_table.rowCount()):
            for column in range(self.horario_guardia_table.columnCount()):
                self.horario_guardia_table.setItem(row, column, QTableWidgetItem())

        row_layout4.addWidget(self.horario_guardia_table)

        form_layout.addRow(row_layout4)

        layout.addLayout(form_layout)

        # Crear un layout horizontal para los botones
        button_layout = QHBoxLayout()
        button_layout.addStretch()  # Añadir un espacio flexible para empujar los botones a la derecha

        self.save_button = QPushButton("Guardar")
        self.save_button.setFixedSize(150, 30)  # Establecer tamaño fijo
        self.save_button.setIcon(QIcon("iconos/guardar.png"))  # Establecer icono
        self.save_button.clicked.connect(self.save)
        button_layout.addWidget(self.save_button)
        
        self.clear_button = QPushButton("Limpiar")
        self.clear_button.setFixedSize(150, 30)  # Establecer tamaño fijo
        self.clear_button.setIcon(QIcon("iconos/limpiar.png"))  # Establecer icono
        self.clear_button.clicked.connect(self.clear_form)
        button_layout.addWidget(self.clear_button)

        layout.addLayout(button_layout)
        
        frame.setLayout(layout)
        return frame

    def show_medicos_frame(self):
        self.stacked_widget.setCurrentWidget(self.medicos_frame)
    
    def calculate_age(self, birthdate):
        today = QDate.currentDate().toPython()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age

    def update_age(self):
        birthdate = self.birthdate_entry.date().toPython()
        age = self.calculate_age(birthdate)
        self.age_label.setText(str(age))

    def save(self):
        tipo = self.tipo_combobox.currentText()
        cedula = self.cedula_entry.text()
        primer_nombre = self.primer_nombre_entry.text()
        segundo_nombre = self.segundo_nombre_entry.text()
        primer_apellido = self.primer_apellido_entry.text()
        segundo_apellido = self.segundo_apellido_entry.text()
        birthdate = self.birthdate_entry.date().toPython()
        telefono = self.telefono_entry.text()
        direccion = self.direccion_entry.text()
        genero = self.genero_combobox.currentText()
        estado_civil = self.estado_civil_combobox.currentText()
        numero_registro_medico = self.numero_registro_medico_entry.text()
        horario_guardia = self.get_selected_hours()

        if not cedula:
            QMessageBox.warning(self, "Error", "El campo 'Cédula' es obligatorio.")
            return
        if not primer_nombre:
            QMessageBox.warning(self, "Error", "El campo 'Primer Nombre' es obligatorio.")
            return
        if not primer_apellido:
            QMessageBox.warning(self, "Error", "El campo 'Primer Apellido' es obligatorio.")
            return
        if not birthdate:
            QMessageBox.warning(self, "Error", "El campo 'Fecha de Nacimiento' es obligatorio.")
            return
        if not telefono:
            QMessageBox.warning(self, "Error", "El campo 'Teléfono' es obligatorio.")
            return
        if not direccion:
            QMessageBox.warning(self, "Error", "El campo 'Dirección' es obligatorio.")
            return
        if not numero_registro_medico:
            QMessageBox.warning(self, "Error", "El campo 'Registro MPPPS' es obligatorio.")
            return
        if not horario_guardia:
            QMessageBox.warning(self, "Error", "El campo 'Horario de Guardia' es obligatorio.")
            return

        # Convertir el horario de guardia a formato de texto
        horario_guardia_texto = self.convertir_horario_guardia(horario_guardia)

        # Verificar si la cédula ya existe
        db = CreateConnection()
        connection = db.create_connection()
        if connection is None:
            QMessageBox.critical(self, "Error", "Error al conectar con la base de datos")
            return

        try:
            cursor = connection.cursor()
            query = "SELECT * FROM medicooenfermero WHERE cedula = %s"
            cursor.execute(query, (cedula,))
            result = cursor.fetchone()
            if result:
                # Actualizar los datos existentes
                query = """
                UPDATE medicooenfermero
                SET tipo = %s, primer_nombre = %s, segundo_nombre = %s, primer_apellido = %s, segundo_apellido = %s, fecha_nacimiento = %s, telefono = %s, direccion = %s, genero = %s, estado_civil = %s, numero_registro_medico = %s, horario_guardia = %s
                WHERE cedula = %s
                """
                cursor.execute(query, (tipo, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, birthdate, telefono, direccion, genero, estado_civil, numero_registro_medico, horario_guardia_texto, cedula))
            else:
                # Insertar nuevos datos
                query = """
                INSERT INTO medicooenfermero (tipo, cedula, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, fecha_nacimiento, telefono, direccion, genero, estado_civil, numero_registro_medico, horario_guardia)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query, (tipo, cedula, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, birthdate, telefono, direccion, genero, estado_civil, numero_registro_medico, horario_guardia_texto))
            connection.commit()
            QMessageBox.information(self, "Guardado", "Datos guardados correctamente.")
        except Error as e:
            QMessageBox.critical(self, "Error", f"Error al guardar datos: {e}")
        finally:
            db.close_connection(connection)

        # Limpiar el formulario después de guardar
        self.clear_form()

    def clear_form(self):
        self.tipo_combobox.setCurrentIndex(0)
        self.cedula_entry.clear()
        self.primer_nombre_entry.clear()
        self.segundo_nombre_entry.clear()
        self.primer_apellido_entry.clear()
        self.segundo_apellido_entry.clear()
        self.birthdate_entry.setDate(QDate.currentDate())
        self.age_label.clear()
        self.telefono_entry.clear()
        self.direccion_entry.clear()
        self.genero_combobox.setCurrentIndex(0)
        self.estado_civil_combobox.setCurrentIndex(0)
        self.numero_registro_medico_entry.clear()
        self.horario_guardia_table.clearSelection()

    def convert_to_uppercase(self, text):
        sender = self.sender()
        sender.setText(text.upper())

    def get_selected_hours(self):
        selected_hours = []
        for row in range(self.horario_guardia_table.rowCount()):
            for column in range(self.horario_guardia_table.columnCount()):
                item = self.horario_guardia_table.item(row, column)
                if item and item.isSelected():
                    selected_hours.append((row, column))
        return selected_hours

    def convertir_horario_guardia(self, horario_guardia):
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        horario_dict = {dia: [] for dia in dias_semana}

        for row, column in horario_guardia:
            dia = dias_semana[row]
            hora = column
            horario_dict[dia].append(hora)

        horario_guardia_texto = ""
        for dia, horas in horario_dict.items():
            if horas:
                primera_hora = min(horas)
                ultima_hora = max(horas)
                horario_guardia_texto += f"{dia}: {primera_hora}:00 - {ultima_hora}:00; "

        return horario_guardia_texto.strip("; ")

    def insertar_datos(self, tipo, cedula, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, birthdate, telefono, direccion, genero, estado_civil, numero_registro_medico, horario_guardia):
        db = CreateConnection()
        connection = db.create_connection()
        if connection is None:
            QMessageBox.critical(self, "Error", "Error al conectar con la base de datos")
            return

        try:
            cursor = connection.cursor()
            query = """
            INSERT INTO medicooenfermero (tipo, cedula, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, fecha_nacimiento, telefono, direccion, genero, estado_civil, numero_registro_medico, horario_guardia)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (tipo, cedula, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, birthdate, telefono, direccion, genero, estado_civil, numero_registro_medico, horario_guardia))
            connection.commit()
            print("Datos insertados correctamente")
        except Error as e:
            QMessageBox.critical(self, "Error", f"Error al insertar datos: {e}")
        finally:
            db.close_connection(connection)

    def verificar_cedula(self):
        cedula = self.cedula_entry.text()
        if not cedula:
            return

        db = CreateConnection()
        connection = db.create_connection()
        if connection is None:
            QMessageBox.critical(self, "Error", "Error al conectar con la base de datos")
            return

        try:
            cursor = connection.cursor()
            query = "SELECT * FROM medicooenfermero WHERE cedula = %s"
            cursor.execute(query, (cedula,))
            result = cursor.fetchone()
            if result:
                self.cargar_datos(result)
            else:
                QMessageBox.information(self, "Información", "Cédula no encontrada.")
        except Error as e:
            QMessageBox.critical(self, "Error", f"Error al verificar cédula: {e}")
        finally:
            db.close_connection(connection)

    def cargar_datos(self, datos):
        self.tipo_combobox.setCurrentText(datos[0])
        self.cedula_entry.setText(datos[1])
        self.primer_nombre_entry.setText(datos[2])
        self.segundo_nombre_entry.setText(datos[3])
        self.primer_apellido_entry.setText(datos[4])
        self.segundo_apellido_entry.setText(datos[5])
        self.birthdate_entry.setDate(QDate.fromString(datos[6], "yyyy-MM-dd"))
        self.telefono_entry.setText(datos[7])
        self.direccion_entry.setText(datos[8])
        self.genero_combobox.setCurrentText(datos[9])
        self.estado_civil_combobox.setCurrentText(datos[10])
        self.numero_registro_medico_entry.setText(datos[11])
        self.cargar_horario_guardia(datos[12])

    def cargar_horario_guardia(self, horario_guardia_texto):
        self.horario_guardia_table.clearSelection()
        if not horario_guardia_texto:
            return

        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        horarios = horario_guardia_texto.split("; ")
        for horario in horarios:
            dia, horas = horario.split(": ")
            inicio, fin = horas.split(" - ")
            inicio_hora = int(inicio.split(":")[0])
            fin_hora = int(fin.split(":")[0])
            row = dias_semana.index(dia)
            for column in range(inicio_hora, fin_hora + 1):
                item = self.horario_guardia_table.item(row, column)
                if item:
                    item.setSelected(True)