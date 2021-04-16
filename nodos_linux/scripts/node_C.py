#!/usr/bin/env python
# asegura que se ejecute como codigo de python

#Nodo C. Envia a F, recibe de A

#se importan las librerias
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import String

# Intvalue es el valor entero recibido y stringvalue es la cadena a publicar
# Por defecto se asignan los valores 0 y bajo en 100%
IntValue = 0
StringValue = "alto=0/medio=0/bajo=100"

#tratamiento del dato leido, se tienen condicionales dependiendo del valor del dato leido. 
def callback(datos):
    rospy.loginfo(rospy.get_caller_id() + ' I heard %s', datos.data)
    global IntValue
    IntValue = datos.data
    global StringValue
    x = float(IntValue)
    
    # condicionales que definen los valores de alto medio y bajo siguiendo la logica pseudofuzzy
    if x<=256:
	alto = "0"
	medio = "0"
	bajo = "100"
    elif 256<x<=512:
	alto = "0"
	medio = str(int(round(0.3906*x-100)))
	bajo = str(int(round(-0.3906*x+200)))
    elif 512<x<=768:
	alto = str(int(round(0.3906*x-200)))
	medio = str(int(round(-0.3906*x+300)))
	bajo = "0"
    elif x>768:
	alto = "100"
	medio = "0"
	bajo = "0"
    StringValue = "alto=" + alto + "/" + "medio=" + medio + "/" + "bajo=" +  bajo

#funcion node_C, inicializa el nodo, el publicador, el subscriber y publica la cadena stringvalue
def node_C():
    pub = rospy.Publisher('stringC', String, queue_size=10)
    rospy.init_node('node_C', anonymous=False)
    rospy.Subscriber('int', Int16, callback)
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        pub.publish(StringValue)
        rate.sleep()

if __name__ == '__main__':
    try:
        node_C()
    except rospy.ROSInterruptException:
        pass
