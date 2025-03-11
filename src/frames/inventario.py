from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QDateEdit, QFormLayout, QHBoxLayout, QMessageBox, QToolButton, QPushButton, QTableWidget, QTableWidgetItem
from PySide6.QtGui import QIcon
from PySide6.QtCore import QDate, Qt
from servicios import CreateConnection
from mysql.connector import Error
import random

class Inventario(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.cargar_datos()

    def initUI(self):
        layout = QVBoxLayout()

        form_layout = QFormLayout()

        self.serial_input = QLineEdit()
        self.serial_input.setFixedWidth(80)
        
        # Crear el botón de ayuda
        self.help_button = QToolButton()
        self.help_button.setIcon(QIcon("iconos/ayuda.png"))
        self.help_button.setToolTip("Si el equipo no posee serial de bienes nacionales puede generar uno con el botón 'Generar Serial'.")

        # Crear el botón de generar serial
        self.generar_serial_button = QPushButton("Generar Serial")
        self.generar_serial_button.setFixedWidth(100)
        self.generar_serial_button.clicked.connect(self.generar_serial)

        serial_layout = QHBoxLayout()
        serial_layout.addWidget(self.serial_input)
        serial_layout.addWidget(self.help_button)
        serial_layout.addWidget(self.generar_serial_button)

        self.nombre_input = QLineEdit()
        self.nombre_input.setFixedWidth(250)
        self.descripcion_input = QLineEdit()
        self.descripcion_input.setFixedWidth(250)  
        self.fecha_incorporacion_input = QDateEdit(QDate.currentDate())
        self.fecha_incorporacion_input.setFixedWidth(100)
        self.fecha_incorporacion_input.setCalendarPopup(True)
        self.fecha_desincorporacion_input = QDateEdit(QDate.currentDate())
        self.fecha_desincorporacion_input.setFixedWidth(100)
        self.fecha_desincorporacion_input.setCalendarPopup(True)
        self.motivo_desincorporacion_input = QLineEdit()
        self.motivo_desincorporacion_input.setFixedWidth(250)

        form_layout.addRow("Serial:", serial_layout)
        form_layout.addRow("Nombre:", self.nombre_input)
        form_layout.addRow("Descripción:", self.descripcion_input)
        form_layout.addRow("Fecha de Incorporación:", self.fecha_incorporacion_input)
        form_layout.addRow("Fecha de Desincorporación:", self.fecha_desincorporacion_input)
        form_layout.addRow("Motivo de Desincorporación:", self.motivo_desincorporacion_input)

        button_layout = QHBoxLayout()

        guardar_button = QPushButton("Guardar")
        guardar_button.setFixedWidth(100)
        guardar_button.setIcon(QIcon("iconos/guardar.png"))
        guardar_button.clicked.connect(self.guardar_inventario)

        limpiar_button = QPushButton("Limpiar")
        limpiar_button.setFixedWidth(100)
        limpiar_button.setIcon(QIcon("iconos/limpiar.png"))
        limpiar_button.clicked.connect(self.limpiar_formulario)

        button_layout.addWidget(guardar_button)
        button_layout.addWidget(limpiar_button)

        form_layout.addRow(button_layout)

        layout.addLayout(form_layout)

        # Crear el cuadro de lista (QTableWidget)
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(6)
        self.table_widget.setHorizontalHeaderLabels(["Serial", "Nombre", "Descripción", "Fecha de Incorporación", "Fecha de Desincorporación", "Motivo de Desincorporación"])
        self.table_widget.setColumnWidth(0, 80)  # Serial
        self.table_widget.setColumnWidth(1, 120)  # Nombre
        self.table_widget.setColumnWidth(2, 250)  # Descripción
        self.table_widget.setColumnWidth(3, 150)  # Fecha de Incorporación
        self.table_widget.setColumnWidth(4, 150)  # Fecha de Desincorporación
        self.table_widget.setColumnWidth(5, 200)  # Motivo de Desincorporación

        # Establecer el fondo blanco
        self.table_widget.setStyleSheet("background-color: white;")

        # Conectar la señal cellClicked al método cargar_datos_formulario
        self.table_widget.cellClicked.connect(self.cargar_datos_formulario)

        layout.addWidget(self.table_widget)

        self.setLayout(layout)
        
    def generar_serial(self):
        serial = str(random.randint(10000000, 99999999))
        self.serial_input.setText(serial)

    def guardar_inventario(self):
        serial = self.serial_input.text()
        nombre = self.nombre_input.text()
        descripcion = self.descripcion_input.text()
        fecha_incorporacion = self.fecha_incorporacion_input.date().toString("yyyy-MM-dd")
        fecha_desincorporacion = self.fecha_desincorporacion_input.date().toString("yyyy-MM-dd") if self.fecha_desincorporacion_input.date() != QDate.currentDate() else None
        motivo_desincorporacion = self.motivo_desincorporacion_input.text() if self.motivo_desincorporacion_input.text() else None

        if not serial or not nombre or not descripcion or not fecha_incorporacion:
            QMessageBox.warning(self, "Advertencia", "Por favor, complete todos los campos obligatorios.")
            return

        db = CreateConnection()
        conexion = db.create_connection()

        if conexion is None:
            QMessageBox.critical(self, "Error", "No se pudo conectar a la base de datos.")
            return

        cursor = conexion.cursor()

        try:
            # Verificar si el serial ya existe en la base de datos
            cursor.execute("SELECT COUNT(*) FROM inventario WHERE serial = %s", (serial,))
            result = cursor.fetchone()

            if result[0] > 0:
                # Si el serial existe, actualizar los datos
                cursor.execute("""
                    UPDATE inventario
                    SET nombre = %s, descripcion = %s, fecha_incorporacion = %s, fecha_desincorporacion = %s, motivo_desincorporacion = %s
                    WHERE serial = %s
                """, (nombre, descripcion, fecha_incorporacion, fecha_desincorporacion, motivo_desincorporacion, serial))
                conexion.commit()
                QMessageBox.information(self, "Éxito", "Datos actualizados exitosamente.")
            else:
                # Si el serial no existe, insertar un nuevo registro
                cursor.execute("""
                    INSERT INTO inventario (serial, nombre, descripcion, fecha_incorporacion, fecha_desincorporacion, motivo_desincorporacion)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (serial, nombre, descripcion, fecha_incorporacion, fecha_desincorporacion, motivo_desincorporacion))
                conexion.commit()
                QMessageBox.information(self, "Éxito", "Datos guardados exitosamente.")
                
        except Error as e:
            QMessageBox.critical(self, "Error", f"Error al guardar los datos: {e}")
        finally:
            cursor.close()
            db.close_connection(conexion)

        # Recargar los datos de la tabla después de guardar
        self.cargar_datos()

    def limpiar_formulario(self):
        self.serial_input.clear()
        self.nombre_input.clear()
        self.descripcion_input.clear()
        self.fecha_incorporacion_input.setDate(QDate.currentDate())
        self.fecha_desincorporacion_input.setDate(QDate.currentDate())
        self.motivo_desincorporacion_input.clear()

    def cargar_datos(self):
        db = CreateConnection()
        connection = db.create_connection()
        if connection is None:
            QMessageBox.critical(self, "Error", "No se pudo establecer la conexión con la base de datos")
            return

        try:
            cursor = connection.cursor()
            cursor.execute("SELECT serial, nombre, descripcion, fecha_incorporacion, fecha_desincorporacion, motivo_desincorporacion FROM inventario")
            rows = cursor.fetchall()
            self.table_widget.setRowCount(len(rows))
            for row_idx, row_data in enumerate(rows):
                for col_idx, col_data in enumerate(row_data):
                    self.table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
        except Error as e:
            if "No result set to fetch from." not in str(e):
                QMessageBox.critical(self, "Error", f"No se pudieron cargar los datos: {e}")
        finally:
            db.close_connection(connection)

    def cargar_datos_formulario(self, row, column):
        # Obtener los datos de la fila seleccionada
        serial = self.table_widget.item(row, 0).text()
        nombre = self.table_widget.item(row, 1).text()
        descripcion = self.table_widget.item(row, 2).text()
        fecha_incorporacion = self.table_widget.item(row, 3).text()

        # Cargar los datos en los campos correspondientes
        self.serial_input.setText(serial)
        self.nombre_input.setText(nombre)
        self.descripcion_input.setText(descripcion)
        self.fecha_incorporacion_input.setDate(QDate.fromString(fecha_incorporacion, "yyyy-MM-dd"))