//Libraries
#include <Adafruit_Sensor.h>
#include <DHT.h>;

//Constants
#define DHTPIN 7 // What pin we are connected to for temp/humidity sensor
#define DHTTYPE DHT22 // DHT 22 (AM2302)
DHT dht(DHTPIN, DHTTYPE); // Initialize DHT sensor for normal 16mhz Arduino

//Variables for temp/humidity and light data
float hum; //Stores humidity value
float temp; //Stores temperature value
float light; //the analog reading from the analog resistor divider (photoresister)

void setup() {
  // put your setup code here, to run once:
  // Set pins as input and output
  pinMode(7, INPUT);
  pinMode(A0, INPUT);

  Serial.begin(9600);
  dht.begin();
  
}

void loop() {
  //put your main code here, to run repeatedly:

  // Read data and store it to variables hum, temp and light
  hum = dht.readHumidity();
  temp = dht.readTemperature();
  light = analogRead(A0);

  // Convert variable data to string
  String humS = "h" + String(hum);
  String tempS = "t" + String(temp);
  String lightS = "c" + String(light);
  Serial.println(humS);
  delay(500);
  Serial.println(tempS);
  delay(500);
  Serial.println(lightS);
  delay(2000);  
  
}
