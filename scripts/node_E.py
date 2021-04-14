#!/usr/bin/env python
## asegura que se ejecute como codigo de python

## Nodo E, recibe de B y envia a H
#Los nodos E,F,G funcionan de manera similar en la recepcion de los datos
#se importan las librerias
import rospy
from std_msgs.msg import String
# Por defecto se asigna un valor de Bajo al caracter publicado
charE = 'B'

#callback toma el dato string y lo separa para hallar el valor bajo medio y alto enviado mediante split()
def callback(datos):
    global charE
    cadena = datos.data
    rospy.loginfo(cadena)
    partes1= cadena.split('/')
    for i in [0,1,2]:
	partes2= partes1[i].split('=')
	tipo1=partes2[0]
	if tipo1=="bajo":
		bajo=int((partes2[1]))
	if tipo1=="medio":
		medio=int((partes2[1]))
	if tipo1=="alto":
		alto=int((partes2[1]))
    #en este caso el valor booleano solo puede ser  100% alto o 100% bajo
    if alto>bajo:
	charE = 'A'
    else:
	charE = 'B'


#funcion node_E, inicializa el nodo, el publicador, el subscriber y publica el caracter CharE
def node_E():
    #incializacion del publisher
    pub = rospy.Publisher('charE', String, queue_size=1)
    rospy.init_node('node_E', anonymous=False)
    rospy.Subscriber('stringB', String, callback)
    rate = rospy.Rate(0.5) # 0.5hz
    while not rospy.is_shutdown():
        pub.publish(charE)
        rate.sleep()

if __name__ == '__main__':
    try:
        node_E()
    except rospy.ROSInterruptException:
        pass
