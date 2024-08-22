Boolean Arithmetic:

*HalfAdder
![image](https://github.com/user-attachments/assets/ecdda16c-173d-4d51-bfe9-ce6a15117dac)
Como se muestra en la tabla, la salida tiene la forma de un Xor y el carry de salida tiene la forma de un and, por lo que simplemente realizamos las dos operaciones con las entradas y asignamos las salidas correspondientes:

*FullAdder
![image](https://github.com/user-attachments/assets/7db09eb4-849f-4dff-8abf-9d5f616fd505)
Para llevar a cabo este componente, primero se realiza una media suma y luego se realiza otra media suma para obtener dos carrys de salida, respectivamente. Con estos dos carrys de salida, generaremos un or para determinar la salida del carry final.

*Add16
Para desarrollar esta función, se utilizará la función Add16 al pasar la segunda entrada como un vector de unos, lo que dará un incremento de uno a cada uno de los elementos.

