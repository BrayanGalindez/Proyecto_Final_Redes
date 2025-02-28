# Sistema de Monitoreo de Temperatura en Tiempo Real

Este proyecto consiste en un sistema de monitoreo de temperatura en tiempo real utilizando un Arduino, un sensor de temperatura DS18B20 y un módulo Bluetooth HC-05. Los datos de temperatura se envían de forma inalámbrica a una aplicación de escritorio desarrollada en Python, que muestra la temperatura en una interfaz gráfica y genera alertas cuando se supera un umbral predefinido.

## Componentes del Proyecto

1. **Arduino Uno**: Microcontrolador principal.
2. **Sensor de Temperatura DS18B20**: Sensor digital para medir la temperatura.
3. **Módulo Bluetooth HC-05**: Para la transmisión inalámbrica de datos.
4. **Aplicación de Escritorio**: Desarrollada en Python con PyQt5 y Matplotlib.

---

## Configuración del Arduino

### Requisitos
- **Arduino IDE**: Descargar e instalar desde [aquí](https://www.arduino.cc/en/software).
- **Librerías necesarias**:
  - `OneWire`: Para la comunicación con el sensor DS18B20.
  - `DallasTemperature`: Para leer la temperatura del sensor DS18B20.
  - `SoftwareSerial`: Para la comunicación serial con el módulo Bluetooth HC-05.

### Instalación de Librerías
1. Abre el Arduino IDE.
2. Ve a `Sketch` > `Include Library` > `Manage Libraries`.
3. Busca e instala las siguientes librerías:
   - `OneWire`
   - `DallasTemperature`

## Aplicacion de escritorio

### Instalación de Dependencias

Para ejecutar la aplicación de escritorio, es necesario instalar las siguientes dependencias:

1. Clona este repositorio o descarga los archivos del proyecto.
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta el siguiente comando para instalar las dependencias:

- Si trabajas en un entorno virtual (recomendado), asegúrate de activarlo antes de instalar las dependencias:

  ```bash
  # Crear un entorno virtual (solo una vez)
  python -m venv venv

  # Activar el entorno virtual
  # En Windows:
  .\venv\Scripts\activate
  # En macOS/Linux:
  source venv/bin/activate

  # Instalar dependencias
  pip install -r requirements.txt
