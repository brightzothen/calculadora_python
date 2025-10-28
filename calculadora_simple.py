'''
calculadora_simple.py
Autor: Alex Dominguez
Descripción: calculadora básica en Python
Fecha: 28/10/2025
'''

def sumar (a, b):
    return a+b

def restar (a, b):
    return a-b
def multiplicar (a, b):
    return a*b

def dividir (a, b):
    if b == 0:
        return "Error: división entre 0."
    else:
        return a / b
    
def potenciar (a, b):
    return a^b

def main ():

    print('Calculadora simple: ')
    print('===================')

    x = float(input('Introduce el primer número: '))
    y = float(input('Introduce el segundo número: '))

    print(f'Suma: {sumar(x,y)}')
    print(f'Resta: {restar(x,y)}')
    print(f'Multiplicación: {multiplicar(x,y)}')
    print(f'División: {dividir(x,y)}')
    print(f'Potencia: {potenciar(x,y)}')
    print(f'Nueva línea para probar el pull.')

if __name__ == '__main__':
    main()
