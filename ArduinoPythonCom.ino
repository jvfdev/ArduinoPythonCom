const int led = 13;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(led,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
//  digitalWrite(led,HIGH);
//  delay(500);
//  digitalWrite(led,LOW);
//  delay(500);
    if(Serial.available() > 0){
      switch(Serial.read()){
        case '0': digitalWrite(led,LOW);
                  break;
        case '1': digitalWrite(led,HIGH);
                  break;
        default:  break;
      }
    }
    
}
