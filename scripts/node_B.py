#!/usr/bin/env python
## asegura que se ejecute como codigo de python

#Nodo B, Recibe de A. Envia a E

#se importan las librerias a utilizar
import rospy
from std_msgs.msg import Bool
from std_msgs.msg import String

## boolvalue es el valor booleano recibido y stringvalue es la cadena de datos a publicar
## Por defecto se asignan los valores false y bajo en 100%
BoolValue = False
StringValue = "alto=0/medio=0/bajo=100"

#Funcion Callback que utiliza los datos leidos 
# Compara con un If y asigna a StringValue una cadena dependiendo del valor de Boolvalue
def callback(datos):
    rospy.loginfo(rospy.get_caller_id() + ' ha recibido: %s', datos.data)
    global BoolValue
    BoolValue = datos.data
    global StringValue
    if BoolValue == False:
	StringValue = "alto=0/medio=0/bajo=100"
    elif BoolValue == True:
	StringValue = "alto=100/medio=0/bajo=0"
    rospy.loginfo(StringValue)

## node_b inicializa el nodo y llama al callback cada vez que recibe un dato
## Publica Stringvalue en el while not.
def node_B():
    pub = rospy.Publisher('stringB', String, queue_size=10)
    rospy.init_node('node_B', anonymous=False)
    rospy.Subscriber('bool', Bool, callback)
    rate = rospy.Rate(1) # 1hz

    while not rospy.is_shutdown():
        pub.publish(StringValue)
        rate.sleep()

if __name__ == '__main__':
    try:
        node_B()
    except rospy.ROSInterruptException:
        pass
