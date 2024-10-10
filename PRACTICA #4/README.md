# Práctica #4, Ensamblador.

Es importante que los estudiantes tengan ciertos conocimientos y habilidades relacionados al ensamblador. Es por esto  que en el presente proyecto se propone un ensamblador que traduce programas escritos en el lenguaje symbolic Hack assembly a código binario. 


## ¿Cómo se realizó el proyecto?

### Paso 1: Se lee el archivo `.asm`

Primero, necesitamos leer el archivo `.asm`, eliminando los comentarios y líneas vacías. La funcion `read_asm_file` sera la encargada de eso:

```python
def read_asm_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Filtramos los comentarios y las líneas vacías
    clean_lines = []
    for line in lines:
        # Quitamos los espacios y comentarios
        line = line.split('//')[0].strip()
        if line:  # Si la línea no esta vacía despues de limpiar
            clean_lines.append(line)
    return clean_lines
```

### Paso 2: Traduccion de instrucciones tipo A

Las instrucciones tipo A comienzan con `@` y representan un valor numerico. La funcion `translate_a_instruction` se encarga de traducirlas a un valor binario de 16 bits.

```python
def translate_a_instruction(instruction):
    value = instruction[1:]  # Quitamos el '@'
    binary_value = bin(int(value))[2:]  # Convertimos a binario y quitamos '0b'
    return '0' + binary_value.zfill(15)  # Aseguramos que tenga 16 bits
```

### Paso 3: Traduccion de instrucciones tipo C

Las instrucciones tipo C realizan operaciones aritmeticas y logicas. Utilizamos tablas de traduccion para convertir las partes de la instruccion (`comp`, `dest`, `jump`) a codigo binario.

Tablas de traduccion:

```python
comp_table = {
            "0": "0101010",
            "1": "0111111",
            "-1": "0111010",
            "D": "0001100",
            "A": "0110000",
            "M": "1110000",
            "!D": "0001101",
            "!A": "0110001",
            "!M": "1110001",
            "-D": "0001111",
            "-A": "0110011",
            "-M": "1110011",
            "D+1": "0011111",
            "A+1": "0110111",
            "M+1": "1110111",
            "D-1": "0001110",
            "A-1": "0110010",
            "M-1": "1110010",
            "D+A": "0000010",
            "D+M": "1000010",
            "D-A": "0010011",
            "D-M": "1010011",
            "A-D": "0000111",
            "M-D": "1000111",
            "D&A": "0000000",
            "D&M": "1000000",
            "D|A": "0010101",
            "D|M": "1010101"
}

dest_table = {
    'null': '000', 'M': '001', 'D': '010', 'MD': '011', 'A': '100', 'AM': '101', 'AD': '110', 'AMD': '111'
}

jump_table = {
    'null': '000', 'JGT': '001', 'JEQ': '010', 'JGE': '011', 'JLT': '100', 'JNE': '101', 'JLE': '110', 'JMP': '111'
}
```

La funcion `translate_c_instruction` se encarga de la traduccion:

```python
def translate_c_instruction(instruction):
    dest, comp, jump = 'null', '', 'null'
    
    if '=' in instruction:
        dest, instruction = instruction.split('=')
    if ';' in instruction:
        comp, jump = instruction.split(';')
    else:
        comp = instruction
    
    comp_bits = comp_table[comp]
    dest_bits = dest_table[dest]
    jump_bits = jump_table[jump]
    
    return '111' + comp_bits + dest_bits + jump_bits
```

### Paso 4: Manejo de etiquetas y símbolos

Para manejar etiquetas y variables simbolicas tales como `@R0`, `@OUTPUT_D`, utilizamos una tabla de símbolos con su correspondiente numero.

#### Tabla de símbolos:

```python
symbol_table = {
    'R0': 0, 'R1': 1, 'R2': 2, 'R3': 3, 'R4': 4, 'R5': 5, 'R6': 6, 'R7': 7,
    'R8': 8, 'R9': 9, 'R10': 10, 'R11': 11, 'R12': 12, 'R13': 13, 'R14': 14, 'R15': 15,
    'SCREEN': 16384, 'KBD': 24576, 'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 'THAT': 4
}
```

#### Primera pasada: Busqueda e identificacion de etiquetas

En la primera pasada, recorremos el archivo `.asm` para identificar las etiquetas y asignarles direcciones de memoria en la tabla de símbolos.

```python
def first_pass(lines):
    rom_address = 0
    for line in lines:
        if line.startswith('(') and line.endswith(')'):
            label = line[1:-1]  # Extraer el nombre de la etiqueta
            symbol_table[label] = rom_address
        else:
            rom_address += 1  # Solo las instrucciones cuentan como direcciones ROM
```

#### Segunda pasada: Traduccion de instrucciones tipo a y c

En la segunda pasada, traducimos las instrucciones A y C, y reemplazamos las etiquetas y variables con las direcciones correctas.

```python
def second_pass(lines):
    machine_code = []
    ram_address = 16  # Comienza en 16 para las variables

    for line in lines:
        if line.startswith('(') and line.endswith(')'):
            continue  # Las etiquetas se manejaron en la primera pasada

        if line.startswith('@'):
            symbol = line[1:]
            if symbol.isdigit():
                machine_code.append(translate_a_instruction(line))  # Es un numero directo
            else:
                if symbol not in symbol_table:
                    symbol_table[symbol] = ram_address
                    ram_address += 1
                machine_code.append(translate_a_instruction(f"@{symbol_table[symbol]}"))
        else:
            machine_code.append(translate_c_instruction(line))

    return machine_code
```

### Paso 5: Proceso completo de assembler

Finalmente, unimos todo el proceso en una funcion que lea el archivo `.asm`, maneje etiquetas y variables, y genere el archivo `.hack`.

```python
def assemble(file_path):
    lines = read_asm_file(file_path)
    
    # Primera pasada para manejar etiquetas
    first_pass(lines)
    
    # Segunda pasada para traducir instrucciones
    machine_code = second_pass(lines)

    # Escribir el archivo de salida
    output_file = file_path.replace('.asm', '.hack')
    with open(output_file, 'w') as file:
        for instruction in machine_code:
            file.write(instruction + '\n')

    print(f'Archivo {output_file} generado')
```
### Test de verificación
![Copia de Capa Sesión OSI (2)](https://github.com/user-attachments/assets/1be8f086-74b1-49c4-b9d5-bf3541cc2834)


El ensamblador generara un archivo `.hack` con el codigo binario correspondiente

## Teniendo en cuenta las características del ensamblador, ¿Cuál es la principal limitante que observan? Justifique su respuesta.

La principal limitante fue no poder probar el ensamblador directamente en un simulador o entorno real. Como no se podía ejecutar el código para verificar si funcionaba correctamente, confiar solo en la teoría y la lógica del código, sin tener certeza de que cada parte funcionaría como se espera. Lo cual llego a ser un poco complicado porque es mas facil poder depurar el codigo viendo paso por paso como se comporta la traduccion para poder revisar los errores que hayan por el camino.

## BONUS: ¿Por qué es tan importante el ensamblador?
El ensamblador juega un papel crucial como puente entre los lenguajes de programación de alto nivel y el código máquina que la computadora puede ejecutar directamente. Sin esta herramienta, los programadores tendrían que escribir en lenguaje máquina, lo que resultaría extremadamente complicado y propenso a errores, haciendo que el proceso de desarrollo de software fuera mucho más difícil. El ensamblador simplifica este proceso al ofrecer flexibilidad y control sobre los recursos del equipo, lo que lo convierte en una pieza clave en aplicaciones como sistemas embebidos, sistemas operativos y controladores de dispositivos, donde la optimización del rendimiento es esencial.

Además, el ensamblador es la opción preferida en situaciones donde la precisión y la velocidad son fundamentales, ya que puede aprovechar al máximo las capacidades del hardware sin la sobrecarga de los lenguajes de alto nivel. Esto lo hace ideal para áreas críticas en las que cada milisegundo y cada byte de memoria son importantes.




## Referencias
