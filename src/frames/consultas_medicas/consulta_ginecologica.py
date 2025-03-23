from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QDateEdit, QComboBox, QFormLayout, QScrollArea, QToolButton, QFrame, QTableWidget, QTableWidgetItem, QAbstractScrollArea, QSpacerItem, QSizePolicy, QTextEdit, QMessageBox
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, Qt, QDate, QTime, QTimer
from utils import calculate_age  # Importar la función calcular_edad
from servicios import CreateConnection

class ConsultaGinecologica(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        # Crear un QScrollArea y un widget de contenido
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # Desactivar la barra de desplazamiento horizontal
        content_widget = QWidget()
        scroll_area.setWidget(content_widget)

        layout = QVBoxLayout(content_widget)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(scroll_area)

        form_layout = QFormLayout()
        layout.addLayout(form_layout)

        # Crear un layout horizontal para los campos en una misma línea
        h_layout1 = QHBoxLayout()
        h_layout1.setAlignment(Qt.AlignLeft)  # Alinear a la izquierda

        self.cedula_entry = QLineEdit()
        self.cedula_entry.setInputMask("00000000")  # Máscara de entrada para el formato (00000000)
        self.cedula_entry.setFixedWidth(80)
        self.cedula_entry.setPlaceholderText("Cédula")
        self.cedula_entry.textChanged.connect(self.mover_cursor_al_inicio)  # Conectar para mover el cursor al inicio
        self.cedula_entry.editingFinished.connect(self.verificar_cedula) # Conectar la señal editingFinished
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

        h_layout1.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        form_layout.addRow(h_layout1)

        # Crear un layout horizontal para los campos en una misma línea
        h_layout2 = QHBoxLayout()
        h_layout2.setAlignment(Qt.AlignLeft)  # Alinear a la izquierda

        self.fecha_nacimiento_entry = QDateEdit()
        self.fecha_nacimiento_entry.setCalendarPopup(True)
        self.fecha_nacimiento_entry.setFixedWidth(95)
        self.fecha_nacimiento_entry.dateChanged.connect(self.update_age_paciente)
        h_layout2.addWidget(QLabel("Fecha de Nacimiento:"))
        h_layout2.addWidget(self.fecha_nacimiento_entry)

        # Nuevo campo de teléfono
        self.telefono_entry = QLineEdit()
        self.telefono_entry.setInputMask("0000-0000000")  # Máscara de entrada para el formato (0000-0000000)
        self.telefono_entry.setMaxLength(12)
        self.telefono_entry.setFixedWidth(90)
        h_layout2.addWidget(QLabel("Teléfono:"))
        h_layout2.addWidget(self.telefono_entry)

        self.genero_entry = QComboBox()
        self.genero_entry.addItems(["Seleccione", "Masculino", "Femenino", "Otro"])
        self.genero_entry.setFixedWidth(80)
        h_layout2.addWidget(QLabel("Género:"))
        h_layout2.addWidget(self.genero_entry)

        self.estado_civil_entry = QComboBox()
        self.estado_civil_entry.addItems(["Seleccione", "Soltero", "Casado", "Viudo", "Divorciado"])
        self.estado_civil_entry.setFixedWidth(80)
        h_layout2.addWidget(QLabel("Estado Civil:"))
        h_layout2.addWidget(self.estado_civil_entry)

        self.nacionalidad_entry = QComboBox()
        self.nacionalidad_entry.addItems(["Seleccione", "Venezolana", "Extranjera"])
        self.nacionalidad_entry.setFixedWidth(85)
        h_layout2.addWidget(QLabel("Nacionalidad:"))
        h_layout2.addWidget(self.nacionalidad_entry)
        
        self.lugar_nacimiento_entry = QLineEdit()
        self.lugar_nacimiento_entry.setMaxLength(255)
        self.lugar_nacimiento_entry.setFixedWidth(95)
        self.lugar_nacimiento_entry.textChanged.connect(self.convert_to_uppercase)
        h_layout2.addWidget(QLabel("Lugar de Nacimiento:"))
        h_layout2.addWidget(self.lugar_nacimiento_entry)

        h_layout2.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        form_layout.addRow(h_layout2)

        # Crear un layout horizontal para los campos en una misma línea
        h_layout3 = QHBoxLayout()
        h_layout3.setAlignment(Qt.AlignLeft)  # Alinear a la izquierda

        self.profesion_ocupacion_entry = QLineEdit()
        self.profesion_ocupacion_entry.setMaxLength(100)
        self.profesion_ocupacion_entry.setFixedWidth(140)
        self.profesion_ocupacion_entry.textChanged.connect(self.convert_to_uppercase)
        h_layout3.addWidget(QLabel("Profesión/Ocupación:"))
        h_layout3.addWidget(self.profesion_ocupacion_entry)

        self.nombre_apellido_emergencia_entry = QLineEdit()
        self.nombre_apellido_emergencia_entry.setMaxLength(255)
        self.nombre_apellido_emergencia_entry.setFixedWidth(200)
        self.nombre_apellido_emergencia_entry.textChanged.connect(self.convert_to_uppercase)
        h_layout3.addWidget(QLabel("Familiar de Emergencia:"))
        h_layout3.addWidget(self.nombre_apellido_emergencia_entry)

        self.telefono_emergencia_entry = QLineEdit()
        self.telefono_emergencia_entry.setInputMask("0000-0000000")  # Máscara de entrada para el formato (0000-0000000)
        self.telefono_emergencia_entry.setMaxLength(12)
        self.telefono_emergencia_entry.setFixedWidth(120)
        h_layout3.addWidget(QLabel("Teléfono de Emergencia:"))
        h_layout3.addWidget(self.telefono_emergencia_entry)  # Alinear a la izquierda

        self.parentesco_entry = QLineEdit()
        self.parentesco_entry.setMaxLength(20)
        self.parentesco_entry.setFixedWidth(115)
        self.parentesco_entry.textChanged.connect(self.convert_to_uppercase)
        h_layout3.addWidget(QLabel("Parentesco:"))
        h_layout3.addWidget(self.parentesco_entry)

        h_layout3.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        form_layout.addRow(h_layout3)

        # Crear un layout horizontal para los campos en una misma línea
        h_layout4 = QHBoxLayout()
        h_layout4.setAlignment(Qt.AlignLeft)

        self.direccion_entry = QLineEdit()
        self.direccion_entry.setMaxLength(255)
        self.direccion_entry.setFixedWidth(340)
        self.direccion_entry.textChanged.connect(self.convert_to_uppercase)
        h_layout4.addWidget(QLabel("Dirección:"))
        h_layout4.addWidget(self.direccion_entry)

        
        self.g_entry = QLineEdit()
        self.g_entry.setMaxLength(255)
        self.g_entry.setFixedWidth(30)
        h_layout4.addWidget(QLabel("G:"))
        h_layout4.addWidget(self.g_entry)

        self.p_entry = QLineEdit()
        self.p_entry.setMaxLength(255)
        self.p_entry.setFixedWidth(30)
        h_layout4.addWidget(QLabel("P:"))
        h_layout4.addWidget(self.p_entry)

        self.a_entry = QLineEdit()
        self.a_entry.setMaxLength(255)
        self.a_entry.setFixedWidth(30)
        h_layout4.addWidget(QLabel("A:"))
        h_layout4.addWidget(self.a_entry)

        self.e_entry = QLineEdit()
        self.e_entry.setMaxLength(255)
        self.e_entry.setFixedWidth(30)
        h_layout4.addWidget(QLabel("E:"))
        h_layout4.addWidget(self.e_entry)

        self.m_entry = QLineEdit()
        self.m_entry.setMaxLength(255)
        self.m_entry.setFixedWidth(30)
        h_layout4.addWidget(QLabel("M:"))
        h_layout4.addWidget(self.m_entry)

        self.fur_entry = QLineEdit()
        self.fur_entry.setFixedWidth(180)
        h_layout4.addWidget(QLabel("FUR:"))
        h_layout4.addWidget(self.fur_entry)

        self.fpp_entry = QLineEdit()
        self.fpp_entry.setFixedWidth(180)
        h_layout4.addWidget(QLabel("FPP:"))
        h_layout4.addWidget(self.fpp_entry)

        h_layout4.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        form_layout.addRow(h_layout4)

        self.motivo_consulta_entry = QTextEdit()
        self.motivo_consulta_entry.setFixedWidth(960)
        form_layout.addRow(QLabel("Motivo de Consulta:"), self.motivo_consulta_entry)

        self.enfermedad_actual_entry = QTextEdit()
        self.enfermedad_actual_entry.setFixedWidth(960)
        form_layout.addRow(QLabel("Enfermedad Actual:"), self.enfermedad_actual_entry)

        self.antecedentes_personales_entry = QTextEdit()
        self.antecedentes_personales_entry.setFixedWidth(960)
        form_layout.addRow(QLabel("Antecedentes personales:"), self.antecedentes_personales_entry)

        self.antecedentes_familiares_entry = QTextEdit()
        self.antecedentes_familiares_entry.setFixedWidth(960)
        form_layout.addRow(QLabel("Antecedentes Familiares:"), self.antecedentes_familiares_entry)

        self.antecedentes_gineco_obstetricos_entry = QTextEdit()
        self.antecedentes_gineco_obstetricos_entry.setFixedWidth(960)
        form_layout.addRow(QLabel("Antecedentes Gineco<br>Obstetricos:"), self.antecedentes_gineco_obstetricos_entry)

        # Crear un nuevo layout horizontal para los campos adicionales
        h_layout6 = QHBoxLayout()
        h_layout6.setAlignment(Qt.AlignLeft)  # Alinear a la izquierda

        self.menarquia_entry = QLineEdit()
        self.menarquia_entry.setMaxLength(255)
        self.menarquia_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("Menarquia:"))
        h_layout6.addWidget(self.menarquia_entry)

        self.ciclo_entry = QLineEdit()
        self.ciclo_entry.setMaxLength(255)
        self.ciclo_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("Ciclo:"))
        h_layout6.addWidget(self.ciclo_entry)

        self.tipo_entry = QLineEdit()
        self.tipo_entry.setMaxLength(255)
        self.tipo_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("Tipo:"))
        h_layout6.addWidget(self.tipo_entry)

        self.prs_entry = QLineEdit()
        self.prs_entry.setMaxLength(255)
        self.prs_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("PRS:"))
        h_layout6.addWidget(self.prs_entry)

        self.ps_entry = QLineEdit()
        self.ps_entry.setMaxLength(255)
        self.ps_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("PS:"))
        h_layout6.addWidget(self.ps_entry)

        self.menopausia_entry = QLineEdit()
        self.menopausia_entry.setMaxLength(255)
        self.menopausia_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("Menopausia:"))
        h_layout6.addWidget(self.menopausia_entry)

        h_layout6.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        form_layout.addRow(h_layout6)

        # Crear un nuevo layout horizontal para los campos adicionales
        h_layout7 = QHBoxLayout()
        h_layout7.setAlignment(Qt.AlignLeft)  # Alinear a la izquierda

        self.anticonceptivo_entry = QLineEdit()
        self.anticonceptivo_entry.setMaxLength(255)
        self.anticonceptivo_entry.setFixedWidth(100)
        h_layout7.addWidget(QLabel("Anticonceptivo:"))
        h_layout7.addWidget(self.anticonceptivo_entry)

        self.ets_entry = QLineEdit()
        self.ets_entry.setMaxLength(255)
        self.ets_entry.setFixedWidth(100)
        h_layout7.addWidget(QLabel("ETS:"))
        h_layout7.addWidget(self.ets_entry)

        # Crear un layout horizontal para el título "Citología"
        h_layout_citologia = QHBoxLayout()
        self.citologia_button = QToolButton()
        self.citologia_button.setText("Citología")
        self.citologia_button.setStyleSheet("color: black; font-size: 16px; font-weight: bold; text-align: left;")
        self.citologia_button.setCheckable(True)
        self.citologia_button.setChecked(False)
        self.citologia_button.setArrowType(Qt.RightArrow)
        self.citologia_button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon) 
        self.citologia_button.clicked.connect(self.toggle_citologia)
        h_layout_citologia.addWidget(self.citologia_button)
        form_layout.addRow(h_layout_citologia)

        # Crear un widget contenedor para los campos de "Citología"
        self.citologia_widget = QWidget()
        self.citologia_widget.setVisible(False)
        citologia_layout = QVBoxLayout(self.citologia_widget)

        # Crear los campos de "Citología"
        h_layout1 = QHBoxLayout()
        h_layout1.setAlignment(Qt.AlignLeft)  # Alinear a la izquierda

        fecha_entry1 = QDateEdit()
        fecha_entry1.setObjectName("1CFECHA")
        fecha_entry1.setCalendarPopup(True)
        fecha_entry1.setFixedWidth(100)
        h_layout1.addWidget(QLabel("1 CFECHA:"))
        h_layout1.addWidget(fecha_entry1)

        rn_entry1 = QLineEdit()
        rn_entry1.setObjectName("1RN")
        rn_entry1.setMaxLength(255)
        rn_entry1.setFixedWidth(100)
        h_layout1.addWidget(QLabel("1 RN:"))
        h_layout1.addWidget(rn_entry1)

        g_mf_entry1 = QLineEdit()
        g_mf_entry1.setObjectName("1G_MF")
        g_mf_entry1.setMaxLength(255)
        g_mf_entry1.setFixedWidth(100)
        h_layout1.addWidget(QLabel("1 G MF:"))
        h_layout1.addWidget(g_mf_entry1)

        pam_entry1 = QLineEdit()
        pam_entry1.setObjectName("1PAM")
        pam_entry1.setMaxLength(255)
        pam_entry1.setFixedWidth(100)
        h_layout1.addWidget(QLabel("1 PAM:"))
        h_layout1.addWidget(pam_entry1)

        tan_entry1 = QLineEdit()
        tan_entry1.setObjectName("1TAN")
        tan_entry1.setMaxLength(255)
        tan_entry1.setFixedWidth(100)
        h_layout1.addWidget(QLabel("1 TAN:"))
        h_layout1.addWidget(tan_entry1)

        h_layout1.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        citologia_layout.addLayout(h_layout1)

        # Repetir para los siguientes campos
        # 2
        h_layout2 = QHBoxLayout()
        h_layout2.setAlignment(Qt.AlignLeft)

        fecha_entry2 = QDateEdit()
        fecha_entry2.setObjectName("2CFECHA")
        fecha_entry2.setCalendarPopup(True)
        fecha_entry2.setFixedWidth(100)
        h_layout2.addWidget(QLabel("2 CFECHA:"))
        h_layout2.addWidget(fecha_entry2)

        rn_entry2 = QLineEdit()
        rn_entry2.setObjectName("2RN")
        rn_entry2.setMaxLength(255)
        rn_entry2.setFixedWidth(100)
        h_layout2.addWidget(QLabel("2 RN:"))
        h_layout2.addWidget(rn_entry2)

        g_mf_entry2 = QLineEdit()
        g_mf_entry2.setObjectName("2G_MF")
        g_mf_entry2.setMaxLength(255)
        g_mf_entry2.setFixedWidth(100)
        h_layout2.addWidget(QLabel("2 G MF:"))
        h_layout2.addWidget(g_mf_entry2)

        pam_entry2 = QLineEdit()
        pam_entry2.setObjectName("2PAM")
        pam_entry2.setMaxLength(255)
        pam_entry2.setFixedWidth(100)
        h_layout2.addWidget(QLabel("2 PAM:"))
        h_layout2.addWidget(pam_entry2)

        tan_entry2 = QLineEdit()
        tan_entry2.setObjectName("2TAN")
        tan_entry2.setMaxLength(255)
        tan_entry2.setFixedWidth(100)
        h_layout2.addWidget(QLabel("2 TAN:"))
        h_layout2.addWidget(tan_entry2)

        h_layout2.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        citologia_layout.addLayout(h_layout2)

        # 3
        h_layout3 = QHBoxLayout()
        h_layout3.setAlignment(Qt.AlignLeft)

        fecha_entry3 = QDateEdit()
        fecha_entry3.setObjectName("3CFECHA")
        fecha_entry3.setCalendarPopup(True)
        fecha_entry3.setFixedWidth(100)
        h_layout3.addWidget(QLabel("3 CFECHA:"))
        h_layout3.addWidget(fecha_entry3)

        rn_entry3 = QLineEdit()
        rn_entry3.setObjectName("3RN")
        rn_entry3.setMaxLength(255)
        rn_entry3.setFixedWidth(100)
        h_layout3.addWidget(QLabel("3 RN:"))
        h_layout3.addWidget(rn_entry3)

        g_mf_entry3 = QLineEdit()
        g_mf_entry3.setObjectName("3G_MF")
        g_mf_entry3.setMaxLength(255)
        g_mf_entry3.setFixedWidth(100)
        h_layout3.addWidget(QLabel("3 G MF:"))
        h_layout3.addWidget(g_mf_entry3)

        pam_entry3 = QLineEdit()
        pam_entry3.setObjectName("3PAM")
        pam_entry3.setMaxLength(255)
        pam_entry3.setFixedWidth(100)
        h_layout3.addWidget(QLabel("3 PAM:"))
        h_layout3.addWidget(pam_entry3)

        tan_entry3 = QLineEdit()
        tan_entry3.setObjectName("3TAN")
        tan_entry3.setMaxLength(255)
        tan_entry3.setFixedWidth(100)
        h_layout3.addWidget(QLabel("3 TAN:"))
        h_layout3.addWidget(tan_entry3)

        h_layout3.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        citologia_layout.addLayout(h_layout3)

        # 4
        h_layout4 = QHBoxLayout()
        h_layout4.setAlignment(Qt.AlignLeft)

        fecha_entry4 = QDateEdit()
        fecha_entry4.setObjectName("4CFECHA")
        fecha_entry4.setCalendarPopup(True)
        fecha_entry4.setFixedWidth(100)
        h_layout4.addWidget(QLabel("4 CFECHA:"))
        h_layout4.addWidget(fecha_entry4)

        rn_entry4 = QLineEdit()
        rn_entry4.setObjectName("4RN")
        rn_entry4.setMaxLength(255)
        rn_entry4.setFixedWidth(100)
        h_layout4.addWidget(QLabel("4 RN:"))
        h_layout4.addWidget(rn_entry4)

        g_mf_entry4 = QLineEdit()
        g_mf_entry4.setObjectName("4G_MF")
        g_mf_entry4.setMaxLength(255)
        g_mf_entry4.setFixedWidth(100)
        h_layout4.addWidget(QLabel("4 G MF:"))
        h_layout4.addWidget(g_mf_entry4)

        pam_entry4 = QLineEdit()
        pam_entry4.setObjectName("4PAM")
        pam_entry4.setMaxLength(255)
        pam_entry4.setFixedWidth(100)
        h_layout4.addWidget(QLabel("4 PAM:"))
        h_layout4.addWidget(pam_entry4)

        tan_entry4 = QLineEdit()
        tan_entry4.setObjectName("4TAN")
        tan_entry4.setMaxLength(255)
        tan_entry4.setFixedWidth(100)
        h_layout4.addWidget(QLabel("4 TAN:"))
        h_layout4.addWidget(tan_entry4)

        h_layout4.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        citologia_layout.addLayout(h_layout4)

        # 5
        h_layout5 = QHBoxLayout()
        h_layout5.setAlignment(Qt.AlignLeft)

        fecha_entry5 = QDateEdit()
        fecha_entry5.setObjectName("5CFECHA")
        fecha_entry5.setCalendarPopup(True)
        fecha_entry5.setFixedWidth(100)
        h_layout5.addWidget(QLabel("5 CFECHA:"))
        h_layout5.addWidget(fecha_entry5)

        rn_entry5 = QLineEdit()
        rn_entry5.setObjectName("5RN")
        rn_entry5.setMaxLength(255)
        rn_entry5.setFixedWidth(100)
        h_layout5.addWidget(QLabel("5 RN:"))
        h_layout5.addWidget(rn_entry5)

        g_mf_entry5 = QLineEdit()
        g_mf_entry5.setObjectName("5G_MF")
        g_mf_entry5.setMaxLength(255)
        g_mf_entry5.setFixedWidth(100)
        h_layout5.addWidget(QLabel("5 G MF:"))
        h_layout5.addWidget(g_mf_entry5)

        pam_entry5 = QLineEdit()
        pam_entry5.setObjectName("5PAM")
        pam_entry5.setMaxLength(255)
        pam_entry5.setFixedWidth(100)
        h_layout5.addWidget(QLabel("5 PAM:"))
        h_layout5.addWidget(pam_entry5)

        tan_entry5 = QLineEdit()
        tan_entry5.setObjectName("5TAN")
        tan_entry5.setMaxLength(255)
        tan_entry5.setFixedWidth(100)
        h_layout5.addWidget(QLabel("5 TAN:"))
        h_layout5.addWidget(tan_entry5)

        h_layout5.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        citologia_layout.addLayout(h_layout5)

        form_layout.addRow(self.citologia_widget)

        # Crear un layout horizontal para el título "Embarazo Actual"
        h_layout_embarazo_actual = QHBoxLayout()
        self.embarazo_actual_button = QToolButton()
        self.embarazo_actual_button.setText("Embarazo Actual")
        self.embarazo_actual_button.setStyleSheet("color: black; font-size: 16px; font-weight: bold; text-align: left;")
        self.embarazo_actual_button.setCheckable(True)
        self.embarazo_actual_button.setChecked(False)
        self.embarazo_actual_button.setArrowType(Qt.RightArrow)
        self.embarazo_actual_button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon) 
        self.embarazo_actual_button.clicked.connect(self.toggle_embarazo_actual)
        h_layout_embarazo_actual.addWidget(self.embarazo_actual_button)
        form_layout.addRow(h_layout_embarazo_actual)

        # Crear un widget contenedor para los campos de "Embarazo Actual"
        self.embarazo_actual_widget = QWidget()
        self.embarazo_actual_widget.setVisible(False)
        embarazo_actual_layout = QVBoxLayout(self.embarazo_actual_widget)

        # Campos de "Embarazo Actual"
        h_layout_embarazo_actual_fields = QHBoxLayout()
        h_layout_embarazo_actual_fields.setAlignment(Qt.AlignLeft)  # Alinear a la izquierda

        self.planificado_entry = QComboBox()
        self.planificado_entry.addItems(["N/A", "Sí", "No"])
        self.planificado_entry.setFixedWidth(100)
        h_layout_embarazo_actual_fields.addWidget(QLabel("Planificado:"))
        h_layout_embarazo_actual_fields.addWidget(self.planificado_entry)

        self.deseado_entry = QComboBox()
        self.deseado_entry.addItems(["N/A", "Sí", "No"])
        self.deseado_entry.setFixedWidth(100)
        h_layout_embarazo_actual_fields.addWidget(QLabel("Deseado:"))
        h_layout_embarazo_actual_fields.addWidget(self.deseado_entry)

        self.aceptado_entry = QComboBox()
        self.aceptado_entry.addItems(["N/A", "Sí", "No"])
        self.aceptado_entry.setFixedWidth(100)
        h_layout_embarazo_actual_fields.addWidget(QLabel("Aceptado:"))
        h_layout_embarazo_actual_fields.addWidget(self.aceptado_entry)

        h_layout_embarazo_actual_fields.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        embarazo_actual_layout.addLayout(h_layout_embarazo_actual_fields)

        # Subtítulo "Control"
        h_layout_control = QHBoxLayout()
        h_layout_control.setAlignment(Qt.AlignLeft)  # Alinear a la izquierda
        h_layout_control.addWidget(QLabel("Control"))
        embarazo_actual_layout.addLayout(h_layout_control)

        # Campos de "Control"
        h_layout_control_fields = QHBoxLayout()
        h_layout_control_fields.setAlignment(Qt.AlignLeft)  # Alinear a la izquierda

        self.inicio_entry = QLineEdit()
        self.inicio_entry.setMaxLength(255)
        self.inicio_entry.setFixedWidth(100)
        h_layout_control_fields.addWidget(QLabel("Inicio:"))
        h_layout_control_fields.addWidget(self.inicio_entry)

        self.sg_entry = QLineEdit()
        self.sg_entry.setMaxLength(255)
        self.sg_entry.setFixedWidth(100)
        h_layout_control_fields.addWidget(QLabel("SG:"))
        h_layout_control_fields.addWidget(self.sg_entry)

        self.pub_entry = QLineEdit()
        self.pub_entry.setMaxLength(255)
        self.pub_entry.setFixedWidth(50)
        h_layout_control_fields.addWidget(QLabel("Pub:"))
        h_layout_control_fields.addWidget(self.pub_entry)

        self.tab_entry = QLineEdit()
        self.tab_entry.setMaxLength(255)
        self.tab_entry.setFixedWidth(100)
        h_layout_control_fields.addWidget(QLabel("TAB:"))
        h_layout_control_fields.addWidget(self.tab_entry)

        self.privada_entry = QLineEdit()
        self.privada_entry.setMaxLength(255)
        self.privada_entry.setFixedWidth(100)
        h_layout_control_fields.addWidget(QLabel("Privada:"))
        h_layout_control_fields.addWidget(self.privada_entry)

        self.gp_entry = QLineEdit()
        self.gp_entry.setMaxLength(255)
        self.gp_entry.setFixedWidth(100)
        h_layout_control_fields.addWidget(QLabel("GP:"))
        h_layout_control_fields.addWidget(self.gp_entry)

        h_layout_control_fields.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        embarazo_actual_layout.addLayout(h_layout_control_fields)

        # Campo "Complicaciones"
        h_layout_complicaciones = QHBoxLayout()
        h_layout_complicaciones.setAlignment(Qt.AlignLeft)  # Alinear a la izquierda

        self.complicaciones_entry = QLineEdit()
        self.complicaciones_entry.setMaxLength(255)
        self.complicaciones_entry.setFixedWidth(100)
        h_layout_complicaciones.addWidget(QLabel("Complicaciones:"))
        h_layout_complicaciones.addWidget(self.complicaciones_entry)

        h_layout_complicaciones.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        embarazo_actual_layout.addLayout(h_layout_complicaciones)

        # Campos "Inductores" y "Toxoide"
        h_layout_inductores_toxoide = QHBoxLayout()
        h_layout_inductores_toxoide.setAlignment(Qt.AlignLeft)  # Alinear a la izquierda

        self.inductores_entry = QLineEdit()
        self.inductores_entry.setMaxLength(255)
        self.inductores_entry.setFixedWidth(100)
        h_layout_inductores_toxoide.addWidget(QLabel("Inductores:"))
        h_layout_inductores_toxoide.addWidget(self.inductores_entry)

        self.toxoide_entry = QLineEdit()
        self.toxoide_entry.setMaxLength(255)
        self.toxoide_entry.setFixedWidth(100)
        h_layout_inductores_toxoide.addWidget(QLabel("Toxoide:"))
        h_layout_inductores_toxoide.addWidget(self.toxoide_entry)

        h_layout_inductores_toxoide.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        embarazo_actual_layout.addLayout(h_layout_inductores_toxoide)

        form_layout.addRow(self.embarazo_actual_widget)

        # Crear un layout horizontal para el título "Laboratorio"
        h_layout_laboratorio = QHBoxLayout()
        self.laboratorio_button = QToolButton()
        self.laboratorio_button.setText("Laboratorio")
        self.laboratorio_button.setStyleSheet("color: black; font-size: 16px; font-weight: bold; text-align: left;")
        self.laboratorio_button.setCheckable(True)
        self.laboratorio_button.setChecked(False)
        self.laboratorio_button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)  # Colocar el texto a la izquierda de la flecha
        self.laboratorio_button.setArrowType(Qt.RightArrow)
        self.laboratorio_button.clicked.connect(self.toggle_laboratorio)
        h_layout_laboratorio.addWidget(self.laboratorio_button)
        form_layout.addRow(h_layout_laboratorio)

        # Crear un widget contenedor para los campos de "Laboratorio"
        self.laboratorio_widget = QWidget()
        self.laboratorio_widget.setVisible(False)
        laboratorio_layout = QVBoxLayout(self.laboratorio_widget)

        # Crear una tabla para los campos de "Laboratorio"
        self.laboratorio_table = QTableWidget(19, 7)  # 7 filas, 19 columnas
        self.laboratorio_table.setVerticalHeaderLabels([
            "Tipiaje", "HIV", "VDRL", "Toxo Test", "TP", "TPT", "WBC", "Linf", "Gran", 
            "Hb", "Hct", "Plt", "Glicemia", "Urea", "Creat", "Bil Total", "LDH", "TGO", "TGP"
        ])

        # Ajustar el tamaño de la tabla para que sea completamente visible
        self.laboratorio_table.setFixedHeight(600)
        self.laboratorio_table.setFixedWidth(800)

        # Añadir la tabla al layout de "Laboratorio"
        laboratorio_layout.addWidget(self.laboratorio_table)
        form_layout.addRow(self.laboratorio_widget)

        # Crear un layout horizontal para el título "Uroanálisis"
        h_layout_uroanalisis = QHBoxLayout()
        self.uroanalisis_button = QToolButton()
        self.uroanalisis_button.setText("Uroanálisis")
        self.uroanalisis_button.setStyleSheet("color: black; font-size: 16px; font-weight: bold; text-align: left;")
        self.uroanalisis_button.setCheckable(True)
        self.uroanalisis_button.setChecked(False)
        self.uroanalisis_button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.uroanalisis_button.setArrowType(Qt.RightArrow)
        self.uroanalisis_button.clicked.connect(self.toggle_uroanalisis)
        h_layout_uroanalisis.addWidget(self.uroanalisis_button)
        form_layout.addRow(h_layout_uroanalisis)

        # Crear un widget contenedor para los campos de "Uroanálisis"
        self.uroanalisis_widget = QWidget()
        self.uroanalisis_widget.setVisible(False)
        uroanalisis_layout = QVBoxLayout(self.uroanalisis_widget)

        # Crear los campos de "Uroanálisis" en el orden especificado
        h_layout = QHBoxLayout()
        h_layout.setAlignment(Qt.AlignLeft)  # Alinear a la izquierda

        v_layout1 = QVBoxLayout()
        color_entry1 = QLineEdit()
        color_entry1.setObjectName("1Color")
        color_entry1.setMaxLength(255)
        color_entry1.setFixedWidth(100)
        v_layout1.addWidget(QLabel("1 Color:"))
        v_layout1.addWidget(color_entry1)

        aspecto_entry1 = QLineEdit()
        aspecto_entry1.setObjectName("1Aspecto")
        aspecto_entry1.setMaxLength(255)
        aspecto_entry1.setFixedWidth(100)
        v_layout1.addWidget(QLabel("1 Aspecto:"))
        v_layout1.addWidget(aspecto_entry1)

        densidad_entry1 = QLineEdit()
        densidad_entry1.setObjectName("1Densidad")
        densidad_entry1.setMaxLength(255)
        densidad_entry1.setFixedWidth(100)
        v_layout1.addWidget(QLabel("1 Densidad:"))
        v_layout1.addWidget(densidad_entry1)

        leucocitos_entry1 = QLineEdit()
        leucocitos_entry1.setObjectName("1Leucocitos")
        leucocitos_entry1.setMaxLength(255)
        leucocitos_entry1.setFixedWidth(100)
        v_layout1.addWidget(QLabel("1 Leucocitos:"))
        v_layout1.addWidget(leucocitos_entry1)

        hematies_entry1 = QLineEdit()
        hematies_entry1.setObjectName("1Hematies")
        hematies_entry1.setMaxLength(255)
        hematies_entry1.setFixedWidth(100)
        v_layout1.addWidget(QLabel("1 Hematíes:"))
        v_layout1.addWidget(hematies_entry1)

        proteinas_entry1 = QLineEdit()
        proteinas_entry1.setObjectName("1Proteinas")
        proteinas_entry1.setMaxLength(255)
        proteinas_entry1.setFixedWidth(100)
        v_layout1.addWidget(QLabel("1 Proteínas:"))
        v_layout1.addWidget(proteinas_entry1)

        otros_entry1 = QLineEdit()
        otros_entry1.setObjectName("1Otros")
        otros_entry1.setMaxLength(255)
        otros_entry1.setFixedWidth(100)
        v_layout1.addWidget(QLabel("1 Otros:"))
        v_layout1.addWidget(otros_entry1)

        h_layout.addLayout(v_layout1)

        # Repetir para los siguientes campos
        v_layout2 = QVBoxLayout()
        color_entry2 = QLineEdit()
        color_entry2.setObjectName("2Color")
        color_entry2.setMaxLength(255)
        color_entry2.setFixedWidth(100)
        v_layout2.addWidget(QLabel("2 Color:"))
        v_layout2.addWidget(color_entry2)

        aspecto_entry2 = QLineEdit()
        aspecto_entry2.setObjectName("2Aspecto")
        aspecto_entry2.setMaxLength(255)
        aspecto_entry2.setFixedWidth(100)
        v_layout2.addWidget(QLabel("2 Aspecto:"))
        v_layout2.addWidget(aspecto_entry2)

        densidad_entry2 = QLineEdit()
        densidad_entry2.setObjectName("2Densidad")
        densidad_entry2.setMaxLength(255)
        densidad_entry2.setFixedWidth(100)
        v_layout2.addWidget(QLabel("2 Densidad:"))
        v_layout2.addWidget(densidad_entry2)

        leucocitos_entry2 = QLineEdit()
        leucocitos_entry2.setObjectName("2Leucocitos")
        leucocitos_entry2.setMaxLength(255)
        leucocitos_entry2.setFixedWidth(100)
        v_layout2.addWidget(QLabel("2 Leucocitos:"))
        v_layout2.addWidget(leucocitos_entry2)

        hematies_entry2 = QLineEdit()
        hematies_entry2.setObjectName("2Hematies")
        hematies_entry2.setMaxLength(255)
        hematies_entry2.setFixedWidth(100)
        v_layout2.addWidget(QLabel("2 Hematíes:"))
        v_layout2.addWidget(hematies_entry2)

        proteinas_entry2 = QLineEdit()
        proteinas_entry2.setObjectName("2Proteinas")
        proteinas_entry2.setMaxLength(255)
        proteinas_entry2.setFixedWidth(100)
        v_layout2.addWidget(QLabel("2 Proteínas:"))
        v_layout2.addWidget(proteinas_entry2)

        otros_entry2 = QLineEdit()
        otros_entry2.setObjectName("2Otros")
        otros_entry2.setMaxLength(255)
        otros_entry2.setFixedWidth(100)
        v_layout2.addWidget(QLabel("2 Otros:"))
        v_layout2.addWidget(otros_entry2)

        h_layout.addLayout(v_layout2)

        # Repetir para los siguientes campos
        v_layout3 = QVBoxLayout()
        color_entry3 = QLineEdit()
        color_entry3.setObjectName("3Color")
        color_entry3.setMaxLength(255)
        color_entry3.setFixedWidth(100)
        v_layout3.addWidget(QLabel("3 Color:"))
        v_layout3.addWidget(color_entry3)

        aspecto_entry3 = QLineEdit()
        aspecto_entry3.setObjectName("3Aspecto")
        aspecto_entry3.setMaxLength(255)
        aspecto_entry3.setFixedWidth(100)
        v_layout3.addWidget(QLabel("3 Aspecto:"))
        v_layout3.addWidget(aspecto_entry3)

        densidad_entry3 = QLineEdit()
        densidad_entry3.setObjectName("3Densidad")
        densidad_entry3.setMaxLength(255)
        densidad_entry3.setFixedWidth(100)
        v_layout3.addWidget(QLabel("3 Densidad:"))
        v_layout3.addWidget(densidad_entry3)

        leucocitos_entry3 = QLineEdit()
        leucocitos_entry3.setObjectName("3Leucocitos")
        leucocitos_entry3.setMaxLength(255)
        leucocitos_entry3.setFixedWidth(100)
        v_layout3.addWidget(QLabel("3 Leucocitos:"))
        v_layout3.addWidget(leucocitos_entry3)

        hematies_entry3 = QLineEdit()
        hematies_entry3.setObjectName("3Hematies")
        hematies_entry3.setMaxLength(255)
        hematies_entry3.setFixedWidth(100)
        v_layout3.addWidget(QLabel("3 Hematíes:"))
        v_layout3.addWidget(hematies_entry3)

        proteinas_entry3 = QLineEdit()
        proteinas_entry3.setObjectName("3Proteinas")
        proteinas_entry3.setMaxLength(255)
        proteinas_entry3.setFixedWidth(100)
        v_layout3.addWidget(QLabel("3 Proteínas:"))
        v_layout3.addWidget(proteinas_entry3)

        otros_entry3 = QLineEdit()
        otros_entry3.setObjectName("3Otros")
        otros_entry3.setMaxLength(255)
        otros_entry3.setFixedWidth(100)
        v_layout3.addWidget(QLabel("3 Otros:"))
        v_layout3.addWidget(otros_entry3)

        h_layout.addLayout(v_layout3)

        # Repetir para los siguientes campos
        v_layout4 = QVBoxLayout()
        color_entry4 = QLineEdit()
        color_entry4.setObjectName("4Color")
        color_entry4.setMaxLength(255)
        color_entry4.setFixedWidth(100)
        v_layout4.addWidget(QLabel("4 Color:"))
        v_layout4.addWidget(color_entry4)

        aspecto_entry4 = QLineEdit()
        aspecto_entry4.setObjectName("4Aspecto")
        aspecto_entry4.setMaxLength(255)
        aspecto_entry4.setFixedWidth(100)
        v_layout4.addWidget(QLabel("4 Aspecto:"))
        v_layout4.addWidget(aspecto_entry4)

        densidad_entry4 = QLineEdit()
        densidad_entry4.setObjectName("4Densidad")
        densidad_entry4.setMaxLength(255)
        densidad_entry4.setFixedWidth(100)
        v_layout4.addWidget(QLabel("4 Densidad:"))
        v_layout4.addWidget(densidad_entry4)

        leucocitos_entry4 = QLineEdit()
        leucocitos_entry4.setObjectName("4Leucocitos")
        leucocitos_entry4.setMaxLength(255)
        leucocitos_entry4.setFixedWidth(100)
        v_layout4.addWidget(QLabel("4 Leucocitos:"))
        v_layout4.addWidget(leucocitos_entry4)

        hematies_entry4 = QLineEdit()
        hematies_entry4.setObjectName("4Hematies")
        hematies_entry4.setMaxLength(255)
        hematies_entry4.setFixedWidth(100)
        v_layout4.addWidget(QLabel("4 Hematíes:"))
        v_layout4.addWidget(hematies_entry4)

        proteinas_entry4 = QLineEdit()
        proteinas_entry4.setObjectName("4Proteinas")
        proteinas_entry4.setMaxLength(255)
        proteinas_entry4.setFixedWidth(100)
        v_layout4.addWidget(QLabel("4 Proteínas:"))
        v_layout4.addWidget(proteinas_entry4)

        otros_entry4 = QLineEdit()
        otros_entry4.setObjectName("4Otros")
        otros_entry4.setMaxLength(255)
        otros_entry4.setFixedWidth(100)
        v_layout4.addWidget(QLabel("4 Otros:"))
        v_layout4.addWidget(otros_entry4)

        h_layout.addLayout(v_layout4)

        uroanalisis_layout.addLayout(h_layout)

        form_layout.addRow(self.uroanalisis_widget)

        # Crear un layout horizontal para el título "Ecosonograma Obstétrico"
        h_layout_ecosonograma = QHBoxLayout()
        self.ecosonograma_button = QToolButton()
        self.ecosonograma_button.setText("Ecosonograma Obstétrico")
        self.ecosonograma_button.setStyleSheet("color: black; font-size: 16px; font-weight: bold; text-align: left;")
        self.ecosonograma_button.setCheckable(True)
        self.ecosonograma_button.setChecked(False)
        self.ecosonograma_button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.ecosonograma_button.setArrowType(Qt.RightArrow)
        self.ecosonograma_button.clicked.connect(self.toggle_ecosonograma)
        h_layout_ecosonograma.addWidget(self.ecosonograma_button)
        form_layout.addRow(h_layout_ecosonograma)

        # Crear un widget contenedor para los campos de "Ecosonograma Obstétrico"
        self.ecosonograma_widget = QWidget()
        self.ecosonograma_widget.setVisible(False)
        ecosonograma_layout = QVBoxLayout(self.ecosonograma_widget)

        # Crear los campos de "Ecosonograma Obstétrico" con los nombres indicados
        h_layout1 = QHBoxLayout()
        h_layout1.setAlignment(Qt.AlignLeft)  # Alinear a la izquierda

        fecha_edad_gestacional_entry1 = QDateEdit()
        fecha_edad_gestacional_entry1.setObjectName("1_Fecha_Edad_Gestacional")
        fecha_edad_gestacional_entry1.setCalendarPopup(True)
        fecha_edad_gestacional_entry1.setFixedWidth(100)
        h_layout1.addWidget(QLabel("1 Fecha Edad Gestacional:"))
        h_layout1.addWidget(fecha_edad_gestacional_entry1)

        extrapolado_para_entry1 = QLineEdit()
        extrapolado_para_entry1.setObjectName("1_Extrapolado_Para")
        extrapolado_para_entry1.setMaxLength(255)
        extrapolado_para_entry1.setFixedWidth(100)
        h_layout1.addWidget(QLabel("1 Extrapolado Para:"))
        h_layout1.addWidget(extrapolado_para_entry1)

        h_layout1.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        ecosonograma_layout.addLayout(h_layout1)

        h_layout2 = QHBoxLayout()
        h_layout2.setAlignment(Qt.AlignLeft)  # Alinear a la izquierda

        fecha_edad_gestacional_entry2 = QDateEdit()
        fecha_edad_gestacional_entry2.setObjectName("2_Fecha_Edad_Gestacional")
        fecha_edad_gestacional_entry2.setCalendarPopup(True)
        fecha_edad_gestacional_entry2.setFixedWidth(100)
        h_layout2.addWidget(QLabel("2 Fecha Edad Gestacional:"))
        h_layout2.addWidget(fecha_edad_gestacional_entry2)

        extrapolado_para_entry2 = QLineEdit()
        extrapolado_para_entry2.setObjectName("2_Extrapolado_Para")
        extrapolado_para_entry2.setMaxLength(255)
        extrapolado_para_entry2.setFixedWidth(100)
        h_layout2.addWidget(QLabel("2 Extrapolado Para:"))
        h_layout2.addWidget(extrapolado_para_entry2)

        h_layout2.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        ecosonograma_layout.addLayout(h_layout2)

        h_layout3 = QHBoxLayout()
        h_layout3.setAlignment(Qt.AlignLeft)  # Alinear a la izquierda

        fecha_edad_gestacional_entry3 = QDateEdit()
        fecha_edad_gestacional_entry3.setObjectName("3_Fecha_Edad_Gestacional")
        fecha_edad_gestacional_entry3.setCalendarPopup(True)
        fecha_edad_gestacional_entry3.setFixedWidth(100)
        h_layout3.addWidget(QLabel("3 Fecha Edad Gestacional:"))
        h_layout3.addWidget(fecha_edad_gestacional_entry3)

        extrapolado_para_entry3 = QLineEdit()
        extrapolado_para_entry3.setObjectName("3_Extrapolado_Para")
        extrapolado_para_entry3.setMaxLength(255)
        extrapolado_para_entry3.setFixedWidth(100)
        h_layout3.addWidget(QLabel("3 Extrapolado Para:"))
        h_layout3.addWidget(extrapolado_para_entry3)

        h_layout3.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        ecosonograma_layout.addLayout(h_layout3)

        h_layout4 = QHBoxLayout()
        h_layout4.setAlignment(Qt.AlignLeft)  # Alinear a la izquierda

        fecha_edad_gestacional_entry4 = QDateEdit()
        fecha_edad_gestacional_entry4.setObjectName("4_Fecha_Edad_Gestacional")
        fecha_edad_gestacional_entry4.setCalendarPopup(True)
        fecha_edad_gestacional_entry4.setFixedWidth(100)
        h_layout4.addWidget(QLabel("4 Fecha Edad Gestacional:"))
        h_layout4.addWidget(fecha_edad_gestacional_entry4)

        extrapolado_para_entry4 = QLineEdit()
        extrapolado_para_entry4.setObjectName("4_Extrapolado_Para")
        extrapolado_para_entry4.setMaxLength(255)
        extrapolado_para_entry4.setFixedWidth(100)
        h_layout4.addWidget(QLabel("4 Extrapolado Para:"))
        h_layout4.addWidget(extrapolado_para_entry4)

        h_layout4.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        ecosonograma_layout.addLayout(h_layout4)

        h_layout5 = QHBoxLayout()
        h_layout5.setAlignment(Qt.AlignLeft)  # Alinear a la izquierda

        fecha_edad_gestacional_entry5 = QDateEdit()
        fecha_edad_gestacional_entry5.setObjectName("5_Fecha_Edad_Gestacional")
        fecha_edad_gestacional_entry5.setCalendarPopup(True)
        fecha_edad_gestacional_entry5.setFixedWidth(100)
        h_layout5.addWidget(QLabel("5 Fecha Edad Gestacional:"))
        h_layout5.addWidget(fecha_edad_gestacional_entry5)

        extrapolado_para_entry5 = QLineEdit()
        extrapolado_para_entry5.setObjectName("5_Extrapolado_Para")
        extrapolado_para_entry5.setMaxLength(255)
        extrapolado_para_entry5.setFixedWidth(100)
        h_layout5.addWidget(QLabel("5 Extrapolado Para:"))
        h_layout5.addWidget(extrapolado_para_entry5)

        h_layout5.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        ecosonograma_layout.addLayout(h_layout5)

        form_layout.addRow(self.ecosonograma_widget)

        # Crear un layout horizontal para el título "Radiocefalopelvimetría"
        h_layout_radiocefalopelvimetria = QHBoxLayout()
        self.radiocefalopelvimetria_button = QToolButton()
        self.radiocefalopelvimetria_button.setText("Radiocefalopelvimetría")
        self.radiocefalopelvimetria_button.setStyleSheet("color: black; font-size: 16px; font-weight: bold; text-align: left;")
        self.radiocefalopelvimetria_button.setCheckable(True)
        self.radiocefalopelvimetria_button.setChecked(False)
        self.radiocefalopelvimetria_button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.radiocefalopelvimetria_button.setArrowType(Qt.RightArrow)
        self.radiocefalopelvimetria_button.clicked.connect(self.toggle_radiocefalopelvimetria)
        h_layout_radiocefalopelvimetria.addWidget(self.radiocefalopelvimetria_button)
        form_layout.addRow(h_layout_radiocefalopelvimetria)

        # Crear un widget contenedor para los campos de "Radiocefalopelvimetría"
        self.radiocefalopelvimetria_widget = QWidget()
        self.radiocefalopelvimetria_widget.setVisible(False)
        radiocefalopelvimetria_layout = QVBoxLayout(self.radiocefalopelvimetria_widget)

        # Crear una tabla para los campos de "Radiocefalopelvimetría"
        self.radiocefalopelvimetria_table = QTableWidget(3, 4)  # 4 filas, 4 columnas
        self.radiocefalopelvimetria_table.setHorizontalHeaderLabels(["Diámetro", "Estrecho Superior", "Estrecho Medio", "Estrecho Inferior"])
        self.radiocefalopelvimetria_table.setVerticalHeaderLabels(["AP", "Transverso", "Oblicuo"])

        # Ajustar el tamaño de la tabla para que sea completamente visible
        self.radiocefalopelvimetria_table.setFixedHeight(160)
        self.radiocefalopelvimetria_table.setFixedWidth(480)
        #self.laboratorio_table.setFixedHeight(self.laboratorio_table.verticalHeader().length() + self.laboratorio_table.horizontalHeader().height())
        #self.laboratorio_table.setFixedWidth(self.laboratorio_table.horizontalHeader().length())


        # Añadir la tabla al layout de "Radiocefalopelvimetría"
        radiocefalopelvimetria_layout.addWidget(self.radiocefalopelvimetria_table)
        form_layout.addRow(self.radiocefalopelvimetria_widget)

        self.general_entry = QTextEdit()
        self.general_entry.setFixedWidth(960)
        form_layout.addRow(QLabel("GENERAL:"), self.general_entry)

        # Crear un layout horizontal para los campos adicionales
        h_layout7 = QHBoxLayout()
        h_layout7.setAlignment(Qt.AlignLeft)  # Alinear a la izquierda

        self.fc_entry = QLineEdit()
        self.fc_entry.setMaxLength(255)
        self.fc_entry.setFixedWidth(100)
        h_layout7.addWidget(QLabel("FC:"))
        h_layout7.addWidget(self.fc_entry)

        self.fr_entry = QLineEdit()
        self.fr_entry.setMaxLength(255)
        self.fr_entry.setFixedWidth(100)
        h_layout7.addWidget(QLabel("FR:"))
        h_layout7.addWidget(self.fr_entry)

        self.pa_entry = QLineEdit()
        self.pa_entry.setMaxLength(255)
        self.pa_entry.setFixedWidth(100)
        h_layout7.addWidget(QLabel("PA:"))
        h_layout7.addWidget(self.pa_entry)

        self.tem_entry = QLineEdit()
        self.tem_entry.setMaxLength(255)
        self.tem_entry.setFixedWidth(100)
        h_layout7.addWidget(QLabel("TEM:"))
        h_layout7.addWidget(self.tem_entry)

        self.t_entry = QLineEdit()
        self.t_entry.setMaxLength(255)
        self.t_entry.setFixedWidth(100)
        h_layout7.addWidget(QLabel("T:"))
        h_layout7.addWidget(self.t_entry)

        self.p1_entry = QLineEdit()
        self.p1_entry.setMaxLength(255)
        self.p1_entry.setFixedWidth(100)
        h_layout7.addWidget(QLabel("1P:"))
        h_layout7.addWidget(self.p1_entry)

        self.imc_entry = QLineEdit()
        self.imc_entry.setMaxLength(255)
        self.imc_entry.setFixedWidth(100)
        h_layout7.addWidget(QLabel("IMC:"))
        h_layout7.addWidget(self.imc_entry)

        h_layout7.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        form_layout.addRow(h_layout7)

        self.mamas_entry = QTextEdit()
        self.mamas_entry.setFixedWidth(960)
        form_layout.addRow(QLabel("MAMAS:"), self.mamas_entry)

        self.cardio_pulmonar_entry = QTextEdit()
        self.cardio_pulmonar_entry.setFixedWidth(960)
        form_layout.addRow(QLabel("CARDIO PULMONAR:"), self.cardio_pulmonar_entry)

        self.abdomen_entry = QTextEdit()
        self.abdomen_entry.setFixedWidth(960)
        form_layout.addRow(QLabel("ABDOMEN:"), self.abdomen_entry)

        self.genitales_entry = QTextEdit()
        self.genitales_entry.setFixedWidth(960)
        form_layout.addRow(QLabel("GENITALES:"), self.genitales_entry)
     
        self.tacto_entry = QTextEdit()
        self.tacto_entry.setFixedWidth(960)
        form_layout.addRow(QLabel("TACTO:"), self.tacto_entry)

        self.especulo_entry = QTextEdit()
        self.especulo_entry.setFixedWidth(960)
        form_layout.addRow(QLabel("ESPECULO:"), self.especulo_entry)

        self.extremidades_entry = QTextEdit()
        self.extremidades_entry.setFixedWidth(960)
        form_layout.addRow(QLabel("EXTREMIDADES:"), self.extremidades_entry)

        self.neurologico_entry = QTextEdit()
        self.neurologico_entry.setFixedWidth(960)
        form_layout.addRow(QLabel("NEUROLÓGICO:"), self.neurologico_entry)

        self.diagnostico_admision_entry = QTextEdit()
        self.diagnostico_admision_entry.setFixedWidth(960)
        form_layout.addRow(QLabel("DIAGNOSTICO DE<br>INGRESO:"), self.diagnostico_admision_entry)

        self.comentarios_entry = QTextEdit()
        self.comentarios_entry.setFixedWidth(960)
        form_layout.addRow(QLabel("COMENTARIOS:"), self.comentarios_entry)

        # Crear un layout horizontal para los botones
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignRight)  # Alinear a la derecha
        button_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Configurar el botón de "Atrás"
        self.back_button = QPushButton("Atrás")
        self.back_button.setIcon(QIcon("iconos/atras.png"))  # Establecer la imagen del botón
        self.back_button.setIconSize(QSize(24, 24))  # Ajustar el tamaño de la imagen
        self.back_button.setFixedSize(100, 40)  # Ajustar el tamaño del botón
        self.back_button.clicked.connect(self.go_back)
        button_layout.addWidget(self.back_button)

        # Botón "Limpiar" en la esquina inferior derecha
        self.clear_button = QPushButton("Limpiar")
        self.clear_button.setIcon(QIcon("iconos/limpiar.png"))  # Establecer la imagen del botón
        self.clear_button.setIconSize(QSize(24, 24))  # Ajustar el tamaño de la imagen
        self.clear_button.setFixedSize(100, 40)  # Ajustar el tamaño del botón
        self.clear_button.clicked.connect(self.clear_all_fields)  # Conectar la señal
        button_layout.addWidget(self.clear_button)

        # Botón "Guardar" en la esquina inferior derecha
        self.save_button = QPushButton("Guardar")
        self.save_button.setIcon(QIcon("iconos/guardar.png"))  # Establecer la imagen del botón
        self.save_button.setIconSize(QSize(24, 24))  # Ajustar el tamaño de la imagen
        self.save_button.setFixedSize(100, 40)  # Ajustar el tamaño del botón
        self.save_button.clicked.connect(self.save_data)
        button_layout.addWidget(self.save_button)

        layout.addLayout(button_layout)

        # Layout para la fecha y hora en la parte inferior izquierda
        datetime_layout = QHBoxLayout()
        datetime_layout.setAlignment(Qt.AlignBottom | Qt.AlignLeft)

        # Labels para mostrar la fecha y la hora
        self.date_label = QLabel()
        self.time_label = QLabel()

        datetime_layout.addWidget(self.date_label)
        datetime_layout.addWidget(self.time_label)

        layout.addLayout(datetime_layout)

        # Timer para actualizar la hora cada segundo
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_datetime)
        self.timer.start(1000)  # Actualizar cada 1000 ms (1 segundo)

        # Inicializar la fecha y la hora
        self.update_datetime()

    def update_datetime(self):
        # Obtener la fecha y hora actual
        current_date = QDate.currentDate().toString("yyyy-MM-dd")
        current_time = QTime.currentTime().toString("hh:mm:ss")

        # Mostrar la fecha y la hora en los labels
        self.date_label.setText("Fecha: " + current_date + "  ")
        self.time_label.setText("Hora: " + current_time)

    def clear_all_fields(self):
        self.cedula_entry.clear()
        self.primer_nombre_entry.clear()
        self.segundo_nombre_entry.clear()
        self.primer_apellido_entry.clear()
        self.segundo_apellido_entry.clear()
        self.age_label_paciente.clear()
        self.fecha_nacimiento_entry.setDate(QDate.currentDate())
        self.telefono_entry.clear()
        self.genero_entry.setCurrentIndex(0)
        self.estado_civil_entry.setCurrentIndex(0)
        self.nacionalidad_entry.setCurrentIndex(0)
        self.profesion_ocupacion_entry.clear()
        self.lugar_nacimiento_entry.clear()
        self.nombre_apellido_emergencia_entry.clear()
        self.telefono_emergencia_entry.clear()
        self.parentesco_entry.clear()
        self.direccion_entry.clear()
        self.g_entry.clear()
        self.p_entry.clear()
        self.a_entry.clear()
        self.e_entry.clear()
        self.m_entry.clear()
        self.fur_entry.clear()
        self.fpp_entry.clear()
        self.motivo_consulta_entry.clear()
        self.enfermedad_actual_entry.clear()
        self.menarquia_entry.clear()
        self.ciclo_entry.clear()
        self.tipo_entry.clear()
        self.prs_entry.clear()
        self.ps_entry.clear()
        self.menopausia_entry.clear()
        self.anticonceptivo_entry.clear()
        self.ets_entry.clear()
        self.planificado_entry.setCurrentIndex(0)
        self.deseado_entry.setCurrentIndex(0)
        self.aceptado_entry.setCurrentIndex(0)
        self.inicio_entry.clear()
        self.sg_entry.clear()
        self.pub_entry.clear()
        self.tab_entry.clear()
        self.privada_entry.clear()
        self.gp_entry.clear()
        self.complicaciones_entry.clear()
        self.inductores_entry.clear()
        self.toxoide_entry.clear()
        self.general_entry.clear()
        self.fc_entry.clear()
        self.fr_entry.clear()
        self.pa_entry.clear()
        self.tem_entry.clear()
        self.t_entry.clear()
        self.p1_entry.clear()
        self.imc_entry.clear()
        self.mamas_entry.clear()
        self.cardio_pulmonar_entry.clear()
        self.abdomen_entry.clear()
        self.genitales_entry.clear()
        self.tacto_entry.clear()
        self.especulo_entry.clear()
        self.extremidades_entry.clear()
        self.neurologico_entry.clear()
        self.diagnostico_admision_entry.clear()
        self.comentarios_entry.clear()

        # Limpiar los campos de Citología
        self.citologia_widget.findChild(QDateEdit, "1CFECHA").setDate(QDate.currentDate())
        self.citologia_widget.findChild(QLineEdit, "1RN").clear()
        self.citologia_widget.findChild(QLineEdit, "1G_MF").clear()
        self.citologia_widget.findChild(QLineEdit, "1PAM").clear()
        self.citologia_widget.findChild(QLineEdit, "1TAN").clear()

        self.citologia_widget.findChild(QDateEdit, "2CFECHA").setDate(QDate.currentDate())
        self.citologia_widget.findChild(QLineEdit, "2RN").clear()
        self.citologia_widget.findChild(QLineEdit, "2G_MF").clear()
        self.citologia_widget.findChild(QLineEdit, "2PAM").clear()
        self.citologia_widget.findChild(QLineEdit, "2TAN").clear()

        self.citologia_widget.findChild(QDateEdit, "3CFECHA").setDate(QDate.currentDate())
        self.citologia_widget.findChild(QLineEdit, "3RN").clear()
        self.citologia_widget.findChild(QLineEdit, "3G_MF").clear()
        self.citologia_widget.findChild(QLineEdit, "3PAM").clear()
        self.citologia_widget.findChild(QLineEdit, "3TAN").clear()

        self.citologia_widget.findChild(QDateEdit, "4CFECHA").setDate(QDate.currentDate())
        self.citologia_widget.findChild(QLineEdit, "4RN").clear()
        self.citologia_widget.findChild(QLineEdit, "4G_MF").clear()
        self.citologia_widget.findChild(QLineEdit, "4PAM").clear()
        self.citologia_widget.findChild(QLineEdit, "4TAN").clear()

        self.citologia_widget.findChild(QDateEdit, "5CFECHA").setDate(QDate.currentDate())
        self.citologia_widget.findChild(QLineEdit, "5RN").clear()
        self.citologia_widget.findChild(QLineEdit, "5G_MF").clear()
        self.citologia_widget.findChild(QLineEdit, "5PAM").clear()
        self.citologia_widget.findChild(QLineEdit, "5TAN").clear()
        
        # Limpiar los campos de Ecosonograma Obstétrico
        self.ecosonograma_widget.findChild(QDateEdit, "1_Fecha_Edad_Gestacional").setDate(QDate.currentDate())
        self.ecosonograma_widget.findChild(QLineEdit, "1_Extrapolado_Para").clear()

        self.ecosonograma_widget.findChild(QDateEdit, "2_Fecha_Edad_Gestacional").setDate(QDate.currentDate())
        self.ecosonograma_widget.findChild(QLineEdit, "2_Extrapolado_Para").clear()

        self.ecosonograma_widget.findChild(QDateEdit, "3_Fecha_Edad_Gestacional").setDate(QDate.currentDate())
        self.ecosonograma_widget.findChild(QLineEdit, "3_Extrapolado_Para").clear()

        self.ecosonograma_widget.findChild(QDateEdit, "4_Fecha_Edad_Gestacional").setDate(QDate.currentDate())
        self.ecosonograma_widget.findChild(QLineEdit, "4_Extrapolado_Para").clear()

        self.ecosonograma_widget.findChild(QDateEdit, "5_Fecha_Edad_Gestacional").setDate(QDate.currentDate())
        self.ecosonograma_widget.findChild(QLineEdit, "5_Extrapolado_Para").clear()

        # Limpiar los campos de Uroanálisis
        self.uroanalisis_widget.findChild(QLineEdit, "1Color").clear()
        self.uroanalisis_widget.findChild(QLineEdit, "1Aspecto").clear()
        self.uroanalisis_widget.findChild(QLineEdit, "1Densidad").clear()
        self.uroanalisis_widget.findChild(QLineEdit, "1Leucocitos").clear()
        self.uroanalisis_widget.findChild(QLineEdit, "1Hematies").clear()
        self.uroanalisis_widget.findChild(QLineEdit, "1Proteinas").clear()
        self.uroanalisis_widget.findChild(QLineEdit, "1Otros").clear()

        self.uroanalisis_widget.findChild(QLineEdit, "2Color").clear()
        self.uroanalisis_widget.findChild(QLineEdit, "2Aspecto").clear()
        self.uroanalisis_widget.findChild(QLineEdit, "2Densidad").clear()
        self.uroanalisis_widget.findChild(QLineEdit, "2Leucocitos").clear()
        self.uroanalisis_widget.findChild(QLineEdit, "2Hematies").clear()
        self.uroanalisis_widget.findChild(QLineEdit, "2Proteinas").clear()
        self.uroanalisis_widget.findChild(QLineEdit, "2Otros").clear()

        self.uroanalisis_widget.findChild(QLineEdit, "3Color").clear()
        self.uroanalisis_widget.findChild(QLineEdit, "3Aspecto").clear()
        self.uroanalisis_widget.findChild(QLineEdit, "3Densidad").clear()
        self.uroanalisis_widget.findChild(QLineEdit, "3Leucocitos").clear()
        self.uroanalisis_widget.findChild(QLineEdit, "3Hematies").clear()
        self.uroanalisis_widget.findChild(QLineEdit, "3Proteinas").clear()
        self.uroanalisis_widget.findChild(QLineEdit, "3Otros").clear()

        self.uroanalisis_widget.findChild(QLineEdit, "4Color").clear()
        self.uroanalisis_widget.findChild(QLineEdit, "4Aspecto").clear()
        self.uroanalisis_widget.findChild(QLineEdit, "4Densidad").clear()
        self.uroanalisis_widget.findChild(QLineEdit, "4Leucocitos").clear()
        self.uroanalisis_widget.findChild(QLineEdit, "4Hematies").clear()
        self.uroanalisis_widget.findChild(QLineEdit, "4Proteinas").clear()
        self.uroanalisis_widget.findChild(QLineEdit, "4Otros").clear()

        # Limpiar la tabla de Laboratorio
        for row in range(self.laboratorio_table.rowCount()):
            for col in range(self.laboratorio_table.columnCount()):
                item = self.laboratorio_table.item(row, col)
                if item is not None:
                    item.setText("")

        # Limpiar la tabla de Radiocefalopelvimetría
        for row in range(self.radiocefalopelvimetria_table.rowCount()):
            for col in range(self.radiocefalopelvimetria_table.columnCount()):
                item = self.radiocefalopelvimetria_table.item(row, col)
                if item is not None:
                    item.setText("")

    def go_back(self):
        self.parent.show_main_menu()

    def convert_to_uppercase(self, text):
        sender = self.sender()
        sender.setText(text.upper())

    def update_age_paciente(self, qdate):
        birthdate = qdate.toPython()  # Convertir QDate a datetime.date
        edad = calculate_age(birthdate)
        self.age_label_paciente.setText(str(edad))

    def mover_cursor_al_inicio(self):
        if self.cedula_entry.text() == "":
            self.cedula_entry.setCursorPosition(0)

    def verificar_cedula(self):
        cedula = self.cedula_entry.text()
        if cedula:
            db = CreateConnection()
            connection = db.create_connection()
            if connection is None:
                QMessageBox.critical(self, "Error", "No se pudo conectar a la base de datos.")
                return

            cursor = connection.cursor()
            try:
                cursor.execute("SELECT * FROM pacientes WHERE cedula = %s", (cedula,))
                paciente = cursor.fetchone()

                if paciente:
                    # Cargar los datos del paciente en el formulario
                    self.primer_nombre_entry.setText(paciente[1])
                    self.segundo_nombre_entry.setText(paciente[2])
                    self.primer_apellido_entry.setText(paciente[3])
                    self.segundo_apellido_entry.setText(paciente[4])
                    
                    fecha_nacimiento = QDate.fromString(str(paciente[5]), "yyyy-MM-dd") if paciente[5] else QDate.currentDate()
                    self.fecha_nacimiento_entry.setDate(fecha_nacimiento)
                    
                    self.telefono_entry.setText(paciente[6])
                    self.genero_entry.setCurrentText(paciente[8])
                    self.estado_civil_entry.setCurrentText(paciente[9])
                    self.nacionalidad_entry.setCurrentText(paciente[11])
                    self.lugar_nacimiento_entry.setText(paciente[7])
                    self.profesion_ocupacion_entry.setText(paciente[12])
                    self.nombre_apellido_emergencia_entry.setText(paciente[14])
                    self.telefono_emergencia_entry.setText(paciente[15])
                    self.parentesco_entry.setText(paciente[16])
                    self.direccion_entry.setText(paciente[10])

                    QMessageBox.information(self, "Información", "Datos del paciente cargados exitosamente.")

                    # Verificar si existe en consultaginecologica y cargar los datos
                    self.cargar_datos_consulta_ginecologica(cedula)
                else:
                    return
            except Exception as e:
                print(f"Error al verificar la cédula: {e}")
                QMessageBox.critical(self, "Error", f"Error al verificar la cédula: {e}")
            finally:
                connection.close()

    def cargar_datos_consulta_ginecologica(self, cedula):
        db = CreateConnection()
        connection = db.create_connection()
        if connection is None:
            QMessageBox.critical(self, "Error", "No se pudo conectar a la base de datos.")
            return

        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM consultaginecologica WHERE paciente_cedula = %s", (cedula,))
            consulta = cursor.fetchone()

            if consulta:
                # Cargar los datos de la consulta ginecológica en el formulario
                self.g_entry.setText(consulta[2] or "")
                self.p_entry.setText(consulta[3] or "")
                self.a_entry.setText(consulta[4] or "")
                self.e_entry.setText(consulta[5] or "")
                self.m_entry.setText(consulta[6] or "")
                self.fur_entry.setText(consulta[7] or "")
                self.fpp_entry.setText(consulta[8] or "")
                self.motivo_consulta_entry.setText(consulta[9] or "")
                self.enfermedad_actual_entry.setText(consulta[10] or "")
                self.menarquia_entry.setText(consulta[11] or "")
                self.ciclo_entry.setText(consulta[12] or "")
                self.tipo_entry.setText(consulta[13] or "")
                self.prs_entry.setText(consulta[14] or "")
                self.ps_entry.setText(consulta[15] or "")
                self.menopausia_entry.setText(consulta[16] or "")
                self.anticonceptivo_entry.setText(consulta[17] or "")
                self.ets_entry.setText(consulta[18] or "")
                self.planificado_entry.setCurrentText(consulta[19] or "N/A")
                self.deseado_entry.setCurrentText(consulta[20] or "N/A")
                self.aceptado_entry.setCurrentText(consulta[21] or "N/A")
                self.inicio_entry.setText(consulta[22] or "")
                self.sg_entry.setText(consulta[23] or "")
                self.pub_entry.setText(consulta[24] or "")
                self.tab_entry.setText(consulta[25] or "")
                self.privada_entry.setText(consulta[26] or "")
                self.gp_entry.setText(consulta[27] or "")
                self.complicaciones_entry.setText(consulta[28] or "")
                self.inductores_entry.setText(consulta[29] or "")
                self.toxoide_entry.setText(consulta[30] or "")
                self.general_entry.setText(consulta[31] or "")
                self.fc_entry.setText(consulta[32] or "")
                self.fr_entry.setText(consulta[33] or "")
                self.pa_entry.setText(consulta[34] or "")
                self.tem_entry.setText(consulta[35] or "")
                self.t_entry.setText(consulta[36] or "")
                self.p1_entry.setText(consulta[37] or "")
                self.imc_entry.setText(consulta[38] or "")
                self.mamas_entry.setText(consulta[39] or "")
                self.cardio_pulmonar_entry.setText(consulta[40] or "")
                self.abdomen_entry.setText(consulta[41] or "")
                self.genitales_entry.setText(consulta[42] or "")
                self.tacto_entry.setText(consulta[43] or "")
                self.especulo_entry.setText(consulta[44] or "")
                self.extremidades_entry.setText(consulta[45] or "")
                self.neurologico_entry.setText(consulta[46] or "")
                self.diagnostico_admision_entry.setText(consulta[47] or "")
                self.comentarios_entry.setText(consulta[48] or "")

                # Citologia
                cfecha1 = QDate.fromString(consulta[49], "yyyy-MM-dd") if consulta[49] else QDate.currentDate()
                self.citologia_widget.findChild(QDateEdit, "1CFECHA").setDate(cfecha1)
                self.citologia_widget.findChild(QLineEdit, "1RN").setText(consulta[50] or "")
                self.citologia_widget.findChild(QLineEdit, "1G_MF").setText(consulta[51] or "")
                self.citologia_widget.findChild(QLineEdit, "1PAM").setText(consulta[52] or "")
                self.citologia_widget.findChild(QLineEdit, "1TAN").setText(consulta[53] or "")

                cfecha2 = QDate.fromString(consulta[54], "yyyy-MM-dd") if consulta[54] else QDate.currentDate()
                self.citologia_widget.findChild(QDateEdit, "2CFECHA").setDate(cfecha2)
                self.citologia_widget.findChild(QLineEdit, "2RN").setText(consulta[55] or "")
                self.citologia_widget.findChild(QLineEdit, "2G_MF").setText(consulta[56] or "")
                self.citologia_widget.findChild(QLineEdit, "2PAM").setText(consulta[57] or "")
                self.citologia_widget.findChild(QLineEdit, "2TAN").setText(consulta[58] or "")

                cfecha3 = QDate.fromString(consulta[59], "yyyy-MM-dd") if consulta[59] else QDate.currentDate()
                self.citologia_widget.findChild(QDateEdit, "3CFECHA").setDate(cfecha3)
                self.citologia_widget.findChild(QLineEdit, "3RN").setText(consulta[60] or "")
                self.citologia_widget.findChild(QLineEdit, "3G_MF").setText(consulta[61] or "")
                self.citologia_widget.findChild(QLineEdit, "3PAM").setText(consulta[62] or "")
                self.citologia_widget.findChild(QLineEdit, "3TAN").setText(consulta[63] or "")

                cfecha4 = QDate.fromString(consulta[64], "yyyy-MM-dd") if consulta[64] else QDate.currentDate()
                self.citologia_widget.findChild(QDateEdit, "4CFECHA").setDate(cfecha4)
                self.citologia_widget.findChild(QLineEdit, "4RN").setText(consulta[65] or "")
                self.citologia_widget.findChild(QLineEdit, "4G_MF").setText(consulta[66] or "")
                self.citologia_widget.findChild(QLineEdit, "4PAM").setText(consulta[67] or "")
                self.citologia_widget.findChild(QLineEdit, "4TAN").setText(consulta[68] or "")

                cfecha5 = QDate.fromString(consulta[69], "yyyy-MM-dd") if consulta[69] else QDate.currentDate()
                self.citologia_widget.findChild(QDateEdit, "5CFECHA").setDate(cfecha5)
                self.citologia_widget.findChild(QLineEdit, "5RN").setText(consulta[70] or "")
                self.citologia_widget.findChild(QLineEdit, "5G_MF").setText(consulta[71] or "")
                self.citologia_widget.findChild(QLineEdit, "5PAM").setText(consulta[72] or "")
                self.citologia_widget.findChild(QLineEdit, "5TAN").setText(consulta[73] or "")

                # Laboratorio
                tipiaje_values = consulta[74].split("-") if consulta[74] else []
                hiv_values = consulta[75].split("-") if consulta[75] else []
                vdrl_values = consulta[76].split("-") if consulta[76] else []
                toxo_test_values = consulta[77].split("-") if consulta[77] else []
                tp_values = consulta[78].split("-") if consulta[78] else []
                tpt_values = consulta[79].split("-") if consulta[79] else []
                wbc_values = consulta[80].split("-") if consulta[80] else []
                linf_values = consulta[81].split("-") if consulta[81] else []
                gran_values = consulta[82].split("-") if consulta[82] else []
                hb_values = consulta[83].split("-") if consulta[83] else []
                hct_values = consulta[84].split("-") if consulta[84] else []
                plt_values = consulta[85].split("-") if consulta[85] else []
                glicemia_values = consulta[86].split("-") if consulta[86] else []
                urea_values = consulta[87].split("-") if consulta[87] else []
                creat_values = consulta[88].split("-") if consulta[88] else []
                bil_total_values = consulta[89].split("-") if consulta[89] else []
                ldh_values = consulta[90].split("-") if consulta[90] else []
                tgo_values = consulta[91].split("-") if consulta[91] else []
                tgp_values = consulta[92].split("-") if consulta[92] else []

                for i in range(self.laboratorio_table.columnCount()):
                    if i < len(tipiaje_values):
                        item = QTableWidgetItem(tipiaje_values[i])
                        self.laboratorio_table.setItem(0, i, item)
                    if i < len(hiv_values):
                        item = QTableWidgetItem(hiv_values[i])
                        self.laboratorio_table.setItem(1, i, item)
                    if i < len(vdrl_values):
                        item = QTableWidgetItem(vdrl_values[i])
                        self.laboratorio_table.setItem(2, i, item)
                    if i < len(toxo_test_values):
                        item = QTableWidgetItem(toxo_test_values[i])
                        self.laboratorio_table.setItem(3, i, item)
                    if i < len(tp_values):
                        item = QTableWidgetItem(tp_values[i])
                        self.laboratorio_table.setItem(4, i, item)
                    if i < len(tpt_values):
                        item = QTableWidgetItem(tpt_values[i])
                        self.laboratorio_table.setItem(5, i, item)
                    if i < len(wbc_values):
                        item = QTableWidgetItem(wbc_values[i])
                        self.laboratorio_table.setItem(6, i, item)
                    if i < len(linf_values):
                        item = QTableWidgetItem(linf_values[i])
                        self.laboratorio_table.setItem(7, i, item)
                    if i < len(gran_values):
                        item = QTableWidgetItem(gran_values[i])
                        self.laboratorio_table.setItem(8, i, item)
                    if i < len(hb_values):
                        item = QTableWidgetItem(hb_values[i])
                        self.laboratorio_table.setItem(9, i, item)
                    if i < len(hct_values):
                        item = QTableWidgetItem(hct_values[i])
                        self.laboratorio_table.setItem(10, i, item)
                    if i < len(plt_values):
                        item = QTableWidgetItem(plt_values[i])
                        self.laboratorio_table.setItem(11, i, item)
                    if i < len(glicemia_values):
                        item = QTableWidgetItem(glicemia_values[i])
                        self.laboratorio_table.setItem(12, i, item)
                    if i < len(urea_values):
                        item = QTableWidgetItem(urea_values[i])
                        self.laboratorio_table.setItem(13, i, item)
                    if i < len(creat_values):
                        item = QTableWidgetItem(creat_values[i])
                        self.laboratorio_table.setItem(14, i, item)
                    if i < len(bil_total_values):
                        item = QTableWidgetItem(bil_total_values[i])
                        self.laboratorio_table.setItem(15, i, item)
                    if i < len(ldh_values):
                        item = QTableWidgetItem(ldh_values[i])
                        self.laboratorio_table.setItem(16, i, item)
                    if i < len(tgo_values):
                        item = QTableWidgetItem(tgo_values[i])
                        self.laboratorio_table.setItem(17, i, item)
                    if i < len(tgp_values):
                        item = QTableWidgetItem(tgp_values[i])
                        self.laboratorio_table.setItem(18, i, item)

                # Uroanalisis
                self.uroanalisis_widget.findChild(QLineEdit, "1Color").setText(consulta[93] or "")
                self.uroanalisis_widget.findChild(QLineEdit, "1Aspecto").setText(consulta[94] or "")
                self.uroanalisis_widget.findChild(QLineEdit, "1Densidad").setText(consulta[95] or "")
                self.uroanalisis_widget.findChild(QLineEdit, "1Leucocitos").setText(consulta[96] or "")
                self.uroanalisis_widget.findChild(QLineEdit, "1Hematies").setText(consulta[97] or "")
                self.uroanalisis_widget.findChild(QLineEdit, "1Proteinas").setText(consulta[98] or "")
                self.uroanalisis_widget.findChild(QLineEdit, "1Otros").setText(consulta[99] or "")

                self.uroanalisis_widget.findChild(QLineEdit, "2Color").setText(consulta[100] or "")
                self.uroanalisis_widget.findChild(QLineEdit, "2Aspecto").setText(consulta[101] or "")
                self.uroanalisis_widget.findChild(QLineEdit, "2Densidad").setText(consulta[102] or "")
                self.uroanalisis_widget.findChild(QLineEdit, "2Leucocitos").setText(consulta[103] or "")
                self.uroanalisis_widget.findChild(QLineEdit, "2Hematies").setText(consulta[104] or "")
                self.uroanalisis_widget.findChild(QLineEdit, "2Proteinas").setText(consulta[105] or "")
                self.uroanalisis_widget.findChild(QLineEdit, "2Otros").setText(consulta[106] or "")

                self.uroanalisis_widget.findChild(QLineEdit, "3Color").setText(consulta[107] or "")
                self.uroanalisis_widget.findChild(QLineEdit, "3Aspecto").setText(consulta[108] or "")
                self.uroanalisis_widget.findChild(QLineEdit, "3Densidad").setText(consulta[109] or "")
                self.uroanalisis_widget.findChild(QLineEdit, "3Leucocitos").setText(consulta[110] or "")
                self.uroanalisis_widget.findChild(QLineEdit, "3Hematies").setText(consulta[111] or "")
                self.uroanalisis_widget.findChild(QLineEdit, "3Proteinas").setText(consulta[112] or "")
                self.uroanalisis_widget.findChild(QLineEdit, "3Otros").setText(consulta[113] or "")

                self.uroanalisis_widget.findChild(QLineEdit, "4Color").setText(consulta[114] or "")
                self.uroanalisis_widget.findChild(QLineEdit, "4Aspecto").setText(consulta[115] or "")
                self.uroanalisis_widget.findChild(QLineEdit, "4Densidad").setText(consulta[116] or "")
                self.uroanalisis_widget.findChild(QLineEdit, "4Leucocitos").setText(consulta[117] or "")
                self.uroanalisis_widget.findChild(QLineEdit, "4Hematies").setText(consulta[118] or "")
                self.uroanalisis_widget.findChild(QLineEdit, "4Proteinas").setText(consulta[119] or "")
                self.uroanalisis_widget.findChild(QLineEdit, "4Otros").setText(consulta[120] or "")

                # Ecosonograma
                fecha_edad_gestacional1 = QDate.fromString(consulta[121], "yyyy-MM-dd") if consulta[121] else QDate.currentDate()
                self.ecosonograma_widget.findChild(QDateEdit, "1_Fecha_Edad_Gestacional").setDate(fecha_edad_gestacional1)
                self.ecosonograma_widget.findChild(QLineEdit, "1_Extrapolado_Para").setText(consulta[122] or "")

                fecha_edad_gestacional2 = QDate.fromString(consulta[123], "yyyy-MM-dd") if consulta[123] else QDate.currentDate()
                self.ecosonograma_widget.findChild(QDateEdit, "2_Fecha_Edad_Gestacional").setDate(fecha_edad_gestacional2)
                self.ecosonograma_widget.findChild(QLineEdit, "2_Extrapolado_Para").setText(consulta[124] or "")

                fecha_edad_gestacional3 = QDate.fromString(consulta[125], "yyyy-MM-dd") if consulta[125] else QDate.currentDate()
                self.ecosonograma_widget.findChild(QDateEdit, "3_Fecha_Edad_Gestacional").setDate(fecha_edad_gestacional3)
                self.ecosonograma_widget.findChild(QLineEdit, "3_Extrapolado_Para").setText(consulta[126] or "")

                fecha_edad_gestacional4 = QDate.fromString(consulta[127], "yyyy-MM-dd") if consulta[127] else QDate.currentDate()
                self.ecosonograma_widget.findChild(QDateEdit, "4_Fecha_Edad_Gestacional").setDate(fecha_edad_gestacional4)
                self.ecosonograma_widget.findChild(QLineEdit, "4_Extrapolado_Para").setText(consulta[128] or "")

                fecha_edad_gestacional5 = QDate.fromString(consulta[129], "yyyy-MM-dd") if consulta[129] else QDate.currentDate()
                self.ecosonograma_widget.findChild(QDateEdit, "5_Fecha_Edad_Gestacional").setDate(fecha_edad_gestacional5)
                self.ecosonograma_widget.findChild(QLineEdit, "5_Extrapolado_Para").setText(consulta[130] or "")

                # Radiocefalopelvimetria
                diametro_values = consulta[131].split("-") if consulta[131] else []
                estrecho_superior_values = consulta[132].split("-") if consulta[132] else []
                estrecho_medio_values = consulta[133].split("-") if consulta[133] else []
                estrecho_inferior_values = consulta[134].split("-") if consulta[134] else []

                for i in range(self.radiocefalopelvimetria_table.columnCount()):
                    if i < len(diametro_values):
                        item = QTableWidgetItem(diametro_values[i])
                        self.radiocefalopelvimetria_table.setItem(0, i, item)
                    if i < len(estrecho_superior_values):
                        item = QTableWidgetItem(estrecho_superior_values[i])
                        self.radiocefalopelvimetria_table.setItem(1, i, item)
                    if i < len(estrecho_medio_values):
                        item = QTableWidgetItem(estrecho_medio_values[i])
                        self.radiocefalopelvimetria_table.setItem(2, i, item)
                    if i < len(estrecho_inferior_values):
                        item = QTableWidgetItem(estrecho_inferior_values[i])
                        self.radiocefalopelvimetria_table.setItem(3, i, item)

                QMessageBox.information(self, "Información", "Datos de la consulta ginecológica cargados exitosamente.")
            else:
                QMessageBox.information(self, "Información", "No se encontró ninguna consulta ginecológica para esta cédula.")

        except Exception as e:
            print(f"Error al cargar los datos de la consulta ginecológica: {e}")
            QMessageBox.critical(self, "Error", f"Error al cargar los datos de la consulta ginecológica: {e}")
        finally:
            connection.close()

    def toggle_embarazo_actual(self):
        if self.embarazo_actual_button.isChecked():
            self.embarazo_actual_button.setArrowType(Qt.DownArrow)
            self.embarazo_actual_widget.setVisible(True)
        else:
            self.embarazo_actual_button.setArrowType(Qt.RightArrow)
            self.embarazo_actual_widget.setVisible(False)

    def toggle_laboratorio(self):
        if self.laboratorio_button.isChecked():
            self.laboratorio_button.setArrowType(Qt.DownArrow)
            self.laboratorio_widget.setVisible(True)
        else:
            self.laboratorio_button.setArrowType(Qt.RightArrow)
            self.laboratorio_widget.setVisible(False)

    def toggle_uroanalisis(self):
        if self.uroanalisis_button.isChecked():
            self.uroanalisis_button.setArrowType(Qt.DownArrow)
            self.uroanalisis_widget.setVisible(True)
        else:
            self.uroanalisis_button.setArrowType(Qt.RightArrow)
            self.uroanalisis_widget.setVisible(False)

    def toggle_ecosonograma(self):
        if self.ecosonograma_button.isChecked():
            self.ecosonograma_button.setArrowType(Qt.DownArrow)
            self.ecosonograma_widget.setVisible(True)
        else:
            self.ecosonograma_button.setArrowType(Qt.RightArrow)
            self.ecosonograma_widget.setVisible(False)

    def toggle_radiocefalopelvimetria(self):
        if self.radiocefalopelvimetria_button.isChecked():
            self.radiocefalopelvimetria_button.setArrowType(Qt.DownArrow)
            self.radiocefalopelvimetria_widget.setVisible(True)
        else:
            self.radiocefalopelvimetria_button.setArrowType(Qt.RightArrow)
            self.radiocefalopelvimetria_widget.setVisible(False)

    def toggle_citologia(self):
        if self.citologia_button.isChecked():
            self.citologia_button.setArrowType(Qt.DownArrow)
            self.citologia_widget.setVisible(True)
        else:
            self.citologia_button.setArrowType(Qt.RightArrow)
            self.citologia_widget.setVisible(False)

    def save_data(self):
        # Obtener los datos de los campos
        cedula = self.cedula_entry.text()
        primer_nombre = self.primer_nombre_entry.text()
        segundo_nombre = self.segundo_nombre_entry.text()
        primer_apellido = self.primer_apellido_entry.text()
        segundo_apellido = self.segundo_apellido_entry.text()
        fecha_nacimiento = self.fecha_nacimiento_entry.date().toString("yyyy-MM-dd")
        telefono = self.telefono_entry.text()
        genero = self.genero_entry.currentText()
        estado_civil = self.estado_civil_entry.currentText()
        nacionalidad = self.nacionalidad_entry.currentText()
        lugar_nacimiento = self.lugar_nacimiento_entry.text()
        profesion_ocupacion = self.profesion_ocupacion_entry.text()
        nombre_apellido_emergencia = self.nombre_apellido_emergencia_entry.text()
        telefono_emergencia = self.telefono_emergencia_entry.text()
        parentesco = self.parentesco_entry.text()
        direccion = self.direccion_entry.text()

        # Datos para la tabla consultaginecologica
        g = self.g_entry.text()
        p = self.p_entry.text()
        a = self.a_entry.text()
        e = self.e_entry.text()
        m = self.m_entry.text()
        fur = self.fur_entry.text()
        fpp = self.fpp_entry.text()
        motivo_consulta = self.motivo_consulta_entry.toPlainText()
        enfermedad_actual = self.enfermedad_actual_entry.toPlainText()
        menarquia = self.menarquia_entry.text()
        ciclo = self.ciclo_entry.text()
        tipo = self.tipo_entry.text()
        prs = self.prs_entry.text()
        ps = self.ps_entry.text()
        menopausia = self.menopausia_entry.text()
        anticonceptivo = self.anticonceptivo_entry.text()
        ets = self.ets_entry.text()
        planificado = self.planificado_entry.currentText()
        deseado = self.deseado_entry.currentText()
        aceptado = self.aceptado_entry.currentText()
        inicio = self.inicio_entry.text()
        sg = self.sg_entry.text()
        pub = self.pub_entry.text()
        tab = self.tab_entry.text()
        privada = self.privada_entry.text()
        gp = self.gp_entry.text()
        complicaciones = self.complicaciones_entry.text()
        inductores = self.inductores_entry.text()
        toxoide = self.toxoide_entry.text()
        general = self.general_entry.toPlainText()
        fc = self.fc_entry.text()
        fr = self.fr_entry.text()
        pa = self.pa_entry.text()
        tem = self.tem_entry.text()
        t = self.t_entry.text()
        p1 = self.p1_entry.text()
        imc = self.imc_entry.text()
        mamas = self.mamas_entry.toPlainText()
        cardio_pulmonar = self.cardio_pulmonar_entry.toPlainText()
        abdomen = self.abdomen_entry.toPlainText()
        genitales = self.genitales_entry.toPlainText()
        tacto = self.tacto_entry.toPlainText()
        especulo = self.especulo_entry.toPlainText()
        extremidades = self.extremidades_entry.toPlainText()
        neurologico = self.neurologico_entry.toPlainText()
        diagnostico_admision = self.diagnostico_admision_entry.toPlainText()
        comentarios = self.comentarios_entry.toPlainText()

        # Obtener los datos de los campos de Citología
        cfecha1 = self.citologia_widget.findChild(QDateEdit, "1CFECHA").date().toString("yyyy-MM-dd")
        rn1 = self.citologia_widget.findChild(QLineEdit, "1RN").text()
        g_mf1 = self.citologia_widget.findChild(QLineEdit, "1G_MF").text()
        pam1 = self.citologia_widget.findChild(QLineEdit, "1PAM").text()
        tan1 = self.citologia_widget.findChild(QLineEdit, "1TAN").text()

        cfecha2 = self.citologia_widget.findChild(QDateEdit, "2CFECHA").date().toString("yyyy-MM-dd")
        rn2 = self.citologia_widget.findChild(QLineEdit, "2RN").text()
        g_mf2 = self.citologia_widget.findChild(QLineEdit, "2G_MF").text()
        pam2 = self.citologia_widget.findChild(QLineEdit, "2PAM").text()
        tan2 = self.citologia_widget.findChild(QLineEdit, "2TAN").text()

        cfecha3 = self.citologia_widget.findChild(QDateEdit, "3CFECHA").date().toString("yyyy-MM-dd")
        rn3 = self.citologia_widget.findChild(QLineEdit, "3RN").text()
        g_mf3 = self.citologia_widget.findChild(QLineEdit, "3G_MF").text()
        pam3 = self.citologia_widget.findChild(QLineEdit, "3PAM").text()
        tan3 = self.citologia_widget.findChild(QLineEdit, "3TAN").text()

        cfecha4 = self.citologia_widget.findChild(QDateEdit, "4CFECHA").date().toString("yyyy-MM-dd")
        rn4 = self.citologia_widget.findChild(QLineEdit, "4RN").text()
        g_mf4 = self.citologia_widget.findChild(QLineEdit, "4G_MF").text()
        pam4 = self.citologia_widget.findChild(QLineEdit, "4PAM").text()
        tan4 = self.citologia_widget.findChild(QLineEdit, "4TAN").text()

        cfecha5 = self.citologia_widget.findChild(QDateEdit, "5CFECHA").date().toString("yyyy-MM-dd")
        rn5 = self.citologia_widget.findChild(QLineEdit, "5RN").text()
        g_mf5 = self.citologia_widget.findChild(QLineEdit, "5G_MF").text()
        pam5 = self.citologia_widget.findChild(QLineEdit, "5PAM").text()
        tan5 = self.citologia_widget.findChild(QLineEdit, "5TAN").text()

        # Obtener los datos de Ecosonograma Obstétrico
        fecha_edad_gestacional1 = self.ecosonograma_widget.findChild(QDateEdit, "1_Fecha_Edad_Gestacional").date().toString("yyyy-MM-dd")
        extrapolado_para1 = self.ecosonograma_widget.findChild(QLineEdit, "1_Extrapolado_Para").text()

        fecha_edad_gestacional2 = self.ecosonograma_widget.findChild(QDateEdit, "2_Fecha_Edad_Gestacional").date().toString("yyyy-MM-dd")
        extrapolado_para2 = self.ecosonograma_widget.findChild(QLineEdit, "2_Extrapolado_Para").text()

        fecha_edad_gestacional3 = self.ecosonograma_widget.findChild(QDateEdit, "3_Fecha_Edad_Gestacional").date().toString("yyyy-MM-dd")
        extrapolado_para3 = self.ecosonograma_widget.findChild(QLineEdit, "3_Extrapolado_Para").text()

        fecha_edad_gestacional4 = self.ecosonograma_widget.findChild(QDateEdit, "4_Fecha_Edad_Gestacional").date().toString("yyyy-MM-dd")
        extrapolado_para4 = self.ecosonograma_widget.findChild(QLineEdit, "4_Extrapolado_Para").text()

        fecha_edad_gestacional5 = self.ecosonograma_widget.findChild(QDateEdit, "5_Fecha_Edad_Gestacional").date().toString("yyyy-MM-dd")
        extrapolado_para5 = self.ecosonograma_widget.findChild(QLineEdit, "5_Extrapolado_Para").text()

        # Obtener los datos de la tabla de Laboratorio
        tipiaje = "-".join([self.laboratorio_table.item(0, i).text() if self.laboratorio_table.item(0, i) else "" for i in range(self.laboratorio_table.columnCount())])
        hiv = "-".join([self.laboratorio_table.item(1, i).text() if self.laboratorio_table.item(1, i) else "" for i in range(self.laboratorio_table.columnCount())])
        vdrl = "-".join([self.laboratorio_table.item(2, i).text() if self.laboratorio_table.item(2, i) else "" for i in range(self.laboratorio_table.columnCount())])
        toxo_test = "-".join([self.laboratorio_table.item(3, i).text() if self.laboratorio_table.item(3, i) else "" for i in range(self.laboratorio_table.columnCount())])
        tp = "-".join([self.laboratorio_table.item(4, i).text() if self.laboratorio_table.item(4, i) else "" for i in range(self.laboratorio_table.columnCount())])
        tpt = "-".join([self.laboratorio_table.item(5, i).text() if self.laboratorio_table.item(5, i) else "" for i in range(self.laboratorio_table.columnCount())])
        wbc = "-".join([self.laboratorio_table.item(6, i).text() if self.laboratorio_table.item(6, i) else "" for i in range(self.laboratorio_table.columnCount())])
        linf = "-".join([self.laboratorio_table.item(7, i).text() if self.laboratorio_table.item(7, i) else "" for i in range(self.laboratorio_table.columnCount())])
        gran = "-".join([self.laboratorio_table.item(8, i).text() if self.laboratorio_table.item(8, i) else "" for i in range(self.laboratorio_table.columnCount())])
        hb = "-".join([self.laboratorio_table.item(9, i).text() if self.laboratorio_table.item(9, i) else "" for i in range(self.laboratorio_table.columnCount())])
        hct = "-".join([self.laboratorio_table.item(10, i).text() if self.laboratorio_table.item(10, i) else "" for i in range(self.laboratorio_table.columnCount())])
        plt = "-".join([self.laboratorio_table.item(11, i).text() if self.laboratorio_table.item(11, i) else "" for i in range(self.laboratorio_table.columnCount())])
        glicemia = "-".join([self.laboratorio_table.item(12, i).text() if self.laboratorio_table.item(12, i) else "" for i in range(self.laboratorio_table.columnCount())])
        urea = "-".join([self.laboratorio_table.item(13, i).text() if self.laboratorio_table.item(13, i) else "" for i in range(self.laboratorio_table.columnCount())])
        creat = "-".join([self.laboratorio_table.item(14, i).text() if self.laboratorio_table.item(14, i) else "" for i in range(self.laboratorio_table.columnCount())])
        bil_total = "-".join([self.laboratorio_table.item(15, i).text() if self.laboratorio_table.item(15, i) else "" for i in range(self.laboratorio_table.columnCount())])
        ldh = "-".join([self.laboratorio_table.item(16, i).text() if self.laboratorio_table.item(16, i) else "" for i in range(self.laboratorio_table.columnCount())])
        tgo = "-".join([self.laboratorio_table.item(17, i).text() if self.laboratorio_table.item(17, i) else "" for i in range(self.laboratorio_table.columnCount())])
        tgp = "-".join([self.laboratorio_table.item(18, i).text() if self.laboratorio_table.item(18, i) else "" for i in range(self.laboratorio_table.columnCount())])

        # Obtener los datos de Uroanálisis
        color1 = self.uroanalisis_widget.findChild(QLineEdit, "1Color").text()
        aspecto1 = self.uroanalisis_widget.findChild(QLineEdit, "1Aspecto").text()
        densidad1 = self.uroanalisis_widget.findChild(QLineEdit, "1Densidad").text()
        leucocitos1 = self.uroanalisis_widget.findChild(QLineEdit, "1Leucocitos").text()
        hematies1 = self.uroanalisis_widget.findChild(QLineEdit, "1Hematies").text()
        proteinas1 = self.uroanalisis_widget.findChild(QLineEdit, "1Proteinas").text()
        otros1 = self.uroanalisis_widget.findChild(QLineEdit, "1Otros").text()

        color2 = self.uroanalisis_widget.findChild(QLineEdit, "2Color").text()
        aspecto2 = self.uroanalisis_widget.findChild(QLineEdit, "2Aspecto").text()
        densidad2 = self.uroanalisis_widget.findChild(QLineEdit, "2Densidad").text()
        leucocitos2 = self.uroanalisis_widget.findChild(QLineEdit, "2Leucocitos").text()
        hematies2 = self.uroanalisis_widget.findChild(QLineEdit, "2Hematies").text()
        proteinas2 = self.uroanalisis_widget.findChild(QLineEdit, "2Proteinas").text()
        otros2 = self.uroanalisis_widget.findChild(QLineEdit, "2Otros").text()

        color3 = self.uroanalisis_widget.findChild(QLineEdit, "3Color").text()
        aspecto3 = self.uroanalisis_widget.findChild(QLineEdit, "3Aspecto").text()
        densidad3 = self.uroanalisis_widget.findChild(QLineEdit, "3Densidad").text()
        leucocitos3 = self.uroanalisis_widget.findChild(QLineEdit, "3Leucocitos").text()
        hematies3 = self.uroanalisis_widget.findChild(QLineEdit, "3Hematies").text()
        proteinas3 = self.uroanalisis_widget.findChild(QLineEdit, "3Proteinas").text()
        otros3 = self.uroanalisis_widget.findChild(QLineEdit, "3Otros").text()

        color4 = self.uroanalisis_widget.findChild(QLineEdit, "4Color").text()
        aspecto4 = self.uroanalisis_widget.findChild(QLineEdit, "4Aspecto").text()
        densidad4 = self.uroanalisis_widget.findChild(QLineEdit, "4Densidad").text()
        leucocitos4 = self.uroanalisis_widget.findChild(QLineEdit, "4Leucocitos").text()
        hematies4 = self.uroanalisis_widget.findChild(QLineEdit, "4Hematies").text()
        proteinas4 = self.uroanalisis_widget.findChild(QLineEdit, "4Proteinas").text()
        otros4 = self.uroanalisis_widget.findChild(QLineEdit, "4Otros").text()

        # Obtener los datos de la tabla de Radiocefalopelvimetría
        diametro = "-".join([self.radiocefalopelvimetria_table.item(0, i).text() if self.radiocefalopelvimetria_table.item(0, i) else "" for i in range(self.radiocefalopelvimetria_table.columnCount())])
        estrecho_superior = "-".join([self.radiocefalopelvimetria_table.item(1, i).text() if self.radiocefalopelvimetria_table.item(1, i) else "" for i in range(self.radiocefalopelvimetria_table.columnCount())])
        estrecho_medio = "-".join([self.radiocefalopelvimetria_table.item(2, i).text() if self.radiocefalopelvimetria_table.item(2, i) else "" for i in range(self.radiocefalopelvimetria_table.columnCount())])
        estrecho_inferior = "-".join([self.radiocefalopelvimetria_table.item(3, i).text() if self.radiocefalopelvimetria_table.item(3, i) else "" for i in range(self.radiocefalopelvimetria_table.columnCount())])

        # Obtener la fecha y hora actual
        fecha_actual = QDate.currentDate().toString("yyyy-MM-dd")
        hora_actual = QTime.currentTime().toString("hh:mm:ss")

        # Conectar a la base de datos y guardar los datos
        db = CreateConnection()
        connection = db.create_connection()
        if connection is None:
            print("Error al conectar a la base de datos")
            return

        cursor = connection.cursor()

        try:
            # Insertar datos en la tabla pacientes
            cursor.execute("""
                INSERT INTO pacientes (cedula, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, fecha_nacimiento, telefono, genero, estado_civil, nacionalidad, lugar_nacimiento, profesion_ocupacion, nombre_apellido_emergencia, telefono_emergencia, parentesco, direccion)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (cedula, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, fecha_nacimiento, telefono, genero, estado_civil, nacionalidad, lugar_nacimiento, profesion_ocupacion, nombre_apellido_emergencia, telefono_emergencia, parentesco, direccion))

            # Insertar datos en la tabla consultaginecologica
            cursor.execute("""
                INSERT INTO consultaginecologica (paciente_cedula, g, p, a, e, m, fur, fpp, motivo_consulta, enfermedad_actual, menarquia, ciclo, tipo, prs, ps, menopausia, anticonceptivo, ets, planificado, deseado, aceptado, inicio, sg, pub, tab, privada, gp, complicaciones, inductores, toxoide, general, fc, fr, pa, tem, t, p1, imc, mamas, cardio_pulmonar, abdomen, genitales, tacto, especulo, extremidades, neurologico, diagnostico_ingreso, comentarios,
                    1cfecha, 1rn, 1g_mf, 1pam, 1tan,
                    2cfecha, 2rn, 2g_mf, 2pam, 2tan,
                    3cfecha, 3rn, 3g_mf, 3pam, 3tan,
                    4cfecha, 4rn, 4g_mf, 4pam, 4tan,
                    5cfecha, 5rn, 5g_mf, 5pam, 5tan,
                    tipiaje, hiv, vdrl, toxo_test, tp, tpt, wbc, linf, gran, hb, hct, plt, glicemia, urea, creat, bil_total, ldh, tgo, tgp,
                    1color, 1aspecto, 1densidad, 1leucocitos, 1hematies, 1proteinas, 1otros,
                    2color, 2aspecto, 2densidad, 2leucocitos, 2hematies, 2proteinas, 2otros,
                    3color, 3aspecto, 3densidad, 3leucocitos, 3hematies, 3proteinas, 3otros,
                    4color, 4aspecto, 4densidad, 4leucocitos, 4hematies, 4proteinas, 4otros,
                    1fecha_edad_gestacional, 1extrapolado_para,
                    2fecha_edad_gestacional, 2extrapolado_para,
                    3fecha_edad_gestacional, 3extrapolado_para,
                    4fecha_edad_gestacional, 4extrapolado_para,
                    5fecha_edad_gestacional, 5extrapolado_para,
                    diametro, estrecho_superior, estrecho_medio, estrecho_inferior,
                    fecha, hora)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                       %s, %s, %s, %s, %s,
                       %s, %s, %s, %s, %s,
                       %s, %s, %s, %s, %s,
                       %s, %s, %s, %s, %s,
                       %s, %s, %s, %s, %s,
                       %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                       %s, %s, %s, %s, %s, %s, %s,
                       %s, %s, %s, %s, %s, %s, %s,
                       %s, %s, %s, %s, %s, %s, %s,
                       %s, %s, %s, %s, %s, %s, %s,
                       %s, %s,
                       %s, %s,
                       %s, %s,
                       %s, %s,
                       %s, %s,
                       %s, %s, %s, %s, %s, %s)
            """, (cedula, g, p, a, e, m, fur, fpp, motivo_consulta, enfermedad_actual, menarquia, ciclo, tipo, prs, ps, menopausia, anticonceptivo, ets, planificado, deseado, aceptado, inicio, sg, pub, tab, privada, gp, complicaciones, inductores, toxoide, general, fc, fr, pa, tem, t, p1, imc, mamas, cardio_pulmonar, abdomen, genitales, tacto, especulo, extremidades, neurologico, diagnostico_admision, comentarios,
                  cfecha1, rn1, g_mf1, pam1, tan1,
                  cfecha2, rn2, g_mf2, pam2, tan2,
                  cfecha3, rn3, g_mf3, pam3, tan3,
                  cfecha4, rn4, g_mf4, pam4, tan4,
                  cfecha5, rn5, g_mf5, pam5, tan5,
                  tipiaje, hiv, vdrl, toxo_test, tp, tpt, wbc, linf, gran, hb, hct, plt, glicemia, urea, creat, bil_total, ldh, tgo, tgp,
                  color1, aspecto1, densidad1, leucocitos1, hematies1, proteinas1, otros1,
                  color2, aspecto2, densidad2, leucocitos2, hematies2, proteinas2, otros2,
                  color3, aspecto3, densidad3, leucocitos3, hematies3, proteinas3, otros3,
                  color4, aspecto4, densidad4, leucocitos4, hematies4, proteinas4, otros4,
                  fecha_edad_gestacional1, extrapolado_para1,
                  fecha_edad_gestacional2, extrapolado_para2,
                  fecha_edad_gestacional3, extrapolado_para3,
                  fecha_edad_gestacional4, extrapolado_para4,
                  fecha_edad_gestacional5, extrapolado_para5,
                  diametro, estrecho_superior, estrecho_medio, estrecho_inferior,
                  fecha_actual, hora_actual))

            # Confirmar la transacción
            connection.commit()
            QMessageBox.information(self, "Éxito", "Datos guardados exitosamente.")
            self.clear_all_fields()  # Limpiar los campos después de guardar
        except Exception as e:
            print(f"Error al guardar los datos: {e}")
            connection.rollback()
            QMessageBox.critical(self, "Error", f"Error al guardar los datos: {e}")
        finally:
            # Cerrar la conexión
            connection.close()