const int banda = 7; 
const int piston = 2; 
const int sensor = 10;
int valor = 0; 
int incomingByte;         //Byte de llegada  
int i = 0;    
 
void setup() {
  Serial.begin(9600);
  pinMode(banda, OUTPUT);
  pinMode(piston, OUTPUT);
  pinMode(sensor, INPUT);
}
 
void loop() {
  valor = digitalRead(sensor);            //leer el sensor
  if(valor == HIGH){                       //Si no detecta nada mantiene el led verde encendido, es decir, la banda transportadora encendida
      digitalWrite(banda, HIGH);
      digitalWrite(piston, LOW);
      Serial.write('1');
    }
  if(valor == LOW){                        //Si se detecta algo tenemos que mandar la señal
      Serial.write('2');
  
  }
  incomingByte = Serial.read();
  if (incomingByte == '3') {
      digitalWrite(banda, LOW);
      digitalWrite(piston, HIGH);
      
      while (valor == LOW){
        valor = digitalRead(sensor);
        }      
      digitalWrite(banda, HIGH);
      digitalWrite(piston, LOW);
      }
}
