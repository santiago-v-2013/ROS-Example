/*
 * Se incluye la libreria de ros serial
 * se establece el tipo de dato a utilizar
 */

#include <ros.h>
#include <std_msgs/Bool.h>
#include <std_msgs/Int16.h>
#include <std_msgs/Float64.h>
#include <std_msgs/String.h>

#include <TimerOne.h>

/******************************************************************/

// se inicializan las variables de ros para los diferentes tipos de dato
ros::NodeHandle  nh;

std_msgs::Bool bool_value;
std_msgs::Int16 int_value;
std_msgs::Float64 float_value;
ros::Publisher pub1("arduinoBool", &bool_value);
ros::Publisher pub2("arduinoInt", &int_value);
ros::Publisher pub3("arduinoFloat", &float_value);

/******************************************************************/

// En esta seccion se definen los pines del arduino
const int pot1 = A6; // entrada analogica potenciometro 1
int val1; //valor potenciometro 1

const int pot2 = A7; // entrada analogica potenciometro 2
int val2; //valor potenciometro 2


// se definen los pines del puente H L298D
const int IN1 = 8; // in1 e in2 se definen para establecer
const int IN2 = 9; // el sentido de giro
const int ENA = 10; // en este pin se define el pwm del motor

const int boton = 4;

/******************************************************************/

// se define el callback donde se envian los datos al motor
void pwmVel(const std_msgs::String& vel_value)
{

  String aux = vel_value.data;
  int vel = aux.toInt();
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  analogWrite(ENA, vel);
   
}

// es la funcion de la interrupcion por timer para mirar cada 5 segundos
// si ha llegado o no el dato

void verify()
{ 

  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  analogWrite(ENA, 0);
  nh.spinOnce();
     
}

// se define el suscriptor
ros::Subscriber<std_msgs::String> sub("velocity",pwmVel);

// se configura el arduino
void setup()
{
  
  nh.initNode();
  nh.advertise(pub1);
  nh.advertise(pub2);
  nh.advertise(pub3);
  nh.subscribe(sub);
  pinMode(boton,INPUT);
  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(13, OUTPUT);

  Timer1.initialize(5000000);         // Dispara cada 2500 ms
  Timer1.attachInterrupt(verify);

}

//se envian los datos leidos en los pines mediante el publicador
void loop()
{

  val1 = analogRead(pot1);
  val2 = analogRead(pot2);
  bool_value.data = digitalRead(boton);
  int_value.data = val1;
  float_value.data = (float)val2/4.0;
  pub1.publish( &bool_value );
  pub2.publish( &int_value );
  pub3.publish( &float_value );
  delay(100);
  
}
