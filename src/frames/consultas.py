from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QFormLayout, QComboBox, QHBoxLayout, QLineEdit, QPushButton, QListWidget

class Consultas(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        # Crear y agregar el frame de consultas
        consultas_frame = self.create_consultas_frame()
        layout.addWidget(consultas_frame)

        self.setLayout(layout)

    def create_consultas_frame(self):
        frame = QWidget()
        layout = QFormLayout(frame)

        # Sexo
        self.sexo_combobox_consultas = QComboBox()
        self.sexo_combobox_consultas.addItems(["Masculino", "Femenino"])
        layout.addRow(QLabel("Sexo:"), self.sexo_combobox_consultas)

        # Edad mínima y máxima en un QHBoxLayout
        edad_layout = QHBoxLayout()
        self.edad_min_combobox_consultas = QComboBox()
        self.edad_min_combobox_consultas.addItems([str(i) for i in range(101)])
        edad_layout.addWidget(QLabel("Edad Mínima:"))
        edad_layout.addWidget(self.edad_min_combobox_consultas)

        self.edad_max_combobox_consultas = QComboBox()
        self.edad_max_combobox_consultas.addItems([str(i) for i in range(101)])
        edad_layout.addWidget(QLabel("Edad Máxima:"))
        edad_layout.addWidget(self.edad_max_combobox_consultas)

        layout.addRow(edad_layout)

        self.direccion_entry_consultas = QLineEdit()
        self.direccion_entry_consultas.setStyleSheet("background-color: white;")
        layout.addRow(QLabel("Dirección:"), self.direccion_entry_consultas)

        self.tipo_enfermedad_entry_consultas = QLineEdit()
        self.tipo_enfermedad_entry_consultas.setStyleSheet("background-color: white;")
        layout.addRow(QLabel("Tipo de Enfermedad:"), self.tipo_enfermedad_entry_consultas)

        # Embarazadas
        self.embarazadas_combobox_consultas = QComboBox()
        self.embarazadas_combobox_consultas.addItems(["Sí", "No"])
        layout.addRow(QLabel("Embarazadas:"), self.embarazadas_combobox_consultas)

        # Botón de búsqueda
        self.search_button_consultas = QPushButton("Buscar")
        self.search_button_consultas.setFixedSize(150, 30)  # Establecer tamaño fijo
        self.search_button_consultas.clicked.connect(self.search_consultas)
        layout.addRow(self.search_button_consultas)

        # Lista de resultados
        self.consultas_list = QListWidget()
        layout.addRow(QLabel("Resultados de Consultas:"), self.consultas_list)

        frame.setLayout(layout)
        return frame

    def search_consultas(self):
        sexo = self.sexo_combobox_consultas.currentText()
        edad_min = self.edad_min_combobox_consultas.currentText()
        edad_max = self.edad_max_combobox_consultas.currentText()
        direccion = self.direccion_entry_consultas.text()
        tipo_enfermedad = self.tipo_enfermedad_entry_consultas.text()
        embarazadas = self.embarazadas_combobox_consultas.currentText()

        # Aquí puedes agregar la lógica para realizar la búsqueda en la base de datos
        # y actualizar la lista de resultados (self.consultas_list)

        # Ejemplo de actualización de la lista de resultados
        self.consultas_list.clear()

        # Filtrar resultados según los criterios especificados
        results = self.filter_consultas(sexo, edad_min, edad_max, direccion, tipo_enfermedad, embarazadas)
        for result in results:
            self.consultas_list.addItem(result)

    def filter_consultas(self, sexo, edad_min, edad_max, direccion, tipo_enfermedad, embarazadas):
        # Aquí puedes agregar la lógica para filtrar los resultados de la base de datos
        # Este es un ejemplo de cómo podrías hacerlo con datos ficticios
        all_consultas = [
            {"sexo": "Masculino", "edad": "30", "direccion": "Calle 1", "tipo_enfermedad": "Gripe", "embarazadas": "No"},
            {"sexo": "Femenino", "edad": "25", "direccion": "Calle 2", "tipo_enfermedad": "Covid-19", "embarazadas": "Sí"},
            # Agrega más datos ficticios aquí
        ]

        filtered_consultas = []
        for consulta in all_consultas:
            if (sexo == consulta["sexo"] or not sexo) and \
               (not edad_min or int(consulta["edad"]) >= int(edad_min)) and \
               (not edad_max or int(consulta["edad"]) <= int(edad_max)) and \
               (direccion in consulta["direccion"] or not direccion) and \
               (tipo_enfermedad in consulta["tipo_enfermedad"] or not tipo_enfermedad) and \
               (embarazadas == consulta["embarazadas"] or not embarazadas):
                filtered_consultas.append(f"Sexo: {consulta['sexo']}, Edad: {consulta['edad']}, Dirección: {consulta['direccion']}, Tipo de Enfermedad: {consulta['tipo_enfermedad']}, Embarazadas: {consulta['embarazadas']}")

        return filtered_consultas