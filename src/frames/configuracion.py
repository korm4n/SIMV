from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QMessageBox, QFileDialog, QColorDialog, QHBoxLayout, QFrame, QGridLayout, QSpacerItem, QSizePolicy, QComboBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import os
import re
from servicios import CreateConnection
import time
from frames.db_config import BACKGROUND_COLOR, TITLE_COLOR, LINEEDIT_BACKGROUND_COLOR, LINEEDIT_TEXT_COLOR, TEXT_COLOR
from frames.db_config import CLEAR_BUTTON_DISABLED
import frames.db_config as db_config

class Configuracion(QWidget):
    def __init__(self):
        super().__init__()
        self.frames = {}  # Inicializar el diccionario de frames
        self.config_frame = self.create_configuracion_frame()  # Crear el frame de configuración
        layout = QVBoxLayout()
        layout.addWidget(self.config_frame)
        self.setLayout(layout)
        
        # Definir hospital_name_label_inicio
        self.hospital_name_label_inicio = QLabel()
        
        self.initUI()
        self.load_configuracion()

    def create_configuracion_frame(self):
        frame = QWidget()
        main_layout = QVBoxLayout(frame)
        
        # Frame superior con la configuración existente
        config_layout = QFormLayout()
        
        self.hospital_id_entry = QLineEdit()
        self.hospital_id_entry.setStyleSheet("background-color: white; color: black;")
        self.hospital_id_entry.setMaxLength(10)
        self.hospital_id_entry.setFixedWidth(50)
        self.hospital_id_entry.setReadOnly(True)  # Hacer que el campo no sea editable
        config_layout.addRow(QLabel("ID del Hospital:"), self.hospital_id_entry)
        
        self.hospital_name_entry = QLineEdit()
        self.hospital_name_entry.setStyleSheet("background-color: white; color: black;")
        self.hospital_name_entry.setMaxLength(255)
        self.hospital_name_entry.setFixedWidth(350)
        config_layout.addRow(QLabel("Nombre del Hospital:"), self.hospital_name_entry)
        
        self.direccion_entry_hospital = QLineEdit()
        self.direccion_entry_hospital.setStyleSheet("background-color: white; color: black;")
        self.direccion_entry_hospital.setMaxLength(255)
        self.direccion_entry_hospital.setFixedWidth(350)
        config_layout.addRow(QLabel("Dirección:"), self.direccion_entry_hospital)
        
        self.telefono_entry_hospital = QLineEdit()
        self.telefono_entry_hospital.setStyleSheet("background-color: white; color: black;")
        self.telefono_entry_hospital.setMaxLength(20)
        self.telefono_entry_hospital.setFixedWidth(100)
        config_layout.addRow(QLabel("Teléfono:"), self.telefono_entry_hospital)
        
        self.tipo_entry_hospital = QComboBox()
        self.tipo_entry_hospital.addItems(["I", "II", "III", "IV", "V"])
        self.tipo_entry_hospital.setFixedWidth(50)
        config_layout.addRow(QLabel("Tipo:"), self.tipo_entry_hospital)
        
        self.zona_entry_hospital = QComboBox()
        self.zona_entry_hospital.addItems(["Rural", "Urbana", "Mixta"])
        self.zona_entry_hospital.setFixedWidth(80)
        config_layout.addRow(QLabel("Zona:"), self.zona_entry_hospital)
        
        self.save_button_configuracion = QPushButton("Guardar")
        self.save_button_configuracion.setFixedSize(150, 30)  # Establecer tamaño fijo
        self.save_button_configuracion.setStyleSheet("background-color: grey; color: white;")
        self.save_button_configuracion.clicked.connect(self.save_configuracion)
        config_layout.addRow(self.save_button_configuracion)
        
        self.clear_button_configuracion = QPushButton("Limpiar Información")
        self.clear_button_configuracion.setFixedSize(150, 30)  # Establecer tamaño fijo
        self.clear_button_configuracion.setStyleSheet("background-color: grey; color: white;")
        self.clear_button_configuracion.clicked.connect(self.clear_configuracion_form)
        config_layout.addRow(self.clear_button_configuracion)
        
        main_layout.addLayout(config_layout)
        
        # Añadir un espaciador para ocupar el espacio restante
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_layout.addItem(spacer)
        
        # Frame inferior con dos subframes
        bottom_frame = QFrame()
        bottom_layout = QHBoxLayout(bottom_frame)
        
        # Subframe para la paleta de colores
        color_palette_frame = QFrame()
        color_palette_layout = QVBoxLayout(color_palette_frame)
        
        self.change_text_color_button = QPushButton("Cambiar Color de Texto")
        self.change_text_color_button.setStyleSheet("background-color: grey; color: white;")
        self.change_text_color_button.clicked.connect(self.change_text_color)
        color_palette_layout.addWidget(self.change_text_color_button)
        
        # Añadir botones para cambiar el color de cada frame
        self.change_frame_color_buttons = {}
        for frame_name in ["informacion del hospital", "configuracion de colores", "credenciales"]:
            button = QPushButton(f"Cambiar Color de {frame_name}")
            button.setStyleSheet("background-color: grey; color: white;")
            button.clicked.connect(lambda _, fn=frame_name: self.change_frame_color(fn))
            color_palette_layout.addWidget(button)
            self.change_frame_color_buttons[frame_name] = button
        
        bottom_layout.addWidget(color_palette_frame)
        
        # Subframe para la configuración de la base de datos
        db_config_frame = QFrame()
        db_config_layout = QFormLayout(db_config_frame)
        
        # Agregar el título "Credenciales de Conexión"
        db_config_title = QLabel("<b>Credenciales de Conexión</b>")
        db_config_title.setAlignment(Qt.AlignCenter)  # Centrar el título
        db_config_layout.addRow(db_config_title)
        
        self.db_user_entry = QLineEdit()
        self.db_user_entry.setStyleSheet("background-color: white; color: black;")
        self.db_user_entry.setMaxLength(200)
        self.db_user_entry.setFixedWidth(200)  # Reducir el ancho a la mitad
        db_config_layout.addRow(QLabel("Usuario:"), self.db_user_entry)
        
        self.db_password_entry = QLineEdit()
        self.db_password_entry.setStyleSheet("background-color: white; color: black;")
        self.db_password_entry.setMaxLength(200)
        self.db_password_entry.setFixedWidth(200)  # Reducir el ancho a la mitad
        self.db_password_entry.setEchoMode(QLineEdit.Password)
        db_config_layout.addRow(QLabel("Contraseña:"), self.db_password_entry)
        
        # Centrar el botón "Guardar"
        self.create_db_button = QPushButton("Guardar")
        self.create_db_button.setFixedSize(150, 30)
        self.create_db_button.setStyleSheet("background-color: grey; color: white;")
        self.create_db_button.clicked.connect(self.create_database)
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.create_db_button)
        button_layout.addStretch()
        db_config_layout.addRow(button_layout)
        
        bottom_layout.addWidget(db_config_frame)
        
        main_layout.addWidget(bottom_frame)
        
        frame.setLayout(main_layout)
        
        # Agregar los frames al diccionario self.frames
        self.frames["informacion del hospital"] = frame
        self.frames["configuracion de colores"] = color_palette_frame
        self.frames["credenciales"] = db_config_frame
        
        return frame

    def show_configuracion_frame(self):
        self.config_frame.show()
        self.config_frame.raise_()

    def save_configuracion(self):
        hospital_id = self.hospital_id_entry.text()
        nombre_hospital = self.hospital_name_entry.text()
        direccion = self.direccion_entry_hospital.text()
        telefono = self.telefono_entry_hospital.text()
        tipo = self.tipo_entry_hospital.text()
        zona = self.zona_entry_hospital.currentText()

        if not nombre_hospital or not direccion or not telefono or not tipo or not zona:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        # Validar el formato del teléfono
        if not re.match(r'^\d{4}-\d{7}$', telefono):
            QMessageBox.warning(self, "Error", "El formato del teléfono debe ser 0000-0000000.")
            return

        db_connection = CreateConnection()
        connection = None
        try:
            connection = db_connection.create_connection()
            cursor = connection.cursor()

            if hospital_id:
                query = """
                    UPDATE hospital
                    SET nombre = %s, direccion = %s, telefono = %s, tipo = %s, zona = %s
                    WHERE id = %s
                """
                cursor.execute(query, (nombre_hospital, direccion, telefono, tipo, zona, hospital_id))
            else:
                query = """
                    INSERT INTO hospital (nombre, direccion, telefono, tipo, zona)
                    VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(query, (nombre_hospital, direccion, telefono, tipo, zona))

            connection.commit()
            
            # Actualizar el nombre del hospital en la pantalla de inicio
            self.update_hospital_name()
            
            # Bloquear el botón "Limpiar Información" permanentemente
            self.clear_button_configuracion.setEnabled(False)
            db_config.CLEAR_BUTTON_DISABLED = True
            with open(os.path.join(os.path.dirname(__file__), 'db_config.py'), 'a') as config_file:
                config_file.write(f"\nCLEAR_BUTTON_DISABLED = True\n")
            
            QMessageBox.information(self, "Guardado", "Datos del hospital guardados correctamente.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al guardar los datos: {e}")
        finally:
            if connection:
                db_connection.close_connection(connection)

    def clear_configuracion_form(self):
        self.hospital_name_entry.clear()
        self.direccion_entry_hospital.clear()
        self.telefono_entry_hospital.clear()
        self.tipo_entry_hospital.clear()
        self.zona_entry_hospital.setCurrentIndex(0)

    def update_hospital_name(self):
        self.hospital_name_label_inicio.setText(self.hospital_name_entry.text())

    def load_configuracion(self):
        db_connection = CreateConnection()
        connection = None
        try:
            connection = db_connection.create_connection()
            cursor = connection.cursor()
            query = "SELECT id, nombre, direccion, telefono, tipo, zona FROM hospital LIMIT 1"
            cursor.execute(query)
            result = cursor.fetchone()
            if result:
                self.hospital_id_entry.setText(str(result[0]))
                self.hospital_name_entry.setText(result[1])
                self.direccion_entry_hospital.setText(result[2])
                self.telefono_entry_hospital.setText(result[3])
                self.tipo_entry_hospital.setCurrentText(result[4])
                self.zona_entry_hospital.setCurrentText(result[5])
                self.update_hospital_name()
                
                # Deshabilitar el botón "Guardar" si ya hay datos guardados
                self.save_button_configuracion.setEnabled(False)
                self.save_button_configuracion.setText("Registro realizado una única vez")
            if CLEAR_BUTTON_DISABLED:
                self.clear_button_configuracion.setEnabled(False)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al cargar los datos: {e}")
        finally:
            if connection:
                db_connection.close_connection(connection)

    def select_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Seleccionar Imagen", "", "Images (*.png *.xpm *.jpg *.jpeg *.bmp);;All Files (*)", options=options)
        if file_name:
            self.image_label_inicio.setPixmap(QPixmap(file_name).scaled(self.image_label_inicio.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def change_button_frame_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_frame.setStyleSheet(f"background-color: {color.name()};")

    def change_right_frames_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            for frame in self.frames.values():
                frame.setStyleSheet(f"background-color: {color.name()};")

    def change_text_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            for frame_name, frame in self.frames.items():
                if frame_name != "Configuracion":
                    for widget in frame.findChildren(QLabel):
                        if widget not in [self.hospital_name_label_inicio]:
                            widget.setStyleSheet(f"color: {color.name()};")
                if frame_name == "Inicio":
                    self.hospital_name_label_inicio.setStyleSheet(f"font-size: 40px; color: {color.name()};")
        
            # Cambiar el color de los textos en el frame de configuración
            for widget in self.findChildren(QLabel):
                if widget not in [self.date_label, self.hospital_name_label_inicio] and not isinstance(widget.parent(), QPushButton):
                    widget.setStyleSheet(f"color: {color.name()};")

    def create_database(self):
        db_user = self.db_user_entry.text()
        db_password = self.db_password_entry.text()

        if not db_user or not db_password:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        # Guardar las credenciales en un archivo de configuración
        config_path = os.path.join(os.path.dirname(__file__), 'db_config.py')
        with open(config_path, 'w') as config_file:
            config_file.write(f"DB_USER = '{db_user}'\n")
            config_file.write(f"DB_PASSWORD = '{db_password}'\n")

        QMessageBox.information(self, "Almacenado", "Credenciales guardadas correctamente.")

        # Intentar realizar la conexión a la base de datos
        db_connection = CreateConnection()
        connection = db_connection.create_connection()
        attempts = 0
        while not connection or not connection.is_connected():
            if attempts >= 3:  # Limitar el número de intentos a 3
                QMessageBox.warning(self, "Error de Conexión", "No se pudo conectar a la base de datos después de varios intentos. Verifique las credenciales e intente nuevamente.")
                return
            time.sleep(5)  # Esperar 5 segundos antes de reintentar
            connection = db_connection.create_connection()
            attempts += 1

        QMessageBox.information(self, "Conexión Exitosa", "Conexión a la base de datos realizada correctamente.")

    def change_frame_color(self, frame_name):
        color = QColorDialog.getColor()
        if color.isValid():
            frame = self.frames.get(frame_name)
            if frame:
                frame.setStyleSheet(f"background-color: {color.name()};")

    def initUI(self):
        layout = QVBoxLayout()

        # Botones para seleccionar colores
        self.background_color_button = QPushButton("Seleccionar color de fondo")
        self.background_color_button.clicked.connect(self.select_background_color)
        layout.addWidget(self.background_color_button)

        self.title_color_button = QPushButton("Seleccionar color del título")
        self.title_color_button.clicked.connect(self.select_title_color)
        layout.addWidget(self.title_color_button)

        self.lineedit_background_color_button = QPushButton("Seleccionar color de fondo de los cuadros de texto")
        self.lineedit_background_color_button.clicked.connect(self.select_lineedit_background_color)
        layout.addWidget(self.lineedit_background_color_button)

        self.lineedit_text_color_button = QPushButton("Seleccionar color del texto de los cuadros de texto")
        self.lineedit_text_color_button.clicked.connect(self.select_lineedit_text_color)
        layout.addWidget(self.lineedit_text_color_button)

        self.text_color_button = QPushButton("Seleccionar color del texto")
        self.text_color_button.clicked.connect(self.select_text_color)
        layout.addWidget(self.text_color_button)

        self.setLayout(layout)

    def select_background_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            global BACKGROUND_COLOR
            BACKGROUND_COLOR = color.name()
            self.update_stylesheet()

    def select_title_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            global TITLE_COLOR
            TITLE_COLOR = color.name()
            self.update_stylesheet()

    def select_lineedit_background_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            global LINEEDIT_BACKGROUND_COLOR
            LINEEDIT_BACKGROUND_COLOR = color.name()
            self.update_stylesheet()

    def select_lineedit_text_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            global LINEEDIT_TEXT_COLOR
            LINEEDIT_TEXT_COLOR = color.name()
            self.update_stylesheet()

    def select_text_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            global TEXT_COLOR
            TEXT_COLOR = color.name()
            self.update_stylesheet()

    def update_stylesheet(self):
        self.parent().setStyleSheet(self.parent().get_stylesheet())