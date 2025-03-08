from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QStatusBar, QMenu, QPushButton, QWidgetAction, QMessageBox, QStackedWidget, QSizePolicy
from PySide6.QtCore import QTimer, Qt, QPoint, QSize
from PySide6.QtGui import QIcon
from servicios import CreateConnection
import sys
from datetime import datetime
from frames.inicio import Inicio
from frames.medicos_enfermeras import MedicosEnfermeras
from frames.pacientes import Pacientes
from frames.historial_medico import HistorialMedico
from frames.consultas import Consultas
from frames.farmacia import Farmacia
from frames.configuracion import Configuracion

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("C:\\Users\\kervinfb\\OneDrive\\Documents\\Sistema de Informacion Medica\\sistema-informacion-medica\\src\\iconos\\SIMV.png"))
        self.initUI()
        self.initTimer()
        self.setStyleSheet(self.load_stylesheet())

    def load_stylesheet(self):
        with open("c:\\Users\\kervinfb\\OneDrive\\Documents\\Sistema de Informacion Medica\\sistema-informacion-medica\\src\\style.qss", "r") as file:
            return file.read()

    def get_stylesheet(self):
        with open("style.qss", "r") as file:
            return file.read()

    def initUI(self):
        self.setWindowTitle("Resultado de la Conexión")
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.main_layout = QHBoxLayout()
        
        self.menu_layout = QVBoxLayout()
        self.content_layout = QVBoxLayout()
        
        self.etiqueta = QLabel("", self)
        self.content_layout.addWidget(self.etiqueta)
            
        self.status_label = QLabel("", self)
        self.menu_layout.addWidget(self.status_label)
        
        self.main_layout.addLayout(self.menu_layout)
        self.main_layout.addLayout(self.content_layout)
        
        self.central_widget.setLayout(self.main_layout)
        
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        
        self.status_label = QLabel("", self)
        self.status_bar.addPermanentWidget(self.status_label)
        
        self.resize(800, 600)  # Iniciar en pantalla completa

        self.menu_bar = self.menuBar()

        # Crear un espacio antes del ícono de hamburguesa
        espacio_antes_hamburguesa = QLabel()
        espacio_antes_hamburguesa.setFixedWidth(3)  # Ajusta el ancho del espacio a 3 píxeles
        self.menu_bar.setCornerWidget(espacio_antes_hamburguesa, Qt.TopLeftCorner)

        # Agregar el ícono de hamburguesa a la barra de menú izquierda
        self.hamburger_action = QLabel()
        pixmap = QIcon("C:\\Users\\kervinfb\\OneDrive\\Documents\\Sistema de Informacion Medica\\sistema-informacion-medica\\src\\iconos\\ih2.png").pixmap(20, 30)
        mask = pixmap.createMaskFromColor(Qt.transparent)
        pixmap.fill(Qt.black)
        pixmap.setMask(mask)
        self.hamburger_action.setPixmap(pixmap)
        self.hamburger_action.mousePressEvent = self.mostrar_menu_hamburguesa
        self.menu_bar.setCornerWidget(self.hamburger_action, Qt.TopLeftCorner)

        # Crear un espacio antes de la fecha y hora
        espacio_antes_fecha_hora = QWidget()
        espacio_antes_fecha_hora.setFixedWidth(10)  # Ajusta el ancho del espacio según sea necesario
        self.menu_bar.setCornerWidget(espacio_antes_fecha_hora, Qt.TopRightCorner)

        # Crear un QLabel para la fecha y hora
        self.fecha_hora_label = QLabel()
        self.fecha_hora_label.setStyleSheet("font-size: 18px;")  # Incrementar el tamaño de la fuente a 24
        self.menu_bar.setCornerWidget(self.fecha_hora_label, Qt.TopRightCorner)

        # Actualizar la fecha y hora periódicamente
        self.actualizar_fecha_hora()
        self.fecha_hora_timer = QTimer(self)
        self.fecha_hora_timer.timeout.connect(self.actualizar_fecha_hora)
        self.fecha_hora_timer.start(1000)  # Actualizar cada segundo

        # Crear el menú desplegable
        self.menu_hamburguesa = QMenu(self)

        # Crear un layout vertical para los botones dentro del menú hamburguesa
        botones_layout = QVBoxLayout()
        botones_layout.setAlignment(Qt.AlignTop)  # Alinear los botones en la parte superior

        # Crear botones y conectar sus señales
        botones = ["Inicio", "Médicos/Enfermeras", "Pacientes", "Historial Médico", "Consultas", "Farmacia", "Configuración"]
        iconos = [
            "C:\\Users\\kervinfb\\OneDrive\\Documents\\Sistema de Informacion Medica\\sistema-informacion-medica\\src\\iconos\\inicio.png",
            "C:\\Users\\kervinfb\\OneDrive\\Documents\\Sistema de Informacion Medica\\sistema-informacion-medica\\src\\iconos\\medicos.png",
            "C:\\Users\\kervinfb\\OneDrive\\Documents\\Sistema de Informacion Medica\\sistema-informacion-medica\\src\\iconos\\pacientes.png",
            "C:\\Users\\kervinfb\\OneDrive\\Documents\\Sistema de Informacion Medica\\sistema-informacion-medica\\src\\iconos\\historial.png",
            "C:\\Users\\kervinfb\\OneDrive\\Documents\\Sistema de Informacion Medica\\sistema-informacion-medica\\src\\iconos\\consultas.png",
            "C:\\Users\\kervinfb\\OneDrive\\Documents\\Sistema de Informacion Medica\\sistema-informacion-medica\\src\\iconos\\farmacia.png",
            "C:\\Users\\kervinfb\\OneDrive\\Documents\\Sistema de Informacion Medica\\sistema-informacion-medica\\src\\iconos\\config.png"
        ]
        self.buttons = {}
        max_width = 320

        for nombre, icono in zip(botones, iconos):
            boton = QPushButton(nombre)
            boton.setIcon(QIcon(icono))  # Establecer el icono del botón
            boton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  # Permitir que el ancho se ajuste al contenido
            boton.setCheckable(True)  # Hacer el botón checkable
            boton.clicked.connect(lambda checked, n=nombre: self.cambiar_frame(n.replace("<br>", " ")))
            boton.clicked.connect(self.actualizar_botones)  # Conectar la señal para actualizar el estado de los botones
            botones_layout.addWidget(boton)
            self.buttons[nombre] = boton

        # Aplicar estilos a los botones del menú de hamburguesa
        button_style_hamburguesa = """
            QPushButton {
                text-align: left;
                padding: 10px;
                font-size: 18px;  /* Tamaño de fuente más grande */
                color: blue;
                border-radius: 10px;  /* Esquinas redondeadas */
                background-color: #f0f0f0;  /* Color de fondo */
            }

            QPushButton:hover {
                background-color: rgb(128, 128, 128);  /* Color de fondo al pasar el mouse */
                color: white;  /* Color del texto al pasar el mouse */
            }
            QPushButton:checked {
                background-color: silver;  /* Color de fondo cuando está seleccionado */
                color: black;  /* Color del texto cuando está seleccionado */
            }
        """

        for key, button in self.buttons.items():
            button.setIconSize(QSize(24, 24))  # Establecer tamaño del icono
            button.setFixedHeight(40)  # Establecer altura fija para los botones
            button.setStyleSheet(button_style_hamburguesa)

        # Crear un widget para contener el layout de los botones
        botones_widget = QWidget()
        botones_widget.setLayout(botones_layout)

        # Agregar el widget de botones al menú hamburguesa
        action = QWidgetAction(self.menu_hamburguesa)
        action.setDefaultWidget(botones_widget)
        self.menu_hamburguesa.addAction(action)

        # Crear un QStackedWidget para cambiar entre los frames
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # Permitir que el QStackedWidget se expanda

        # Agregar los frames al QStackedWidget
        self.frames = {
            "Inicio": Inicio(),
            "Médicos/Enfermeras": MedicosEnfermeras(),
            "Pacientes": Pacientes(),
            "Historial Médico": HistorialMedico(),
            "Consultas": Consultas(),
            "Farmacia": Farmacia(),
            "Configuración": Configuracion(),
        }
        for frame in self.frames.values():
            self.stacked_widget.addWidget(frame)

        # Agregar el QStackedWidget al layout de contenido
        self.content_layout.addWidget(self.stacked_widget)

        # Mostrar el frame "Inicio" al iniciar la aplicación
        self.cambiar_frame("Inicio")
        self.buttons["Inicio"].setChecked(True)  # Marcar el botón "Inicio" como seleccionado al inicio

    def mostrar_menu_hamburguesa(self, event):
        if self.menu_hamburguesa.isVisible():
            self.menu_hamburguesa.hide()
        else:
            self.menu_hamburguesa.exec(self.hamburger_action.mapToGlobal(QPoint(0, self.hamburger_action.height())))

    def boton_click(self):
        print("Botón presionado")

    def initTimer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_resultado)
        self.timer.start(5000)  # 5000 ms = 5 segundos

    def actualizar_resultado(self):
        createconnection = CreateConnection()
        connection = createconnection.create_connection()
        estado = createconnection.check_connection(connection)
        mensaje = "Conectado" if estado == "Conectado" else "Desconectado"
        self.status_label.setText(mensaje)

    def actualizar_fecha_hora(self):
        now = datetime.now()
        self.fecha_hora_label.setText(now.strftime("%Y-%m-%d %H:%M:%S  "))

    def actualizar_botones(self):
        for boton in self.buttons.values():
            boton.setChecked(False)
        sender = self.sender()
        if sender:
            sender.setChecked(True)

    def cambiar_frame(self, nombre):
        frame = self.frames.get(nombre)
        if frame:
            self.stacked_widget.setCurrentWidget(frame)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Mensaje',
            "¿Está seguro de que desea cerrar la aplicación?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

