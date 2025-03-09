from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class Inventario(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        label = QLabel("Inventario")
        layout.addWidget(label)
        self.setLayout(layout)