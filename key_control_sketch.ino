int inputByte = 0;

void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600);
  while (!Serial)
    digitalWrite(13, HIGH);   
    delay(200);              
    digitalWrite(13, LOW);
    delay(200); 
    ;
}

void loop() {
  inputByte = Serial.read();
  if(inputByte > 0){
    digitalWrite(13, HIGH);   
    delay(150);              
    digitalWrite(13, LOW); 
  }  
}
