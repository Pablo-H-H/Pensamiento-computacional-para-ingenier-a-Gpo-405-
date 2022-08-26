import random

"""Cada una de las palabra_n contiene la lista que se usará para el juego y
las aplica cambiando el valor"""
#lista de los valores usados: numero_letras, palabra_adivinar, pista_n (n = al no. de la pregunta)
def palabra_0 ():
    numero_letras = 5
    palabra_adivinar = "perro"
    pista_0 = "Es algo que vive"
    pista_1 = "Es peludo"
    pista_2 = "Es una mascota"
    pista_3 = "Es el mejor amigo del hombre"
    return numero_letras, palabra_adivinar, pista_0, pista_1, pista_2, pista_3;

def palabra_1 ():
    numero_letras = 4
    palabra_adivinar = "pato"
    pista_0 = "Esta vivo"
    pista_1 = "Puede nadar y caminar"
    pista_2 = "Suele de ser color amarillo o blanco"
    pista_3 = "Tiene plumas"
    return numero_letras, palabra_adivinar, pista_0, pista_1, pista_2, pista_3;
def palabra_2 ():
    numero_letras = 5
    palabra_adivinar = "fruta"
    pista_0 = "Se suele vender"
    pista_1 = "Es dulce"
    pista_2 = "Lo puedes encontrar en el supermercado"
    pista_3 = "Viene de los arboles"
    return numero_letras, palabra_adivinar, pista_0, pista_1, pista_2, pista_3;

def palabra_3 ():
    numero_letras = 5
    palabra_adivinar = "piano"
    pista_0 = "Es de gran tamaño"
    pista_1 = "Normalmente es de madera"
    pista_2 = "Tiene cuerdas"
    pista_3 = "Es un instrumento"
    return numero_letras, palabra_adivinar, pista_0, pista_1, pista_2, pista_3;
def palabra_4 ():
    numero_letras = 4
    palabra_adivinar = "flor"
    pista_0 = "Esta vivo"
    pista_1 = "La puedes encontrar en el suelo"
    pista_2 = "Es de colores"
    pista_3 = "Esta en las plantas"
    return numero_letras, palabra_adivinar, pista_0, pista_1, pista_2, pista_3;

"""Genera un número a lazar y verifica el numero de la lista para pedirle
los valores correspondientes"""
numero_lista = random.randint(0,4)

if (numero_lista == 0):
    numero_letras, palabra_adivinar, pista_0, pista_1, pista_2, pista_3 = palabra_0()
    
if (numero_lista == 1):
    numero_letras, palabra_adivinar, pista_0, pista_1, pista_2, pista_3 = palabra_1()
    
if (numero_lista == 2):
    numero_letras, palabra_adivinar, pista_0, pista_1, pista_2, pista_3 = palabra_2()
    
if (numero_lista == 3):
    numero_letras, palabra_adivinar, pista_0, pista_1, pista_2, pista_3 = palabra_3()
    
if (numero_lista == 4):
    numero_letras, palabra_adivinar, pista_0, pista_1, pista_2, pista_3 = palabra_4()
    
"""Los imprime para comprobar si los datos son correctos,
en la version final esto sera elimiado"""
print ("tu palabra tiene", numero_letras, "letras", "- " * numero_letras)
print (palabra_adivinar)
print(pista_0)
print(pista_1)
print(pista_2)
print(pista_3)
