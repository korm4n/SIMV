import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QScrollArea, QToolButton, QMessageBox, QPushButton
from PySide6.QtCore import Qt, Signal, QSize
from PySide6.QtGui import QIcon

class MainWindow(QMainWindow):
    datos_cargados = Signal(dict)  # Señal para pasar los datos

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Historia Clínica")
        self.setGeometry(100, 100, 820, 560)  # Establece las dimensiones de la ventana
        self.setStyleSheet("background-color: white;")  # Establece el color de fondo a blanco

        # Crear el widget central y el layout principal
        central_widget = QWidget()
        main_layout = QVBoxLayout()

        # Crear secciones
        antecedentes_personales_campos = [
            "adenitis", "alergia_p", "amigdalitis", "artritis", "asma", "bilharziasis", "blenorragia",
            "bronquitis", "buba", "catarros", "chagas", "chancros", "difteria", "diarreas", "hansen",
            "influenzas", "lechina", "necatoriasis", "neumonia", "otitis", "paludismo", "parasitos",
            "parotiditis", "pleuresía", "quirurgicos", "rinolangititis", "rubeola", "sarampion",
            "sifilis", "sindrome_disentericos", "tuberculosis", "tifoidea", "traumatismos", "vacunaciones",
            "otros"
        ]
        antecedentes_personales_layout = self.crear_seccion("Antecedentes Personales", antecedentes_personales_campos)
        main_layout.addLayout(antecedentes_personales_layout)

        antecedentes_familiares_campos = [
            "alergia", "artritis_p", "cancer", "cardio_vasculares", "diabetes", "enf_digestivas",
            "enf_renales", "intoxicaciones", "neuromentales", "sifilis_p", "tuberculosis_p", "otros_2_12"
        ]
        antecedentes_familiares_layout = self.crear_seccion("Antecedentes Familiares", antecedentes_familiares_campos)
        main_layout.addLayout(antecedentes_familiares_layout)

        habitos_psicologicos_campos = [
            "alcohol", "chimo", "deportes", "drogas", "ocupacion", "problemas_familiares",
            "rasgos_personales", "sexuales", "siesta", "sueño", "tabaco", "otros_3_10"
        ]
        habitos_psicologicos_layout = self.crear_seccion("Hábitos Psicológicos", habitos_psicologicos_campos)
        main_layout.addLayout(habitos_psicologicos_layout)

        examen_funcional_general_campos = [
            "aumento_de_peso", "fiebre", "nutricion", "perdida_de_peso", "sudores_nocturnos",
            "temblores", "otros_4_7"
        ]
        examen_funcional_general_layout = self.crear_seccion("Examen Funcional General", examen_funcional_general_campos)
        main_layout.addLayout(examen_funcional_general_layout)

        piel_campos = [
            "color", "humedad", "contextura", "temperatura", "pigmentacion", "equimosis",
            "cianosis", "petequias", "erupcion", "unas", "nobulos", "vascularizacion",
            "cicatrices", "fistulas", "ulceras", "otros_1_16"
        ]
        piel_layout = self.crear_seccion("Piel", piel_campos)
        main_layout.addLayout(piel_layout)

        cabeza_campos = [
            "configuracion", "fontanelas", "reblandecimiento", "circunferencia", "dolor_de_cabeza", "cabellos", "otros_2_7"
        ]
        cabeza_layout = self.crear_seccion("Cabeza", cabeza_campos)
        main_layout.addLayout(cabeza_layout)

        ojos_campos = [
            "conjuntiva", "esclerotica", "cornea", "pupilas", "movimiento", "desviacion",
            "nistagmus", "ptosis", "exoftalmos", "agudeza_visual", "oftalmoscopicos", "otros_3_12"
        ]
        ojos_layout = self.crear_seccion("Ojos", ojos_campos)
        main_layout.addLayout(ojos_layout)

        oidos_campos = [
            "pabellon", "conducto_extremo", "timpano", "audicion", "secreciones", "mastoides",
            "dolor_de_oido", "otros_4_8", "otros_3_12"
        ]
        oidos_layout = self.crear_seccion("Oídos", oidos_campos)
        main_layout.addLayout(oidos_layout)

        nariz_campos = [
            "fosas_nasales", "mucosas", "tabique", "meatos", "diafanoscopia", "sensibilidad_de_los_senos",
            "secrecion_nasal", "otros_5_8"
        ]
        nariz_layout = self.crear_seccion("Nariz", nariz_campos)
        main_layout.addLayout(nariz_layout)

        boca_campos = [
            "aliento", "labios", "dientes", "encías", "mucosas_bucales", "lengua",
            "conductos_salivales", "paralisis_y_trismo", "otros_6_9"
        ]
        boca_layout = self.crear_seccion("Boca", boca_campos)
        main_layout.addLayout(boca_layout)

        faringe_campos = [
            "amigdalas", "adenoides", "rino_faringe", "disfagia", "dolor_de_la_faringe", "otros_7_6"
        ]
        faringe_layout = self.crear_seccion("Faringe", faringe_campos)
        main_layout.addLayout(faringe_layout)

        cuello_campos = [
            "movilidad", "ganglios", "tiroides", "vasos", "traquea", "otros_8_6"
        ]
        cuello_layout = self.crear_seccion("Cuello", cuello_campos)
        main_layout.addLayout(cuello_layout)

        ganglios_campos = [
            "cervicales", "occipitales", "supraclaviculares", "axilares", "epitrocleares", "inguinales", "otros_9_7"
        ]
        ganglios_layout = self.crear_seccion("Ganglios Linfáticos", ganglios_campos)
        main_layout.addLayout(ganglios_layout)

        torax_campos = [
            "forma", "simetria", "expansion", "palpitacion", "respiracion", "otros_10_6"
        ]
        torax_layout = self.crear_seccion("Tórax", torax_campos)
        main_layout.addLayout(torax_layout)

        senos_campos = [
            "nodulos", "secreciones_pecho", "pezones", "otros_11_4"
        ]
        senos_layout = self.crear_seccion("Senos", senos_campos)
        main_layout.addLayout(senos_layout)

        pulmones_campos = [
            "fremito", "percusion", "auscultacion", "ruidos_adventicios", "pectoriloquia_afona", "broncofonia", "otros_12_7"
        ]
        pulmones_layout = self.crear_seccion("Pulmones", pulmones_campos)
        main_layout.addLayout(pulmones_layout)

        corazon_campos = [
            "latidos_de_la_punta", "thrill", "pulsacion", "ritmo", "ruidos", "galopes", "frotes", "otros_13_8"
        ]
        corazon_layout = self.crear_seccion("Corazón", corazon_campos)
        main_layout.addLayout(corazon_layout)

        vasos_campos = [
            "pulso_h", "paredes_vasculares", "caracteres", "otros_14_4"
        ]
        vasos_layout = self.crear_seccion("Vasos Sanguíneos", vasos_campos)
        main_layout.addLayout(vasos_layout)

        abdomen_campos = [
            "aspecto", "circunferencia_abdomen", "peristalsis", "cicatrices_abdomen", "defensa", "sensibilidad_abdomen",
            "contracturas", "tumoraciones", "ascitis", "higado", "rinones", "bazo", "hernias", "otros_15_14"
        ]
        abdomen_layout = self.crear_seccion("Abdomen", abdomen_campos)
        main_layout.addLayout(abdomen_layout)

        genitales_masculinos_campos = [
            "cicatrices_genitales", "lesiones", "secreciones_genitales", "escroto", "epididimo", "deferentes",
            "testiculos", "prostata", "seminales", "otros_16_10"
        ]
        genitales_masculinos_layout = self.crear_seccion("Genitales Masculinos", genitales_masculinos_campos)
        main_layout.addLayout(genitales_masculinos_layout)

        genitales_femeninos_campos = [
            "labios_genitales", "bartholino", "perine", "vagina", "cuello", "utero",
            "anexos", "parametrico", "saco_de_douglas", "otros_17_10"
        ]
        genitales_femeninos_layout = self.crear_seccion("Genitales Femeninos", genitales_femeninos_campos)
        main_layout.addLayout(genitales_femeninos_layout)

        recto_campos = [
            "fisuras", "fistula_anal", "hemorroides", "esfinter", "tumoraciones_anales", "prolapso",
            "heces", "otros_18_8"
        ]
        recto_layout = self.crear_seccion("Recto", recto_campos)
        main_layout.addLayout(recto_layout)

        huesos_campos = [
            "deformidades", "inflamaciones", "rubicindes", "sensibilidad_muscular", "movimientos", "masas_musculares", "otros_19_7"
        ]
        huesos_layout = self.crear_seccion("Huesos, Articulaciones y Músculos", huesos_campos)
        main_layout.addLayout(huesos_layout)

        extremidades_campos = [
            "color_piel", "edema", "temblor", "deformidades_piel", "ulceras_piel", "varices", "otros_20_7"
        ]
        extremidades_layout = self.crear_seccion("Extremidades", extremidades_campos)
        main_layout.addLayout(extremidades_layout)

        neurologico_campos = [
            "sensibilidad_objetiva", "motilidad", "reflectividad", "escritura", "troficos", "marcha",
            "romberg", "orientacion", "lenguaje", "coordinacion", "otros_21_11"
        ]
        neurologico_layout = self.crear_seccion("Neurológico y Psíquico", neurologico_campos)
        main_layout.addLayout(neurologico_layout)

        # Crear un QScrollArea y establecer el main_layout como su widget
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_content = QWidget()
        scroll_content.setLayout(main_layout)
        scroll_area.setWidget(scroll_content)

        # Establecer el scroll_area como el widget central
        self.setCentralWidget(scroll_area)

        # Añadir el botón para cargar datos en variables temporales
        cargar_datos_btn = QPushButton("Cargar")
        cargar_datos_btn.setStyleSheet("color: black; font-size: 14px;")
        cargar_datos_btn.setIcon(QIcon("iconos/cargar.png"))  # Establecer el ícono
        cargar_datos_btn.setIconSize(QSize(16, 16))  # Establecer el tamaño del ícono
        cargar_datos_btn.clicked.connect(self.cargar_datos)
        main_layout.addWidget(cargar_datos_btn, alignment=Qt.AlignRight)

    # Función para alternar la visibilidad de una sección
    def toggle_seccion(self, boton, widget):
        if boton.isChecked():
            boton.setArrowType(Qt.DownArrow)
            widget.setVisible(True)
        else:
            boton.setArrowType(Qt.RightArrow)
            widget.setVisible(False)

    # Sobrescribir el evento de cierre de la ventana
    def closeEvent(self, event):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle('Salir')
        msg_box.setText("¿Desea salir sin guardar, guardar la información o cancelar?")
        msg_box.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        msg_box.setButtonText(QMessageBox.Save, "Guardar")
        msg_box.setButtonText(QMessageBox.Discard, "Descartar")
        msg_box.setButtonText(QMessageBox.Cancel, "Cancelar")
        msg_box.setDefaultButton(QMessageBox.Cancel)
        msg_box.setStyleSheet("color: black;")
        reply = msg_box.exec()

        if reply == QMessageBox.Save:
            # Lógica para guardar la información
            event.accept()
        elif reply == QMessageBox.Discard:
            event.accept()
        else:
            event.ignore()

    def crear_seccion(self, titulo, campos):
        seccion_layout = QVBoxLayout()
        boton = QToolButton()
        boton.setText(titulo)
        boton.setStyleSheet("color: black; font-size: 16px; font-weight: bold; text-align: left;")
        boton.setCheckable(True)
        boton.setChecked(False)  # Iniciar replegado
        boton.setArrowType(Qt.RightArrow)  # Flecha apuntando a la derecha
        boton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        boton.clicked.connect(lambda: self.toggle_seccion(boton, campos_widget))

        campos_layout = QVBoxLayout()
        campos_widget = QWidget()
        campos_widget.setLayout(campos_layout)
        campos_widget.setVisible(False)  # Iniciar replegado

        for i in range(0, len(campos), 3):
            h_layout = QHBoxLayout()
            for campo in campos[i:i+3]:
                v_layout = QVBoxLayout()
                label = QLabel(f"{campo.capitalize()}:")
                label.setStyleSheet("color: black;")
                line_edit = QLineEdit()
                line_edit.setFixedWidth(250)
                line_edit.setStyleSheet("color: black;")
                v_layout.addWidget(label)
                v_layout.addWidget(line_edit)
                h_layout.addLayout(v_layout)
                setattr(self, f"{campo}_entry", line_edit)  # Guardar el QLineEdit en una variable de instancia
            campos_layout.addLayout(h_layout)

        seccion_layout.addWidget(boton)
        seccion_layout.addWidget(campos_widget)
        return seccion_layout

    def cargar_datos(self):
        # Aquí se cargan los datos de los campos en variables temporales
        datos = {}
        for campo in dir(self):
            if campo.endswith('_entry'):
                datos[campo] = getattr(self, campo).text()
        # Emitir la señal con los datos
        self.datos_cargados.emit(datos)
        self.close()  # Cerrar la ventana después de cargar los datos

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()