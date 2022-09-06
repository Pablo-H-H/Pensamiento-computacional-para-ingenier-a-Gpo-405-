import random

#La funcion comprueba si el usuario ingreso más de una palabra por error
def validacion(letra_usuario):
    if (len(letra_usuario) == 1):
        return True
    else:
        return False
    
#La funcion comprueba si la letra ya se usó
def lertra_usada_comprobacion(letra_usuario, letras_usadas):
    if (letra_usuario not in letras_usadas):
        letras_usadas.append(letra_usuario)
        return True
    else:
        return False

def letra_si_esta (palabra_escogida, letra_usuario):
    if (letra_usuario in palabra_escogida):
        print ("la letra esta en la palabra")
        return True
    
def eliminar_letra  (palabra_escogida_destruible, letra_usuario):
    for x in range (len(palabra_escogida_destruible)):
        palabra_escogible_destruible = palabra_escogida_destruible.replace(letra_usuario[x], "")
    print (palabra_escogible_destruible)
    return palabra_escogida_destruible
#lista de los valores usados: numero_letras, palabra_adivinar, pista_n (n = al no. de la pregunta)
#Escoge una palabra a lazar y comprueba cual era la palabra
lista_palabras = ["perro", "pato","piano", "fruta", "flor"]
palabra_escogida = random.choice(lista_palabras)
if ("perro" == palabra_escogida):
    lista_pistas = ["Es algo que vive", "Es peludo", "Es una mascota", "Es el mejor amigo del hombre"]
    longitud_palabra = len(palabra_escogida)
if ("pato" == palabra_escogida):
    lista_pistas = ["Esta vivo", "Puede nadar y caminar", "Suele de ser color amarillo o blanco", "Tiene plumas"]
    longitud_palabra = len(palabra_escogida)
if ("fruta" == palabra_escogida):
    lista_pistas = ["Se suele vender", "Es dulce", "Lo puedes encontrar en el supermercado", "Viene de los arboles"]
    longitud_palabra = len(palabra_escogida)
if ("piano" == palabra_escogida):
    lista_pistas = ["Es de gran tamaño", "Normalmente es de madera", "Tiene cuerdas", "Es un instrumento"]
    longitud_palabra = len(palabra_escogida)
if ("flor" == palabra_escogida):
    lista_pistas = ["Esta viva", "La puedes encontrar en el suelo", "Es de colores", "Esta en las plantas"]
    longitud_palabra = len(palabra_escogida)
#Comprobacion de las palabras
print ("Tu Palabra Es: ", palabra_escogida)
print ("Tu Palabra Tiene:", longitud_palabra, " letras", "_ " * longitud_palabra)
print ("Tus Pistas Son: ", lista_pistas)
#Esta parte se usa para que el usuario meta una letra, guarda la letra y comprueba si la letra ya esta en uso
valido = False
letra_valida = True
adivinado = False
letra_no_usada = True
letras_usadas = []
palabra_escogida_destruible = palabra_escogida
while not adivinado:
    while not valido:
        letra_usuario = input("ingresa una letra profavor: ")
        letra_valida = validacion(letra_usuario)
        if letra_valida:
            print("Valor valido!!!")
            letra_no_usada = lertra_usada_comprobacion(letra_usuario, letras_usadas)
            if letra_no_usada:
                print (letras_usadas)
                print("Esa letra No Estaba Usada")
                if (letra_si_esta (palabra_escogida, letra_usuario)):
                    palabra_escogible_destruible = eliminar_letra  (palabra_escogida_destruible, letra_usuario)
                    valido = False
            else:
                print ("letra usada")
                valido = False
        else:
            valido = False
            print("Valor No Valido, Ingresa Una Letra A La Vez")
            



"""Los imprime para comprobar si los datos son correctos,
en la version final esto sera elimiado"""