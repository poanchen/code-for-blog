#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>

const int AirValue = 640; // you might need to calibrate this number, instruction is down below
const int WaterValue = 353; // you might need to calibrate this number, instruction is down below
const int DrySoilMoisturePercentage = 50;
const int SoilMoisturePin = A0;
const int RelayPin = D2;
int soilMoistureValue = 0;
int soilmoisturepercent = 0;
int plantJustWatered = 0;

void setup() {
  Serial.begin(115200);
  WiFi.begin("Wi-Fi name", "Wi-Fi password");
  pinMode(SoilMoisturePin, INPUT);
  pinMode(RelayPin, OUTPUT);
  digitalWrite(RelayPin, HIGH);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Waiting for connection...");
  }
}

void loop() {
  soilMoistureValue = analogRead(SoilMoisturePin);
  soilmoisturepercent = map(soilMoistureValue, AirValue, WaterValue, 0, 100);
  Serial.print(soilmoisturepercent);
  Serial.println("%");
  plantJustWatered = 0;
  if (soilmoisturepercent <= DrySoilMoisturePercentage) {
    Serial.println("Water pumps running...");
    digitalWrite(RelayPin, LOW);
    delay(3500);
    plantJustWatered = 1;
  }
  Serial.println("Water pumps stopped...");
  digitalWrite(RelayPin, HIGH);
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    // get the Azure Functions url by following this doc, https://docs.microsoft.com/azure/azure-functions/functions-create-first-azure-function#test-the-function
    http.begin("http://iotc-fnce72a5dmyl4xs.azurewebsites.net/api/IoTCIntegration?code=1v//IKFDfdJKOdfdsoMKlkpJNOfdoOrpIWuystxtBHJUds==");
    http.addHeader("Content-Type", "application/json");
    // you can get your deviceId by going over this doc, https://docs.microsoft.com/azure/iot-central/core/concepts-get-connected#connect-a-single-device
    String moistureData = "{\"device\": {\"deviceId\": \"1wc1sdkminp\"},\"measurements\": {\"MoisturePercentage\": \"" + String(soilmoisturepercent) + "\", \"PlantJustWatered\": \"" + String(plantJustWatered) + "\"}}";
    int httpCode = http.POST(moistureData);
    if (httpCode == 200) {
      Serial.println("Moisture data sent successfully...");
    } else {
      Serial.println("Moisture data failed to send...");  
    }
    http.end();
  }
  delay(60000);
}