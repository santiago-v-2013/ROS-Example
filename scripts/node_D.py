#!/usr/bin/env python
## asegura que se ejecute como codigo de python

# Nodo D, recibe de A, Envia a G

#se importan las librerias
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import String

## floatvalue es el valor flotante recibido y stringvalue es la cadena de datos a publicar
## Por defecto se asignan los valores 0 y bajo en 100%
FloatValue = 0
StringValue = "alto=0/medio=0/bajo=100"

#tratamiento del dato leido, se tienen condicionales dependiendo del valor del dato leido.
def callback(datos):
    rospy.loginfo(rospy.get_caller_id() + ' ha recibido %s', datos.data)
    global FloatValue
    FloatValue = datos.data
    global StringValue
    x = FloatValue
    # condicionales que definen los valores de alto medio y bajo siguiendo la logica pseudofuzzy
    if x<=64:
	alto = "0"
	medio = "0"
	bajo = "100"
    elif 64<x<=128:
	alto = "0"
	medio = str(int(round(1.5625*x-100)))
	bajo = str(int(round(-1.5625*x+200)))
    elif 128<x<=192:
	alto = str(int(round(1.5625*x-200)))
	medio = str(int(round(-1.5625*x+300)))
	bajo = "0"
    elif x>192:
	alto = "100"
	medio = "0"
	bajo = "0"
    StringValue = "alto=" + alto + "/" + "medio=" + medio + "/" + "bajo=" +  bajo

#funcion node_D, inicializa el nodo, el publicador, el subscriber y publica la cadena stringvalue
def node_D():
    pub = rospy.Publisher('stringD', String, queue_size=10)
    rospy.init_node('node_D', anonymous=False)
    rospy.Subscriber('float', Float64, callback)
    rate = rospy.Rate(1) # 1hz
    BoolValue = True
    while not rospy.is_shutdown():
        pub.publish(StringValue)
        rate.sleep()

if __name__ == '__main__':
    try:
        node_D()
    except rospy.ROSInterruptException:
        pass

