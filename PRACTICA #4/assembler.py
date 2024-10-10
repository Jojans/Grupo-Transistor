# -*- coding: utf-8 -*-
"""Assembler.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yya_uNAERNWJKCwdL1G3Hkmrbjn7FW0S
"""

def read_asm_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Filtramos los comentarios y las líneas vacías
    clean_lines = []
    for line in lines:
        # Quitamos los espacios y comentarios
        line = line.split('//')[0].strip()
        if line:  # Si la línea no está vacía después de limpiar
            clean_lines.append(line)
    return clean_lines

#Ejecutamos el programa y abrimos el add.asm para ver si si elimina los comentarios y las lineas blancas
if __name__ == "__main__":
    lines = read_asm_file('Add.asm')
    for line in lines:
        print(line)

def translate_a_instruction(instruction):
    value = instruction[1:]  # Quitamos el '@'
    binary_value = bin(int(value))[2:]  # Convertimos a binario y quitamos '0b'
    return '0' + binary_value.zfill(15)  # Aseguramos que tenga 16 bits

print(translate_a_instruction('@2'))

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

print(translate_c_instruction('D=A'))

def translate_instruction(instruction):
    if instruction.startswith('@'):
        return translate_a_instruction(instruction)
    else:
        return translate_c_instruction(instruction)

symbol_table = {
    'R0': 0, 'R1': 1, 'R2': 2, 'R3': 3, 'R4': 4, 'R5': 5, 'R6': 6, 'R7': 7,
    'R8': 8, 'R9': 9, 'R10': 10, 'R11': 11, 'R12': 12, 'R13': 13, 'R14': 14, 'R15': 15,
    'SCREEN': 16384, 'KBD': 24576, 'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 'THAT': 4
}

def first_pass(lines):
    rom_address = 0
    for line in lines:
        if line.startswith('(') and line.endswith(')'):
            label = line[1:-1]  # Extraer el nombre de la etiqueta
            symbol_table[label] = rom_address
        else:
            rom_address += 1  # Solo las instrucciones cuentan como direcciones ROM

def second_pass(lines):
    machine_code = []
    ram_address = 16  # Comienza en 16 para variables dinámicas

    for line in lines:
        if line.startswith('(') and line.endswith(')'):
            continue  # Las etiquetas se manejaron en la primera pasada

        if line.startswith('@'):
            symbol = line[1:]
            if symbol.isdigit():
                machine_code.append(translate_a_instruction(line))  # Es un número directo
            else:
                if symbol not in symbol_table:
                    symbol_table[symbol] = ram_address
                    ram_address += 1
                machine_code.append(translate_a_instruction(f"@{symbol_table[symbol]}"))
        else:
            machine_code.append(translate_c_instruction(line))

    return machine_code

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

    print(f'Archivo {output_file} generado exitosamente.')

assemble('C:\Users\CENTIC\Descargas\Assembler\Fuerza-Sistematica\PRACTICA #4\Add\Add.asm')
