*CPU:

Este archivo define la Unidad Central de Procesamiento (CPU) del computador virtual. La CPU es la parte del computador que ejecuta instrucciones de programas almacenados en la memoria.La CPU está compuesta por una unidad de control y una unidad aritmético-lógica (ALU, por sus siglas en inglés), junto con registros internos.

La unidad de control es responsable de interpretar las instrucciones de programa y controlar el flujo de datos dentro de la CPU.La ALU realiza operaciones aritméticas y lógicas en los datos, como sumas, restas, y operaciones booleanas.

CPU.hdl especifica cómo se conectan y operan estos componentes para ejecutar instrucciones del lenguaje de máquina del computador virtual. Se implementa este archivo utilizando HDL para simular el comportamiento de una CPU.

*Memory:

La memoria es un componente esencial de cualquier sistema informático, ya que almacena datos y programas que el computador necesita para operar.

En el contexto de este proyecto, la memoria está implementada como una serie de registros, donde cada registro tiene una dirección única y almacena un bit.

Memory.hdl define cómo se comporta esta memoria, incluyendo operaciones como lectura y escritura.Se implementa este archivo utilizando el lenguaje de descripción de hardware (HDL) para simular el comportamiento de una memoria en el computador virtual.

*Computer:

Este archivo define el computador virtual completo al integrar la CPU, la memoria y otros componentes esenciales.

Combina la funcionalidad de la CPU y la memoria para crear un sistema informático completamente funcional.Además de la CPU y la memoria, el computador virtual también incluye otros componentes como contadores, buses de datos y control, y registros especiales.

Computer.hdl especifica cómo se conectan y operan estos componentes para ejecutar programas almacenados en la memoria.Se implementa este archivo para simular un computador virtual completamente funcional que pueda ejecutar programas escritos en el lenguaje de máquina del proyecto "From Nand to Tetris".

Estos tres archivos representan los componentes fundamentales de un sistema informático y son esenciales para la comprensión y construcción del computador virtual en el curso "From Nand to Tetris". Gracias a esto podemos aprender no solo cómo funcionan estos componentes individualmente, sino también cómo interactúan entre sí para ejecutar programas y realizar tareas computacionales.
