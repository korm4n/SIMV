from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFormLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QDateEdit, QTextEdit, QCheckBox, QSpacerItem, QSizePolicy, QMessageBox
from PySide6.QtGui import QIntValidator, QDoubleValidator, QIcon
from PySide6.QtCore import QSize, Qt, QDate, QTime
from utils import calculate_age  # Importar la función desde utils.py
from frames.consultas_medicas.Historia_Clinica.Historia_clinica_p import MainWindow  # Importar la clase MainWindow
from servicios import CreateConnection  # Importar la clase para la conexión a la base de datos
from mysql.connector import Error  # Importar la clase Error

class ConsultaGeneral(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.datos_historia_clinica_cargados = False  # Bandera para verificar si se han cargado los datos de historia clínica
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Definir todas las variables temporales como QLineEdit
        self.adenitis_entry = QLineEdit()
        self.alergia_p_entry = QLineEdit()
        self.amigdalitis_entry = QLineEdit()
        self.artritis_p_entry = QLineEdit()
        self.asma_entry = QLineEdit()
        self.bilharziasis_entry = QLineEdit()
        self.blenorragia_entry = QLineEdit()
        self.bronquitis_entry = QLineEdit()
        self.buba_entry = QLineEdit()
        self.catarros_entry = QLineEdit()
        self.chagas_entry = QLineEdit()
        self.chancros_entry = QLineEdit()
        self.difteria_entry = QLineEdit()
        self.diarreas_entry = QLineEdit()
        self.hansen_entry = QLineEdit()
        self.influenzas_entry = QLineEdit()
        self.lechina_entry = QLineEdit()
        self.necatoriasis_entry = QLineEdit()
        self.neumonia_entry = QLineEdit()
        self.otitis_entry = QLineEdit()
        self.paludismo_entry = QLineEdit()
        self.parasitos_entry = QLineEdit()
        self.parotiditis_entry = QLineEdit()
        self.pleuresia_entry = QLineEdit()
        self.quirurgicos_entry = QLineEdit()
        self.rinolangititis_entry = QLineEdit()
        self.rubeola_entry = QLineEdit()
        self.sarampion_entry = QLineEdit()
        self.sifilis_p_entry = QLineEdit()
        self.sindrome_disentericos_entry = QLineEdit()
        self.tuberculosis_p_entry = QLineEdit()
        self.tifoidea_entry = QLineEdit()
        self.traumatismos_entry = QLineEdit()
        self.vacunaciones_entry = QLineEdit()
        self.otros_entry = QLineEdit()
        self.aumento_de_peso_entry = QLineEdit()
        self.fiebre_entry = QLineEdit()
        self.nutricion_entry = QLineEdit()
        self.perdida_de_peso_entry = QLineEdit()
        self.sudores_nocturnos_entry = QLineEdit()
        self.temblores_entry = QLineEdit()
        self.otros_4_7_entry = QLineEdit()
        self.color_entry = QLineEdit()
        self.humedad_entry = QLineEdit()
        self.contextura_entry = QLineEdit()
        self.temperatura_entry_1 = QLineEdit()
        self.pigmentacion_entry = QLineEdit()
        self.equimosis_entry = QLineEdit()
        self.cianosis_entry = QLineEdit()
        self.petequias_entry = QLineEdit()
        self.erupcion_entry = QLineEdit()
        self.unas_entry = QLineEdit()
        self.nobulos_entry = QLineEdit()
        self.vascularizacion_entry = QLineEdit()
        self.cicatrices_entry = QLineEdit()
        self.fistulas_entry = QLineEdit()
        self.ulceras_entry = QLineEdit()
        self.otros_1_16_entry = QLineEdit()
        self.configuracion_entry = QLineEdit()
        self.fontanelas_entry = QLineEdit()
        self.reblandecimiento_entry = QLineEdit()
        self.circunferencia_entry = QLineEdit()
        self.dolor_de_cabeza_entry = QLineEdit()
        self.cabellos_entry = QLineEdit()
        self.otros_2_7_entry = QLineEdit()
        self.conjuntiva_entry = QLineEdit()
        self.esclerotica_entry = QLineEdit()
        self.cornea_entry = QLineEdit()
        self.pupilas_entry = QLineEdit()
        self.movimiento_entry = QLineEdit()
        self.desviacion_entry = QLineEdit()
        self.nistagmus_entry = QLineEdit()
        self.ptosis_entry = QLineEdit()
        self.exoftalmos_entry = QLineEdit()
        self.agudeza_visual_entry = QLineEdit()
        self.oftalmoscopicos_entry = QLineEdit()
        self.otros_3_12_entry = QLineEdit()
        self.pabellon_entry = QLineEdit()
        self.conducto_extremo_entry = QLineEdit()
        self.timpano_entry = QLineEdit()
        self.audicion_entry = QLineEdit()
        self.secreciones_entry = QLineEdit()
        self.mastoides_entry = QLineEdit()
        self.dolor_de_oido_entry = QLineEdit()
        self.otros_4_8_entry = QLineEdit()
        self.fosas_nasales_entry = QLineEdit()
        self.mucosas_entry = QLineEdit()
        self.tabique_entry = QLineEdit()
        self.meatos_entry = QLineEdit()
        self.diafanoscopia_entry = QLineEdit()
        self.sensibilidad_de_los_senos_entry = QLineEdit()
        self.secrecion_nasal_entry = QLineEdit()
        self.otros_5_8_entry = QLineEdit()
        self.aliento_entry = QLineEdit()
        self.labios_entry = QLineEdit()
        self.dientes_entry = QLineEdit()
        self.encias_entry = QLineEdit()
        self.mucosas_bucales_entry = QLineEdit()
        self.lengua_entry = QLineEdit()
        self.conductos_salivales_entry = QLineEdit()
        self.paralisis_y_trismo_entry = QLineEdit()
        self.otros_6_9_entry = QLineEdit()
        self.amigdalas_entry = QLineEdit()
        self.adenoides_entry = QLineEdit()
        self.rino_faringe_entry = QLineEdit()
        self.disfagia_entry = QLineEdit()
        self.dolor_de_la_faringe_entry = QLineEdit()
        self.otros_7_6_entry = QLineEdit()
        self.movilidad_entry = QLineEdit()
        self.ganglios_entry = QLineEdit()
        self.tiroides_entry = QLineEdit()
        self.vasos_entry = QLineEdit()
        self.traquea_entry = QLineEdit()
        self.otros_8_6_entry = QLineEdit()
        self.cervicales_entry = QLineEdit()
        self.occipitales_entry = QLineEdit()
        self.supraclaviculares_entry = QLineEdit()
        self.axilares_entry = QLineEdit()
        self.epitrocleares_entry = QLineEdit()
        self.inguinales_entry = QLineEdit()
        self.otros_9_7_entry = QLineEdit()
        self.forma_entry = QLineEdit()
        self.simetria_entry = QLineEdit()
        self.expansion_entry = QLineEdit()
        self.palpitacion_entry = QLineEdit()
        self.respiracion_entry_2 = QLineEdit()
        self.otros_10_6_entry = QLineEdit()
        self.nodulos_entry = QLineEdit()
        self.secreciones_pecho_entry = QLineEdit()
        self.pezones_entry = QLineEdit()
        self.otros_11_4_entry = QLineEdit()
        self.fremito_entry = QLineEdit()
        self.percusion_entry = QLineEdit()
        self.auscultacion_entry = QLineEdit()
        self.ruidos_adventicios_entry = QLineEdit()
        self.pectoriloquia_afona_entry = QLineEdit()
        self.broncofonia_entry = QLineEdit()
        self.otros_12_7_entry = QLineEdit()
        self.latidos_de_la_punta_entry = QLineEdit()
        self.thrill_entry = QLineEdit()
        self.pulsacion_entry = QLineEdit()
        self.ritmo_entry = QLineEdit()
        self.ruidos_entry = QLineEdit()
        self.galopes_entry = QLineEdit()
        self.frotes_entry = QLineEdit()
        self.otros_13_8_entry = QLineEdit()
        self.pulso_h_entry = QLineEdit()
        self.paredes_vasculares_entry = QLineEdit()
        self.caracteres_entry = QLineEdit()
        self.otros_14_4_entry = QLineEdit()
        self.aspecto_entry = QLineEdit()
        self.circunferencia_abdomen_entry = QLineEdit()
        self.peristalsis_entry = QLineEdit()
        self.cicatrices_abdomen_entry = QLineEdit()
        self.defensa_entry = QLineEdit()
        self.sensibilidad_abdomen_entry = QLineEdit()
        self.contracturas_entry = QLineEdit()
        self.tumoraciones_entry = QLineEdit()
        self.ascitis_entry = QLineEdit()
        self.higado_entry = QLineEdit()
        self.rinones_entry = QLineEdit()
        self.bazo_entry = QLineEdit()
        self.hernias_entry = QLineEdit()
        self.otros_15_14_entry = QLineEdit()
        self.cicatrices_genitales_entry = QLineEdit()
        self.lesiones_entry = QLineEdit()
        self.secreciones_genitales_entry = QLineEdit()
        self.escroto_entry = QLineEdit()
        self.epididimo_entry = QLineEdit()
        self.deferentes_entry = QLineEdit()
        self.testiculos_entry = QLineEdit()
        self.prostata_entry = QLineEdit()
        self.seminales_entry = QLineEdit()
        self.otros_16_10_entry = QLineEdit()
        self.labios_genitales_entry = QLineEdit()
        self.bartholino_entry = QLineEdit()
        self.perine_entry = QLineEdit()
        self.vagina_entry = QLineEdit()
        self.cuello_entry = QLineEdit()
        self.utero_entry = QLineEdit()
        self.anexos_entry = QLineEdit()
        self.parametrico_entry = QLineEdit()
        self.saco_de_douglas_entry = QLineEdit()
        self.otros_17_10_entry = QLineEdit()
        self.fisuras_entry = QLineEdit()
        self.fistula_anal_entry = QLineEdit()
        self.hemorroides_entry = QLineEdit()
        self.esfinter_entry = QLineEdit()
        self.tumoraciones_anales_entry = QLineEdit()
        self.prolapso_entry = QLineEdit()
        self.heces_entry = QLineEdit()
        self.otros_18_8_entry = QLineEdit()
        self.deformidades_entry = QLineEdit()
        self.inflamaciones_entry = QLineEdit()
        self.rubicindes_entry = QLineEdit()
        self.sensibilidad_muscular_entry = QLineEdit()
        self.movimientos_entry = QLineEdit()
        self.masas_musculares_entry = QLineEdit()
        self.otros_19_7_entry = QLineEdit()
        self.color_piel_entry = QLineEdit()
        self.edema_entry = QLineEdit()
        self.temblor_entry = QLineEdit()
        self.deformidades_piel_entry = QLineEdit()
        self.ulceras_piel_entry = QLineEdit()
        self.varices_entry = QLineEdit()
        self.otros_20_7_entry = QLineEdit()
        self.sensibilidad_objetiva_entry = QLineEdit()
        self.motilidad_entry = QLineEdit()
        self.reflectividad_entry = QLineEdit()
        self.escritura_entry = QLineEdit()
        self.troficos_entry = QLineEdit()
        self.marcha_entry = QLineEdit()
        self.romberg_entry = QLineEdit()
        self.orientacion_entry = QLineEdit()
        self.lenguaje_entry = QLineEdit()
        self.coordinacion_entry = QLineEdit()
        self.otros_21_11_entry = QLineEdit()
        self.alergia_entry = QLineEdit()
        self.artritis_entry = QLineEdit()
        self.cancer_entry = QLineEdit()
        self.cardio_vasculares_entry = QLineEdit()
        self.diabetes_entry = QLineEdit()
        self.enf_digestivas_entry = QLineEdit()
        self.enf_renales_entry = QLineEdit()
        self.intoxicaciones_entry = QLineEdit()
        self.neuromentales_entry = QLineEdit()
        self.sifilis_entry = QLineEdit()
        self.tuberculosis_entry = QLineEdit()
        self.otros_2_12_entry = QLineEdit()
        self.alcohol_entry = QLineEdit()
        self.chimo_entry = QLineEdit()
        self.deportes_entry = QLineEdit()
        self.drogas_entry = QLineEdit()
        self.ocupacion_entry = QLineEdit()
        self.problemas_familiares_entry = QLineEdit()
        self.rasgos_personales_entry = QLineEdit()
        self.sexuales_entry = QLineEdit()
        self.siesta_entry = QLineEdit()
        self.sueño_entry = QLineEdit()
        self.tabaco_entry = QLineEdit()
        self.otros_3_10_entry = QLineEdit()

        # Crear el formulario de paciente
        form_layout = QFormLayout()
        layout.addLayout(form_layout)

        # Crear un layout horizontal para los campos en una misma línea
        h_layout1 = QHBoxLayout()

        self.cedula_entry = QLineEdit()
        self.cedula_entry.setMaxLength(20)
        self.cedula_entry.setFixedWidth(100)
        self.cedula_entry.textChanged.connect(self.convert_to_uppercase)
        h_layout1.addWidget(QLabel("Cédula:"))
        h_layout1.addWidget(self.cedula_entry)

        self.primer_nombre_entry = QLineEdit()
        self.primer_nombre_entry.setMaxLength(255)
        self.primer_nombre_entry.setFixedWidth(120)
        self.primer_nombre_entry.textChanged.connect(self.convert_to_uppercase)
        h_layout1.addWidget(QLabel("Primer Nombre:"))
        h_layout1.addWidget(self.primer_nombre_entry)

        self.segundo_nombre_entry = QLineEdit()
        self.segundo_nombre_entry.setMaxLength(255)
        self.segundo_nombre_entry.setFixedWidth(100)
        self.segundo_nombre_entry.textChanged.connect(self.convert_to_uppercase)
        h_layout1.addWidget(QLabel("Segundo Nombre:"))
        h_layout1.addWidget(self.segundo_nombre_entry)

        self.primer_apellido_entry = QLineEdit()
        self.primer_apellido_entry.setMaxLength(255)
        self.primer_apellido_entry.setFixedWidth(120)
        self.primer_apellido_entry.textChanged.connect(self.convert_to_uppercase)
        h_layout1.addWidget(QLabel("Primer Apellido:"))
        h_layout1.addWidget(self.primer_apellido_entry)

        self.segundo_apellido_entry = QLineEdit()
        self.segundo_apellido_entry.setMaxLength(255)
        self.segundo_apellido_entry.setFixedWidth(100)
        self.segundo_apellido_entry.textChanged.connect(self.convert_to_uppercase)
        h_layout1.addWidget(QLabel("Segundo Apellido:"))
        h_layout1.addWidget(self.segundo_apellido_entry)

        self.age_label_paciente = QLabel()
        self.age_label_paciente.setFixedWidth(30)
        h_layout1.addWidget(QLabel("Edad:"))
        h_layout1.addWidget(self.age_label_paciente)

        form_layout.addRow(h_layout1)

        # Crear un layout horizontal para los campos en una misma línea
        h_layout2 = QHBoxLayout()

        self.fecha_nacimiento_entry = QDateEdit()
        self.fecha_nacimiento_entry.setCalendarPopup(True)
        self.fecha_nacimiento_entry.setFixedWidth(100)
        self.fecha_nacimiento_entry.dateChanged.connect(self.update_age_paciente)
        h_layout2.addWidget(QLabel("Fecha de Nacimiento:"))
        h_layout2.addWidget(self.fecha_nacimiento_entry)

        # Nuevo campo de teléfono
        self.telefono_entry = QLineEdit()
        self.telefono_entry.setMaxLength(20)
        self.telefono_entry.setFixedWidth(90)
        self.telefono_entry.textChanged.connect(self.convert_to_uppercase)
        h_layout2.addWidget(QLabel("Teléfono:"))
        h_layout2.addWidget(self.telefono_entry)

        self.genero_entry = QComboBox()
        self.genero_entry.addItems(["Seleccione", "Masculino", "Femenino"])
        self.genero_entry.setFixedWidth(80)
        h_layout2.addWidget(QLabel("Género:"))
        h_layout2.addWidget(self.genero_entry)

        self.estado_civil_entry = QComboBox()
        self.estado_civil_entry.addItems(["Seleccione", "Soltero", "Casado", "Viudo", "Divorciado"])
        self.estado_civil_entry.setFixedWidth(80)
        h_layout2.addWidget(QLabel("Estado Civil:"))
        h_layout2.addWidget(self.estado_civil_entry)

        self.nacionalidad_entry = QLineEdit()
        self.nacionalidad_entry.setMaxLength(20)
        self.nacionalidad_entry.setFixedWidth(90)
        self.nacionalidad_entry.textChanged.connect(self.convert_to_uppercase)
        h_layout2.addWidget(QLabel("Nacionalidad:"))
        h_layout2.addWidget(self.nacionalidad_entry)

        self.profesion_ocupacion_entry = QLineEdit()
        self.profesion_ocupacion_entry.setMaxLength(100)
        self.profesion_ocupacion_entry.setFixedWidth(110)
        self.profesion_ocupacion_entry.textChanged.connect(self.convert_to_uppercase)
        h_layout2.addWidget(QLabel("Profesión/Ocupación:"))
        h_layout2.addWidget(self.profesion_ocupacion_entry)

        form_layout.addRow(h_layout2)

        # Crear un layout horizontal para los campos en una misma línea
        h_layout3 = QHBoxLayout()

        self.lugar_nacimiento_entry = QLineEdit()
        self.lugar_nacimiento_entry.setMaxLength(255)
        self.lugar_nacimiento_entry.setFixedWidth(100)
        self.lugar_nacimiento_entry.textChanged.connect(self.convert_to_uppercase)
        h_layout3.addWidget(QLabel("Lugar de Nacimiento:"))
        h_layout3.addWidget(self.lugar_nacimiento_entry)

        self.religion_entry = QLineEdit()
        self.religion_entry.setMaxLength(20)
        self.religion_entry.setFixedWidth(100)
        self.religion_entry.textChanged.connect(self.convert_to_uppercase)
        h_layout3.addWidget(QLabel("Religión:"))
        h_layout3.addWidget(self.religion_entry)

        self.nombre_apellido_emergencia_entry = QLineEdit()
        self.nombre_apellido_emergencia_entry.setMaxLength(255)
        self.nombre_apellido_emergencia_entry.setFixedWidth(150)
        self.nombre_apellido_emergencia_entry.textChanged.connect(self.convert_to_uppercase)
        h_layout3.addWidget(QLabel("Familiar de Emergencia:"))
        h_layout3.addWidget(self.nombre_apellido_emergencia_entry)

        self.telefono_emergencia_entry = QLineEdit()
        self.telefono_emergencia_entry.setMaxLength(20)
        self.telefono_emergencia_entry.setFixedWidth(100)
        self.telefono_emergencia_entry.textChanged.connect(self.convert_to_uppercase)
        h_layout3.addWidget(QLabel("Teléfono de Emergencia:"))
        h_layout3.addWidget(self.telefono_emergencia_entry)

        self.parentesco_entry = QLineEdit()
        self.parentesco_entry.setMaxLength(20)
        self.parentesco_entry.setFixedWidth(100)
        self.parentesco_entry.textChanged.connect(self.convert_to_uppercase)
        h_layout3.addWidget(QLabel("Parentesco:"))
        h_layout3.addWidget(self.parentesco_entry)

        form_layout.addRow(h_layout3)

        # Crear un layout horizontal para los campos en una misma línea
        h_layout4 = QHBoxLayout()

        self.direccion_entry = QLineEdit()
        self.direccion_entry.setMaxLength(255)
        self.direccion_entry.setFixedWidth(280)
        self.direccion_entry.textChanged.connect(self.convert_to_uppercase)
        h_layout4.addWidget(QLabel("Dirección:"))
        h_layout4.addWidget(self.direccion_entry)

        self.temperatura_entry = QLineEdit()
        self.temperatura_entry.setValidator(QDoubleValidator(0, 100, 2))
        self.temperatura_entry.setFixedWidth(50)
        self.temperatura_entry.setPlaceholderText("Temp")
        h_layout4.addWidget(self.temperatura_entry)

        self.pulso_entry = QLineEdit()
        self.pulso_entry.setValidator(QIntValidator(0, 300))
        self.pulso_entry.setFixedWidth(50)
        self.pulso_entry.setPlaceholderText("Pulso")
        h_layout4.addWidget(self.pulso_entry)

        self.respiracion_entry = QLineEdit()
        self.respiracion_entry.setValidator(QIntValidator(0, 100))
        self.respiracion_entry.setFixedWidth(80)
        self.respiracion_entry.setPlaceholderText("Respiración")
        h_layout4.addWidget(self.respiracion_entry)

        self.frecuencia_cardiaca_entry = QLineEdit()
        self.frecuencia_cardiaca_entry.setValidator(QIntValidator(0, 300))
        self.frecuencia_cardiaca_entry.setFixedWidth(90)
        self.frecuencia_cardiaca_entry.setPlaceholderText("Ritmo Cardíaco")
        h_layout4.addWidget(self.frecuencia_cardiaca_entry)

        self.tension_arterial_maxima_entry = QLineEdit()
        self.tension_arterial_maxima_entry.setValidator(QIntValidator(0, 300))
        self.tension_arterial_maxima_entry.setFixedWidth(100)
        self.tension_arterial_maxima_entry.setPlaceholderText("Tensión Máxima")
        h_layout4.addWidget(self.tension_arterial_maxima_entry)

        self.tension_arterial_minima_entry = QLineEdit()
        self.tension_arterial_minima_entry.setValidator(QIntValidator(0, 300))
        self.tension_arterial_minima_entry.setFixedWidth(100)
        self.tension_arterial_minima_entry.setPlaceholderText("Tensión Mínima")
        h_layout4.addWidget(self.tension_arterial_minima_entry)

        self.peso_entry = QLineEdit()
        self.peso_entry.setValidator(QDoubleValidator(0, 500, 2))
        self.peso_entry.setFixedWidth(45)
        self.peso_entry.setPlaceholderText("Peso")
        h_layout4.addWidget(self.peso_entry)

        self.talla_entry = QLineEdit()
        self.talla_entry.setValidator(QDoubleValidator(0, 3, 2))
        self.talla_entry.setFixedWidth(40)
        self.talla_entry.setPlaceholderText("Talla")
        h_layout4.addWidget(self.talla_entry)

        self.grasa_corporal_entry = QLineEdit()
        self.grasa_corporal_entry.setValidator(QDoubleValidator(0, 100, 2))
        self.grasa_corporal_entry.setFixedWidth(95)
        self.grasa_corporal_entry.setPlaceholderText("Grasa Corporal")
        h_layout4.addWidget(self.grasa_corporal_entry)

        self.indice_masa_corporal_entry = QLineEdit()
        self.indice_masa_corporal_entry.setValidator(QDoubleValidator(0, 100, 2))
        self.indice_masa_corporal_entry.setFixedWidth(95)
        self.indice_masa_corporal_entry.setPlaceholderText("Masa Corporal")
        h_layout4.addWidget(self.indice_masa_corporal_entry)

        form_layout.addRow(h_layout4)

        self.motivo_consulta_entry = QTextEdit()
        self.motivo_consulta_entry.setFixedWidth(1020)
        form_layout.addRow(QLabel("Motivo de Consulta:"), self.motivo_consulta_entry)

        self.enfermedad_actual_entry = QTextEdit()
        self.enfermedad_actual_entry.setFixedWidth(1020)
        form_layout.addRow(QLabel("Enfermedad Actual:"), self.enfermedad_actual_entry)

        self.diagnostico_admision_entry = QTextEdit()
        self.diagnostico_admision_entry.setFixedWidth(1020)
        form_layout.addRow(QLabel("Diagnóstico de<br>Admisión:"), self.diagnostico_admision_entry)

        self.intervencion_tratamiento_entry = QTextEdit()
        self.intervencion_tratamiento_entry.setFixedWidth(1020)
        form_layout.addRow(QLabel("Intervención y/o <br>Tratamiento:"), self.intervencion_tratamiento_entry)

        self.diagnostico_final_entry = QTextEdit()
        self.diagnostico_final_entry.setFixedWidth(1020)
        form_layout.addRow(QLabel("Diagnóstico Final:"), self.diagnostico_final_entry)

        h_layout5 = QHBoxLayout()

        self.estado_actual_entry = QComboBox()
        self.estado_actual_entry.addItems(["Seleccione", "Mejora", "Ingreso", "Muerte"])
        self.estado_actual_entry.setFixedWidth(100)
        self.estado_actual_entry.currentIndexChanged.connect(self.update_autopsia_state)  # Conectar la señal
        h_layout5.addWidget(QLabel("Estado Actual:"))
        h_layout5.addWidget(self.estado_actual_entry)

        self.autopsia_entry = QComboBox()
        self.autopsia_entry.addItems(["Seleccione", "Si", "No"])
        self.autopsia_entry.setFixedWidth(100)
        self.autopsia_entry.setEnabled(False)  # Deshabilitar inicialmente
        h_layout5.addWidget(QLabel("Autopsia Pedida:"))
        h_layout5.addWidget(self.autopsia_entry)

        self.fecha_alta_entry = QDateEdit(QDate.currentDate())  # Establecer la fecha actual
        self.fecha_alta_entry.setCalendarPopup(True)
        self.fecha_alta_entry.setFixedWidth(100)
        h_layout5.addWidget(QLabel("Fecha de Alta:"))
        h_layout5.addWidget(self.fecha_alta_entry)

        self.hora_alta_entry = QLineEdit(QTime.currentTime().toString("HH:mm"))  # Establecer la hora actual
        self.hora_alta_entry.setFixedWidth(100)
        h_layout5.addWidget(QLabel("Hora de Alta:"))
        h_layout5.addWidget(self.hora_alta_entry)

          # Agregar un espaciador para empujar la hora a la izquierda
        h_layout5.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        form_layout.addRow(h_layout5)

        # Crear un layout horizontal para los botones en la parte inferior
        button_layout = QHBoxLayout()
    
        # Botón "Historia Clínica" en la esquina inferior izquierda
        self.historia_clinica_button = QPushButton("Historia Clínica")
        self.historia_clinica_button.setIcon(QIcon("iconos/historial.png"))  # Establecer la imagen del botón
        self.historia_clinica_button.setIconSize(QSize(24, 24))  # Ajustar el tamaño de la imagen
        self.historia_clinica_button.setFixedSize(150, 40)  # Ajustar el tamaño del botón
        self.historia_clinica_button.clicked.connect(self.open_historia_clinica)  # Conectar la señal
        button_layout.addWidget(self.historia_clinica_button, alignment=Qt.AlignLeft)

        # Espaciador para empujar los botones hacia las esquinas
        button_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Botón "Atrás" en la esquina inferior derecha
        self.back_button = QPushButton("Atrás")
        self.back_button.setIcon(QIcon("iconos/atras.png"))  # Establecer la imagen del botón
        self.back_button.setIconSize(QSize(24, 24))  # Ajustar el tamaño de la imagen
        self.back_button.setFixedSize(100, 40)  # Ajustar el tamaño del botón
        self.back_button.clicked.connect(self.go_back)
        button_layout.addWidget(self.back_button, alignment=Qt.AlignRight)

        # Botón "Guardar" en la esquina inferior derecha
        self.save_button = QPushButton("Guardar")
        self.save_button.setIcon(QIcon("iconos/guardar.png"))  # Establecer la imagen del botón
        self.save_button.setIconSize(QSize(24, 24))  # Ajustar el tamaño de la imagen
        self.save_button.setFixedSize(100, 40)  # Ajustar el tamaño del botón
        self.save_button.clicked.connect(self.save_data)
        button_layout.addWidget(self.save_button, alignment=Qt.AlignRight)

        layout.addLayout(button_layout)

        # Conectar la señal de datos cargados
        self.historia_clinica_window = MainWindow()
        self.historia_clinica_window.datos_cargados.connect(self.recibir_datos_historia_clinica)

    def go_back(self):
        self.parent.show_main_menu()

    def update_age_paciente(self):
        birthdate = self.fecha_nacimiento_entry.date().toPython()
        age = calculate_age(birthdate)
        self.age_label_paciente.setText(str(age))

    def update_autopsia_state(self):
        if self.estado_actual_entry.currentText() == "Muerte":
            self.autopsia_entry.setEnabled(True)
        else:
            self.autopsia_entry.setEnabled(False)

    def open_historia_clinica(self):
        self.historia_clinica_window.show()

    def recibir_datos_historia_clinica(self, datos):
        for i, (campo, valor) in enumerate(datos.items(), start=1):
            if hasattr(self, campo):
                print(f"{i}. Recibiendo {campo}: {valor}")  # Depuración
                widget = getattr(self, campo)
                if isinstance(widget, QLineEdit):
                    widget.setText(valor.upper())
                elif isinstance(widget, QComboBox):
                    index = widget.findText(valor, Qt.MatchFixedString)
                    if index >= 0:
                        widget.setCurrentIndex(index)
                elif isinstance(widget, QTextEdit):
                    widget.setPlainText(valor.upper())
        self.datos_historia_clinica_cargados = True  # Activar la bandera cuando se carguen los datos

    def convert_to_uppercase(self, text):
        sender = self.sender()
        sender.setText(text.upper())

    def save_data(self):
        
        # Recopilar datos del formulario y convertir a mayúsculas
        paciente_data = {
            "cedula": self.cedula_entry.text().upper(),
            "primer_nombre": self.primer_nombre_entry.text().upper(),
            "segundo_nombre": self.segundo_nombre_entry.text().upper(),
            "primer_apellido": self.primer_apellido_entry.text().upper(),
            "segundo_apellido": self.segundo_apellido_entry.text().upper(),
            "fecha_nacimiento": self.fecha_nacimiento_entry.date().toString("yyyy-MM-dd"),
            "telefono": self.telefono_entry.text().upper(),
            "genero": self.genero_entry.currentText(),
            "estado_civil": self.estado_civil_entry.currentText(),
            "nacionalidad": self.nacionalidad_entry.text().upper(),
            "profesion_ocupacion": self.profesion_ocupacion_entry.text().upper(),
            "lugar_nacimiento": self.lugar_nacimiento_entry.text().upper(),
            "religion": self.religion_entry.text().upper(),
            "nombre_apellido_emergencia": self.nombre_apellido_emergencia_entry.text().upper(),
            "telefono_emergencia": self.telefono_emergencia_entry.text().upper(),
            "parentesco": self.parentesco_entry.text().upper(),
            "direccion": self.direccion_entry.text().upper()  # Agregar el campo direccion
        }

        # Verificar campos obligatorios
        campos_obligatorios = ["cedula", "primer_nombre", "primer_apellido", "fecha_nacimiento", "telefono", "genero", "estado_civil", "nacionalidad", "profesion_ocupacion", "lugar_nacimiento", "religion", "nombre_apellido_emergencia", "telefono_emergencia", "parentesco", "direccion"]
        campos_faltantes = [campo for campo in campos_obligatorios if not paciente_data[campo]]

        if campos_faltantes:
            QMessageBox.warning(self, "Campos Obligatorios Faltantes", f"Por favor complete los siguientes campos obligatorios: {', '.join(campos_faltantes)}")
            return

        paciente_cedula = paciente_data["cedula"]

        historia_clinica_personal_data = {
            "temperatura": self.temperatura_entry.text(),
            "pulso": self.pulso_entry.text(),
            "respiracion": self.respiracion_entry.text(),
            "frecuencia_cardiaca": self.frecuencia_cardiaca_entry.text(),
            "tension_arterial_maxima": self.tension_arterial_maxima_entry.text(),
            "tension_arterial_minima": self.tension_arterial_minima_entry.text(),
            "peso": self.peso_entry.text(),
            "talla": self.talla_entry.text(),
            "grasa_corporal": self.grasa_corporal_entry.text(),
            "indice_masa_corporal": self.indice_masa_corporal_entry.text(),
            "motivo_consulta": self.motivo_consulta_entry.toPlainText(),
            "enfermedad_actual": self.enfermedad_actual_entry.toPlainText(),
            "diagnostico_admision": self.diagnostico_admision_entry.toPlainText(),
            "intervencion_tratamiento": self.intervencion_tratamiento_entry.toPlainText(),
            "diagnostico_final": self.diagnostico_final_entry.toPlainText(),
            "estado_actual": self.estado_actual_entry.currentText(),
            "autopsia_pedida": self.autopsia_entry.currentText(),
            "fecha_alta": self.fecha_alta_entry.date().toString("yyyy-MM-dd"),
            "hora_alta": self.hora_alta_entry.text(),
            "adenitis": self.adenitis_entry.text(),
            "alergia_p": self.alergia_p_entry.text(),
            "amigdalitis": self.amigdalitis_entry.text(),
            "artritis_p": self.artritis_p_entry.text(),
            "asma": self.asma_entry.text(),
            "bilharziasis": self.bilharziasis_entry.text(),
            "blenorragia": self.blenorragia_entry.text(),
            "bronquitis": self.bronquitis_entry.text(),
            "buba": self.buba_entry.text(),
            "catarros": self.catarros_entry.text(),
            "chagas": self.chagas_entry.text(),
            "chancros": self.chancros_entry.text(),
            "difteria": self.difteria_entry.text(),
            "diarreas": self.diarreas_entry.text(),
            "hansen": self.hansen_entry.text(),
            "influenzas": self.influenzas_entry.text(),
            "lechina": self.lechina_entry.text(),
            "necatoriasis": self.necatoriasis_entry.text(),
            "neumonia": self.neumonia_entry.text(),
            "otitis": self.otitis_entry.text(),
            "paludismo": self.paludismo_entry.text(),
            "parasitos": self.parasitos_entry.text(),
            "parotiditis": self.parotiditis_entry.text(),
            "pleuresia": self.pleuresia_entry.text(),
            "quirurgicos": self.quirurgicos_entry.text(),
            "rinolangititis": self.rinolangititis_entry.text(),
            "rubeola": self.rubeola_entry.text(),
            "sarampion": self.sarampion_entry.text(),
            "sifilis_p": self.sifilis_p_entry.text(),
            "sindrome_disentericos": self.sindrome_disentericos_entry.text(),
            "tuberculosis_p": self.tuberculosis_p_entry.text(),
            "tifoidea": self.tifoidea_entry.text(),
            "traumatismos": self.traumatismos_entry.text(),
            "vacunaciones": self.vacunaciones_entry.text(),
            "otros": self.otros_entry.text(),
            "aumento_de_peso": self.aumento_de_peso_entry.text(),
            "fiebre": self.fiebre_entry.text(),
            "nutricion": self.nutricion_entry.text(),
            "perdida_de_peso": self.perdida_de_peso_entry.text(),
            "sudores_nocturnos": self.sudores_nocturnos_entry.text(),
            "temblores": self.temblores_entry.text(),
            "otros_4_7": self.otros_4_7_entry.text(),
            "alergia": self.alergia_entry.text(),
            "artritis": self.artritis_entry.text(),
            "cancer": self.cancer_entry.text(),
            "cardio_vasculares": self.cardio_vasculares_entry.text(),
            "diabetes": self.diabetes_entry.text(),
            "enf_digestivas": self.enf_digestivas_entry.text(),
            "enf_renales": self.enf_renales_entry.text(),
            "intoxicaciones": self.intoxicaciones_entry.text(),
            "neuromentales": self.neuromentales_entry.text(),
            "sifilis": self.sifilis_entry.text(),
            "tuberculosis": self.tuberculosis_entry.text(),
            "otros_2_12": self.otros_2_12_entry.text(),
            "alcohol": self.alcohol_entry.text(),
            "chimo": self.chimo_entry.text(),
            "deportes": self.deportes_entry.text(),
            "drogas": self.drogas_entry.text(),
            "ocupacion": self.ocupacion_entry.text(),
            "problemas_familiares": self.problemas_familiares_entry.text(),
            "rasgos_personales": self.rasgos_personales_entry.text(),
            "sexuales": self.sexuales_entry.text(),
            "siesta": self.siesta_entry.text(),
            "sueño": self.sueño_entry.text(),
            "tabaco": self.tabaco_entry.text(),
            "otros_3_10": self.otros_3_10_entry.text()
        }

        historia_clinica_personal1_data = {
            "color": self.color_entry.text(),
            "humedad": self.humedad_entry.text(),
            "contextura": self.contextura_entry.text(),
            "temperatura": self.temperatura_entry_1.text(),
            "pigmentacion": self.pigmentacion_entry.text(),
            "equimosis": self.equimosis_entry.text(),
            "cianosis": self.cianosis_entry.text(),
            "petequias": self.petequias_entry.text(),
            "erupcion": self.erupcion_entry.text(),
            "unas": self.unas_entry.text(),
            "nobulos": self.nobulos_entry.text(),
            "vascularizacion": self.vascularizacion_entry.text(),
            "cicatrices": self.cicatrices_entry.text(),
            "fistulas": self.fistulas_entry.text(),
            "ulceras": self.ulceras_entry.text(),
            "otros_1_16": self.otros_1_16_entry.text(),
            "configuracion": self.configuracion_entry.text(),
            "fontanelas": self.fontanelas_entry.text(),
            "reblandecimiento": self.reblandecimiento_entry.text(),
            "circunferencia": self.circunferencia_entry.text(),
            "dolor_de_cabeza": self.dolor_de_cabeza_entry.text(),
            "cabellos": self.cabellos_entry.text(),
            "otros_2_7": self.otros_2_7_entry.text(),
            "conjuntiva": self.conjuntiva_entry.text(),
            "esclerotica": self.esclerotica_entry.text(),
            "cornea": self.cornea_entry.text(),
            "pupilas": self.pupilas_entry.text(),
            "movimiento": self.movimiento_entry.text(),
            "desviacion": self.desviacion_entry.text(),
            "nistagmus": self.nistagmus_entry.text(),
            "ptosis": self.ptosis_entry.text(),
            "exoftalmos": self.exoftalmos_entry.text(),
            "agudeza_visual": self.agudeza_visual_entry.text(),
            "oftalmoscopicos": self.oftalmoscopicos_entry.text(),
            "otros_3_12": self.otros_3_12_entry.text(),
            "pabellon": self.pabellon_entry.text(),
            "conducto_extremo": self.conducto_extremo_entry.text(),
            "timpano": self.timpano_entry.text(),
            "audicion": self.audicion_entry.text(),
            "secreciones": self.secreciones_entry.text(),
            "mastoides": self.mastoides_entry.text(),
            "dolor_de_oido": self.dolor_de_oido_entry.text(),
            "otros_4_8": self.otros_4_8_entry.text(),
            "fosas_nasales": self.fosas_nasales_entry.text(),
            "mucosas": self.mucosas_entry.text(),
            "tabique": self.tabique_entry.text(),
            "meatos": self.meatos_entry.text(),
            "diafanoscopia": self.diafanoscopia_entry.text(),
            "sensibilidad_de_los_senos": self.sensibilidad_de_los_senos_entry.text(),
            "secrecion_nasal": self.secrecion_nasal_entry.text(),
            "otros_5_8": self.otros_5_8_entry.text(),
            "aliento": self.aliento_entry.text(),
            "labios": self.labios_entry.text(),
            "dientes": self.dientes_entry.text(),
            "encias": self.encias_entry.text(),
            "mucosas_bucales": self.mucosas_bucales_entry.text(),
            "lengua": self.lengua_entry.text(),
            "conductos_salivales": self.conductos_salivales_entry.text(),
            "paralisis_y_trismo": self.paralisis_y_trismo_entry.text(),
            "otros_6_9": self.otros_6_9_entry.text(),
            "amigdalas": self.amigdalas_entry.text(),
            "adenoides": self.adenoides_entry.text(),
            "rino_faringe": self.rino_faringe_entry.text(),
            "disfagia": self.disfagia_entry.text(),
            "dolor_de_la_faringe": self.dolor_de_la_faringe_entry.text(),
            "otros_7_6": self.otros_7_6_entry.text(),
            "movilidad": self.movilidad_entry.text(),
            "ganglios": self.ganglios_entry.text(),
            "tiroides": self.tiroides_entry.text(),
            "vasos": self.vasos_entry.text(),
            "traquea": self.traquea_entry.text(),
            "otros_8_6": self.otros_8_6_entry.text(),
            "cervicales": self.cervicales_entry.text(),
            "occipitales": self.occipitales_entry.text(),
            "supraclaviculares": self.supraclaviculares_entry.text(),
            "axilares": self.axilares_entry.text(),
            "epitrocleares": self.epitrocleares_entry.text(),
            "inguinales": self.inguinales_entry.text(),
            "otros_9_7": self.otros_9_7_entry.text(),
            "forma": self.forma_entry.text(),
            "simetria": self.simetria_entry.text(),
            "expansion": self.expansion_entry.text(),
            "palpitacion": self.palpitacion_entry.text(),
            "respiracion": self.respiracion_entry_2.text(),
            "otros_10_6": self.otros_10_6_entry.text(),
            "nodulos": self.nodulos_entry.text(),
            "secreciones_pecho": self.secreciones_pecho_entry.text(),
            "pezones": self.pezones_entry.text(),
            "otros_11_4": self.otros_11_4_entry.text(),
            "fremito": self.fremito_entry.text(),
            "percusion": self.percusion_entry.text(),
            "auscultacion": self.auscultacion_entry.text(),
            "ruidos_adventicios": self.ruidos_adventicios_entry.text(),
            "pectoriloquia_afona": self.pectoriloquia_afona_entry.text(),
            "broncofonia": self.broncofonia_entry.text(),
            "otros_12_7": self.otros_12_7_entry.text(),
            "latidos_de_la_punta": self.latidos_de_la_punta_entry.text(),
            "thrill": self.thrill_entry.text(),
            "pulsacion": self.pulsacion_entry.text(),
            "ritmo": self.ritmo_entry.text(),
            "ruidos": self.ruidos_entry.text(),
            "galopes": self.galopes_entry.text(),
            "frotes": self.frotes_entry.text(),
            "otros_13_8": self.otros_13_8_entry.text()
        }

        # Depuración de datos de historia clínica personal 1
        print("Datos de Historia Clínica Personal 1:")
        for i, (campo, valor) in enumerate(historia_clinica_personal1_data.items(), start=1):
            print(f"{i}. {campo}: {valor}")

        historia_clinica_personal2_data = {
            "pulso_h": self.pulso_h_entry.text(),
            "paredes_vasculares": self.paredes_vasculares_entry.text(),
            "caracteres": self.caracteres_entry.text(),
            "otros_14_4": self.otros_14_4_entry.text(),
            "aspecto": self.aspecto_entry.text(),
            "circunferencia_abdomen": self.circunferencia_abdomen_entry.text(),
            "peristalsis": self.peristalsis_entry.text(),
            "cicatrices_abdomen": self.cicatrices_abdomen_entry.text(),
            "defensa": self.defensa_entry.text(),
            "sensibilidad_abdomen": self.sensibilidad_abdomen_entry.text(),
            "contracturas": self.contracturas_entry.text(),
            "tumoraciones": self.tumoraciones_entry.text(),
            "ascitis": self.ascitis_entry.text(),
            "higado": self.higado_entry.text(),
            "rinones": self.rinones_entry.text(),
            "bazo": self.bazo_entry.text(),
            "hernias": self.hernias_entry.text(),
            "otros_15_14": self.otros_15_14_entry.text(),
            "cicatrices_genitales": self.cicatrices_genitales_entry.text(),
            "lesiones": self.lesiones_entry.text(),
            "secreciones_genitales": self.secreciones_genitales_entry.text(),
            "escroto": self.escroto_entry.text(),
            "epididimo": self.epididimo_entry.text(),
            "deferentes": self.deferentes_entry.text(),
            "testiculos": self.testiculos_entry.text(),
            "prostata": self.prostata_entry.text(),
            "seminales": self.seminales_entry.text(),
            "otros_16_10": self.otros_16_10_entry.text(),
            "labios_genitales": self.labios_genitales_entry.text(),
            "bartholino": self.bartholino_entry.text(),
            "perine": self.perine_entry.text(),
            "vagina": self.vagina_entry.text(),
            "cuello": self.cuello_entry.text(),
            "utero": self.utero_entry.text(),
            "anexos": self.anexos_entry.text(),
            "parametrico": self.parametrico_entry.text(),
            "saco_de_douglas": self.saco_de_douglas_entry.text(),
            "otros_17_10": self.otros_17_10_entry.text(),
            "fisuras": self.fisuras_entry.text(),
            "fistula_anal": self.fistula_anal_entry.text(),
            "hemorroides": self.hemorroides_entry.text(),
            "esfinter": self.esfinter_entry.text(),
            "tumoraciones_anales": self.tumoraciones_anales_entry.text(),
            "prolapso": self.prolapso_entry.text(),
            "heces": self.heces_entry.text(),
            "otros_18_8": self.otros_18_8_entry.text(),
            "deformidades": self.deformidades_entry.text(),  # Nueva entrada
            "inflamaciones": self.inflamaciones_entry.text(),  # Nueva entrada
            "rubicindes": self.rubicindes_entry.text(),  # Nueva entrada
            "sensibilidad_muscular": self.sensibilidad_muscular_entry.text(),  # Nueva entrada
            "movimientos": self.movimientos_entry.text(),  # Nueva entrada
            "masas_musculares": self.masas_musculares_entry.text(),  # Nueva entrada
            "otros_19_7": self.otros_19_7_entry.text(),  # Nueva entrada
            "color_piel": self.color_piel_entry.text(),  # Nueva entrada
            "edema": self.edema_entry.text(),  # Nueva entrada
            "temblor": self.temblor_entry.text(),  # Nueva entrada
            "deformidades_piel": self.deformidades_piel_entry.text(),  # Nueva entrada
            "ulceras_piel": self.ulceras_piel_entry.text(),  # Nueva entrada
            "varices": self.varices_entry.text(),  # Nueva entrada
            "otros_20_7": self.otros_20_7_entry.text(),  # Nueva entrada
            "sensibilidad_objetiva": self.sensibilidad_objetiva_entry.text(),
            "motilidad": self.motilidad_entry.text(),
            "reflectividad": self.reflectividad_entry.text(),
            "escritura": self.escritura_entry.text(),
            "troficos": self.troficos_entry.text(),
            "marcha": self.marcha_entry.text(),
            "romberg": self.romberg_entry.text(),
            "orientacion": self.orientacion_entry.text(),
            "lenguaje": self.lenguaje_entry.text(),
            "coordinacion": self.coordinacion_entry.text(),
            "otros_21_11": self.otros_21_11_entry.text()
        }

        # Depuración de datos de historia clínica personal 2
        print("Datos de Historia Clínica Personal 2:")
        for i, (campo, valor) in enumerate(historia_clinica_personal2_data.items(), start=1):
            print(f"{i}. {campo}: {valor}")
        
        # Conectar a la base de datos y guardar los datos
        db = CreateConnection()
        connection = db.create_connection()
        if connection:
            try:
                cursor = connection.cursor()

                # Guardar datos en la tabla pacientes
                query_paciente = """
                    INSERT INTO pacientes (cedula, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, fecha_nacimiento, telefono, genero, estado_civil, nacionalidad, profesion_ocupacion, lugar_nacimiento, religion, nombre_apellido_emergencia, telefono_emergencia, parentesco, direccion)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query_paciente, (
                    paciente_data["cedula"], paciente_data["primer_nombre"], paciente_data["segundo_nombre"], paciente_data["primer_apellido"], paciente_data["segundo_apellido"],
                    paciente_data["fecha_nacimiento"], paciente_data["telefono"], paciente_data["genero"], paciente_data["estado_civil"], paciente_data["nacionalidad"], paciente_data["profesion_ocupacion"],
                    paciente_data["lugar_nacimiento"], paciente_data["religion"], paciente_data["nombre_apellido_emergencia"], paciente_data["telefono_emergencia"], paciente_data["parentesco"], paciente_data["direccion"]
                ))

                # Guardar datos en la tabla HistoriaClinicaPersonal
                query_historia_clinica_personal = """
                    INSERT INTO historia_clinica_personal (paciente_cedula, temperatura, pulso, respiracion, frecuencia_cardiaca, tension_arterial_maxima, tension_arterial_minima, peso, talla, grasa_corporal, indice_masa_corporal, motivo_consulta, enfermedad_actual, diagnostico_admision, intervencion_tratamiento, diagnostico_final, estado_actual, autopsia_pedida, fecha_alta, hora_alta, adenitis, alergia_p, amigdalitis, artritis_p, asma, bilharziasis, blenorragia, bronquitis, buba, catarros, chagas, chancros, difteria, diarreas, hansen, influenzas, lechina, necatoriasis, neumonia, otitis, paludismo, parasitos, parotiditis, pleuresia, quirurgicos, rinolangititis, rubeola, sarampion, sifilis_p, sindrome_disentericos, tuberculosis_p, tifoidea, traumatismos, vacunaciones, otros, aumento_de_peso, fiebre, nutricion, perdida_de_peso, sudores_nocturnos, temblores, otros_4_7, alergia, artritis, cancer, cardio_vasculares, diabetes, enf_digestivas, enf_renales, intoxicaciones, neuromentales, sifilis, tuberculosis, otros_2_12, alcohol, chimo, deportes, drogas, ocupacion, problemas_familiares, rasgos_personales, sexuales, siesta, sueño, tabaco, otros_3_10)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query_historia_clinica_personal, (
                    paciente_cedula, historia_clinica_personal_data["temperatura"], historia_clinica_personal_data["pulso"], historia_clinica_personal_data["respiracion"], historia_clinica_personal_data["frecuencia_cardiaca"], historia_clinica_personal_data["tension_arterial_maxima"],
                    historia_clinica_personal_data["tension_arterial_minima"], historia_clinica_personal_data["peso"], historia_clinica_personal_data["talla"], historia_clinica_personal_data["grasa_corporal"], historia_clinica_personal_data["indice_masa_corporal"],
                    historia_clinica_personal_data["motivo_consulta"], historia_clinica_personal_data["enfermedad_actual"], historia_clinica_personal_data["diagnostico_admision"], historia_clinica_personal_data["intervencion_tratamiento"], historia_clinica_personal_data["diagnostico_final"],
                    historia_clinica_personal_data["estado_actual"], historia_clinica_personal_data["autopsia_pedida"], historia_clinica_personal_data["fecha_alta"], historia_clinica_personal_data["hora_alta"],
                    historia_clinica_personal_data["adenitis"], historia_clinica_personal_data["alergia_p"], historia_clinica_personal_data["amigdalitis"], historia_clinica_personal_data["artritis_p"], historia_clinica_personal_data["asma"], historia_clinica_personal_data["bilharziasis"],
                    historia_clinica_personal_data["blenorragia"], historia_clinica_personal_data["bronquitis"], historia_clinica_personal_data["buba"], historia_clinica_personal_data["catarros"], historia_clinica_personal_data["chagas"], historia_clinica_personal_data["chancros"],
                    historia_clinica_personal_data["difteria"], historia_clinica_personal_data["diarreas"], historia_clinica_personal_data["hansen"], historia_clinica_personal_data["influenzas"], historia_clinica_personal_data["lechina"], historia_clinica_personal_data["necatoriasis"],
                    historia_clinica_personal_data["neumonia"], historia_clinica_personal_data["otitis"], historia_clinica_personal_data["paludismo"], historia_clinica_personal_data["parasitos"], historia_clinica_personal_data["parotiditis"], historia_clinica_personal_data["pleuresia"],
                    historia_clinica_personal_data["quirurgicos"], historia_clinica_personal_data["rinolangititis"], historia_clinica_personal_data["rubeola"], historia_clinica_personal_data["sarampion"], historia_clinica_personal_data["sifilis_p"], historia_clinica_personal_data["sindrome_disentericos"],
                    historia_clinica_personal_data["tuberculosis_p"], historia_clinica_personal_data["tifoidea"], historia_clinica_personal_data["traumatismos"], historia_clinica_personal_data["vacunaciones"], historia_clinica_personal_data["otros"], historia_clinica_personal_data["aumento_de_peso"],
                    historia_clinica_personal_data["fiebre"], historia_clinica_personal_data["nutricion"], historia_clinica_personal_data["perdida_de_peso"], historia_clinica_personal_data["sudores_nocturnos"], historia_clinica_personal_data["temblores"], historia_clinica_personal_data["otros_4_7"],
                    historia_clinica_personal_data["alergia"], historia_clinica_personal_data["artritis"], historia_clinica_personal_data["cancer"], historia_clinica_personal_data["cardio_vasculares"], historia_clinica_personal_data["diabetes"], historia_clinica_personal_data["enf_digestivas"],
                    historia_clinica_personal_data["enf_renales"], historia_clinica_personal_data["intoxicaciones"], historia_clinica_personal_data["neuromentales"], historia_clinica_personal_data["sifilis"], historia_clinica_personal_data["tuberculosis"], historia_clinica_personal_data["otros_2_12"],
                    historia_clinica_personal_data["alcohol"], historia_clinica_personal_data["chimo"], historia_clinica_personal_data["deportes"], historia_clinica_personal_data["drogas"], historia_clinica_personal_data["ocupacion"], historia_clinica_personal_data["problemas_familiares"],
                    historia_clinica_personal_data["rasgos_personales"], historia_clinica_personal_data["sexuales"], historia_clinica_personal_data["siesta"], historia_clinica_personal_data["sueño"], historia_clinica_personal_data["tabaco"], historia_clinica_personal_data["otros_3_10"]
                ))

                query_historia_clinica_personal1 = """
                    INSERT INTO historia_clinica_personal1 (paciente_cedula, color, humedad, contextura, temperatura, pigmentacion, equimosis, cianosis, petequias, erupcion, unas, nobulos, vascularizacion, cicatrices, fistulas, ulceras, otros_1_16, configuracion, fontanelas, reblandecimiento, circunferencia, dolor_de_cabeza, cabellos, otros_2_7, conjuntiva, esclerotica, cornea, pupilas, movimiento, desviacion, nistagmus, ptosis, exoftalmos, agudeza_visual, oftalmoscopicos, otros_3_12, pabellon, conducto_extremo, timpano, audicion, secreciones, mastoides, dolor_de_oido, otros_4_8, fosas_nasales, mucosas, tabique, meatos, diafanoscopia, sensibilidad_de_los_senos, secrecion_nasal, otros_5_8, aliento, labios, dientes, encías, mucosas_bucales, lengua, conductos_salivales, paralisis_y_trismo, otros_6_9, amigdalas, adenoides, rino_faringe, disfagia, dolor_de_la_faringe, otros_7_6, movilidad, ganglios, tiroides, vasos, traquea, otros_8_6, cervicales, occipitales, supraclaviculares, axilares, epitrocleares, inguinales, otros_9_7, forma, simetria, expansion, palpitacion, respiracion, otros_10_6, nodulos, secreciones_pecho, pezones, otros_11_4, fremito, percusion, auscultacion, ruidos_adventicios, pectoriloquia_afona, broncofonia, otros_12_7, latidos_de_la_punta, thrill, pulsacion, ritmo, ruidos, galopes, frotes, otros_13_8)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """

                cursor.execute(query_historia_clinica_personal1, (
                    paciente_cedula, historia_clinica_personal1_data["color"], historia_clinica_personal1_data["humedad"], historia_clinica_personal1_data["contextura"], historia_clinica_personal1_data["temperatura"],
                    historia_clinica_personal1_data["pigmentacion"], historia_clinica_personal1_data["equimosis"], historia_clinica_personal1_data["cianosis"], historia_clinica_personal1_data["petequias"],
                    historia_clinica_personal1_data["erupcion"], historia_clinica_personal1_data["unas"], historia_clinica_personal1_data["nobulos"], historia_clinica_personal1_data["vascularizacion"],
                    historia_clinica_personal1_data["cicatrices"], historia_clinica_personal1_data["fistulas"], historia_clinica_personal1_data["ulceras"], historia_clinica_personal1_data["otros_1_16"],
                    historia_clinica_personal1_data["configuracion"], historia_clinica_personal1_data["fontanelas"], historia_clinica_personal1_data["reblandecimiento"], historia_clinica_personal1_data["circunferencia"],
                    historia_clinica_personal1_data["dolor_de_cabeza"], historia_clinica_personal1_data["cabellos"], historia_clinica_personal1_data["otros_2_7"], historia_clinica_personal1_data["conjuntiva"],
                    historia_clinica_personal1_data["esclerotica"], historia_clinica_personal1_data["cornea"], historia_clinica_personal1_data["pupilas"], historia_clinica_personal1_data["movimiento"],
                    historia_clinica_personal1_data["desviacion"], historia_clinica_personal1_data["nistagmus"], historia_clinica_personal1_data["ptosis"], historia_clinica_personal1_data["exoftalmos"],
                    historia_clinica_personal1_data["agudeza_visual"], historia_clinica_personal1_data["oftalmoscopicos"], historia_clinica_personal1_data["otros_3_12"], historia_clinica_personal1_data["pabellon"],
                    historia_clinica_personal1_data["conducto_extremo"], historia_clinica_personal1_data["timpano"], historia_clinica_personal1_data["audicion"], historia_clinica_personal1_data["secreciones"],
                    historia_clinica_personal1_data["mastoides"], historia_clinica_personal1_data["dolor_de_oido"], historia_clinica_personal1_data["otros_4_8"], historia_clinica_personal1_data["fosas_nasales"],
                    historia_clinica_personal1_data["mucosas"], historia_clinica_personal1_data["tabique"], historia_clinica_personal1_data["meatos"], historia_clinica_personal1_data["diafanoscopia"],
                    historia_clinica_personal1_data["sensibilidad_de_los_senos"], historia_clinica_personal1_data["secrecion_nasal"], historia_clinica_personal1_data["otros_5_8"],
                    historia_clinica_personal1_data["aliento"], historia_clinica_personal1_data["labios"], historia_clinica_personal1_data["dientes"], historia_clinica_personal1_data["encias"],
                    historia_clinica_personal1_data["mucosas_bucales"], historia_clinica_personal1_data["lengua"], historia_clinica_personal1_data["conductos_salivales"], historia_clinica_personal1_data["paralisis_y_trismo"],
                    historia_clinica_personal1_data["otros_6_9"], historia_clinica_personal1_data["amigdalas"], historia_clinica_personal1_data["adenoides"], historia_clinica_personal1_data["rino_faringe"],
                    historia_clinica_personal1_data["disfagia"], historia_clinica_personal1_data["dolor_de_la_faringe"], historia_clinica_personal1_data["otros_7_6"], historia_clinica_personal1_data["movilidad"],
                    historia_clinica_personal1_data["ganglios"], historia_clinica_personal1_data["tiroides"], historia_clinica_personal1_data["vasos"], historia_clinica_personal1_data["traquea"],
                    historia_clinica_personal1_data["otros_8_6"], historia_clinica_personal1_data["cervicales"], historia_clinica_personal1_data["occipitales"], historia_clinica_personal1_data["supraclaviculares"],
                    historia_clinica_personal1_data["axilares"], historia_clinica_personal1_data["epitrocleares"], historia_clinica_personal1_data["inguinales"], historia_clinica_personal1_data["otros_9_7"],
                    historia_clinica_personal1_data["forma"], historia_clinica_personal1_data["simetria"], historia_clinica_personal1_data["expansion"], historia_clinica_personal1_data["palpitacion"],
                    historia_clinica_personal1_data["respiracion"], historia_clinica_personal1_data["otros_10_6"], historia_clinica_personal1_data["nodulos"], historia_clinica_personal1_data["secreciones_pecho"],
                    historia_clinica_personal1_data["pezones"], historia_clinica_personal1_data["otros_11_4"], historia_clinica_personal1_data["fremito"], historia_clinica_personal1_data["percusion"],
                    historia_clinica_personal1_data["auscultacion"], historia_clinica_personal1_data["ruidos_adventicios"], historia_clinica_personal1_data["pectoriloquia_afona"], historia_clinica_personal1_data["broncofonia"],
                    historia_clinica_personal1_data["otros_12_7"], historia_clinica_personal1_data["latidos_de_la_punta"], historia_clinica_personal1_data["thrill"], historia_clinica_personal1_data["pulsacion"],
                    historia_clinica_personal1_data["ritmo"], historia_clinica_personal1_data["ruidos"], historia_clinica_personal1_data["galopes"], historia_clinica_personal1_data["frotes"],
                    historia_clinica_personal1_data["otros_13_8"]
                ))

                # Guardar datos en la tabla historia_clinica_personal2
                query_historia_clinica_personal2 = """
                    INSERT INTO historia_clinica_personal2 (paciente_cedula, pulso_h, paredes_vasculares, caracteres, otros_14_4, aspecto, circunferencia_abdomen, peristalsis, cicatrices_abdomen, defensa, sensibilidad_abdomen, contracturas, tumoraciones, ascitis, higado, rinones, bazo, hernias, otros_15_14, cicatrices_genitales, lesiones, secreciones_genitales, escroto, epididimo, deferentes, testiculos, prostata, seminales, otros_16_10, labios_genitales, bartholino, perine, vagina, cuello, utero, anexos, parametrico, saco_de_douglas, otros_17_10, fisuras, fistula_anal, hemorroides, esfinter, tumoraciones_anales, prolapso, heces, otros_18_8, deformidades, inflamaciones, rubicindes, sensibilidad_muscular, movimientos, masas_musculares, otros_19_7, color_piel, edema, temblor, deformidades_piel, ulceras_piel, varices, otros_20_7, sensibilidad_objetiva, motilidad, reflectividad, escritura, troficos, marcha, romberg, orientacion, lenguaje, coordinacion, otros_21_11)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """

                num_placeholders = query_historia_clinica_personal2.count('%s')
                print("Número de %s en query_historia_clinica_personal2:", num_placeholders)

                historia_clinica_personal2_values = (
                    paciente_cedula, historia_clinica_personal2_data["pulso_h"], historia_clinica_personal2_data["paredes_vasculares"], historia_clinica_personal2_data["caracteres"], historia_clinica_personal2_data["otros_14_4"],
                    historia_clinica_personal2_data["aspecto"], historia_clinica_personal2_data["circunferencia_abdomen"], historia_clinica_personal2_data["peristalsis"], historia_clinica_personal2_data["cicatrices_abdomen"],
                    historia_clinica_personal2_data["defensa"], historia_clinica_personal2_data["sensibilidad_abdomen"], historia_clinica_personal2_data["contracturas"], historia_clinica_personal2_data["tumoraciones"],
                    historia_clinica_personal2_data["ascitis"], historia_clinica_personal2_data["higado"], historia_clinica_personal2_data["rinones"], historia_clinica_personal2_data["bazo"],
                    historia_clinica_personal2_data["hernias"], historia_clinica_personal2_data["otros_15_14"], historia_clinica_personal2_data["cicatrices_genitales"], historia_clinica_personal2_data["lesiones"],
                    historia_clinica_personal2_data["secreciones_genitales"], historia_clinica_personal2_data["escroto"], historia_clinica_personal2_data["epididimo"], historia_clinica_personal2_data["deferentes"],
                    historia_clinica_personal2_data["testiculos"], historia_clinica_personal2_data["prostata"], historia_clinica_personal2_data["seminales"], historia_clinica_personal2_data["otros_16_10"],
                    historia_clinica_personal2_data["labios_genitales"], historia_clinica_personal2_data["bartholino"], historia_clinica_personal2_data["perine"], historia_clinica_personal2_data["vagina"],
                    historia_clinica_personal2_data["cuello"], historia_clinica_personal2_data["utero"], historia_clinica_personal2_data["anexos"], historia_clinica_personal2_data["parametrico"],
                    historia_clinica_personal2_data["saco_de_douglas"], historia_clinica_personal2_data["otros_17_10"], historia_clinica_personal2_data["fisuras"], historia_clinica_personal2_data["fistula_anal"],
                    historia_clinica_personal2_data["hemorroides"], historia_clinica_personal2_data["esfinter"], historia_clinica_personal2_data["tumoraciones_anales"], historia_clinica_personal2_data["prolapso"],
                    historia_clinica_personal2_data["heces"], historia_clinica_personal2_data["otros_18_8"], historia_clinica_personal2_data["deformidades"], historia_clinica_personal2_data["inflamaciones"],
                    historia_clinica_personal2_data["rubicindes"], historia_clinica_personal2_data["sensibilidad_muscular"], historia_clinica_personal2_data["movimientos"], historia_clinica_personal2_data["masas_musculares"],
                    historia_clinica_personal2_data["otros_19_7"], historia_clinica_personal2_data["color_piel"], historia_clinica_personal2_data["edema"], historia_clinica_personal2_data["temblor"],
                    historia_clinica_personal2_data["deformidades_piel"], historia_clinica_personal2_data["ulceras_piel"], historia_clinica_personal2_data["varices"], historia_clinica_personal2_data["otros_20_7"],
                    historia_clinica_personal2_data["sensibilidad_objetiva"], historia_clinica_personal2_data["motilidad"], historia_clinica_personal2_data["reflectividad"], historia_clinica_personal2_data["escritura"],
                    historia_clinica_personal2_data["troficos"], historia_clinica_personal2_data["marcha"], historia_clinica_personal2_data["romberg"], historia_clinica_personal2_data["orientacion"],
                    historia_clinica_personal2_data["lenguaje"], historia_clinica_personal2_data["coordinacion"], historia_clinica_personal2_data["otros_21_11"]
                )
                print("Datos insertados en historia_clinica_personal2:", historia_clinica_personal2_data)
                print("Consulta SQL ejecutada para historia_clinica_personal2:", cursor.statement)

                # Depuración: imprimir la consulta y los valores
                print("Query Historia Clinica Personal 2:", query_historia_clinica_personal2)
                print("Número de valores:", len(historia_clinica_personal2_values))
                print("Valores Historia Clinica Personal 2:", historia_clinica_personal2_values)

                cursor.execute(query_historia_clinica_personal2, historia_clinica_personal2_values)
                print("Datos insertados en historia_clinica_personal2:", historia_clinica_personal2_data)
                print("Consulta SQL ejecutada para historia_clinica_personal2:", cursor.statement)

                # Commit de los cambios
                connection.commit()

                # Mostrar un mensaje de éxito
                QMessageBox.information(self, "Éxito", "Datos guardados correctamente.")
            except Error as e:
                print(f"Error al guardar los datos: {e}")  # Imprimir el error en la consola
                QMessageBox.critical(self, "Error", f"Error al guardar los datos: {e}")
            finally:
                db.close_connection(connection)
        else:
            QMessageBox.critical(self, "Error", "No se pudo conectar a la base de datos.")