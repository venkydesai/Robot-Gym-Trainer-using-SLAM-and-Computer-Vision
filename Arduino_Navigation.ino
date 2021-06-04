

//Left Side Motor
const int EnableL=5;
const int HighL=6;
const int LowL=7;

//Right Side Motor
const int EnableR=10;
const int HighR=8;
const int LowR=12;

const int D0=2;
const int D1=3;
const int D2=4;


int a,b,c,d,data;
void Data()
{
  a= digitalRead(D0);
  b= digitalRead(D1);
  c= digitalRead(D2);
  

  data=c*4+b*2+a*1;

  
}





void setup() {
 

  pinMode(EnableL,OUTPUT);
  pinMode(HighL,OUTPUT);
  pinMode(EnableL,OUTPUT);

  pinMode(EnableR,OUTPUT);
  pinMode(HighR,OUTPUT);
  pinMode(EnableR,OUTPUT);

  pinMode(D0,INPUT_PULLUP); //INPUT_PULLUP
  pinMode(D1,INPUT_PULLUP);
  pinMode(D2,INPUT_PULLUP);
  



}

void Forward()
{
  digitalWrite(HighL, LOW);
  digitalWrite(LowL, HIGH);
  analogWrite(EnableL,255);
  
  
  digitalWrite(HighR, HIGH);
  digitalWrite(LowR, LOW);
  analogWrite(EnableR,255);
  delay(300);
  Stop();
}

void Backward()
{
  digitalWrite(HighL, HIGH);
  digitalWrite(LowL, LOW);
  analogWrite(EnableL,255);

  
  digitalWrite(HighR, LOW);
  digitalWrite(LowR, HIGH);
  analogWrite(EnableR,255);
}

void Left()
{
  digitalWrite(HighL, HIGH);
  digitalWrite(LowL, LOW);
  analogWrite(EnableL,255);
  
  
  digitalWrite(HighR, HIGH);
  digitalWrite(LowR, LOW);
  analogWrite(EnableR,255);
  delay(600);
  Stop();
}




void Right()
{
  digitalWrite(HighL, LOW);
  digitalWrite(LowL, HIGH);
  analogWrite(EnableL,255);
  
  
  digitalWrite(HighR, LOW);
  digitalWrite(LowR, HIGH);
  analogWrite(EnableR,255);
  delay(300);
  Stop();
}



void Stop()
{
    
  digitalWrite(HighL, LOW);
  digitalWrite(LowL, HIGH);
  analogWrite(EnableL,0);
  
  
  digitalWrite(HighR, HIGH);
  digitalWrite(LowR, LOW);
  analogWrite(EnableR,0);
  
  }  

void loop() {
  Data();
 
  
    if(data==0)
    {
      Forward();
      }
    else if(data==1)
   {
   Backward();
   }  
    else if  (data==2 )
    {
      Stop();
      }
    
    else if(data==3)
    {
   Left();
    }
    
    else if(data==4)
   {
   Right();
   }
   
}
