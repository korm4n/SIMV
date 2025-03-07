from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QFormLayout, QLineEdit, QDateEdit, QPushButton, QMessageBox
from PySide6.QtCore import QDate

class Farmacia(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(self.create_farmacia_frame())
        self.setLayout(layout)

    def create_farmacia_frame(self):
        frame = QWidget()
        layout = QFormLayout(frame)
        
        self.nombre_farmaco_entry = QLineEdit()
        self.nombre_farmaco_entry.setStyleSheet("background-color: white;")
        self.nombre_farmaco_entry.setMaxLength(200)  # Limitar a 200 caracteres
        self.nombre_farmaco_entry.setFixedWidth(400)  # Ajustar tamaño del campo
        layout.addRow(QLabel("Nombre del Fármaco:"), self.nombre_farmaco_entry)

        self.fecha_elaboracion_entry = QDateEdit()
        self.fecha_elaboracion_entry.setStyleSheet("background-color: white;")
        layout.addRow(QLabel("Fecha de Elaboración:"), self.fecha_elaboracion_entry)
        self.fecha_elaboracion_entry.setCalendarPopup(True)

        self.lote_entry = QLineEdit()
        self.lote_entry.setStyleSheet("background-color: white;")
        self.lote_entry.setMaxLength(200)  # Limitar a 200 caracteres
        self.lote_entry.setFixedWidth(400)  # Ajustar tamaño del campo
        layout.addRow(QLabel("Lote del Medicamento:"), self.lote_entry)

        self.fecha_caducidad_entry = QDateEdit()
        self.fecha_caducidad_entry.setStyleSheet("background-color: white;")
        layout.addRow(QLabel("Fecha de Caducidad:"), self.fecha_caducidad_entry)
        self.fecha_caducidad_entry.setCalendarPopup(True)

        self.cantidades_recibidas_entry = QLineEdit()
        self.cantidades_recibidas_entry.setStyleSheet("background-color: white;")
        self.cantidades_recibidas_entry.setMaxLength(200)  # Limitar a 200 caracteres
        self.cantidades_recibidas_entry.setFixedWidth(400)  # Ajustar tamaño del campo
        layout.addRow(QLabel("Cantidades Recibidas:"), self.cantidades_recibidas_entry)

        self.cantidades_disponibles_entry = QLineEdit()
        self.cantidades_disponibles_entry.setStyleSheet("background-color: white;")
        self.cantidades_disponibles_entry.setMaxLength(200)  # Limitar a 200 caracteres
        self.cantidades_disponibles_entry.setFixedWidth(400)  # Ajustar tamaño del campo
        layout.addRow(QLabel("Cantidades Disponibles:"), self.cantidades_disponibles_entry)

        self.save_button_farmacia = QPushButton("Guardar")
        self.save_button_farmacia.setFixedSize(150, 30)  # Establecer tamaño fijo
        self.save_button_farmacia.clicked.connect(self.save_farmacia)
        layout.addRow(self.save_button_farmacia)
        
        self.clear_button_farmacia = QPushButton("Limpiar Información")
        self.clear_button_farmacia.setFixedSize(150, 30)  # Establecer tamaño fijo
        self.clear_button_farmacia.clicked.connect(self.clear_farmacia_form)
        layout.addRow(self.clear_button_farmacia)
        
        frame.setLayout(layout)
        return frame

    def save_farmacia(self):
        nombre_farmaco = self.nombre_farmaco_entry.text()
        fecha_elaboracion = self.fecha_elaboracion_entry.date().toPython()
        lote = self.lote_entry.text()
        fecha_caducidad = self.fecha_caducidad_entry.date().toPython()
        cantidades_recibidas = self.cantidades_recibidas_entry.text()
        cantidades_disponibles = self.cantidades_disponibles_entry.text()

        if not nombre_farmaco or not lote or not cantidades_recibidas or not cantidades_disponibles:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        # Aquí puedes agregar la lógica para guardar los datos en la base de datos
        QMessageBox.information(self, "Guardado", "Datos del fármaco guardados correctamente.")

    def clear_farmacia_form(self):
        self.nombre_farmaco_entry.clear()
        self.fecha_elaboracion_entry.setDate(QDate.currentDate())
        self.lote_entry.clear()
        self.fecha_caducidad_entry.setDate(QDate.currentDate())
        self.cantidades_recibidas_entry.clear()
        self.cantidades_disponibles_entry.clear()