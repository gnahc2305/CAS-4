# Juego de Piedra, Papel y Tijeras
import random
# se elige un número aleatorio del 1 al 3
a = round(random.uniform(1,3))
# se pide la eleccion del usuario
b = input("Piedra, Papel o Tijeras: ").capitalize()
# se crea una variable vacia
c = ""
# se crean las distintas opciones
pi = "Piedra"
pa = "Papel"
ti = "Tijeras"

# se crea una funcion para que la computadora elija una de las opciones
def cp():
    if a == 1:
        global c
        c = pi
        print("Computadora: " + c)
    elif a == 2:
        c = pa
        print("Computadora: " + c)
    elif a == 3:
        c = ti
        print("Computadora: " + c)


cp()

# se crea otra funcion para ver el resultado
def resultado():
    if b == pi and c == pi:
        print("Empate")
    elif b == pi and c == pa:
        print("Perdiste")
    elif b == pi and c == ti:
        print("Ganaste!")

    elif b == pa and c == pi:
        print("Ganaste!")
    elif b == pa and c == pa:
        print("Empate")
    elif b == pa and c == ti:
        print("Perdiste")

    elif b == ti and c == pi:
        print("Perdiste")
    elif b == ti and c == pa:
        print("Ganaste!")
    elif b == ti and c == ti:
        print("Empate")


resultado()


