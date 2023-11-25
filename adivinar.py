"""  Implementa un juego donde el usuario intenta adivinar un número generado por la computadora"""
import random

numero = random.randint(1, 10)
usuario = 0
intentos = 0

while intentos < 5:
    usuario = int(input("Ingrese un número entre 1 y 10: "))
    if usuario < 1 or numero > 10:
        print("El número ingresado no está en el rango solicitado")
    if  usuario == numero:
        print("¡Adivinaste!")
        break
    else :
        intentos += 1
        if usuario > numero:
            print("El número ingresado es mayor al número a adivinar")
        else:
            print("El número ingresado es menor al número a adivinar")
        if intentos == 5:
            print("Perdiste")
            break
