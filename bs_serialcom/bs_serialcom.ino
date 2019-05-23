void setup() {
  Serial.begin(9600);
  pinMode(13,OUTPUT);
  digitalWrite(13,LOW);
}

void loop() {
  if(Serial.available() > 0){
  char serialData = Serial.read();

  if(serialData == '1')
    digitalWrite(13,HIGH);
  if(serialData == '0')
    digitalWrite(13,LOW);}
}
