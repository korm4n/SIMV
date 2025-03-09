from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QDateEdit, QFormLayout, QMessageBox, QListWidget, QCalendarWidget, QToolButton, QHBoxLayout
from PySide6.QtGui import QIcon
from PySide6.QtCore import QDate, QSize, Qt
from servicios import CreateConnection  # Importar la clase CreateConnection
import random

class Inventario(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.load_stylesheet()

    def initUI(self):
        layout = QVBoxLayout()
        
        form_layout = QFormLayout()
        
        self.serial_input = QLineEdit()
        self.serial_input.setFixedWidth(80)
        
        # Crear el botón de ayuda
        self.help_button = QToolButton()
        self.help_button.setIcon(QIcon("c:/Users/kervinfb/OneDrive/Documents/Sistema de Informacion Medica/sistema-informacion-medica/src/iconos/ayuda.png"))
        self.help_button.setToolTip("Si el equipo no posee serial de bienes nacionales puede generar uno con el botón 'Generar Serial'.")
        self.help_button.clicked.connect(self.show_help_message)
        
        self.generate_serial_button = QPushButton("Generar Serial")
        self.generate_serial_button.setFixedWidth(90)
        self.generate_serial_button.clicked.connect(self.generate_serial)
        
        self.nombre_input = QLineEdit()
        self.nombre_input.setFixedWidth(250)
        self.descripcion_input = QLineEdit()
        self.descripcion_input.setFixedWidth(250)
        self.fecha_incorporacion_input = QDateEdit()
        self.fecha_incorporacion_input.setCalendarPopup(True)
        self.fecha_incorporacion_input.setDate(QDate.currentDate())
        self.fecha_incorporacion_input.setCalendarWidget(QCalendarWidget())
        self.fecha_incorporacion_input.setFixedWidth(120)
        self.fecha_desincorporacion_input = QDateEdit()
        self.fecha_desincorporacion_input.setCalendarPopup(True)
        self.fecha_desincorporacion_input.setDate(QDate.currentDate())
        self.fecha_desincorporacion_input.setCalendarWidget(QCalendarWidget())
        self.fecha_desincorporacion_input.setFixedWidth(120)
        
        # Añadir el campo de serial, el botón de ayuda y el botón de generar serial al formulario
        serial_layout = QHBoxLayout()
        serial_layout.addWidget(self.serial_input)
        serial_layout.addWidget(self.help_button)
        serial_layout.addWidget(self.generate_serial_button)
        
        form_layout.addRow("Serial:", serial_layout)
        form_layout.addRow("Nombre:", self.nombre_input)
        form_layout.addRow("Descripción:", self.descripcion_input)
        form_layout.addRow("Fecha de Incorporación:", self.fecha_incorporacion_input)
        form_layout.addRow("Fecha de Desincorporación:", self.fecha_desincorporacion_input)
        
        self.save_button = QPushButton("Guardar")
        self.save_button.setFixedWidth(90)
        self.save_button.setIcon(QIcon("iconos/guardar.png"))
        self.save_button.setIconSize(QSize(16, 16))
        self.save_button.clicked.connect(self.save_data)
        
        self.clear_button = QPushButton("Limpiar")
        self.clear_button.setFixedWidth(90)
        self.clear_button.setIcon(QIcon("iconos/limpiar.png"))
        self.clear_button.setIconSize(QSize(16, 16))
        self.clear_button.clicked.connect(self.clear_fields)
        
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignLeft)  # Alinear los botones a la izquierda
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.clear_button)
        
        self.inventario_list = QListWidget()
        self.load_inventario_list()
        
        layout.addLayout(form_layout)
        layout.addLayout(button_layout)
        layout.addWidget(self.inventario_list)
        
        self.setLayout(layout)
    
    def load_stylesheet(self):
        with open("c:/Users/kervinfb/OneDrive/Documents/Sistema de Informacion Medica/sistema-informacion-medica/src/style.qss", "r") as file:
            self.setStyleSheet(file.read())
    
    def generate_serial(self):
        serial = str(random.randint(10000000, 99999999))
        self.serial_input.setText(serial)
    
    def save_data(self):
        serial = self.serial_input.text()
        nombre = self.nombre_input.text()
        descripcion = self.descripcion_input.text()
        fecha_incorporacion = self.fecha_incorporacion_input.date().toString("yyyy-MM-dd")
        fecha_desincorporacion = self.fecha_desincorporacion_input.date().toString("yyyy-MM-dd") if self.fecha_desincorporacion_input.date() != QDate.currentDate() else None
        
        if not serial or not nombre or not descripcion or not fecha_incorporacion:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos obligatorios.")
            return
        
        try:
            db_connection = CreateConnection()
            connection = db_connection.create_connection()
            if connection:
                cursor = connection.cursor()
                cursor.execute("""
                    INSERT INTO Inventario (serial, nombre, descripcion, fecha_incorporacion, fecha_desincorporacion)
                    VALUES (%s, %s, %s, %s, %s)
                """, (serial, nombre, descripcion, fecha_incorporacion, fecha_desincorporacion))
                connection.commit()
                cursor.close()
                db_connection.close_connection(connection)
                QMessageBox.information(self, "Éxito", "Datos guardados exitosamente.")
                self.load_inventario_list()  # Recargar la lista de inventario
            else:
                QMessageBox.critical(self, "Error", "No se pudo conectar a la base de datos.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo guardar los datos: {e}")
    
    def load_inventario_list(self):
        try:
            db_connection = CreateConnection()
            connection = db_connection.create_connection()
            if connection:
                cursor = connection.cursor()
                cursor.execute("SELECT serial, nombre, descripcion, fecha_incorporacion, fecha_desincorporacion FROM Inventario")
                inventario_items = cursor.fetchall()
                cursor.close()
                db_connection.close_connection(connection)
                
                self.inventario_list.clear()
                for item in inventario_items:
                    serial, nombre, descripcion, fecha_incorporacion, fecha_desincorporacion = item
                    fecha_desincorporacion_text = fecha_desincorporacion if fecha_desincorporacion else "N/A"
                    self.inventario_list.addItem(f"Serial: {serial}, Nombre: {nombre}, Descripción: {descripcion}, Fecha de Incorporación: {fecha_incorporacion}, Fecha de Desincorporación: {fecha_desincorporacion_text}")
            else:
                QMessageBox.critical(self, "Error", "No se pudo conectar a la base de datos.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo cargar la lista de inventario: {e}")

        # Establecer el fondo blanco para la lista de inventario
        self.inventario_list.setStyleSheet("background-color: white;")
    
    def show_help_message(self):
        QMessageBox.information(self, "Ayuda", "Si el equipo no posee serial de bienes nacionales puede generar uno con el botón 'Generar Serial'.")
    
    def clear_fields(self):
        self.serial_input.clear()
        self.nombre_input.clear()
        self.descripcion_input.clear()
        self.fecha_incorporacion_input.setDate(QDate.currentDate())
        self.fecha_desincorporacion_input.setDate(QDate.currentDate())