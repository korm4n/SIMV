from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QListWidget, QListWidgetItem, QTableWidget, QTableWidgetItem, QLineEdit, QPushButton, QHeaderView
from PySide6.QtCore import Qt, QEvent
from servicios import CreateConnection
from datetime import datetime
from PySide6.QtGui import QPixmap, QPainter, QColor  # Importar QPixmap, QPainter y QColor para manejar imágenes
import os

class Inicio(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()  # Asegúrate de que este método se esté llamando
        self.installEventFilter(self)  # Instalar el filtro de eventos

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(self.create_inicio_frame())
        self.setLayout(layout)

    def eventFilter(self, source, event):
        if event.type() == QEvent.Show:
            self.update_medicos_list()  # Actualizar la lista al mostrar el widget
        return super().eventFilter(source, event)

    def get_medicos_de_guardia(self):
        # Crear una conexión a la base de datos
        db = CreateConnection()
        connection = db.create_connection()

        if connection is None:
            print("No se pudo establecer la conexión con la base de datos.")
            return [], "Ambulatorio Rural Tipo III Carmen Isidra Bracho"  # Nombre por defecto

        # Consultar los médicos de guardia
        cursor = connection.cursor()
        cursor.execute("SELECT primer_nombre, primer_apellido, genero, especialidad, horario_guardia, tipo FROM medicooenfermero")
        medicos = cursor.fetchall()

        # Consultar el nombre del hospital
        cursor.execute("SELECT nombre FROM hospital LIMIT 1")
        hospital = cursor.fetchone()
        hospital_name = hospital[0] if hospital else "Ambulatorio Rural Tipo III Carmen Isidra Bracho"  # Nombre por defecto

        connection.close()

        # Obtener el día actual
        dia_actual = datetime.now().strftime("%A").lower()
        dias_semana = {
            "monday": "Lunes",
            "tuesday": "Martes",
            "wednesday": "Miércoles",
            "thursday": "Jueves",
            "friday": "Viernes",
            "saturday": "Sábado",
            "sunday": "Domingo"
        }
        dia_actual1 = dias_semana[dia_actual]

        # Obtener todos los médicos de guardia del día actual
        medicos_de_guardia = []
        for medico in medicos:
            primer_nombre, primer_apellido, genero, especialidad, horario_guardia, tipo = medico
            horarios = horario_guardia.split(';')
            for horario in horarios:
                dia, horas = horario.split(':', 1)  # Limitar el número de divisiones a 1
                if dia.strip() == dia_actual1:
                    medicos_de_guardia.append((primer_nombre, primer_apellido, genero, especialidad, horas.strip(), tipo))

        return medicos_de_guardia, hospital_name

    def create_inicio_frame(self):
        frame = QWidget()
        layout = QVBoxLayout(frame)
        layout.setAlignment(Qt.AlignTop)

        # Obtener el nombre del hospital
        _, hospital_name = self.get_medicos_de_guardia()

        # Hospital name label
        hospital_name_layout = QHBoxLayout()
        hospital_name_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Añadir la imagen antes del nombre del hospital
        self.hospital_image_label_inicio = QLabel()
        pixmap_inicio = QPixmap("iconos/baston de esculapio.png")  # Ruta de la imagen
        pixmap_inicio = pixmap_inicio.scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation)  # Redimensionar la imagen
        self.hospital_image_label_inicio.setPixmap(pixmap_inicio)
        self.hospital_image_label_inicio.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # Bloquear tamaño
        hospital_name_layout.addWidget(self.hospital_image_label_inicio)

        self.hospital_name_label_inicio = QLabel(hospital_name)
        self.hospital_name_label_inicio.setStyleSheet("font-size: 40px; color: Blue;")
        self.hospital_name_label_inicio.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # Bloquear tamaño
        hospital_name_layout.addWidget(self.hospital_name_label_inicio)

        # Añadir la imagen después del nombre del hospital
        self.hospital_image_label = QLabel()
        pixmap = QPixmap("iconos/baston de esculapio.png")  # Ruta de la imagen
        pixmap = pixmap.scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation)  # Redimensionar la imagen
        self.hospital_image_label.setPixmap(pixmap)
        self.hospital_image_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # Bloquear tamaño
        hospital_name_layout.addWidget(self.hospital_image_label)

        hospital_name_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))
        layout.addLayout(hospital_name_layout)

        # Añadir el cuadro con la imagen debajo del nombre del hospital como marca de agua
        self.imagen_label = QLabel()
        image_path = os.path.join(os.path.dirname(__file__), '..', '..', 'imagen', 'hospital1.png')
        if os.path.exists(image_path):
            pixmap_imagen = QPixmap(image_path)  # Ruta de la imagen desde configuración
            pixmap_imagen = pixmap_imagen.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)  # Redimensionar la imagen

            # Crear una imagen semi-transparente
            transparent_pixmap = QPixmap(pixmap_imagen.size())
            transparent_pixmap.fill(Qt.transparent)
            painter = QPainter(transparent_pixmap)
            painter.setOpacity(0.5)  # Ajustar la transparencia aquí (0.5 es 50%)
            painter.drawPixmap(0, 0, pixmap_imagen)
            painter.end()

            self.imagen_label.setPixmap(transparent_pixmap)
        self.imagen_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.imagen_label)

        # Layout para médicos y enfermeras de guardia
        guardia_layout = QVBoxLayout()
        guardia_layout.addStretch()

        # Añadir la imagen "estrella de la vida" encima de los médicos de guardia
        self.estrella_vida_label = QLabel()
        pixmap_estrella = QPixmap("iconos/estrella de la vida.png")  # Ruta de la imagen
        pixmap_estrella = pixmap_estrella.scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation)  # Redimensionar la imagen

        # Crear un QHBoxLayout para controlar la disposición de la imagen y el espacio
        estrella_layout = QHBoxLayout()
        estrella_layout.addSpacerItem(QSpacerItem(90, 10, QSizePolicy.Fixed, QSizePolicy.Minimum))
        estrella_layout.addWidget(self.estrella_vida_label, alignment=Qt.AlignLeft | Qt.AlignVCenter)

        self.estrella_vida_label.setPixmap(pixmap_estrella)
        guardia_layout.addLayout(estrella_layout)

        guardia_layout.addWidget(QLabel("Médicos y Enfermeras de Guardia:"))

        # Crear un QHBoxLayout para colocar el QListWidget en la parte inferior izquierda
        bottom_layout = QHBoxLayout()
        bottom_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)  # Alinear a la izquierda y al centro verticalmente
        bottom_layout.addWidget(self.create_medicos_list_widget())
        bottom_layout.addSpacerItem(QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Expanding))

        # Crear un layout para la lista de pacientes y los campos de entrada
        pacientes_layout = QHBoxLayout()
        pacientes_layout.setAlignment(Qt.AlignBottom | Qt.AlignRight)

        # Campos de entrada y botón "Siguiente"
        input_layout = QVBoxLayout()
        self.cedula_input = QLineEdit()
        self.cedula_input.setPlaceholderText("Cédula")
        self.cedula_input.setFixedWidth(100)
        self.cedula_input.editingFinished.connect(self.verificar_cedula)  # Conectar el evento de edición terminada
        input_layout.addWidget(self.cedula_input)

        self.primer_nombre_input = QLineEdit()
        self.primer_nombre_input.setPlaceholderText("Primer Nombre")
        self.primer_nombre_input.setFixedWidth(100)
        self.primer_nombre_input.textChanged.connect(self.convertir_a_mayusculas)
        input_layout.addWidget(self.primer_nombre_input)

        self.primer_apellido_input = QLineEdit()
        self.primer_apellido_input.setPlaceholderText("Primer Apellido")
        self.primer_apellido_input.setFixedWidth(100)
        self.primer_apellido_input.textChanged.connect(self.convertir_a_mayusculas)
        self.primer_apellido_input.editingFinished.connect(self.agregar_paciente)  # Conectar el evento de edición terminada
        input_layout.addWidget(self.primer_apellido_input)

        self.siguiente_button = QPushButton("Siguiente")
        self.siguiente_button.setFixedWidth(100)
        self.siguiente_button.clicked.connect(self.siguiente_paciente)  # Conectar el evento del botón
        input_layout.addWidget(self.siguiente_button)

        pacientes_layout.addLayout(input_layout)

        # Tabla de lista de pacientes
        self.pacientes_table = QTableWidget()
        self.pacientes_table.setColumnCount(3)
        self.pacientes_table.setHorizontalHeaderLabels(["Cédula", "Primer Nombre", "Primer Apellido"])
        
        # Ajustar el tamaño de las columnas al contenido
        self.pacientes_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.pacientes_table.horizontalHeader().setStretchLastSection(True)
        
        # Configurar la política de tamaño de la tabla
        self.pacientes_table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.pacientes_table.setFixedSize(300, 700)  # Establecer tamaño fijo para la tabla de pacientes
        
        pacientes_layout.addWidget(self.pacientes_table)

        bottom_layout.addLayout(pacientes_layout)
        guardia_layout.addLayout(bottom_layout)

        layout.addLayout(guardia_layout)

        # Añadir el texto de Voltaire en la parte inferior central
        quote_label = QLabel()
        quote_label.setText("No hay hombre más digno de estimación que el médico que, habiendo estudiado la naturaleza desde su juventud, conoce las propiedades del cuerpo humano, las enfermedades que le atacan y los remedios que pueden beneficiarle y que ejerce su arte. - Voltaire")
        quote_label.setAlignment(Qt.AlignCenter)
        quote_label.setWordWrap(True)
        quote_label.setStyleSheet("font-size: 12px; color: black;")
        layout.addWidget(quote_label)

        return frame

    def create_medicos_list_widget(self):
        # Crear QListWidget para mostrar los médicos de guardia
        self.medicos_list_widget = QListWidget()
        return self.medicos_list_widget

    def update_medicos_list(self):
        # Limpiar la lista existente
        self.medicos_list_widget.clear()

        # Obtener y mostrar los médicos de guardia
        medicos, hospital_name = self.get_medicos_de_guardia()
        #print(f"Medicos de guardia: {medicos}")  # Mensaje de depuración

        for medico in medicos:
            primer_nombre, primer_apellido, genero, especialidad, horario_dia, tipo = medico
            if tipo.lower() == "medico":
                titulo = "Dr." if genero.lower() == "masculino" else "Dra."
            else:
                titulo = "ENFERMERO." if genero.lower() == "masculino" else "ENFERMERA."  # Asegurarse de que titulo siempre tenga un valor
            
            # Verificar si la especialidad es None o null
            especialidad_text = especialidad if especialidad else ""
            item_text = f"{titulo} {primer_nombre} {primer_apellido} - {especialidad_text} ({horario_dia})"
            list_item = QListWidgetItem(item_text)
            self.medicos_list_widget.addItem(list_item)
            #print(f"Agregado a la lista: {item_text}")  # Mensaje de depuración

    def verificar_cedula(self):
        cedula = self.cedula_input.text()
        if not cedula:
            return

        # Crear una conexión a la base de datos
        db = CreateConnection()
        connection = db.create_connection()

        if connection is None:
            print("No se pudo establecer la conexión con la base de datos.")
            return

        cursor = connection.cursor()
        cursor.execute("SELECT primer_nombre, primer_apellido FROM pacientes WHERE cedula = %s", (cedula,))
        paciente = cursor.fetchone()
        connection.close()

        if paciente:
            primer_nombre, primer_apellido = paciente
            self.primer_nombre_input.setText(primer_nombre)
            self.primer_apellido_input.setText(primer_apellido)

    def agregar_paciente(self):
        cedula = self.cedula_input.text()
        primer_nombre = self.primer_nombre_input.text()
        primer_apellido = self.primer_apellido_input.text()

        if not cedula or not primer_nombre or not primer_apellido:
            return

        row_position = self.pacientes_table.rowCount()
        self.pacientes_table.insertRow(row_position)
        self.pacientes_table.setItem(row_position, 0, QTableWidgetItem(cedula))
        self.pacientes_table.setItem(row_position, 1, QTableWidgetItem(primer_nombre))
        self.pacientes_table.setItem(row_position, 2, QTableWidgetItem(primer_apellido))

        # Ordenar la tabla en orden descendente por cédula
        self.pacientes_table.sortItems(0, Qt.DescendingOrder)

        # Limpiar los campos de entrada
        self.cedula_input.clear()
        self.primer_nombre_input.clear()
        self.primer_apellido_input.clear()

    def siguiente_paciente(self):
        if self.pacientes_table.rowCount() > 0:
            self.pacientes_table.removeRow(0)

    def convertir_a_mayusculas(self, text):
        sender = self.sender()
        sender.blockSignals(True)
        sender.setText(text.upper())
        sender.blockSignals(False)