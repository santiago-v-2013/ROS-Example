#!/usr/bin/env python
# la linea 1 especifica que este archivo se compila en python

# importar libreria de ros para python
import rospy
from std_msgs.msg import String

#Por defecto los valores que se asignan estan en bajo o en 0 y la velocidad en 60 para el PWM
VelValue = "60"
BoolValue = "B"
val1 = 0
IntValue = "B"
val2 = 0
FloatValue = "B"
val3 = 0
suma = 0

#Al igual que en el nodo A, existe una funcion callback por cada subscriptor y cada una se encarga de asignar el dato recibido a una variable
# en este caso, boolvalue, intvalue y floatvalue son variables string que reciben unicamente un caracter
def callback_bool(datos):
    rospy.loginfo(rospy.get_caller_id() + ' boolChar = %s', datos.data)
    global BoolValue 
    BoolValue = datos.data

def callback_int(datos):
    rospy.loginfo(rospy.get_caller_id() + ' intChar = %s', datos.data)
    global IntValue
    IntValue  = datos.data

def callback_float(datos):
    rospy.loginfo(rospy.get_caller_id() + ' floatChar = %s', datos.data)
    global FloatValue
    FloatValue = datos.data

# esta funcion se encarga de comparar los valores de las tres variables que reciben Alto, Bajo o Medio 
# asi mismo decide el valor de velocidad que debe enviar segun el criterio definido por los diseñadores
def arbol_decision():
    global VelValue

    if BoolValue == "B":
    	val1 = 1
    elif BoolValue == "A":
	val1 = 3

    if FloatValue == "B":
    	val2 = 1
    elif FloatValue == "M":
	val2 = 2
    elif FloatValue == "A":
	val2 = 3

    if IntValue == "B":
    	val3 = 1
    elif IntValue == "M":
	val3 = 2
    elif IntValue == "A":
	val3 = 3

    suma = val1 + val2 + val3

    if suma == 3:
    	VelValue = "100"
    elif suma == 4:
    	VelValue = "126"
    elif suma == 5:
    	VelValue = "152"
    elif suma == 6:
    	VelValue = "178"
    elif suma == 7:
    	VelValue = "204"
    elif suma == 8:
    	VelValue = "230"
    elif suma == 9:
    	VelValue = "255"			
#Esta funcion se ejecuta en el main y contiene la inicializacion del nodo 
#asi como la creacion de los objetos publicadores y subscriptores
def node_H():
    rospy.init_node('node_H', anonymous=False)
    sub1 = rospy.Subscriber('charE', String, callback_bool)
    sub2 = rospy.Subscriber('charF', String, callback_int)
    sub3 = rospy.Subscriber('charG', String, callback_float)
    pub = rospy.Publisher('velocity', String, queue_size=10)
    rate = rospy.Rate(0.2) # 0.2hz
    while not rospy.is_shutdown():
	arbol_decision()
	pub.publish(VelValue)
	rate.sleep()

if __name__ == '__main__':
    try:
        node_H()
    except rospy.ROSInterruptException:
        pass
