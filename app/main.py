import sys
import serial
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel
from PyQt5.QtCore import QTimer, Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.dates as mdates

class TemperatureUI(QWidget):
    def __init__(self):
        super().__init__()

        # Widget y Layout
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        # Etiqueta para mostrar la temperatura
        self.temperature_label = QLabel("Esperando datos...", self)
        self.temperature_label.setAlignment(Qt.AlignCenter)  # Centrado de texto
        self.temperature_label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: #fff;
            background-color: #2c3e50;
            padding: 10px;
            border-radius: 8px;
        """)
        self.layout.addWidget(self.temperature_label)

        # Botón para mostrar/ocultar el gráfico en tiempo real
        self.toggle_plot_button = QPushButton("Mostrar Gráfico en Tiempo Real", self)
        self.toggle_plot_button.setStyleSheet("""
            font-size: 16px;
            font-weight: bold;
            color: #fff;
            background-color: #3498db;
            padding: 10px;
            border-radius: 8px;
        """)
        self.layout.addWidget(self.toggle_plot_button)

        # Estilo del widget principal
        self.setStyleSheet("""
            background-color: #34495e;
            border-radius: 12px;
        """)


class TemperatureApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle("Monitor de Temperatura")
        self.setGeometry(100, 100, 800, 600)  # Ventana más grande
        self.setStyleSheet("background-color: #34495e;")  # Fondo oscuro para la ventana

        # Inicializar la interfaz gráfica
        self.ui = TemperatureUI()  # Crear instancia de la UI
        self.setCentralWidget(self.ui)

        # Configuración del puerto serial (Bluetooth)
        self.serial_port = serial.Serial('COM9', 9600, timeout=1)
        print("Conectado al puerto serial:", self.serial_port.name)

        # Temporizador para leer datos del puerto serial
        self.timer = QTimer()
        self.timer.timeout.connect(self.read_serial_data)
        self.timer.start(1000)  # Lee cada 1 segundo

        # Umbral de temperatura para la alerta
        self.temperature_threshold = 27  # Umbral de 27°C

        # Lista para almacenar las temperaturas y sus timestamps
        self.temperature_data = []

        # Configuración del gráfico en tiempo real
        self.real_time_plot_enabled = False
        self.setup_real_time_plot()

        # Conectar el botón para mostrar/ocultar el gráfico en tiempo real
        self.ui.toggle_plot_button.clicked.connect(self.toggle_real_time_plot)

    def setup_real_time_plot(self):
        """Configura el gráfico en tiempo real."""
        # Crear una figura de Matplotlib
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)

        # Configurar el gráfico
        self.ax.set_title("Gráfico de Temperatura en Tiempo Real")
        self.ax.set_xlabel("Tiempo")
        self.ax.set_ylabel("Temperatura (°C)")
        self.ax.grid(True)

        # Inicializar listas para los datos del gráfico
        self.timestamps = []
        self.temperatures = []

        # Agregar el gráfico a la interfaz
        self.ui.layout.addWidget(self.canvas)
        self.canvas.setVisible(False)  # Ocultar inicialmente

    def toggle_real_time_plot(self):
        """Muestra u oculta el gráfico en tiempo real."""
        self.real_time_plot_enabled = not self.real_time_plot_enabled
        self.canvas.setVisible(self.real_time_plot_enabled)
        if self.real_time_plot_enabled:
            self.ui.toggle_plot_button.setText("Ocultar Gráfico en Tiempo Real")
        else:
            self.ui.toggle_plot_button.setText("Mostrar Gráfico en Tiempo Real")

    def read_serial_data(self):
        if self.serial_port.in_waiting > 0:
            # Leer la línea de datos enviada por el Arduino
            data = self.serial_port.readline().decode('utf-8').strip()
            print("Datos recibidos:", data)

            try:
                # Extraer la parte numérica de la cadena (eliminar "Temperatura: " y " °C")
                temperature_str = data.replace("Temperatura: ", "").replace(" °C", "")
                # Convertir los datos a float (temperatura)
                temperature = float(temperature_str)
                # Actualizar la etiqueta con la temperatura
                self.ui.temperature_label.setText(f"{temperature}°C")

                # Guardar la temperatura y el timestamp
                timestamp = datetime.now()
                self.temperature_data.append((timestamp, temperature))

                # Actualizar el gráfico en tiempo real si está habilitado
                if self.real_time_plot_enabled:
                    self.timestamps.append(timestamp)
                    self.temperatures.append(temperature)

                    # Limitar el número de puntos en el gráfico (opcional)
                    if len(self.timestamps) > 60:  # Mostrar solo los últimos 60 puntos
                        self.timestamps.pop(0)
                        self.temperatures.pop(0)

                    # Actualizar el gráfico
                    self.ax.clear()
                    self.ax.plot(self.timestamps, self.temperatures, marker="o", linestyle="-", color="b")
                    self.ax.set_title("Gráfico de Temperatura en Tiempo Real")
                    self.ax.set_xlabel("Tiempo")
                    self.ax.set_ylabel("Temperatura (°C)")
                    self.ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
                    self.ax.grid(True)
                    self.figure.autofmt_xdate()
                    self.canvas.draw()

                # Verificar si la temperatura supera el umbral
                if temperature > self.temperature_threshold:
                    # Cambiar el estilo para alerta
                    self.ui.temperature_label.setStyleSheet("""
                        font-size: 24px;
                        font-weight: bold;
                        color: #fff;
                        background-color: #e74c3c;
                        padding: 10px;
                        border-radius: 8px;
                    """)
                else:
                    # Restaurar el estilo normal
                    self.ui.temperature_label.setStyleSheet("""
                        font-size: 24px;
                        font-weight: bold;
                        color: #fff;
                        background-color: #2c3e50;
                        padding: 10px;
                        border-radius: 8px;
                    """)
            except ValueError:
                print("Error: No se pudo convertir los datos a temperatura.")

    def closeEvent(self, event):
        # Cerrar el puerto serial al cerrar la aplicación
        self.serial_port.close()
        print("Puerto serial cerrado.")
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TemperatureApp()
    window.show()
    sys.exit(app.exec_())