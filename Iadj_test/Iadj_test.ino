int led = 8; 
 

void setup() {
  // put your setup code here, to run once:
pinMode(led, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
 analogWrite(led, 25);
}
