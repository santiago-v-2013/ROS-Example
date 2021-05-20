# ROS-Publisher y suscriber al mismo tiempo

## Introduccion

_En este proyecto de ejemplo se realiza la conexion de 11 nodos de manera que se envien diferentes tipos de datos entre ellos y posteriormente se genere envio y recepcion de datos desde un Arduino Mega 2560_

## Nodos en Linux

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
