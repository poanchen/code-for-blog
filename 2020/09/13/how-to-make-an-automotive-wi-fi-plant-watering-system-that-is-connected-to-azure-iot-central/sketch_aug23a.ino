const int AirValue = 640; // you might need to calibrate this number, instruction is down below
const int WaterValue = 353; // you might need to calibrate this number, instruction is down below
const int SoilMoisturePin = A0;
int soilMoistureValue = 0;
int soilmoisturepercent = 0;

void setup() {
  Serial.begin(115200);
  pinMode(SoilMoisturePin, INPUT);
}

void loop() {
  soilMoistureValue = analogRead(SoilMoisturePin);
  soilmoisturepercent = map(soilMoistureValue, AirValue, WaterValue, 0, 100);
  Serial.print(soilmoisturepercent);
  Serial.println("%");
  delay(60000);
}