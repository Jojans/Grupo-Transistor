Boolean Logic:

Cualquier aparato electrónico que se tome tiene como base fundamental y esencial el uso de compuertas lógicas, estas trabajan con el algebra booleana para llevar a cabo tareas pertinentes, pero existe un problema, llegar a entender dichas compuertas de manera dinámica y cabal no es algo sencillo. Es por ello que se propone la siguiente práctica en donde con ayuda del software NAND2Tetris se busca entender con comodidad los saberes que son menester para una correcta compresión de los aparatos electrónicos en su capa fundamental, esto con ayuda de la programación.

*Not

![image](https://github.com/user-attachments/assets/dc2279d8-0569-4b2d-9661-fe5e9d12ee80)

La compuerta NAND permite la implementación de esta compuerta, en la que ambas entradas siempre tienen el mismo valor, lo que resulta en la negación del valor de la entrada inicial.

*And

Utilizamos la compuerta NOT previamente construida para crear esta compuerta y simplemente negamos las salidas del valor NAND.

*Or

Para construir esta compuerta, simplemente ejecutamos una operación AND con las entradas negadas.

*Xor

![image](https://github.com/user-attachments/assets/92f518c3-5baf-4fe3-92b8-3675995a6277)

Para comenzar a diseñar esta compuerta, invertimos cada una de las entradas. Luego, realizamos dos operaciones AND: una con la primera entrada invertida y la segunda entrada sin invertir, y otra con la primera entrada invertida y la segunda entrada sin invertir. Finalmente, utilizamos una operación OR para combinar los resultados de ambas operaciones AND.

*Mux

![image](https://github.com/user-attachments/assets/1c8ef40e-c7f7-4d88-87ce-3929ba27a49c)

Comenzamos con la tabla de verdad para crear esta compuerta, a partir de la cual construimos un mapa de Karnaugh. Este mapa nos brinda una expresión de las operaciones AND, OR y NOT que ya hemos creado. Construimos el multiplexor necesario para la operación con esta expresión.

*DMux

Iniciamos con la tabla de verdad para crear esta compuerta y observamos que la salida "a" se puede expresar como una operación AND entre la entrada y la negación del selector, mientras que la salida "b" se puede expresar como una operación AND entre la entrada y el selector. Podemos comenzar a construir el demultiplexor ahora que hemos creado estas compuertas específicas.

*Not16

Para construir esta compuerta, simplemente aplicamos la operación NOT que previamente hemos creado, repetida dieciséis veces.

*And16

Para construir esta puerta, simplemente aplicamos la operación And que hemos creado anteriormente, dieciséis veces.

*Or16

Para construir esta compuerta, simplemente repetimos dieciséis veces la operación Or que previamente hemos creado.

*Mux16

Para construir esta compuerta, simplemente aplicamos dieciséis veces la operación Mux que previamente hemos creado.

*Or8Way

![image](https://github.com/user-attachments/assets/071e5ca7-9057-4011-bdf4-929a70e6e081)

Para crear esta compuerta, usamos la operación OR que hemos construido anteriormente. Realizamos una operación OR entre la primera entrada y la segunda, y luego entre el resultado anterior y la siguiente. Repetimos este proceso hasta combinar las ocho compuertas necesarias.

*Mux4Way16

Para llevar a cabo esta operación, dividimos las entradas en pares y aplicamos la operación MUX a cada par. Esto nos da dos resultados distintos que también utilizamos la operación MuX.

*DMux4Way

Para realizar esta tarea, dividimos las entradas en pares y aplicamos la operación DMUX a cada par. Esto nos da dos resultados distintos a los que también aplicamos la operación DMUX.

*DMux8Way

Agrupamos las entradas en pares y aplicamos la operación DMUX a cada par para llevar a cabo esta operación. Esto nos da dos resultados distintos, a los que también aplicamos la operación DMUX.


Preguntas adicionales:

¿Que consideraciones importantes debe tener en cuenta para trabajar con Nand2Tetris?

Para trabajar con Nand2Tetris es necesario conocer la estructura de la interfaz gráfica de usuario, con el objetivo de comprender las diferentes herramientas, materiales e información presente en el curso. Destacando que el objetivo principal de Nand2Tetris es la realización de 12 proyectos los cuales contienen el material necesario para posteriormente desarrollarlo de manera práctica cada uno de ellos en el simulador encontrado en el apartado de Software.

¿Qué otras herramientas similares a Nand2Tetris existen? (De mínimo dos ejemplos)

Existen diversas herramientas que sirven para cumplir funciones similares a las que realiza Nand2Tetris ejemplo de ello son:

-Logisim: es una herramienta educativa de software diseñada para la creación y simulación de circuitos digitales. 

-Digital works: Es una herramienta para estudiar el comportamiento de los circuitos digitales. 

Fuentes: 
- https://cburch.com/logisim/ 
- https://www.mecanique.co.uk/shop/index.php?route=product/category&path=89 
