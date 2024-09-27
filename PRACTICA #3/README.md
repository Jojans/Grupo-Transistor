# Tercera Práctica
En esta práctica se abordará el Proyecto 4 del asignado curso de Nand2Tetris, enfocado en el desarrollo y manejo del lenguaje de máquina. Este proyecto es clave para comprender cómo se traduce el código de alto nivel a un conjunto de instrucciones que el hardware puede ejecutar directamente. A lo largo de esta práctica, se trabajará con el diseño y la implementación de un traductor que convierta código de lenguaje de máquina en instrucciones entendibles para la arquitectura de la computadora Hack, sentando las bases para el siguiente desafío, el Proyecto 5, que profundiza en la arquitectura computacional. Este enfoque escalonado permitirá conectar el funcionamiento del software con los componentes físicos del sistema, proporcionando una visión integral del funcionamiento de un computador desde sus niveles más básicos.

## Preguntas Planteadas
### ¿Por qué el lenguaje de máquina es importante para definir la arquitectura computacional?
Porque proporciona una descripción abstracta pero precisa de las capacidades del computador, ayuda a comprender el diseño del hardware, facilita la programación de bajo nivel y sirve como base para la construcción física del sistema computacional, haciendo que el lenguaje de máquina sea una interfaz directa entre el diseño del hardware y las capacidades de programación, por tanto, le permite una ejecución más eficiente y un control preciso del sistema.

### ¿Qué diferencia ven entre arquitectura computacional, arquitectura de software y arquitectura del sistema? Justifique su respuesta.
La principal diferencia entre la arquitectura computacional, la arquitectura de software y la arquitectura del sistema está en su enfoque. La arquitectura computacional se centra en el hardware, mientras que la arquitectura de software se enfoca en cómo está organizado y diseñado el software. Por otro lado, la arquitectura del sistema engloba ambos, hardware y software, y se encarga de cómo interactúan para lograr los objetivos del sistema.

Otras diferencias que pueden resaltar son:
* Arquitectura Computacional: Es básicamente el diseño de los componentes físicos de una computadora, como la CPU, la memoria, y los dispositivos de entrada y salida. Se preocupa por cómo estos elementos trabajan juntos para ejecutar programas. Ejemplos de esta arquitectura son los enfoques como la arquitectura von Neumann o los modelos RISC y CISC.
* Arquitectura de Software: Se ocupa de cómo se estructura y organiza el software dentro de un sistema. Aquí entran decisiones sobre los módulos, las interfaces y cómo se conectan entre sí para cumplir con lo que el sistema necesita hacer. Ejemplos de esto incluyen la arquitectura en tres capas o la de microservicios.
* Arquitectura del Sistema: Es la visión más general que abarca todo el sistema, tanto el hardware como el software. Se enfoca en cómo ambos se coordinan para que el sistema funcione correctamente, considerando cosas como la gestión de recursos, la comunicación entre procesos, y la tolerancia a fallos. Todo esto buscando que las partes trabajen juntas para cumplir con los objetivos del sistema.

### Como informático o computista: ¿La arquitectura computacional o la arquitectura del sistema no tiene en cuenta igualmente la arquitectura de software? Justifique su respuesta.
La arquitectura del sistema por definición debe abarcar la arquitectura computacional y la de software de forma cabal, pues como se mencionaba con anterioridad su enfoque es como tal el sistema que podría incluir no solo software sino otras herramientas, como dispositivos de redes por ejemplo. Por contraparte la aquitectura computacional típicamente no abarca la de software, pero, últimamente con los diferentes avances y el auge de la IA, es posible encontrar arquitectura computacional enlazada con software debido al uso de IA para diferentes tareas. 


## Referencias
* Bass, L., Clements, P., & Kazman, R. (2012). Software architecture in practice (3rd ed.). Addison-Wesley.
* IEEE Computer Society. (n.d.). Software engineering body of knowledge (SWEBOK). https://www.computer.org/education/bodies-of-knowledge/software-engineering
* GeeksforGeeks. (2023). RISC vs CISC architecture. https://www.geeksforgeeks.org/risc-vs-cisc-architecture/
* Pawar, D. (2023, May 8). Impact of artificial intelligence on computer architecture. Medium. https://medium.com/@dhiraj.pawar21/impact-of-artificial-intelligence-on-computer-architecture-6539d33eb055
* GeeksforGeeks. (2022, December 2). Difference between System Architecture and Software Architecture. GeeksforGeeks. https://www.geeksforgeeks.org/difference-between-system-architecture-and-software-architecture/
* Diapositivas Proyecto 4: https://www.nand2tetris.org/_files/ugd/44046b_d70026d8c1424487a451eaba3e372132.pdf
