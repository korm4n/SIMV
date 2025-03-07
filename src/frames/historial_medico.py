from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QListWidget, QPushButton, QStackedLayout

class HistorialMedico(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.stacked_layout = QStackedLayout()
        self.layout.addLayout(self.stacked_layout)

        self.historia_medica_frame = self.create_historia_medica_frame()
        self.stacked_layout.addWidget(self.historia_medica_frame)

    def create_historia_medica_frame(self):
        frame = QWidget()
        layout = QVBoxLayout(frame)
        layout.addWidget(QLabel("Historia Médica del Paciente"))
        self.paciente_list = QListWidget()
        layout.addWidget(self.paciente_list)
        frame.setLayout(layout)
        return frame

    def mostrar_historial_medico(self):
        self.stacked_layout.setCurrentWidget(self.historia_medica_frame)