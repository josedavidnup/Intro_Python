# python 13_if.py

pet = input("Cuál es tu mascota favorita? ")

if pet == "perro":
    print("Los perros son lo mejor")
elif pet == "gato":
    print("Los gatos son lo mejor")
elif pet == "pez":
    print("No me gustan los peces")
else:
    print("Lo siento, no conozco esa mascota")

#RETO

num = int(input('pon un numero: ')) % 2

if num == 0: 
    print('es par')
else:
    print('es impar')

