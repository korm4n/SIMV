from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QDateEdit, QComboBox, QFormLayout, QScrollArea
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, Qt

class ConsultaGinecologica(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        # Crear un QScrollArea y un widget de contenido
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        content_widget = QWidget()
        scroll_area.setWidget(content_widget)

        layout = QVBoxLayout(content_widget)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(scroll_area)

        form_layout = QFormLayout()
        layout.addLayout(form_layout)

        # Crear un layout horizontal para los campos en una misma línea
        h_layout1 = QHBoxLayout()

        self.cedula_entry = QLineEdit()
        self.cedula_entry.setInputMask("00000000")  # Máscara de entrada para el formato (00000000)
        self.cedula_entry.setFixedWidth(100)
        self.cedula_entry.setPlaceholderText("Cédula")
        self.cedula_entry.editingFinished.connect(self.verificar_cedula)  # Conectar el evento de edición terminada
        self.cedula_entry.textChanged.connect(self.mover_cursor_al_inicio)  # Conectar para mover el cursor al inicio
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
        self.telefono_entry.setInputMask("0000-0000000")  # Máscara de entrada para el formato (0000-0000000)
        self.telefono_entry.setMaxLength(12)
        self.telefono_entry.setFixedWidth(110)
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
        self.nacionalidad_entry.setFixedWidth(90)
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
        self.telefono_emergencia_entry.setInputMask("0000-0000000")  # Máscara de entrada para el formato (0000-0000000)
        self.telefono_emergencia_entry.setMaxLength(12)
        self.telefono_emergencia_entry.setFixedWidth(110)
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

        form_layout.addRow(h_layout4)

   # Crear un layout horizontal para los campos adicionales
        h_layout5 = QHBoxLayout()

        self.g_entry = QLineEdit()
        self.g_entry.setMaxLength(255)
        self.g_entry.setFixedWidth(100)
        h_layout5.addWidget(QLabel("G:"))
        h_layout5.addWidget(self.g_entry)

        self.p_entry = QLineEdit()
        self.p_entry.setMaxLength(255)
        self.p_entry.setFixedWidth(100)
        h_layout5.addWidget(QLabel("P:"))
        h_layout5.addWidget(self.p_entry)

        self.a_entry = QLineEdit()
        self.a_entry.setMaxLength(255)
        self.a_entry.setFixedWidth(100)
        h_layout5.addWidget(QLabel("A:"))
        h_layout5.addWidget(self.a_entry)

        self.e_entry = QLineEdit()
        self.e_entry.setMaxLength(255)
        self.e_entry.setFixedWidth(100)
        h_layout5.addWidget(QLabel("E:"))
        h_layout5.addWidget(self.e_entry)

        self.m_entry = QLineEdit()
        self.m_entry.setMaxLength(255)
        self.m_entry.setFixedWidth(100)
        h_layout5.addWidget(QLabel("M:"))
        h_layout5.addWidget(self.m_entry)

        self.fur_entry = QLineEdit()
        self.fur_entry.setFixedWidth(100)
        h_layout5.addWidget(QLabel("FUR:"))
        h_layout5.addWidget(self.fur_entry)

        self.fpp_entry = QLineEdit()
        self.fpp_entry.setFixedWidth(100)
        h_layout5.addWidget(QLabel("FPP:"))
        h_layout5.addWidget(self.fpp_entry)

        form_layout.addRow(h_layout5)

        # Crear un nuevo layout horizontal para los campos adicionales
        h_layout6 = QHBoxLayout()

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

        form_layout.addRow(h_layout6)

        # Crear un nuevo layout horizontal para los campos adicionales
        h_layout7 = QHBoxLayout()

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

        self.citologia_entry = QLineEdit()
        self.citologia_entry.setMaxLength(255)
        self.citologia_entry.setFixedWidth(100)
        h_layout7.addWidget(QLabel("Citología:"))
        h_layout7.addWidget(self.citologia_entry)

        form_layout.addRow(h_layout7)

        for i in range(1, 9):
            h_layout = QHBoxLayout()

            fecha_entry = QDateEdit()
            fecha_entry.setCalendarPopup(True)
            fecha_entry.setFixedWidth(100)
            h_layout.addWidget(QLabel(f"{i}CFECHA:"))
            h_layout.addWidget(fecha_entry)

            rn_entry = QLineEdit()
            rn_entry.setMaxLength(255)
            rn_entry.setFixedWidth(100)
            h_layout.addWidget(QLabel(f"{i}RN:"))
            h_layout.addWidget(rn_entry)

            g_mf_entry = QLineEdit()
            g_mf_entry.setMaxLength(255)
            g_mf_entry.setFixedWidth(100)
            h_layout.addWidget(QLabel(f"{i}G_MF:"))
            h_layout.addWidget(g_mf_entry)

            pam_entry = QLineEdit()
            pam_entry.setMaxLength(255)
            pam_entry.setFixedWidth(100)
            h_layout.addWidget(QLabel(f"{i}PAM:"))
            h_layout.addWidget(pam_entry)

            tan_entry = QLineEdit()
            tan_entry.setMaxLength(255)
            tan_entry.setFixedWidth(100)
            h_layout.addWidget(QLabel(f"{i}TAN:"))
            h_layout.addWidget(tan_entry)

            form_layout.addRow(h_layout)

        # Crear un layout horizontal para los campos adicionales
        h_layout6 = QHBoxLayout()

        self.embarazo_actual_entry = QLineEdit()
        self.embarazo_actual_entry.setMaxLength(255)
        self.embarazo_actual_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("Embarazo Actual:"))
        h_layout6.addWidget(self.embarazo_actual_entry)

        self.si_entry = QLineEdit()
        self.si_entry.setMaxLength(255)
        self.si_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("SI:"))
        h_layout6.addWidget(self.si_entry)

        self.no_entry = QLineEdit()
        self.no_entry.setMaxLength(255)
        self.no_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("NO:"))
        h_layout6.addWidget(self.no_entry)

        self.planificado_entry = QLineEdit()
        self.planificado_entry.setMaxLength(255)
        self.planificado_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("Planificado:"))
        h_layout6.addWidget(self.planificado_entry)

        self.inicio_entry = QLineEdit()
        self.inicio_entry.setMaxLength(255)
        self.inicio_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("Inicio:"))
        h_layout6.addWidget(self.inicio_entry)

        self.deseado_entry = QLineEdit()
        self.deseado_entry.setMaxLength(255)
        self.deseado_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("Deseado:"))
        h_layout6.addWidget(self.deseado_entry)

        self.pub_entry = QLineEdit()
        self.pub_entry.setMaxLength(255)
        self.pub_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("Pub:"))
        h_layout6.addWidget(self.pub_entry)

        self.aceptado_entry = QLineEdit()
        self.aceptado_entry.setMaxLength(255)
        self.aceptado_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("Aceptado:"))
        h_layout6.addWidget(self.aceptado_entry)

        self.tab_entry = QLineEdit()
        self.tab_entry.setMaxLength(255)
        self.tab_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("TAB:"))
        h_layout6.addWidget(self.tab_entry)

        self.inductores_entry = QLineEdit()
        self.inductores_entry.setMaxLength(255)
        self.inductores_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("Inductores:"))
        h_layout6.addWidget(self.inductores_entry)

        self.toxoide_entry = QLineEdit()
        self.toxoide_entry.setMaxLength(255)
        self.toxoide_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("Toxoide:"))
        h_layout6.addWidget(self.toxoide_entry)

        self.tipiaje_entry = QLineEdit()
        self.tipiaje_entry.setMaxLength(255)
        self.tipiaje_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("TIPIAJE:"))
        h_layout6.addWidget(self.tipiaje_entry)

        self.hiv_entry = QLineEdit()
        self.hiv_entry.setMaxLength(255)
        self.hiv_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("HIV:"))
        h_layout6.addWidget(self.hiv_entry)

        self.vdrl_entry = QLineEdit()
        self.vdrl_entry.setMaxLength(255)
        self.vdrl_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("VDRL:"))
        h_layout6.addWidget(self.vdrl_entry)

        self.toxo_test_entry = QLineEdit()
        self.toxo_test_entry.setMaxLength(255)
        self.toxo_test_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("TOXO_TEST:"))
        h_layout6.addWidget(self.toxo_test_entry)

        self.tp_entry = QLineEdit()
        self.tp_entry.setMaxLength(255)
        self.tp_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("Tp:"))
        h_layout6.addWidget(self.tp_entry)

        self.tpt_entry = QLineEdit()
        self.tpt_entry.setMaxLength(255)
        self.tpt_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("TPT:"))
        h_layout6.addWidget(self.tpt_entry)

        self.wbc_entry = QLineEdit()
        self.wbc_entry.setMaxLength(255)
        self.wbc_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("WBC:"))
        h_layout6.addWidget(self.wbc_entry)

        self.linf_entry = QLineEdit()
        self.linf_entry.setMaxLength(255)
        self.linf_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("Linf:"))
        h_layout6.addWidget(self.linf_entry)

        self.gran_entry = QLineEdit()
        self.gran_entry.setMaxLength(255)
        self.gran_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("gran:"))
        h_layout6.addWidget(self.gran_entry)

        self.hb_entry = QLineEdit()
        self.hb_entry.setMaxLength(255)
        self.hb_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("Hb:"))
        h_layout6.addWidget(self.hb_entry)

        self.hct_entry = QLineEdit()
        self.hct_entry.setMaxLength(255)
        self.hct_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("hct:"))
        h_layout6.addWidget(self.hct_entry)

        self.plt_entry = QLineEdit()
        self.plt_entry.setMaxLength(255)
        self.plt_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("Plt:"))
        h_layout6.addWidget(self.plt_entry)

        self.glicemia_entry = QLineEdit()
        self.glicemia_entry.setMaxLength(255)
        self.glicemia_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("glicemia:"))
        h_layout6.addWidget(self.glicemia_entry)

        self.urea_entry = QLineEdit()
        self.urea_entry.setMaxLength(255)
        self.urea_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("Urea:"))
        h_layout6.addWidget(self.urea_entry)

        self.creat_entry = QLineEdit()
        self.creat_entry.setMaxLength(255)
        self.creat_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("creat:"))
        h_layout6.addWidget(self.creat_entry)

        self.bil_total_entry = QLineEdit()
        self.bil_total_entry.setMaxLength(255)
        self.bil_total_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("Bil_total:"))
        h_layout6.addWidget(self.bil_total_entry)

        self.ldh_entry = QLineEdit()
        self.ldh_entry.setMaxLength(255)
        self.ldh_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("LDH:"))
        h_layout6.addWidget(self.ldh_entry)

        self.tgo_entry = QLineEdit()
        self.tgo_entry.setMaxLength(255)
        self.tgo_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("TGO:"))
        h_layout6.addWidget(self.tgo_entry)

        self.tgp_entry = QLineEdit()
        self.tgp_entry.setMaxLength(255)
        self.tgp_entry.setFixedWidth(100)
        h_layout6.addWidget(QLabel("TGP:"))
        h_layout6.addWidget(self.tgp_entry)

        form_layout.addRow(h_layout6)

           # Crear layouts horizontales para los campos de orina
        for i in range(1, 5):
            h_layout = QHBoxLayout()

            color_entry = QLineEdit()
            color_entry.setMaxLength(255)
            color_entry.setFixedWidth(100)
            h_layout.addWidget(QLabel(f"{i}Color:"))
            h_layout.addWidget(color_entry)

            aspecto_entry = QLineEdit()
            aspecto_entry.setMaxLength(255)
            aspecto_entry.setFixedWidth(100)
            h_layout.addWidget(QLabel(f"{i}Aspecto:"))
            h_layout.addWidget(aspecto_entry)

            densidad_entry = QLineEdit()
            densidad_entry.setMaxLength(255)
            densidad_entry.setFixedWidth(100)
            h_layout.addWidget(QLabel(f"{i}Densidad:"))
            h_layout.addWidget(densidad_entry)

            leucocitos_entry = QLineEdit()
            leucocitos_entry.setMaxLength(255)
            leucocitos_entry.setFixedWidth(100)
            h_layout.addWidget(QLabel(f"{i}Leucocitos:"))
            h_layout.addWidget(leucocitos_entry)

            hematies_entry = QLineEdit()
            hematies_entry.setMaxLength(255)
            hematies_entry.setFixedWidth(100)
            h_layout.addWidget(QLabel(f"{i}Hematíes:"))
            h_layout.addWidget(hematies_entry)

            proteinas_entry = QLineEdit()
            proteinas_entry.setMaxLength(255)
            proteinas_entry.setFixedWidth(100)
            h_layout.addWidget(QLabel(f"{i}Proteínas:"))
            h_layout.addWidget(proteinas_entry)

            otros_entry = QLineEdit()
            otros_entry.setMaxLength(255)
            otros_entry.setFixedWidth(100)
            h_layout.addWidget(QLabel(f"{i}Otros:"))
            h_layout.addWidget(otros_entry)

            form_layout.addRow(h_layout)

        # Crear layouts horizontales para los campos de edad gestacional y extrapolado
        for i in range(1, 6):
            h_layout = QHBoxLayout()

            fecha_edad_gestacional_entry = QDateEdit()
            fecha_edad_gestacional_entry.setCalendarPopup(True)
            fecha_edad_gestacional_entry.setFixedWidth(100)
            h_layout.addWidget(QLabel(f"{i}FECHA_EDAD_GESTACIONAL:"))
            h_layout.addWidget(fecha_edad_gestacional_entry)

            extrapolado_para_entry = QLineEdit()
            extrapolado_para_entry.setMaxLength(255)
            extrapolado_para_entry.setFixedWidth(100)
            h_layout.addWidget(QLabel(f"{i}EXTRAPOLADO_PARA:"))
            h_layout.addWidget(extrapolado_para_entry)

            form_layout.addRow(h_layout)

        # Crear un layout horizontal para los campos adicionales
        h_layout7 = QHBoxLayout()

        self.diametro_entry = QLineEdit()
        self.diametro_entry.setMaxLength(255)
        self.diametro_entry.setFixedWidth(100)
        h_layout7.addWidget(QLabel("Diámetro:"))
        h_layout7.addWidget(self.diametro_entry)

        self.estrecho_superior_entry = QLineEdit()
        self.estrecho_superior_entry.setMaxLength(255)
        self.estrecho_superior_entry.setFixedWidth(100)
        h_layout7.addWidget(QLabel("Estrecho superior:"))
        h_layout7.addWidget(self.estrecho_superior_entry)

        self.ap_entry = QLineEdit()
        self.ap_entry.setMaxLength(255)
        self.ap_entry.setFixedWidth(100)
        h_layout7.addWidget(QLabel("AP:"))
        h_layout7.addWidget(self.ap_entry)

        self.transverso_entry = QLineEdit()
        self.transverso_entry.setMaxLength(255)
        self.transverso_entry.setFixedWidth(100)
        h_layout7.addWidget(QLabel("Transverso:"))
        h_layout7.addWidget(self.transverso_entry)

        self.oblicuo_entry = QLineEdit()
        self.oblicuo_entry.setMaxLength(255)
        self.oblicuo_entry.setFixedWidth(100)
        h_layout7.addWidget(QLabel("Oblicuo:"))
        h_layout7.addWidget(self.oblicuo_entry)

        self.general_entry = QLineEdit()
        self.general_entry.setMaxLength(255)
        self.general_entry.setFixedWidth(100)
        h_layout7.addWidget(QLabel("GENERAL:"))
        h_layout7.addWidget(self.general_entry)

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

        self.mamas_entry = QLineEdit()
        self.mamas_entry.setMaxLength(255)
        self.mamas_entry.setFixedWidth(100)
        h_layout7.addWidget(QLabel("MAMAS:"))
        h_layout7.addWidget(self.mamas_entry)

        self.cardio_pulmonar_entry = QLineEdit()
        self.cardio_pulmonar_entry.setMaxLength(255)
        self.cardio_pulmonar_entry.setFixedWidth(100)
        h_layout7.addWidget(QLabel("CARDIO_PULMONAR:"))
        h_layout7.addWidget(self.cardio_pulmonar_entry)

        self.abdomen_entry = QLineEdit()
        self.abdomen_entry.setMaxLength(255)
        self.abdomen_entry.setFixedWidth(100)
        h_layout7.addWidget(QLabel("ABDOMEN:"))
        h_layout7.addWidget(self.abdomen_entry)

        self.genitales_entry = QLineEdit()
        self.genitales_entry.setMaxLength(255)
        self.genitales_entry.setFixedWidth(100)
        h_layout7.addWidget(QLabel("GENITALES:"))
        h_layout7.addWidget(self.genitales_entry)

        self.tacto_entry = QLineEdit()
        self.tacto_entry.setMaxLength(255)
        self.tacto_entry.setFixedWidth(100)
        h_layout7.addWidget(QLabel("TACTO:"))
        h_layout7.addWidget(self.tacto_entry)

        self.especulo_entry = QLineEdit()
        self.especulo_entry.setMaxLength(255)
        self.especulo_entry.setFixedWidth(100)
        h_layout7.addWidget(QLabel("ESPECULO:"))
        h_layout7.addWidget(self.especulo_entry)

        self.extremidades_entry = QLineEdit()
        self.extremidades_entry.setMaxLength(255)
        self.extremidades_entry.setFixedWidth(100)
        h_layout7.addWidget(QLabel("EXTREMIDADES:"))
        h_layout7.addWidget(self.extremidades_entry)

        self.neurologico_entry = QLineEdit()
        self.neurologico_entry.setMaxLength(255)
        self.neurologico_entry.setFixedWidth(100)
        h_layout7.addWidget(QLabel("NEUROLÓGICO:"))
        h_layout7.addWidget(self.neurologico_entry)

        form_layout.addRow(h_layout7)

        # Crear un layout horizontal para los botones
        button_layout = QHBoxLayout()

        # Configurar el botón de "Atrás"
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

    def go_back(self):
        self.parent.show_main_menu()

    def save_data(self):
        # Aquí puedes agregar la lógica para guardar los datos
        pass

    def convert_to_uppercase(self, text):
        sender = self.sender()
        sender.setText(text.upper())

    def update_age_paciente(self, date):
        # Aquí puedes agregar la lógica para calcular la edad a partir de la fecha de nacimiento
        pass

    def mover_cursor_al_inicio(self):
        if self.cedula_entry.text() == "":
            self.cedula_entry.setCursorPosition(0)

    def verificar_cedula(self):
        # Aquí puedes agregar la lógica para verificar la cédula
        pass