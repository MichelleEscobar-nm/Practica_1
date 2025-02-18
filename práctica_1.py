# -*- coding: utf-8 -*-
"""Práctica_1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HYBZXU56UmxuMQtCz_NRiaFY16kqX-nB
"""

# Definir la jerarquía
jerarquia = {'+': 1, '-': 1, '*': 2, '/': 2, '**': 3}

def dobleasterisco(caracter):
    return caracter in jerarquia or caracter == '*'  # para **

def conversion(expresion):
    salida = []  # La lista en inversa polaca
    pila = []
    i = 0

    while i < len(expresion): #len función para la extensión de números
        if expresion[i].isdigit():  # Si es un número lo capturamos
            numero = ''
            while i < len(expresion) and expresion[i].isdigit():
                numero += expresion[i]
                i += 1
            salida.append(numero)  # append para agregar el número a la salida
            continue  #saltar incremento de i
        elif expresion[i] == '(':  # apilar paréntesis izquierdo
            pila.append(expresion[i])
        elif expresion[i] == ')':  # si es un paréntesis derecho, vaciamos la pila hasta el paréntesis izquierdo
            while pila and pila[-1] != '(':
                salida.append(pila.pop())
            pila.pop()  # Quitamos el paréntesis izquierdo
        elif dobleasterisco(expresion[i]):  # Si es un operador
            # Para operadores como **
            if expresion[i] == '*' and i + 1 < len(expresion) and expresion[i+1] == '*':
                operador = '**'
                i += 1  # Avanzamos para no contar dos veces el segundo '*'
            else:
                operador = expresion[i]

            while (pila and pila[-1] != '(' and
                   jerarquia.get(operador, 0) <= jerarquia.get(pila[-1], 0)):
                salida.append(pila.pop())
            pila.append(operador)  # Apilamos el operador
        # Pasamos al siguiente carácter
        i += 1

    # Al final, vaciamos lo que queda en la pila
    while pila:
        salida.append(pila.pop())

    return ' '.join(salida)

def generar_reporte(expresion, resultado_rpn):
    with open("reporte_conversion.txt", "w") as archivo:
        archivo.write(f"Expresion original: {expresion}\n")
        archivo.write(f"Expresion en notacion polaca inversa: {resultado_rpn}\n")

if __name__ == "__main__":
    expresion = input("Introduce una expresión aritmética (ej. 3 + 5 * ( 2 - 8 )): ")
    resultado_rpn = conversion(expresion)
    print("La expresión en notación polaca inversa es:", resultado_rpn)
    generar_reporte(expresion, resultado_rpn)