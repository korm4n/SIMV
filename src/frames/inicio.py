from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QListWidget, QListWidgetItem
from PySide6.QtCore import Qt, QEvent
from servicios import CreateConnection
from datetime import datetime

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
            return []

        # Consultar los médicos de guardia
        cursor = connection.cursor()
        cursor.execute("SELECT primer_nombre, primer_apellido, genero, especialidad, horario_guardia, tipo FROM medicooenfermero")
        medicos = cursor.fetchall()
        #print(f"Medicos obtenidos de la base de datos: {medicos}")  # Mensaje de depuración

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
        #print(f"Día actual: {dia_actual1}")  # Mensaje de depuración

        # Obtener todos los médicos de guardia del día actual
        medicos_de_guardia = []
        for medico in medicos:
            primer_nombre, primer_apellido, genero, especialidad, horario_guardia, tipo = medico
            horarios = horario_guardia.split(';')
            for horario in horarios:
                dia, horas = horario.split(':', 1)  # Limitar el número de divisiones a 1
                #print(f"Comparando día: {dia.strip()} con día actual: {dia_actual1}")  # Mensaje de depuración
                if dia.strip() == dia_actual1:
                    medicos_de_guardia.append((primer_nombre, primer_apellido, genero, especialidad, horas.strip(), tipo))
        #print(f"Medicos de guardia del día actual: {medicos_de_guardia}")  # Mensaje de depuración

        return medicos_de_guardia

    def create_inicio_frame(self):
        frame = QWidget()
        layout = QVBoxLayout(frame)
        layout.setAlignment(Qt.AlignTop)

        # Hospital name label
        hospital_name_layout = QHBoxLayout()
        hospital_name_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.hospital_name_label_inicio = QLabel("Ambulatorio Rural Tipo III Carmen Isidra Bracho")
        self.hospital_name_label_inicio.setStyleSheet("font-size: 40px; color: Blue;")
        hospital_name_layout.addWidget(self.hospital_name_label_inicio)
        hospital_name_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))
        layout.addLayout(hospital_name_layout)

        layout.addWidget(QLabel("Médicos y Enfermeras de Guardia:"))

        # Crear un QHBoxLayout para colocar el QListWidget en la parte inferior izquierda
        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(self.create_medicos_list_widget())
        bottom_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Expanding))
        layout.addLayout(bottom_layout)

        return frame

    def create_medicos_list_widget(self):
        # Crear QListWidget para mostrar los médicos de guardia
        self.medicos_list_widget = QListWidget()
        return self.medicos_list_widget

    def update_medicos_list(self):
        # Limpiar la lista existente
        self.medicos_list_widget.clear()

        # Obtener y mostrar los médicos de guardia
        medicos = self.get_medicos_de_guardia()
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