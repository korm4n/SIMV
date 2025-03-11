from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QFormLayout, QLineEdit, QDateEdit, QPushButton, QMessageBox, QHBoxLayout, QTableWidget, QTableWidgetItem
from PySide6.QtGui import QIcon
from PySide6.QtCore import QDate
from servicios import CreateConnection  # Importar la clase para manejar la conexión
from mysql.connector import Error  # Importar la excepción Error de mysql.connector
from utils import update_quantity_available  # Importar la función de utils.py

class Farmacia(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(self.create_farmacia_frame())
        layout.addWidget(self.create_medicamentos_table())
        self.setLayout(layout)
        self.data_loaded = False  # Variable para controlar si los datos fueron cargados desde la base de datos

    def create_farmacia_frame(self):
        frame = QWidget()
        layout = QFormLayout(frame)
        
        # Número de Lote, Nombre del Medicamento, Fecha de Vencimiento y Fecha de Elaboración en la misma fila
        lote_nombre_fecha_layout = QHBoxLayout()
        
        self.numero_lote_entry = QLineEdit()
        self.numero_lote_entry.setMaxLength(100)
        self.numero_lote_entry.setFixedWidth(100)
        lote_nombre_fecha_layout.addWidget(QLabel("Número de Lote:"))
        lote_nombre_fecha_layout.addWidget(self.numero_lote_entry)

        self.nombre_medicamento_entry = QLineEdit()
        self.nombre_medicamento_entry.setMaxLength(100)
        self.nombre_medicamento_entry.setFixedWidth(250)
        lote_nombre_fecha_layout.addWidget(QLabel("Nombre del Medicamento:"))
        lote_nombre_fecha_layout.addWidget(self.nombre_medicamento_entry)

        self.fecha_vencimiento_entry = QDateEdit()
        self.fecha_vencimiento_entry.setFixedWidth(100)
        self.fecha_vencimiento_entry.setCalendarPopup(True)
        lote_nombre_fecha_layout.addWidget(QLabel("Fecha de Vencimiento:"))
        lote_nombre_fecha_layout.addWidget(self.fecha_vencimiento_entry)

        self.fecha_elaboracion_entry = QDateEdit()
        self.fecha_elaboracion_entry.setFixedWidth(100)
        self.fecha_elaboracion_entry.setCalendarPopup(True)
        lote_nombre_fecha_layout.addWidget(QLabel("Fecha de Elaboración:"))
        lote_nombre_fecha_layout.addWidget(self.fecha_elaboracion_entry)

        layout.addRow(lote_nombre_fecha_layout)
         
        recibida_usada_devuelta_layout = QHBoxLayout()
        
        self.cantidad_recibida_entry = QLineEdit("0")
        self.cantidad_recibida_entry.setMaxLength(100)
        self.cantidad_recibida_entry.setFixedWidth(100)
        self.cantidad_recibida_entry.editingFinished.connect(self.update_quantity_available)
        recibida_usada_devuelta_layout.addWidget(QLabel("Cantidad Recibida:"))
        recibida_usada_devuelta_layout.addWidget(self.cantidad_recibida_entry)

        self.cantidad_usada_entry = QLineEdit("0")
        self.cantidad_usada_entry.setMaxLength(100)
        self.cantidad_usada_entry.setFixedWidth(100)
        self.cantidad_usada_entry.setReadOnly(True)  # Hacer que el campo no sea editable
        recibida_usada_devuelta_layout.addWidget(QLabel("Cantidad Usada:"))
        recibida_usada_devuelta_layout.addWidget(self.cantidad_usada_entry)

        self.cantidad_devuelta_entry = QLineEdit("0")
        self.cantidad_devuelta_entry.setMaxLength(100)
        self.cantidad_devuelta_entry.setFixedWidth(100)
        self.cantidad_devuelta_entry.editingFinished.connect(self.update_quantity_available)
        recibida_usada_devuelta_layout.addWidget(QLabel("Cantidad Devuelta:"))
        recibida_usada_devuelta_layout.addWidget(self.cantidad_devuelta_entry)

        self.cantidad_desechada_entry = QLineEdit("0")
        self.cantidad_desechada_entry.setMaxLength(100)
        self.cantidad_desechada_entry.setFixedWidth(100)
        self.cantidad_desechada_entry.editingFinished.connect(self.update_quantity_available)
        recibida_usada_devuelta_layout.addWidget(QLabel("Cantidad Desechada:"))
        recibida_usada_devuelta_layout.addWidget(self.cantidad_desechada_entry)

        self.cantidad_que_queda_entry = QLineEdit("0")
        self.cantidad_que_queda_entry.setMaxLength(100)
        self.cantidad_que_queda_entry.setFixedWidth(100)
        self.cantidad_que_queda_entry.setReadOnly(True)  # Hacer que el campo no sea editable
        recibida_usada_devuelta_layout.addWidget(QLabel("Cantidad Disponible:"))
        recibida_usada_devuelta_layout.addWidget(self.cantidad_que_queda_entry)

        layout.addRow(recibida_usada_devuelta_layout)

        concentracion_farmaceutica_contenido_layout = QHBoxLayout()

        self.concentracion_entry = QLineEdit()
        self.concentracion_entry.setMaxLength(100)
        self.concentracion_entry.setFixedWidth(100)
        concentracion_farmaceutica_contenido_layout.addWidget(QLabel("Concentración:"))
        concentracion_farmaceutica_contenido_layout.addWidget(self.concentracion_entry)

        self.forma_farmaceutica_entry = QLineEdit()
        self.forma_farmaceutica_entry.setMaxLength(100)
        self.forma_farmaceutica_entry.setFixedWidth(100)
        concentracion_farmaceutica_contenido_layout.addWidget(QLabel("Forma Farmacéutica:"))
        concentracion_farmaceutica_contenido_layout.addWidget(self.forma_farmaceutica_entry)

        self.codigo_unidad_contenido_entry = QLineEdit()
        self.codigo_unidad_contenido_entry.setMaxLength(100)
        self.codigo_unidad_contenido_entry.setFixedWidth(100)
        concentracion_farmaceutica_contenido_layout.addWidget(QLabel("Cód de Contenido:"))
        concentracion_farmaceutica_contenido_layout.addWidget(self.codigo_unidad_contenido_entry)

        self.capacidad_unidad_contenido_entry = QLineEdit()
        self.capacidad_unidad_contenido_entry.setMaxLength(100)
        self.capacidad_unidad_contenido_entry.setFixedWidth(100)
        concentracion_farmaceutica_contenido_layout.addWidget(QLabel("Cap de Contenido:"))
        concentracion_farmaceutica_contenido_layout.addWidget(self.capacidad_unidad_contenido_entry)

        self.via_administracion_entry = QLineEdit()
        self.via_administracion_entry.setMaxLength(100)
        self.via_administracion_entry.setFixedWidth(100)
        concentracion_farmaceutica_contenido_layout.addWidget(QLabel("Vía de Administración:"))
        concentracion_farmaceutica_contenido_layout.addWidget(self.via_administracion_entry)

        layout.addRow(concentracion_farmaceutica_contenido_layout)

        # Botones Guardar, Limpiar, Buscar y Campo de Búsqueda en la misma fila
        botones_layout = QHBoxLayout()
        self.save_button_farmacia = QPushButton("Guardar")
        self.save_button_farmacia.setIcon(QIcon("iconos/guardar.png"))  # Agregar ícono al botón "Guardar"
        self.save_button_farmacia.setFixedWidth(100)  # Ajustar la longitud del botón a 100 píxeles
        self.save_button_farmacia.clicked.connect(self.save_farmacia)
        botones_layout.addWidget(self.save_button_farmacia)
        
        self.clear_button_farmacia = QPushButton("Limpiar")
        self.clear_button_farmacia.setIcon(QIcon("iconos/limpiar.png"))  # Agregar ícono al botón "Limpiar Información"
        self.clear_button_farmacia.setFixedWidth(100)  # Ajustar la longitud del botón a 100 píxeles
        self.clear_button_farmacia.clicked.connect(self.clear_farmacia_form)
        botones_layout.addWidget(self.clear_button_farmacia)

        self.search_id_entry = QLineEdit()
        self.search_id_entry.setPlaceholderText("Introduzca ID o Lote")
        self.search_id_entry.setFixedWidth(150)
        botones_layout.addWidget(self.search_id_entry)

        self.search_button_farmacia = QPushButton("Buscar")
        self.search_button_farmacia.setIcon(QIcon("iconos/buscar.png"))  # Agregar ícono al botón "Buscar"
        self.search_button_farmacia.setFixedWidth(100)  # Ajustar la longitud del botón a 100 píxeles
        self.search_button_farmacia.clicked.connect(self.search_farmaco)
        botones_layout.addWidget(self.search_button_farmacia)
        
        layout.addRow(botones_layout)
        
        frame.setLayout(layout)
        return frame

    def create_medicamentos_table(self):
        self.table = QTableWidget()
        self.table.setColumnCount(9)
        self.table.setHorizontalHeaderLabels(["ID", "Lote", "Nombre", "Fecha de Elaboración", "Fecha de Vencimiento", "Cantidad Usada", "Cantidad Disponible", "Concentración", "Vía de Administración"])
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection)
        self.table.cellClicked.connect(self.load_medicamento_data)
        self.table.setStyleSheet("background-color: white;")  # Establecer el fondo blanco

        # Ajustar el ancho de las columnas
        self.table.setColumnWidth(0, 50)  # ID
        self.table.setColumnWidth(1, 100)  # Lote
        self.table.setColumnWidth(2, 150)  # Nombre
        self.table.setColumnWidth(3, 150)  # Fecha de Elaboración
        self.table.setColumnWidth(4, 150)  # Fecha de Vencimiento
        self.table.setColumnWidth(5, 100)  # Cantidad Usada
        self.table.setColumnWidth(6, 150)  # Cantidad Disponible
        self.table.setColumnWidth(7, 150)  # Concentración
        self.table.setColumnWidth(8, 150)  # Vía de Administración

        self.load_medicamentos()
        return self.table

    def load_medicamentos(self):
        db = CreateConnection()
        connection = db.create_connection()
        if connection is None:
            QMessageBox.critical(self, "Error", "No se pudo establecer la conexión con la base de datos")
            return

        try:
            cursor = connection.cursor()
            cursor.execute("SELECT id, numero_lote, nombre_medicamento, fecha_elaboracion, fecha_vencimiento, cantidad_usada, cantidad_disponible, concentracion, via_administracion FROM farmacos")
            rows = cursor.fetchall()
            self.table.setRowCount(len(rows))
            for row_idx, row_data in enumerate(rows):
                for col_idx, col_data in enumerate(row_data):
                    self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
        except Error as e:
            if "No result set to fetch from." not in str(e):
                QMessageBox.critical(self, "Error", f"No se pudieron cargar los datos: {e}")
        finally:
            db.close_connection(connection)

    def load_medicamento_data(self, row, column):
        self.numero_lote_entry.setText(self.table.item(row, 1).text())
        self.nombre_medicamento_entry.setText(self.table.item(row, 2).text())
        self.fecha_elaboracion_entry.setDate(QDate.fromString(self.table.item(row, 3).text(), "yyyy-MM-dd"))
        self.fecha_vencimiento_entry.setDate(QDate.fromString(self.table.item(row, 4).text(), "yyyy-MM-dd"))
        self.cantidad_usada_entry.setText(self.table.item(row, 5).text())
        self.cantidad_que_queda_entry.setText(self.table.item(row, 6).text())
        self.concentracion_entry.setText(self.table.item(row, 7).text())
        self.via_administracion_entry.setText(self.table.item(row, 8).text())

        # Obtener los datos adicionales de la base de datos
        numero_lote = self.table.item(row, 1).text()
        db = CreateConnection()
        connection = db.create_connection()
        if connection is None:
            QMessageBox.critical(self, "Error", "No se pudo establecer la conexión con la base de datos")
            return

        try:
            cursor = connection.cursor()
            query = """
            SELECT forma_farmaceutica, codigo_unidad_contenido, capacidad_unidad_contenido
            FROM farmacos
            WHERE numero_lote = %s
            """
            cursor.execute(query, (numero_lote,))
            result = cursor.fetchone()
            if result:
                self.forma_farmaceutica_entry.setText(result[0] if result[0] else "No aplica")
                self.codigo_unidad_contenido_entry.setText(result[1] if result[1] else "No aplica")
                self.capacidad_unidad_contenido_entry.setText(result[2] if result[2] else "No aplica")
            else:
                self.forma_farmaceutica_entry.setText("No aplica")
                self.codigo_unidad_contenido_entry.setText("No aplica")
                self.capacidad_unidad_contenido_entry.setText("No aplica")
        except Error as e:
            QMessageBox.critical(self, "Error", f"No se pudieron cargar los datos adicionales: {e}")
        finally:
            db.close_connection(connection)

        self.data_loaded = True  # Indicar que los datos fueron cargados desde la base de datos

    def save_farmacia(self):
        numero_lote = self.numero_lote_entry.text()
        nombre_medicamento = self.nombre_medicamento_entry.text()
        fecha_vencimiento = self.fecha_vencimiento_entry.date().toString("yyyy-MM-dd")
        fecha_elaboracion = self.fecha_elaboracion_entry.date().toString("yyyy-MM-dd")
        cantidad_recibida = int(self.cantidad_recibida_entry.text())
        cantidad_usada = int(self.cantidad_usada_entry.text())
        cantidad_devuelta = int(self.cantidad_devuelta_entry.text())
        cantidad_desechada = int(self.cantidad_desechada_entry.text())
        cantidad_disponible = int(self.cantidad_que_queda_entry.text())
        concentracion = self.concentracion_entry.text()
        via_administracion = self.via_administracion_entry.text()
        
        # Campos opcionales
        forma_farmaceutica = self.forma_farmaceutica_entry.text() if self.forma_farmaceutica_entry.text() else "No aplica"
        codigo_unidad_contenido = self.codigo_unidad_contenido_entry.text() if self.codigo_unidad_contenido_entry.text() else "No aplica"
        capacidad_unidad_contenido = self.capacidad_unidad_contenido_entry.text() if self.capacidad_unidad_contenido_entry.text() else "No aplica"

        db = CreateConnection()
        connection = db.create_connection()
        if connection is None:
            QMessageBox.critical(self, "Error", "No se pudo establecer la conexión con la base de datos")
            return

        try:
            cursor = connection.cursor()
            if self.data_loaded:
                # Verificar si el lote ya existe
                query = "SELECT COUNT(*) FROM farmacos WHERE numero_lote = %s"
                cursor.execute(query, (numero_lote,))
                result = cursor.fetchone()
                if result[0] > 0:
                    # Actualizar medicamento existente
                    query = """
                    UPDATE farmacos
                    SET nombre_medicamento = %s, fecha_vencimiento = %s, fecha_elaboracion = %s, cantidad_recibida = %s, cantidad_usada = %s, cantidad_devuelta = %s, cantidad_desechada = %s, cantidad_disponible = %s, concentracion = %s, via_administracion = %s, forma_farmaceutica = %s, codigo_unidad_contenido = %s, capacidad_unidad_contenido = %s
                    WHERE numero_lote = %s
                    """
                    cursor.execute(query, (nombre_medicamento, fecha_vencimiento, fecha_elaboracion, cantidad_recibida, cantidad_usada, cantidad_devuelta, cantidad_desechada, cantidad_disponible, concentracion, via_administracion, forma_farmaceutica, codigo_unidad_contenido, capacidad_unidad_contenido, numero_lote))
                else:
                    # Insertar nuevo medicamento con lote diferente
                    cantidad_disponible = cantidad_recibida  # La cantidad disponible es igual a la cantidad recibida
                    query = """
                    INSERT INTO farmacos (numero_lote, nombre_medicamento, fecha_vencimiento, fecha_elaboracion, cantidad_recibida, cantidad_usada, cantidad_devuelta, cantidad_desechada, cantidad_disponible, concentracion, via_administracion, forma_farmaceutica, codigo_unidad_contenido, capacidad_unidad_contenido)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    cursor.execute(query, (numero_lote, nombre_medicamento, fecha_vencimiento, fecha_elaboracion, cantidad_recibida, cantidad_usada, cantidad_devuelta, cantidad_desechada, cantidad_disponible, concentracion, via_administracion, forma_farmaceutica, codigo_unidad_contenido, capacidad_unidad_contenido))
            else:
                # Insertar nuevo medicamento
                cantidad_disponible = cantidad_recibida  # La cantidad disponible es igual a la cantidad recibida
                query = """
                INSERT INTO farmacos (numero_lote, nombre_medicamento, fecha_vencimiento, fecha_elaboracion, cantidad_recibida, cantidad_usada, cantidad_devuelta, cantidad_desechada, cantidad_disponible, concentracion, via_administracion, forma_farmaceutica, codigo_unidad_contenido, capacidad_unidad_contenido)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query, (numero_lote, nombre_medicamento, fecha_vencimiento, fecha_elaboracion, cantidad_recibida, cantidad_usada, cantidad_devuelta, cantidad_desechada, cantidad_disponible, concentracion, via_administracion, forma_farmaceutica, codigo_unidad_contenido, capacidad_unidad_contenido))
            
            connection.commit()
            QMessageBox.information(self, "Éxito", "Datos guardados exitosamente")
            self.load_medicamentos()  # Recargar la tabla después de guardar
            self.clear_farmacia_form()  # Limpiar los campos después de guardar
        except Error as e:
            QMessageBox.critical(self, "Error", f"No se pudieron guardar los datos: {e}")
        finally:
            db.close_connection(connection)
        self.data_loaded = False  # Resetear la variable después de guardar

    def search_farmaco(self):
        search_value = self.search_id_entry.text()
        if not search_value:
            QMessageBox.warning(self, "Advertencia", "Por favor, introduzca un ID o Lote")
            return

        db = CreateConnection()
        connection = db.create_connection()
        if connection is None:
            QMessageBox.critical(self, "Error", "No se pudo establecer la conexión con la base de datos")
            return

        try:
            cursor = connection.cursor()
            query = """
            SELECT numero_lote, nombre_medicamento, fecha_elaboracion, fecha_vencimiento, cantidad_usada, cantidad_disponible, via_administracion 
            FROM farmacos 
            WHERE id = %s OR numero_lote = %s
            """
            cursor.execute(query, (search_value, search_value))
            result = cursor.fetchone()
            if result:
                self.numero_lote_entry.setText(result[0])
                self.nombre_medicamento_entry.setText(result[1])
                self.fecha_elaboracion_entry.setDate(QDate.fromString(result[2], "yyyy-MM-dd"))
                self.fecha_vencimiento_entry.setDate(QDate.fromString(result[3], "yyyy-MM-dd"))
                self.cantidad_usada_entry.setText(result[4])
                self.cantidad_que_queda_entry.setText(result[5])
                self.via_administracion_entry.setText(result[6])
            else:
                QMessageBox.information(self, "Información", "No se encontró ningún fármaco con el ID o Lote proporcionado")
        except Error as e:
            QMessageBox.critical(self, "Error", f"No se pudo realizar la búsqueda: {e}")
        finally:
            db.close_connection(connection)
        self.data_loaded = True  # Indicar que los datos fueron cargados desde la base de datos

    def update_quantity_available(self):
        try:
            cantidad_recibida = int(self.cantidad_recibida_entry.text())
            cantidad_usada = int(self.cantidad_usada_entry.text())
            cantidad_devuelta = int(self.cantidad_devuelta_entry.text())
            cantidad_desechada = int(self.cantidad_desechada_entry.text())
            cantidad_disponible = int(self.cantidad_que_queda_entry.text())
            
            # Actualizar la cantidad disponible
            cantidad_disponible += cantidad_recibida
            cantidad_disponible -= (cantidad_usada + cantidad_devuelta + cantidad_desechada)
            
            self.cantidad_que_queda_entry.setText(str(cantidad_disponible))
        except ValueError as e:
            QMessageBox.critical(self, "Error", str(e))

    def clear_farmacia_form(self):
        self.numero_lote_entry.clear()
        self.nombre_medicamento_entry.clear()
        self.fecha_vencimiento_entry.setDate(QDate.currentDate())
        self.fecha_elaboracion_entry.setDate(QDate.currentDate())
        self.cantidad_recibida_entry.setText("0")
        self.cantidad_usada_entry.setText("0")
        self.cantidad_devuelta_entry.setText("0")
        self.cantidad_desechada_entry.setText("0")
        self.cantidad_que_queda_entry.setText("0")
        self.concentracion_entry.clear()
        self.forma_farmaceutica_entry.clear()
        self.codigo_unidad_contenido_entry.clear()
        self.capacidad_unidad_contenido_entry.clear()
        self.via_administracion_entry.clear()
        self.search_id_entry.clear()