const int AirValue = 640; // you might need to calibrate this number, instruction is down below
const int WaterValue = 353; // you might need to calibrate this number, instruction is down below
const int DrySoilMoisturePercentage = 50;
const int SoilMoisturePin = A0;
const int RelayPin = D2;
int soilMoistureValue = 0;
int soilmoisturepercent = 0;

void setup() {
  Serial.begin(115200);
  pinMode(SoilMoisturePin, INPUT);
  pinMode(RelayPin, OUTPUT);
  digitalWrite(RelayPin, HIGH);
}

void loop() {
  soilMoistureValue = analogRead(SoilMoisturePin);
  soilmoisturepercent = map(soilMoistureValue, AirValue, WaterValue, 0, 100);
  Serial.print(soilmoisturepercent);
  Serial.println("%");
  if (soilmoisturepercent <= DrySoilMoisturePercentage) {
    Serial.println("Water pumps running...");
    digitalWrite(RelayPin, LOW);
    delay(5000);
  }
  Serial.println("Water pumps stopped...");
  digitalWrite(RelayPin, HIGH);
  delay(60000);
}