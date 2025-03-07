from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt

class Inicio(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(self.create_inicio_frame())
        self.setLayout(layout)

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

        layout.addWidget(QLabel("Médicos de Guardia:"))
        layout.addWidget(QLabel("Dr. Juan Pérez - Cardiología (08:00 - 16:00)"))
        layout.addWidget(QLabel("Dra. Ana Gómez - Pediatría (16:00 - 00:00)"))
        layout.addWidget(QLabel("Dr. Luis Martínez - Neurología (00:00 - 08:00)"))

        # Image label
        self.image_label_inicio = QLabel()
        self.image_label_inicio.setFixedSize(50, 50)
        self.image_label_inicio.setStyleSheet("border: none;")
        self.image_label_inicio.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.image_label_inicio)

        return frame