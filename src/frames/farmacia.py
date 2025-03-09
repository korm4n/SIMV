from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QFormLayout, QLineEdit, QDateEdit, QPushButton, QMessageBox, QHBoxLayout
from PySide6.QtGui import QIcon
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
        
        self.cantidad_recibida_entry = QLineEdit()
        self.cantidad_recibida_entry.setMaxLength(100)
        self.cantidad_recibida_entry.setFixedWidth(100)
        recibida_usada_devuelta_layout.addWidget(QLabel("Cantidad Recibida:"))
        recibida_usada_devuelta_layout.addWidget(self.cantidad_recibida_entry)

        self.cantidad_usada_entry = QLineEdit()
        self.cantidad_usada_entry.setMaxLength(100)
        self.cantidad_usada_entry.setFixedWidth(100)
        recibida_usada_devuelta_layout.addWidget(QLabel("Cantidad Usada:"))
        recibida_usada_devuelta_layout.addWidget(self.cantidad_usada_entry)

        self.cantidad_devuelta_entry = QLineEdit()
        self.cantidad_devuelta_entry.setMaxLength(100)
        self.cantidad_devuelta_entry.setFixedWidth(100)
        recibida_usada_devuelta_layout.addWidget(QLabel("Cantidad Devuelta:"))
        recibida_usada_devuelta_layout.addWidget(self.cantidad_devuelta_entry)

        self.cantidad_desechada_entry = QLineEdit()
        self.cantidad_desechada_entry.setMaxLength(100)
        self.cantidad_desechada_entry.setFixedWidth(100)
        recibida_usada_devuelta_layout.addWidget(QLabel("Cantidad Desechada:"))
        recibida_usada_devuelta_layout.addWidget(self.cantidad_desechada_entry)

        self.cantidad_que_queda_entry = QLineEdit()
        self.cantidad_que_queda_entry.setMaxLength(100)
        self.cantidad_que_queda_entry.setFixedWidth(100)
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

        # Botones Guardar y Limpiar en la misma fila
        botones_layout = QHBoxLayout()
        self.save_button_farmacia = QPushButton("Guardar")
        self.save_button_farmacia.setIcon(QIcon("iconos/guardar.png"))  # Agregar ícono al botón "Guardar"
        self.save_button_farmacia.setFixedSize(150, 30)
        self.save_button_farmacia.clicked.connect(self.save_farmacia)
        botones_layout.addWidget(self.save_button_farmacia)
        
        self.clear_button_farmacia = QPushButton("Limpiar")
        self.clear_button_farmacia.setIcon(QIcon("iconos/limpiar.png"))  # Agregar ícono al botón "Limpiar Información"
        self.clear_button_farmacia.setFixedSize(150, 30)
        self.clear_button_farmacia.clicked.connect(self.clear_farmacia_form)
        botones_layout.addWidget(self.clear_button_farmacia)
        
        layout.addRow(botones_layout)
        
        frame.setLayout(layout)
        return frame

    def save_farmacia(self):
        # Implementar lógica para guardar los datos
        pass

    def clear_farmacia_form(self):
        self.numero_lote_entry.clear()
        self.nombre_medicamento_entry.clear()
        self.fecha_vencimiento_entry.setDate(QDate.currentDate())
        self.fecha_elaboracion_entry.setDate(QDate.currentDate())
        self.cantidad_recibida_entry.clear()
        self.cantidad_usada_entry.clear()
        self.cantidad_devuelta_entry.clear()
        self.cantidad_desechada_entry.clear()
        self.cantidad_que_queda_entry.clear()
        self.concentracion_entry.clear()
        self.forma_farmaceutica_entry.clear()
        self.codigo_unidad_contenido_entry.clear()
        self.capacidad_unidad_contenido_entry.clear()
        self.via_administracion_entry.clear()