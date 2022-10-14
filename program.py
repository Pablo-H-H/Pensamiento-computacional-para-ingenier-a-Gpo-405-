"""
Proyecto Demo python
Simulador del juego ahorcado
El programa elige una palabra en la lista de manera aleatoria, el usuario tiene
que ir ingresando letra por letra para al final adivinar la palabra o perder
si no adivina en 4 ocasiones.
Al final del juego el jugador tiene la opcion de volver a jugar con otra
palabra diferente, o en otro caso, cerrar el codigo
"""

#Bibliotecas
import random

"""
============================funciones de preguntas=============================
"""
def palabra_lazar(lista_palabras):
    """
    (uso de funciones, listas)
    elige una palabra a lazar de la lista
    devuelve: una palabra a lazar
    """
    return(random.choice(lista_palabras))

def asignar_palabra(palabra_escogida):
    """
    (uso de funciones, diccionarios)
    usa la palabra escogida para encontrar las pistas correspondientes
    devuelve: una lista de pistas
    """
    dic = {"perro" : ["Es algo que vive", "Es peludo",
                     "Es una mascota", "Es el mejor amigo del hombre"],
         "pato" : ["Esta vivo", "Puede nadar y caminar",
                  "Suele de ser color amarillo o blanco", "Tiene plumas"],
         "fruta" : ["Se suele vender", "Es dulce",
                   "Lo puedes encontrar en el supermercado", "Viene de los arboles"],
         "piano" :["Es de gran tamaño", "Normalmente es de madera",
                  "Tiene cuerdas", "Es un instrumento"],
         "flor" : ["Esta viva", "La puedes encontrar en el suelo",
                 "Es de colores", "Esta en las plantas"]
         }
    lista_pistas = dic[palabra_escogida]
    longitud_palabra = len(palabra_escogida)
    return(lista_pistas, longitud_palabra)

def asigna_casillas(palabra_escogida, letras_correctas):
    """
    (uso de funciones, ciclos, listas)
    usa la longitud de la palabra para crear una lista que
    representa el numero de letras que existen en la palabra
    devuelve: una lista de guiones bajos correspondiente a las letras
    de la palabra a adivinar
    """
    for let in palabra_escogida:
        letras_correctas.append("_")
    return letras_correctas

def prints_inicio(longitud_palabra, letras_correctas, lista_pistas, vidas):
    """
    (uso de funciones)
    recibe: la longitud de la palabra, la lista de guiones bajos correspondientes
    a la longitud de la palabra, la lista de pistas, el numero de vidas
    Manda a imprimir los datos utiles para el jugador
    devuelve: una serie de prints
    """
    print ("- - - - - - - - - - - - - - - - - - - - -")
    print ("Tu Palabra Tiene:", longitud_palabra, "letras", letras_correctas)
    print ("Tu Pista 1 Es: ", lista_pistas[0])
    print ("Tienes: ", vidas, "Vidas")

def validacion(letra_usuario):
    """
    (uso de condicionales, funciones)
    comprueba si el jugador ingreso 1 o mas letras
    devuelve: un verdadero si es 1 letra o falso si son mas de 1
    """
    if (len(letra_usuario) == 1):
        return True
    else:
        return False

def lertra_usada_comprobacion(letra_usuario, letras_usadas):
    """
    (uso de condicionales, funciones, listas)
    usa la letra del usuario para comprobar si esta dentro de la lista de letras usadas
    devuelve: verdadero si no esta en la lista, falso si esta en la lista 
    """
    if (letra_usuario not in letras_usadas):
        letras_usadas.append(letra_usuario)
        return True
    else:
        return False

def letra_si_esta(palabra_escogida, letra_usuario):
    """
    (uso de condicionales, funciones, listas)
    usa la letra del usuario para comprobar si esta dentro de la palabra a adivinar
    devuelve: un true si esta dentro de la palabra a adivinar, un false si no lo esta
    """
    if (letra_usuario in palabra_escogida):
        return True
    else:
        return False
    
def poner_letra_correcta(palabra_escogida, letras_correctas, letra_usuario):
    """
    (uso de ciclos, listas, listas, condicionales, funciones)
    crea una lista hecha con las letras de las palabras escogidas, luego crea un ciclo
    para comprobar si la letra del usuario esta dentro de esta lista guardando su posicion
    en i, cuando encuentre la posicion entonces se le asignara la letra con la posicion
    a la lista de letras correctas
    devuelve: una lista con la posicion de las letras correctas
    """
    palabra_escogida_lista = []
    for let in palabra_escogida:
        palabra_escogida_lista.append(let)
    i = 0
    while i < len(palabra_escogida_lista):
        if (palabra_escogida_lista[i] == letra_usuario):
            letras_correctas[i] = palabra_escogida_lista[i]
        i = i + 1
    return letras_correctas

def poner_letra_incorrecta (letras_erroneas, letra_usuario):
    """
    (uso de funciones, listas)
    usa la letra que no adivino el jugador y la integra a una
    lista para que el jugador sepa que letras a usado
    devuelve: una lista de letras incorrectas
    """
    letras_erroneas.append(letra_usuario)
    return letras_erroneas

def eliminar_letra  (palabra_escogida_destruible, letra_usuario):
    """
    (uso de funciones, ciclos)
    usa un ciclo que recorre cada letra de la palabra destruible y la elimina
    devuelve: una palabra vacia
    """
    for x in range (len(palabra_escogida_destruible)):
        palabra_escogida_destruible = palabra_escogida_destruible.replace(letra_usuario, "")
    return palabra_escogida_destruible

"""
======================parte principal del programa=======================================
"""
valido = False
letra_valida = True
adivinado = False
pregunta_jugar = False
letra_no_usada = True
comp_jugar = False
perdio = False
vidas = 4
letras_usadas = []
letras_erroneas = []
letras_correctas = []
lista_palabras = ["perro", "pato", "piano", "fruta", "flor"]

palabra_escogida = palabra_lazar(lista_palabras)
lista_correctas = asigna_casillas(palabra_escogida, letras_correctas)
lista_pistas, longitud_palabra = asignar_palabra(palabra_escogida)
prints_inicio(longitud_palabra, letras_correctas, lista_pistas, vidas)
palabra_escogida_destruible = palabra_escogida

while (adivinado == False):
    
    while (valido == False):
        letra_usuario = input("Ingresa una letra profavor: ")
        letra_valida = validacion(letra_usuario)
        print("- - - - - - - - - - - - - - - - - - - - -")       
        
        if letra_valida:
            letra_no_usada = lertra_usada_comprobacion(letra_usuario, letras_usadas)
            
            if letra_no_usada:               
                
                if (letra_si_esta (palabra_escogida_destruible, letra_usuario)):
                    
                    letras_correctas = poner_letra_correcta(palabra_escogida, letras_correctas, letra_usuario)
                    print("Tus letras Correctas Son: ", letras_correctas)
                    print("Tus letras erroneas son: ", letras_erroneas)
                    print("la letra ", letra_usuario, " estaba en la palabra")
                    palabra_escogida_destruible = eliminar_letra(palabra_escogida_destruible, letra_usuario)
                    print("- - - - - - - - - - - - - - - - - - - - -")  
                    valido = False
                    
                else:
                    letras_erroneas = poner_letra_incorrecta(letras_erroneas, letra_usuario)
                    print(letra_usuario," no estaba en la palabra, ", end = "")
                    print("Tus letras Correctas Son: ", letras_correctas)
                    print("Tus letras erroneas son: ", letras_erroneas)
                    print("Pierdes una Vida")
                    vidas = vidas - 1
                    print("Te quedan: ", vidas, "Vidas")
            
                    if (vidas == 0):
                        print("- - - - - - - - - - - - - - - - - - - - -") 
                        print ("Ya no te quedan vidas")
                        print ("Tu palabra era: ", palabra_escogida)
                        palabra_escogida_destruible = ""
                        perdio = True
                    else:
                        print("Pista", 5-vidas, ":", lista_pistas[(4-vidas)])
                        print("- - - - - - - - - - - - - - - - - - - - -")  
                        valido = False               
                
                if (palabra_escogida_destruible == ""):
                    lista_palabras.remove(palabra_escogida)
                    comp_jugar = False
                    
                    if (perdio == True):
                        print("Perdiste, mas suerte a la proxima!!!")
                    else:
                        print("Adivinaste la Palabra!!!\nFelicidades, Ganaste!!!")
                        
                    if (lista_palabras == []):
                        print("Acabaste Todas Las Palabras")
                        comp_jugar = True
                        valido = True
                        adivinado = True
                    else:
                        print("Quieres Jugar Otra Vez?")
                        print("Escribe: si o no")
                        
                        while (comp_jugar == False):
                            jugar = input("")
                           
                            if (jugar == "si" or jugar == "Si"):
                                print ("A Jugar")
                                
                                #Reseteamos los valores y mandamos los prints iniciales
                                vidas = 4
                                letras_usadas = []
                                letras_erroneas = []
                                letras_correctas = [] 
                                palabra_escogida = palabra_lazar(lista_palabras)
                                lista_correctas = asigna_casillas(palabra_escogida, letras_correctas)
                                lista_pistas, longitud_palabra = asignar_palabra(palabra_escogida)
                                prints_inicio(longitud_palabra, letras_correctas, lista_pistas, vidas)
                                
                                palabra_escogida_destruible = palabra_escogida
                                perdio = False
                                comp_jugar = True
                                valido = False
                            
                            elif (jugar == "no" or jugar == "No"):
                                print("Hasta la Proxima")
                                comp_jugar = True
                                valido = True
                                adivinado = True
                            
                            else:
                                print("Ingresa un valor Valido")
            
            else:
                print("letra usada")
                   
        else:
            valido = False
            print("Valor No Valido, Ingresa Una Letra A La Vez")
