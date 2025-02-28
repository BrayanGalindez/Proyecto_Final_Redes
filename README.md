# 🌡️ Sistema de Monitoreo de Temperatura en Tiempo Real

Este proyecto permite monitorear la temperatura en tiempo real utilizando un **Arduino**, un **sensor DS18B20** y un **módulo Bluetooth HC-05**. Los datos se envían de forma inalámbrica a una aplicación de escritorio desarrollada en **Python (PyQt5 + Matplotlib)**, que muestra la temperatura en una interfaz gráfica y genera alertas cuando se supera un umbral predefinido. 🚀

---

## 🛠️ Componentes del Proyecto

🔹 **Arduino Uno**: Microcontrolador principal.  
🔹 **Sensor de Temperatura DS18B20**: Sensor digital para medir la temperatura.  
🔹 **Módulo Bluetooth HC-05**: Para la transmisión inalámbrica de datos.  
🔹 **Aplicación de Escritorio**: Desarrollada en Python con **PyQt5** y **Matplotlib**.  

---

## 📌 Configuración del Arduino

### 📂 Archivos del Arduino
La carpeta **`arduino/`** contiene el archivo principal del código **`redes.ino`**.

### 📋 Requisitos
✅ **Arduino IDE**: Descargar e instalar desde [aquí](https://www.arduino.cc/en/software).  
✅ **Librerías necesarias**:
- `OneWire`: Para la comunicación con el sensor DS18B20.
- `DallasTemperature`: Para leer la temperatura del sensor DS18B20.
- `SoftwareSerial`: Para la comunicación serial con el módulo Bluetooth HC-05.

### 📥 Instalación de Librerías
1. Abre el **Arduino IDE**.
2. Ve a `Sketch` > `Include Library` > `Manage Libraries`.
3. Busca e instala las siguientes librerías:
   - ✅ `OneWire`
   - ✅ `DallasTemperature`

4. Conecta el **Arduino Uno** a la PC mediante USB.
5. Abre el archivo **`redes.ino`** y súbelo al Arduino. 🔄

---

## 💻 Aplicación de Escritorio

### 📂 Archivos de la Aplicación
Los archivos de la aplicación están en la carpeta **`app/`**, y contienen:
- 🏷️ `main.py` → Archivo principal que ejecuta la aplicación.
- 🎨 `ui.py` → Archivo encargado de los estilos y la interfaz gráfica.

### 🔧 Instalación de Dependencias
Para ejecutar la aplicación, sigue estos pasos:

1. **Clona este repositorio o descarga los archivos del proyecto**

2. **Abre una terminal en la carpeta del proyecto** y ejecuta:

```bash
# Crear un entorno virtual (recomendado)
python -m venv venv

# Activar el entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### ▶️ Ejecución de la Aplicación
Para iniciar la aplicación, ejecuta el siguiente comando:

```bash
python app/main.py
```

La interfaz gráfica se abrirá mostrando la temperatura en tiempo real. 📊🔥

---

## 🎯 Conclusión
Este sistema permite visualizar la temperatura en tiempo real con una interfaz intuitiva y alertas. Ideal para monitoreo remoto con Arduino y Bluetooth. ¡Pruébalo y mejora tu experiencia con IoT! 🌍⚡

