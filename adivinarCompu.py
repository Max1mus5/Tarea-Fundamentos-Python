"""un juego donde la computadora intenta adivinar un número pensado por el usuario.  """
import random
import time
print("vas a adivinar el numero que estoy pensando entre el 1 y 10\n")
numero = int(input())
intentos = 0
rango = [1, 10]
print("OKEY COMENZAMOS!")
while intentos < 5:
    intentos += 1
    computadora = random.randint(rango[0], rango[1])
    print("¿Es el número " + str(computadora) + "?")
    if computadora == numero:
        print("¡Adivinaste!")
        break
    else :
        if computadora > numero:
            print("El número ingresado es mayor al número a adivinar")
            rango[0]= rango[0] + 1
            time.sleep(3)


        else:
            print("El número ingresado es menor al número a adivinar")
            rango[1]= rango[1] - 1
            time.sleep(3)
        if intentos == 5:
            print("Perdiste XD")
            break
