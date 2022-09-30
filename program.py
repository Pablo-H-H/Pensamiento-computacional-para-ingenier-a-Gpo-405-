import random

def palabra_lazar (lista_palabras):
    return (random.choice(lista_palabras))

def asignar_palabra (palabra_escogida):
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
    return (lista_pistas, longitud_palabra)

def asigna_casillas (palabra_escogida, letras_correctas):
    for let in palabra_escogida:
        letras_correctas.append("_")
    return letras_correctas

def prints_inicio (palabra_escogida, longitud_palabra, letras_correctas, lista_pistas, vidas):
    print ("- - - - - - - - - - - - - - - - - - - - -")
    print ("Tu Palabra Tiene:", longitud_palabra, "letras", letras_correctas)
    print ("Tu Pista 1 Es: ", lista_pistas[0])
    print ("Tienes: ",vidas, "Vidas")

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
        return True
    
def poner_letra_correcta (palabra_escogida, letras_correctas, letra_usuario):
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
    letras_erroneas.append(letra_usuario)
    return letras_erroneas

def eliminar_letra  (palabra_escogida_destruible, letra_usuario):
    for x in range (len(palabra_escogida_destruible)):
        palabra_escogida_destruible = palabra_escogida_destruible.replace(letra_usuario, "")
    return palabra_escogida_destruible


#lista de los valores usados: numero_letras, palabra_adivinar, pista_n (n = al no. de la pregunta)
#Escoge una palabra a lazar y comprueba cual era la palabra
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
lista_palabras = ["perro", "pato","piano", "fruta", "flor"]


palabra_escogida = palabra_lazar (lista_palabras)
lista_correctas = asigna_casillas (palabra_escogida, letras_correctas)
lista_pistas, longitud_palabra = asignar_palabra(palabra_escogida)

#Primeros prints
prints_inicio (palabra_escogida, longitud_palabra, letras_correctas, lista_pistas, vidas)
#Esta parte se usa para que el usuario meta una letra, guarda la letra y comprueba si la letra ya esta en uso

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
                    
                    letras_correctas = poner_letra_correcta (palabra_escogida, letras_correctas, letra_usuario)
                    print ("Tus letras Correctas Son: ",letras_correctas)
                    print ("Tus letras erroneas son: ", letras_erroneas)
                    print ("la letra ", letra_usuario," estaba en la palabra")
                    palabra_escogida_destruible = eliminar_letra (palabra_escogida_destruible, letra_usuario)
                    print("- - - - - - - - - - - - - - - - - - - - -")  
                    valido = False
                    
                else:
                    letras_erroneas = poner_letra_incorrecta (letras_erroneas, letra_usuario)
                    print (letra_usuario," no estaba en la palabra, ", end = "")
                    print ("Tus letras Correctas Son: ",letras_correctas)
                    print ("Tus letras erroneas son: ", letras_erroneas)
                    print ("Pierdes una Vida")
                    vidas = vidas - 1
                    print ("Te quedan: ", vidas, "Vidas")
            
                    if (vidas == 0):
                        print("- - - - - - - - - - - - - - - - - - - - -") 
                        print ("Ya no te quedan vidas")
                        print ("Tu palabra era: ", palabra_escogida)
                        palabra_escogida_destruible = ""
                        perdio = True
                    else:
                        print ("Pista", 5-vidas, ":" ,lista_pistas[(4-vidas)])
                        print("- - - - - - - - - - - - - - - - - - - - -")  
                        valido = False
                
                
                
                if (palabra_escogida_destruible == ""):
                    
                    if (perdio == True):
                        print ("Perdiste, Fin Del Juego")
                    else:
                        print ("Adivinaste la Palabra!!!")
                        
                    lista_palabras.remove(palabra_escogida)
                    comp_jugar = False
                    
                    if (lista_palabras == []):
                        print ("Acabaste Todas Las Palabras")
                        comp_jugar = True
                        valido = True
                        adivinado = True
                    else:
    
                        print ("Quieres Jugar Otra Vez?")
                        print ("Escribe: si o no")
                        while (comp_jugar == False):
                            jugar = input("")
                            if (jugar == "si" or jugar == "Si"):
                                print ("A Jugar")
                                
                                #Reseteamos los valores y mandamos los prints iniciales
                                vidas = 4
                                letras_usadas = []
                                letras_erroneas = []
                                letras_correctas = []
                                
                                palabra_escogida = palabra_lazar (lista_palabras)
                                lista_correctas = asigna_casillas (palabra_escogida, letras_correctas)
                                lista_pistas, longitud_palabra = asignar_palabra(palabra_escogida)
                                
                                prints_inicio (palabra_escogida, longitud_palabra, letras_correctas, lista_pistas, vidas)
                                
                                palabra_escogida_destruible = palabra_escogida
                                
                                perdio = False
                                comp_jugar = True
                                valido = False
                            
                            elif (jugar == "no" or jugar == "No"):
                                print ("Hasta la Proxima")
                                comp_jugar = True
                                valido = True
                                adivinado = True
                            
                            else:
                                print ("Ingresa un valor Valido")
                    
                    
                    
            else:
                print ("letra usada")
               
                
        else:
            valido = False
            print("Valor No Valido, Ingresa Una Letra A La Vez")

"""
Los Valores que se necesitan para debugear como: lista de palabras, la palabra
que se esta adivinando u otras palabras importantes para probar; fueron eliminadas
desde esta version para empezar a disenar la interfaz para el usuario.
"""