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

### Código de Arduino
El siguiente código configura el Arduino para leer la temperatura del sensor DS18B20 y enviar los datos a través del módulo Bluetooth HC-05.

```cpp
#include <SoftwareSerial.h>
#include <OneWire.h>
#include <DallasTemperature.h>

#define ONE_WIRE_BUS 2

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

SoftwareSerial BTSerial(10, 11); // RX, TX

void setup() {
  Serial.begin(9600);
  BTSerial.begin(9600);
  sensors.begin();
}

void loop() {
  sensors.requestTemperatures();
  float temperatureC = sensors.getTempCByIndex(0);
  
  String data = String(temperatureC) + " °C";
  
  // Envía los datos por Bluetooth
  BTSerial.println(data);
  
  // Muestra los datos en el Serial Monitor
  Serial.println(data);
  
  delay(1000);
}
