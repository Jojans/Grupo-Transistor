# Cuarto Proyecto - Machine Language Programming
## Mult.asm:

El programa Mult.asm es un programa en ensamblador diseñado para la arquitectura del computador virtual. Este programa específicamente realiza la multiplicación de dos números enteros positivos sin signo, almacenados en las ubicaciones de memoria R0 y R1, y guardar el resultado en la ubicación de memoria R2.

El programa utiliza un método de multiplicación por sumas sucesivas. La idea básica detrás de este algoritmo es repetir la suma del multiplicando (en este caso R1) tantas veces como el multiplicador indique (en este caso R0). Por ejemplo, para multiplicar 3 por 5, sumaríamos 5 tres veces: 5 + 5 + 5 = 15.

Se inicializa el registro R2 en cero. Este registro se usará para acumular el resultado de la multiplicación.
Se copia el valor de R0 (el multiplicador) en una variable llamada count.
Se establece un bucle etiquetado como LOOP. Este bucle repetirá las siguientes operaciones hasta que count llegue a cero: a. Se verifica si count es cero. Si lo es, el bucle termina y el programa salta a la etiqueta END. b. Se suma el valor de R1 (el multiplicando) al valor acumulado en R2. Esto simula una multiplicación. c. Se decrementa count para seguir realizando la multiplicación el número de veces indicado por el multiplicador.
Después de salir del bucle, el programa entra en una sección etiquetada como END. Esto es simplemente un bucle infinito que detiene la ejecución del programa.

# Fill.asm:

El propósito general de Fill.asm, como el de muchos programas de este tipo dentro del contexto del curso "From Nand to Tetris", es ayudar a los estudiantes a entender y practicar los conceptos de lenguaje de máquina, lenguaje ensamblador y arquitectura del computador, permitiéndoles construir gradualmente una pila de abstracciones que los llevarán desde el nivel más básico de hardware hasta un sistema informático completo y funcional.
