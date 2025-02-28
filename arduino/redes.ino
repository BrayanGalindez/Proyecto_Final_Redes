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