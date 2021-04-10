// python-build-start
// action, verify
// board, arduino:avr:uno
// port, COM3
// ide, 1.8.13
// python-build-end


#include "Adafruit_Sensor.h"
#include "Adafruit_AM2320.h"

Adafruit_AM2320 am2320 = Adafruit_AM2320();


const int dry = 600; // value for dry / in air sensor
const int wet = 260; // value for wet / in water sensor

void setup()
{ 
  Serial.begin(9600);
    while (!Serial) {
      delay(10); // hang out until serial port opens
    }
  am2320.begin(); // start reading temp/humidity
}

void loop()
{
  int sensorValSoilMoisture = analogRead(A0);
  // map this to 0-100 percentage range - to be further calibrated
  int percentageSoilMoisture = map(sensorValSoilMoisture, wet, dry, 100, 0); 

  Serial.print("Soil: ");Serial.println(percentageSoilMoisture);
  Serial.print("Temp: "); Serial.println(am2320.readTemperature());
  Serial.print("Hum: "); Serial.println(am2320.readHumidity());

  // sleep 
  delay(3000);
}
