# ROS-Publisher y suscriber al mismo tiempo

## Introduccion


_Este proyecto consiste en comunicar nodos de Ros con Arduino por comunicacion serial, Para este fin se hizo uso de un Arduino Mega 2560 y se implementa como un nodo de Ros para la comunicación Serial. Del arduino se envian 3 datos por tres topics diferentes y son recibidos por el nodo A, posteriormente se procesar la información utilizando funciones de pertenecia para finalmente decidir la velocidad del motor de acuerdo a los datos obtenidos.

Para realiza esta tarea se hace la conexion de 11 nodos de manera que se envien diferentes tipos de datos entre ellos y posteriormente se genere envio y recepcion de datos desde un Arduino Mega 2560. Estos nodos se organizan como se observa en la siguiente imagen._

![Imagen 1: Organizacion de Nodos](https://github.com/santiago-v-2013/ROS-Publisher_and_suscriber/blob/main/Imagenes/Nodos.PNG)

## Nodos en Linux

_A continuacion de dara una breve descripcion de los nodos.

* Nodo A: Este nodo es un suscriptor-publicador que recibe los 3 tipos de datos provenientes del Arduino y se los envia posteriormente a los nodos B, C y D.
* Nodos B, C y D: Estos nodos reciben la informacion del nodo A y mediante logica fuzzy haciendo uso de funciones de pertenencia (Imagen 2) evalua los valores para darles un un porcentaje entre bajo, medio y alto.
![Imagen 2: Funciones de membresia](https://github.com/santiago-v-2013/ROS-Publisher_and_suscriber/blob/main/Imagenes/F_membresia.PNG)
* Nodos E, F y G: Estos reciben el procentaje de bajo, medio y alto. Luego de evaluar los datos devuelven la letra B, M o A depenediendo de cual fue el mayor porcentaje y enviar esa letra al nodo H.
* Nodo H: Este nodos a partir de la informacion recibida de los nodos E, F y G envia un valor PWM como accion de control al arduino.
* Nodo Arduino: Este nodo recibe la accion de control y de acuerdo a esta varia la velocidad del motor, seguidamente mide el valor de los sensores y lo envia al nodo A.

### Implementación

_1) Una vez se descargan los directorios se deben poner en la ruta /home/Carpeta Usuario/Catkin_Dir/src/Carpeta_nodo/_
_2) Se debe dar permisos a todos los scrpts de Python chmod_ 
```
chmod +x Nombre_script.py
```
_3) Se debe agregar el directorio de catkin al archivo .bashrc, para esto nos dirigimos a Home de la siguiente manera_

```
cd # con solo cd nos dirigimos a home

sudo gedit .bashrc # Se ejecuta el siguiente codigo

source ~/Catkin_dir/devel/setup.bash # Al final del archivo se pega la linea de codigo

```

### Ejecucion

_1)Para ejecutar el codigo se debe en el terminal ejecutar de la suguiente manera_) )

* En el primer terminal se ejecuta roscore
```
roscore
```


* En un terminal diferente para cada scrpt se ejecuta la siguiente sentencia
```
rosrun Carpeta_nodo Nombre_script.py
```
_2) o se ejecuta el launch de la siguiente manera_

```
roslaunch Carpeta_nodo Nombre_launch.launch

```

## Implementacion Nodo Arduino

_1) Una vez esta el codigo listo se debe ejecutar las siguientes sentencias en el terminal_
```
ls -l /dev | grep ACM # se revisa que hay conectado a los puertos

sudo chmod 777 /dev/ttyACM0 # se le dan los permisos al puerto (El cero puede cambiar esta informacion la entrega la sentencia anterior)
```

_2) Se carga el codigo en el arduino y posteriormente se ejecuta las siguientes sentencias de ROS_
```
roscore # nucleo de ROS se debe correr en un terminal

rosrun rosserial_python serial_node.py /dev/ttyACM0 # En un segundo terminal se corre esta sentencia (Nota: Para que esto sirva se debe instalar la libreria rosserial)
```

## Autores

* Santiago Vasquez
