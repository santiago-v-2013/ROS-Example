#!/usr/bin/env python
# Asegura que se ejecute como codigo de python

# Nodo G, recibe de D y envia a H
# Los nodos E,F,G funcionan de manera parecida en la recepcion de los datos

# Se importan las librerias
import rospy
from std_msgs.msg import String

# Por defecto se asigna un valor de Bajo al caracter publicado
charG = 'B'

# Callback toma el dato string y lo separa para hallar el valor bajo medio y alto enviado mediante split()
def callback(datos):
    rospy.loginfo(rospy.get_caller_id() + ' I heard %s', datos.data)  
    global charG
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
    rospy.loginfo(rospy.get_caller_id() + ' Alto = %s' + ' Medio = %s' + ' Bajo = %s', alto,medio,bajo)

    # Condicionales para decidir el caracter a enviar
    if alto>bajo and alto>medio:
	charG = 'A'
    elif medio>bajo and medio>alto:
	charG = 'M'
    elif bajo>medio and bajo>alto:
	charG = 'B'
    elif alto>bajo and alto == medio:
	charF = 'A'
    elif medio>bajo and medio == bajo:
	charF = 'M'

# Funcion node_G, inicializa el nodo, el publicador, el subscriber y publica el caracter CharG
def node_G():
    pub = rospy.Publisher('charG', String, queue_size=10)
    rospy.init_node('node_G', anonymous=False)
    rospy.Subscriber('stringD', String, callback)
    rate = rospy.Rate(0.5) # 0.5hz
    while not rospy.is_shutdown():
        pub.publish(charG)
        rate.sleep()

if __name__ == '__main__':
    try:
        node_G()
    except rospy.ROSInterruptException:
        pass
