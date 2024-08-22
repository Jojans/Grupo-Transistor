Boolean Logic:

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
*And16
*Or16
*Mux16
*Or8Way
*Mux4Way16
*DMux4Way
*DMux8Way







Preguntas adicionales:

¿Que consideraciones importantes debe tener en cuenta para trabajar con Nand2Tetris?
¿Qué otras herramientas similares a Nand2Tetris existen? (De mínimo dos ejemplos)
