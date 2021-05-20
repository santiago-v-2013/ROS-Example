#!/usr/bin/env python
# la linea 1 especifica que este archivo se compila en python

# importar libreria de ros para python
import rospy
# importar librerias para el tipo de dato a publicar
from std_msgs.msg import Bool
from std_msgs.msg import Int16
from std_msgs.msg import Float64

# Por defecto se asignan valores de false y 0 a las variables
BoolValue = False
IntValue = 0
FloatValue = 0.00

# Para cada tipo de variable existe un subscriber cuya funcion callback se encarga del dato recibido y lo asigna a la variable correspondiente
def callback_bool(datos):
    rospy.loginfo(rospy.get_caller_id() + ' bool = %s', datos.data)
    global BoolValue 
    BoolValue = datos.data

def callback_int(datos):
    rospy.loginfo(rospy.get_caller_id() + ' int = %s', datos.data)
    global IntValue
    IntValue  = datos.data

def callback_float(datos):
    rospy.loginfo(rospy.get_caller_id() + ' float = %s', datos.data)
    global FloatValue
    FloatValue = datos.data

# Definir la funcion que se ejecuta en el main	
# Node_A se encarga de inicializar el nodo, crear los objetos publicadores y subscriptores; y tambien de publicar las variables bool, int y float recibidas	
def node_A():
    # crear tres objetos publicadores con rospy.Publisher()
    # Es necesario especificar: 
    # el nombre del topic 'topic_name'
    # el tipo de dato a publicar Bool, String, Int16...
    # el tamano de datos que se almacenan en el buffer	
    pub  = rospy.Publisher('bool', Bool, queue_size=10)
    pub2 = rospy.Publisher('int', Int16, queue_size=10)
    pub3 = rospy.Publisher('float', Float64, queue_size=10)
    sub  = rospy.Subscriber('arduinoBool', Bool, callback_bool)
    sub2  = rospy.Subscriber('arduinoInt', Int16, callback_int)
    sub3  = rospy.Subscriber('arduinoFloat', Float64, callback_float)
    rospy.init_node('node_A', anonymous=False)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pub.publish(BoolValue)
        pub2.publish(IntValue)
	pub3.publish(FloatValue)
        rate.sleep()

if __name__ == '__main__':
    try:
        node_A()
    except rospy.ROSInterruptException:
        pass
