import string
import random
import time

def crearClave(longitud, minMayus, minMinus, minNumeros, minSimbolos):
    caracteres = string.ascii_letters + string.digits + string.punctuation

    random.seed(time.time())

    clave = ''
    while True:
        clave = ''
        for i in range(longitud):
            clave += random.choice(caracteres)

        if (sum(c.islower() for c in clave) >= minMinus
                and sum(c.isupper() for c in clave) >= minMayus
                and sum(c.isdigit() for c in clave) >= minNumeros
                and sum(c in string.punctuation for c in clave) >= minSimbolos):
            break

    return clave

longitud = int(input("Ingrese la longitud de la clave: "))
if(longitud == 0):
    longitud = random.randint(8, 16)
    clave = crearClave(longitud, random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2))
    print("Clave generada: ", clave)
else:
  minMayus = int(input("Ingrese el número mínimo de mayúsculas: "))
  minMinus = int(input("Ingrese el número mínimo de minúsculas: "))
  minNumeros = int(input("Ingrese el número mínimo de números: "))
  minSimbolos = int(input("Ingrese el número mínimo de símbolos: "))

  clave = crearClave(longitud, minMayus, minMinus, minNumeros, minSimbolos)
  print("Clave generada: ", clave)
