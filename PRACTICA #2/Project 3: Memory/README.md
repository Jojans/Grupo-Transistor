Memory:

*Bit

El código del DFF que se proporciona en la plataforma nand2tetris servirá para almacenar el valor del bit. El DFF enviará una señal a intervalos regulares, lo que enviará la salida a un multiplexor normal y definirá la entrada al DFF, que será el valor que se almacenará en el bit.

*Register

El registerpuede almacenar 16 bits, por lo que llamamos la función que se hizo anteriormente 16 veces con las entradas.

*RAM8

Es una memoria con 8 slots para guardar datos, como lo indica su nombre. Se tiene una entrada llamada dirección que guardará los in de in[16], además del Dmux que determinará el lugar, para determinar donde se guardan los datos. El chip Mux imprime el espacio de almacenamiento.

*RAM64
El chip RAM8 se utilizará 8 veces para lograr 64 entradas en la memoria, y gracias a la ecuación vectorial con 6 espacios, se puede determinar en qué unidad de RAM8 se guardarán los datos y cuánto espacio de memoria tiene.

*RAM512
A partir de ahora, todas estas RAM realizan un proceso "recursivo" utilizando los chips anteriores para realizar sus procesos. Por ejemplo, en esta RAM512 tenemos 8 chips RAM64 para obtener los 512 que necesitamos, siendo que la entrada address es de 9. Los tres primeros seleccionarán en qué unidad de RAM64 guardarán los datos, y los restantes se guardarán donde se les ha asignado.

*RAM4K
Como en las anteriores, se utilizará el chip RAM512 en 8 repeticiones para obtener los 4000 espacios necesarios para la operación. El acuerdo tiene 12 entradas, y evidentemente, en las 3 primeras se decide en que RAM512 se guardará y en las demás se parará a guardar.

*RAM16K
Para este propósito, se repetirá el mismo procedimiento, pero esta vez utilizaremos nuestro chip anterior, RAM4K, para utilizarlo 8 veces y que nos brinde 16000 espacios de almacenamiento. El administrador tiene 14 entradas, de las cuales las 3 primeras son para determinar en qué unidad de RAM4K se guardarán las entradas restantes.

*PC
Para iniciar el proceso de desarrollo del computador, primero determinamos lo que el computador va a realizar, en este caso un incremento, y tendrá tres funciones: cargar para cargar lo que ya tiene, set para volver el bit a cero e inc para realizar la operación de incremento. Para desarrollar el computador, primero determinamos cual de las tres operaciones se va a realizar, y luego definimos cual de las tres operaciones se va a realizar, guardando la operación realiza


