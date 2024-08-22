Boolean Arithmetic:

*HalfAdder
![image](https://github.com/user-attachments/assets/ecdda16c-173d-4d51-bfe9-ce6a15117dac)

Como se muestra en la tabla, la salida tiene la forma de un Xor y el carry de salida tiene la forma de un and, por lo que simplemente realizamos las dos operaciones con las entradas y asignamos las salidas correspondientes:

*FullAdder
![image](https://github.com/user-attachments/assets/7db09eb4-849f-4dff-8abf-9d5f616fd505)

Para llevar a cabo este componente, primero se realiza una media suma y luego se realiza otra media suma para obtener dos carrys de salida, respectivamente. Con estos dos carrys de salida, generaremos un or para determinar la salida del carry final.

*Add16

Este componente tiene como objetivo realizar 16 sumas, en las que se realiza una media suma para la primera suma, lo que genera un carry que se utilizará para realizar las siguientes 15 sumas completas.

*Inc16

Para desarrollar esta función, se utilizará la función Add16 al pasar la segunda entrada como un vector de unos, lo que dará un incremento de uno a cada uno de los elementos.

*ALU
![image](https://github.com/user-attachments/assets/5305553e-ecf5-4ea9-a6af-c91c2c32367b)

Para el desarrollo de la alu, es necesario contar con los selectores en la cuneta. Para determinar si el selector deja la entrada x y la entrada y o las transforma en un vector de ceros, utilizaremos un multiplexor. Después de esto, obtendremos un nuevo valor de y y un nuevo valor de x que podremos negar o no según el selector. El valor de x y x se negó en un multiplexor y se negó en otro multiplexor, lo que da como resultado dos nuevas salidas de x y y, Realizamos las funciones añadir16 y and16 y las pasamos a otro multiplexor de 16, lo que nos indicará si el valor de x y x se negó en un multiplexor y se negó en otro multiplexor, lo que da como resultado dos nuevas salidas de x y y, Realizamos las funciones add16 y and16 y las pasamos a otro multiplexor de 16, que determinará si se guarda el valor de add16 o and16 o si se debe negar la funcion. Finalmente, se debe analizar la salida porque si es igual a 0 zr debe retornar el valor de 1 y si es menor que 0 ng debe retornar 1.





