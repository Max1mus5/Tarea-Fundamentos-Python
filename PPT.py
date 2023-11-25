""" Juego de piedra papel o tijera, el usuario debe hacer una eleccion y a la computadora aleatoriamente tendra su eleccion entre piedra, papel o tiejer (1, 2, 3 ) 
respectivamente """
import random
import time
print("Bienvenido al juego de piedra, papel o tijera")
print("1. Piedra")
print("2. Papel")
print("3. Tijera")
print("La partida sera al mejor de 3")
print("¿Cual es tu eleccion?")
eleccion = int(input())
eleccionComputadora = random.randint(1, 3)
puntosUsuario = 0
puntosComputadora = 0
estructura=["Piedra", "Papel", "Tijera"]
while puntosUsuario < 3 and puntosComputadora < 3:
  print("-----------------------------------------------------------")
  if(estructura[eleccion-1] == estructura[eleccionComputadora-1]):
    print("Empate")
    print("Usuario: ", puntosUsuario, "Computadora: ", puntosComputadora)
    print("¿Cual es tu eleccion?")
    eleccion = int(input())
    eleccionComputadora = random.randint(1, 3)
  elif(estructura[eleccion-1] == "Piedra" and estructura[eleccionComputadora-1] == "Papel"):
    print("piedra vs papel")
    puntosComputadora += 1
    print("Gana la computadora")
    print("Usuario: ", puntosUsuario, "Computadora: ", puntosComputadora)
    print("¿Cual es tu eleccion?")
    eleccion = int(input())
    eleccionComputadora = random.randint(1, 3)
  elif(estructura[eleccion-1] == "Piedra" and estructura[eleccionComputadora-1] == "Tijera"):
    prin("piedra vs tijera")
    puntosUsuario += 1
    print("Gana el usuario")
    print("Usuario: ", puntosUsuario, "Computadora: ", puntosComputadora)
    print("¿Cual es tu eleccion?")
    eleccion = int(input())
    eleccionComputadora = random.randint(1, 3)
  elif(estructura[eleccion-1] == "Papel" and estructura[eleccionComputadora-1] == "Tijera"):
    print("papel vs tijera")
    puntosComputadora += 1
    print("Gana la computadora")
    print("Usuario: ", puntosUsuario, "Computadora: ", puntosComputadora)
    print("¿Cual es tu eleccion?")
    eleccion = int(input())
    eleccionComputadora = random.randint(1, 3)
  elif(estructura[eleccion-1] == "Papel" and estructura[eleccionComputadora-1] == "Piedra"):
    print("papel vs piedra")
    puntosUsuario += 1
    print("Gana el usuario")
    print("Usuario: ", puntosUsuario, "Computadora: ", puntosComputadora)
    print("¿Cual es tu eleccion?")
    eleccion = int(input())
    eleccionComputadora = random.randint(1, 3)
  elif(estructura[eleccion-1] == "Tijera" and estructura[eleccionComputadora-1] == "Piedra"):
    print("tijera vs piedra")
    puntosComputadora += 1
    print("Gana la computadora")
    print("Usuario: ", puntosUsuario, "Computadora: ", puntosComputadora)
    print("¿Cual es tu eleccion?")
    eleccion = int(input())
    eleccionComputadora = random.randint(1, 3)
  elif(estructura[eleccion-1] == "Tijera" and estructura[eleccionComputadora-1] == "Papel"):
    print("tijera vs papel")
    puntosUsuario += 1
    print("Gana el usuario")
    print("Usuario: ", puntosUsuario, "Computadora: ", puntosComputadora)
    print("¿Cual es tu eleccion?")
    eleccion = int(input())
    eleccionComputadora = random.randint(1, 3)
  elif(puntosUsuario == 3 or puntosComputadora == 3):
    break

print("Usuario: ", puntosUsuario, "Computadora: ", puntosComputadora)
print("El ganador es: " + ("Usuario" if puntosUsuario > puntosComputadora else "Computadora"))
print("Fin del juego")