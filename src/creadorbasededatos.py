import mysql.connector
from mysql.connector import errorcode
from frames.db_config import DB_USER, DB_PASSWORD

class CrearBaseDatos:

    def __init__(self):
        self.connection = None
        self.usuario = DB_USER
        self.contrasena = DB_PASSWORD

    def crear_base_datos(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user=self.usuario,
                password=self.contrasena
            )
            cursor = self.connection.cursor()

            cursor.execute("SHOW DATABASES LIKE 'sistema_informacion_medica'")
            result = cursor.fetchone()
            if (result):
                print("La base de datos 'sistema_informacion_medica' ya existe.")
                cursor.close()
                self.connection.close()
                return 0

            cursor.execute("CREATE DATABASE sistema_informacion_medica")
            cursor.execute("USE sistema_informacion_medica")

            # Crear tablas
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Hospital (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(255) NOT NULL,
                    direccion VARCHAR(255) NOT NULL,
                    telefono VARCHAR(20) NOT NULL,
                    tipo VARCHAR(50) NOT NULL,
                    zona ENUM('Rural', 'Urbana', 'Mixta') NOT NULL
                ) ENGINE=InnoDB
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS MedicoOEnfermero (
                    tipo ENUM('Medico', 'Enfermero') NOT NULL,
                    cedula VARCHAR(20) PRIMARY KEY,
                    primer_nombre VARCHAR(255) NOT NULL,
                    segundo_nombre VARCHAR(255),
                    primer_apellido VARCHAR(255) NOT NULL,
                    segundo_apellido VARCHAR(255),
                    fecha_nacimiento DATE NOT NULL,
                    telefono VARCHAR(20) NOT NULL,
                    direccion VARCHAR(255) NOT NULL,
                    genero ENUM('Masculino', 'Femenino', 'Otros') NOT NULL,
                    estado_civil ENUM('Soltero', 'Casado', 'Viudo', 'Divorciado') NOT NULL,
                    numero_registro_medico VARCHAR(20),
                    especialidad VARCHAR(50),
                    horario_guardia TEXT NOT NULL,
                    hospital_id INT,
                    FOREIGN KEY (hospital_id) REFERENCES Hospital(id)
                ) ENGINE=InnoDB
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Pacientes (
                    cedula VARCHAR(20) PRIMARY KEY,
                    primer_nombre VARCHAR(255) NOT NULL,
                    segundo_nombre VARCHAR(255),
                    primer_apellido VARCHAR(255) NOT NULL,
                    segundo_apellido VARCHAR(255),
                    fecha_nacimiento DATE NOT NULL,
                    telefono VARCHAR(20) NOT NULL,
                    lugar_nacimiento VARCHAR(255) NOT NULL,
                    genero ENUM('Masculino', 'Femenino') NOT NULL,
                    estado_civil ENUM('Soltero', 'Casado', 'Viudo', 'Divorciado') NOT NULL,
                    direccion VARCHAR(255) NOT NULL,
                    nacionalidad VARCHAR(20) NOT NULL,
                    profesion_ocupacion VARCHAR(100) NOT NULL,
                    religion VARCHAR(20) NOT NULL,
                    nombre_apellido_emergencia VARCHAR(255) NOT NULL,
                    telefono_emergencia TEXT NOT NULL,
                    parentesco VARCHAR(20) NOT NULL
                ) ENGINE=InnoDB
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Historia_Clinica_Personal (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    paciente_cedula VARCHAR(20),
                    temperatura DECIMAL(5, 2),
                    pulso INT,
                    respiracion INT,
                    tension_arterial_maxima INT,
                    tension_arterial_minima INT,
                    frecuencia_cardiaca INT,
                    peso DECIMAL(5, 2),
                    talla DECIMAL(5, 2),
                    grasa_corporal DECIMAL(5, 2),
                    indice_masa_corporal DECIMAL(5, 2),
                    motivo_consulta TEXT,
                    enfermedad_actual TEXT,
                    diagnostico_admision TEXT,
                    intervencion_tratamiento TEXT,
                    diagnostico_final TEXT,
                    estado_actual ENUM('Mejora', 'Ingreso', 'Muerte'),
                    autopsia_pedida ENUM('Si', 'No'),
                    fecha_alta DATE,
                    hora_alta TIME,
                    adenitis TEXT,
                    alergia_p TEXT,
                    amigdalitis TEXT,
                    artritis_p TEXT,
                    asma TEXT,
                    Bilharziasis TEXT,
                    blenorragia TEXT,
                    bronquitis TEXT,
                    buba TEXT,
                    catarros TEXT,
                    chagas TEXT,
                    chancros TEXT,
                    difteria TEXT,
                    diarreas TEXT,
                    hansen TEXT,
                    influenzas TEXT,
                    lechina TEXT,
                    necatoriasis TEXT,
                    neumonia TEXT,
                    otitis TEXT,
                    paludismo TEXT,
                    parasitos TEXT,
                    parotiditis TEXT,
                    pleuresia TEXT,
                    quirurgicos TEXT,
                    rinolangititis TEXT,
                    rubeola TEXT,
                    sarampion TEXT,
                    sifilis_p TEXT,
                    sindrome_disentericos TEXT,
                    tuberculosis_p TEXT,
                    tifoidea TEXT,
                    traumatismos TEXT,
                    vacunaciones TEXT,
                    otros TEXT,
                    alergia TEXT,
                    artritis TEXT,
                    cancer TEXT,
                    cardio_vasculares TEXT,
                    diabetes TEXT,
                    enf_digestivas TEXT,
                    enf_renales TEXT,
                    intoxicaciones TEXT,
                    neuromentales TEXT,
                    sifilis TEXT,
                    tuberculosis TEXT,
                    otros_2_12 TEXT,
                    alcohol TEXT,
                    chimo TEXT,
                    deportes TEXT,
                    drogas TEXT,
                    ocupacion TEXT,
                    problemas_familiares TEXT,
                    rasgos_personales TEXT,
                    sexuales TEXT,
                    siesta TEXT,
                    sueño TEXT,
                    tabaco TEXT,
                    otros_3_10 TEXT,
                    aumento_de_peso TEXT,
                    fiebre TEXT,
                    nutricion TEXT,
                    perdida_de_peso TEXT,
                    sudores_nocturnos TEXT,
                    temblores TEXT,
                    otros_4_7 TEXT,
                    FOREIGN KEY (paciente_cedula) REFERENCES Pacientes(cedula)
                ) ENGINE=InnoDB
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Historia_Clinica_Personal1 (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    paciente_cedula VARCHAR(20),     
                    color TEXT,
                    humedad TEXT,
                    contextura TEXT,
                    temperatura TEXT,
                    pigmentacion TEXT,
                    equimosis TEXT,
                    cianosis TEXT,
                    petequias TEXT,
                    erupcion TEXT,
                    unas TEXT,
                    nobulos TEXT,
                    vascularizacion TEXT,
                    cicatrices TEXT,
                    fistulas TEXT,
                    ulceras TEXT,
                    otros_1_16 TEXT,
                    configuracion TEXT,
                    fontanelas TEXT,
                    reblandecimiento TEXT,
                    circunferencia TEXT,
                    dolor_de_cabeza TEXT,
                    cabellos TEXT,
                    otros_2_7 TEXT,
                    conjuntiva TEXT,
                    esclerotica TEXT,
                    cornea TEXT,
                    pupilas TEXT,
                    movimiento TEXT,
                    desviacion TEXT,
                    nistagmus TEXT,
                    ptosis TEXT,
                    exoftalmos TEXT,
                    agudeza_visual TEXT,
                    oftalmoscopicos TEXT,
                    otros_3_12 TEXT,
                    pabellon TEXT,
                    conducto_extremo TEXT,
                    timpano TEXT,
                    audicion TEXT,
                    secreciones TEXT,
                    mastoides TEXT,
                    dolor_de_oido TEXT,
                    otros_4_8 TEXT,
                    fosas_nasales TEXT,
                    mucosas TEXT,
                    tabique TEXT,
                    meatos TEXT,
                    diafanoscopia TEXT,
                    sensibilidad_de_los_senos TEXT,
                    secrecion_nasal TEXT,
                    otros_5_8 TEXT,
                    aliento TEXT,
                    labios TEXT,
                    dientes TEXT,
                    encías TEXT,
                    mucosas_bucales TEXT,
                    lengua TEXT,
                    conductos_salivales TEXT,
                    paralisis_y_trismo TEXT,
                    otros_6_9 TEXT,
                    amigdalas TEXT,
                    adenoides TEXT,
                    rino_faringe TEXT,
                    disfagia TEXT,
                    dolor_de_la_faringe TEXT,
                    otros_7_6 TEXT,
                    movilidad TEXT,
                    ganglios TEXT,
                    tiroides TEXT,
                    vasos TEXT,
                    traquea TEXT,
                    otros_8_6 TEXT,
                    cervicales TEXT,
                    occipitales TEXT,
                    supraclaviculares TEXT,
                    axilares TEXT,
                    epitrocleares TEXT,
                    inguinales TEXT,
                    otros_9_7 TEXT,
                    forma TEXT,
                    simetria TEXT,
                    expansion TEXT,
                    palpitacion TEXT,
                    respiracion TEXT,
                    otros_10_6 TEXT,
                    nodulos TEXT,
                    secreciones_pecho TEXT,
                    pezones TEXT,
                    otros_11_4 TEXT,
                    fremito TEXT,
                    percusion TEXT,
                    auscultacion TEXT,
                    ruidos_adventicios TEXT,
                    pectoriloquia_afona TEXT,
                    broncofonia TEXT,
                    otros_12_7 TEXT,
                    latidos_de_la_punta TEXT,
                    thrill TEXT,
                    pulsacion TEXT,
                    ritmo TEXT,
                    ruidos TEXT,
                    galopes TEXT,
                    frotes TEXT,
                    otros_13_8 TEXT,
                    FOREIGN KEY (paciente_cedula) REFERENCES Pacientes(cedula)
                ) ENGINE=InnoDB
            ''')
                                         
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Historia_Clinica_Personal2 (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    paciente_cedula VARCHAR(20),               
                    pulso_h TEXT,
                    paredes_vasculares TEXT,
                    caracteres TEXT,
                    otros_14_4 TEXT,
                    aspecto TEXT,
                    circunferencia_abdomen TEXT,
                    peristalsis TEXT,
                    cicatrices_abdomen TEXT,
                    defensa TEXT,
                    sensibilidad_abdomen TEXT,
                    contracturas TEXT,
                    tumoraciones TEXT,
                    ascitis TEXT,
                    higado TEXT,
                    rinones TEXT,
                    bazo TEXT,
                    hernias TEXT,
                    otros_15_14 TEXT,
                    cicatrices_genitales TEXT,
                    lesiones TEXT,
                    secreciones_genitales TEXT,
                    escroto TEXT,
                    epididimo TEXT,
                    deferentes TEXT,
                    testiculos TEXT,
                    prostata TEXT,
                    seminales TEXT,
                    otros_16_10 TEXT,
                    labios_genitales TEXT,
                    bartholino TEXT,
                    perine TEXT,
                    vagina TEXT,
                    cuello TEXT,
                    utero TEXT,
                    anexos TEXT,
                    parametrico TEXT,
                    saco_de_douglas TEXT,
                    otros_17_10 TEXT,
                    fisuras TEXT,
                    fistula_anal TEXT,
                    hemorroides TEXT,
                    esfinter TEXT,
                    tumoraciones_anales TEXT,
                    prolapso TEXT,
                    heces TEXT,
                    otros_18_8 TEXT,
                    deformidades TEXT,
                    inflamaciones TEXT,
                    rubicindes TEXT,
                    sensibilidad_muscular TEXT,
                    movimientos TEXT,
                    masas_musculares TEXT,
                    otros_19_7 TEXT,
                    color_piel TEXT,
                    edema TEXT,
                    temblor TEXT,
                    deformidades_piel TEXT,
                    ulceras_piel TEXT,
                    varices TEXT,
                    otros_20_7 TEXT,
                    sensibilidad_objetiva TEXT,
                    motilidad TEXT,
                    reflectividad TEXT,
                    escritura TEXT,
                    troficos TEXT,
                    marcha TEXT,
                    romberg TEXT,
                    orientacion TEXT,
                    lenguaje TEXT,
                    coordinacion TEXT,
                    otros_21_11 TEXT,
                    FOREIGN KEY (paciente_cedula) REFERENCES Pacientes(cedula)
                ) ENGINE=InnoDB
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS ConsultaGinecologica (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    paciente_cedula VARCHAR(20),
                    G TEXT,
                    P TEXT,
                    A TEXT,
                    E TEXT,
                    M TEXT,
                    FUR TEXT,
                    FPP TEXT,
                    motivo_consulta TEXT,
                    enfermedad_actual TEXT,
                    antecedentes_personales TEXT,
                    antecedentes_familiares TEXT,
                    menarquia TEXT,
                    ciclo TEXT,
                    tipo TEXT,
                    prs TEXT,
                    ps TEXT,
                    menopausia TEXT,
                    anticonceptivo TEXT,
                    ets TEXT,
                    planificado TEXT,
                    deseado TEXT,
                    aceptado TEXT,
                    inicio TEXT,
                    sg TEXT,
                    pub TEXT,
                    tab TEXT,
                    privada TEXT,
                    gp TEXT,
                    complicaciones TEXT,
                    inductores TEXT,
                    toxoide TEXT,
                    general TEXT,
                    fc TEXT,
                    fr TEXT,
                    pa TEXT,
                    tem TEXT,
                    t TEXT,
                    p1 TEXT,
                    imc TEXT,
                    mamas TEXT,
                    cardio_pulmonar TEXT,
                    abdomen TEXT,
                    genitales TEXT,
                    tacto TEXT,
                    especulo TEXT,
                    extremidades TEXT,
                    neurologico TEXT,
                    diagnostico_ingreso TEXT,
                    comentarios TEXT,
                    1cfecha TEXT,
                    1rn TEXT,
                    1g_mf TEXT,
                    1pam TEXT,
                    1tan TEXT,
                    2cfecha TEXT,
                    2rn TEXT,
                    2g_mf TEXT,
                    2pam TEXT,
                    2tan TEXT,
                    3cfecha TEXT,
                    3rn TEXT,
                    3g_mf TEXT,
                    3pam TEXT,
                    3tan TEXT,
                    4cfecha TEXT,
                    4rn TEXT,
                    4g_mf TEXT,
                    4pam TEXT,
                    4tan TEXT,
                    5cfecha TEXT,
                    5rn TEXT,
                    5g_mf TEXT,
                    5pam TEXT,
                    5tan TEXT,
                    tipiaje TEXT,
                    hiv TEXT,
                    vdrl TEXT,
                    toxo_test TEXT,
                    tp TEXT,
                    tpt TEXT,
                    wbc TEXT,
                    linf TEXT,
                    gran TEXT,
                    hb TEXT,
                    hct TEXT,
                    plt TEXT,
                    glicemia TEXT,
                    urea TEXT,
                    creat TEXT,
                    bil_total TEXT,
                    ldh TEXT,
                    tgo TEXT,
                    tgp TEXT,
                    1color TEXT,
                    1aspecto TEXT,
                    1densidad TEXT,
                    1leucocitos TEXT,
                    1hematies TEXT,
                    1proteinas TEXT,
                    1otros TEXT,
                    2color TEXT,
                    2aspecto TEXT,
                    2densidad TEXT,
                    2leucocitos TEXT,
                    2hematies TEXT,
                    2proteinas TEXT,
                    2otros TEXT,
                    3color TEXT,
                    3aspecto TEXT,
                    3densidad TEXT,
                    3leucocitos TEXT,
                    3hematies TEXT,
                    3proteinas TEXT,
                    3otros TEXT,
                    4color TEXT,
                    4aspecto TEXT,
                    4densidad TEXT,
                    4leucocitos TEXT,
                    4hematies TEXT,
                    4proteinas TEXT,
                    4otros TEXT,
                    1fecha_edad_gestacional TEXT,
                    1extrapolado_para TEXT,
                    2fecha_edad_gestacional TEXT,
                    2extrapolado_para TEXT,
                    3fecha_edad_gestacional TEXT,
                    3extrapolado_para TEXT,
                    4fecha_edad_gestacional TEXT,
                    4extrapolado_para TEXT,
                    5fecha_edad_gestacional TEXT,
                    5extrapolado_para TEXT,
                    diametro TEXT,
                    estrecho_superior TEXT,
                    estrecho_medio TEXT,
                    estrecho_inferior TEXT,
                    Fecha date,
                    Hora time,
                    FOREIGN KEY (paciente_cedula) REFERENCES Pacientes(cedula)
                ) ENGINE=InnoDB
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS HistoriaClinicaPediatricaExamenFisicoFuncional (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    paciente_cedula VARCHAR(20),
                    antecedentes_prenatales_y_obstetricos TEXT,
                    neonatal TEXT,
                    pan TEXT,
                    tan TEXT,
                    alimentacion TEXT,
                    desarrollo_psicomotor TEXT,
                    habitos_psicobiologicos TEXT,
                    inmunizaciones TEXT,
                    antecedentes_personales TEXT,
                    antecedentes_epidemiologicos TEXT,
                    historia_familiar TEXT,
                    general TEXT,
                    gastrointestinal TEXT,
                    genitourinario TEXT,
                    FOREIGN KEY (paciente_cedula) REFERENCES Pacientes(cedula)
                ) ENGINE=InnoDB
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS HistoriaClinicaPediatricaExamenFisicoIngreso (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    paciente_cedula VARCHAR(20),
                    estado_general TEXT,
                    piel TEXT,
                    cabeza TEXT,
                    ojos TEXT,
                    oidos TEXT,
                    rinofaringe TEXT,
                    boca TEXT,
                    cuello TEXT,
                    ganglios_linfaticos TEXT,
                    torax_y_pulmones TEXT,
                    corazon_y_venas TEXT,
                    abdomen TEXT,
                    urinarios TEXT,
                    genitales TEXT,
                    huesos TEXT,
                    articulaciones TEXT,
                    neurologico TEXT,
                    resumen_de_ingreso TEXT,
                    impresion_diagnostica TEXT,
                    comentario_de_ingreso TEXT,
                    antecedentes_prenatales TEXT,
                    neonatales TEXT,
                    inmunizacion TEXT,
                    FOREIGN KEY (paciente_cedula) REFERENCES Pacientes(cedula)
                ) ENGINE=InnoDB
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS MedicoPaciente (
                    medico_cedula VARCHAR(20),
                    paciente_cedula VARCHAR(20),
                    PRIMARY KEY (medico_cedula, paciente_cedula),
                    FOREIGN KEY (medico_cedula) REFERENCES MedicoOEnfermero(cedula),
                    FOREIGN KEY (paciente_cedula) REFERENCES Pacientes(cedula)
                ) ENGINE=InnoDB
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Inventario (
                    serial VARCHAR(20) PRIMARY KEY,
                    nombre VARCHAR(255) NOT NULL,
                    descripcion TEXT NOT NULL,
                    fecha_incorporacion DATE NOT NULL,
                    fecha_desincorporacion DATE,
                    motivo_desincorporacion TEXT,       
                    hospital_id INT,
                    FOREIGN KEY (hospital_id) REFERENCES Hospital(id)
                ) ENGINE=InnoDB
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Farmacos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    numero_lote VARCHAR(20) NOT NULL,
                    nombre_medicamento VARCHAR(255) NOT NULL,
                    fecha_vencimiento DATE NOT NULL,
                    fecha_elaboracion DATE NOT NULL,
                    cantidad_recibida INT NOT NULL,
                    cantidad_usada INT NOT NULL,
                    cantidad_devuelta INT NOT NULL,
                    cantidad_desechada INT NOT NULL,
                    cantidad_disponible INT NOT NULL,
                    concentracion VARCHAR(20) NOT NULL,
                    forma_farmaceutica VARCHAR(50) NOT NULL,
                    codigo_unidad_contenido VARCHAR(20) NOT NULL,
                    capacidad_unidad_contenido VARCHAR(20) NOT NULL,
                    via_administracion VARCHAR(20) NOT NULL,
                    hospital_id INT,
                    FOREIGN KEY (hospital_id) REFERENCES Hospital(id)
                ) ENGINE=InnoDB
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS MedicoFarmaco (
                    medico_cedula VARCHAR(20),
                    farmaco_id INT,
                    PRIMARY KEY (medico_cedula, farmaco_id),
                    FOREIGN KEY (medico_cedula) REFERENCES MedicoOEnfermero(cedula),
                    FOREIGN KEY (farmaco_id) REFERENCES Farmacos(id)
                ) ENGINE=InnoDB
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS PacienteFarmaco (
                    paciente_cedula VARCHAR(20),
                    farmaco_id INT,
                    PRIMARY KEY (paciente_cedula, farmaco_id),
                    FOREIGN KEY (paciente_cedula) REFERENCES Pacientes(cedula),
                    FOREIGN KEY (farmaco_id) REFERENCES Farmacos(id)
                ) ENGINE=InnoDB
            ''')

            self.connection.commit()
            cursor.close()
            self.connection.close()
            print("Base de datos creada exitosamente.")
            return 0
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error de acceso: nombre de usuario o contraseña incorrectos.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("La base de datos no existe.")
            else:
                print(err)
            return 1

if __name__ == "__main__":
    creador = CrearBaseDatos()
    exit(creador.crear_base_datos())