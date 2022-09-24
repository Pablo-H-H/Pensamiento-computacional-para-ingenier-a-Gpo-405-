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

def prints_inicio (palabra_escogida, longitud_palabra, lista_pistas, vidas):
    print ("Tu Palabra Es: ", palabra_escogida)
    print ("Tu Palabra Tiene:", longitud_palabra, " letras", "_ " * longitud_palabra)
    print ("Tus Pista Es: ", lista_pistas[0])
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
vidas = 3
letras_usadas = []
lista_palabras = ["perro", "pato","piano", "fruta", "flor"]


palabra_escogida = palabra_lazar (lista_palabras)
lista_pistas, longitud_palabra = asignar_palabra(palabra_escogida)

#Comprobacion de las palabras Con proposito de Debugeo
prints_inicio (palabra_escogida, longitud_palabra, lista_pistas, vidas)
#Esta parte se usa para que el usuario meta una letra, guarda la letra y comprueba si la letra ya esta en uso

palabra_escogida_destruible = palabra_escogida

while (adivinado == False):
    
    
    
    while (valido == False):
        letra_usuario = input("ingresa una letra profavor: ")
        letra_valida = validacion(letra_usuario)
        
        
        
        if letra_valida:
            print("Valor valido!!!")
            letra_no_usada = lertra_usada_comprobacion(letra_usuario, letras_usadas)
            
            
            
            if letra_no_usada:
                print (letras_usadas)
                print("Esa letra No Estaba Usada")
                
                
                
                if (letra_si_esta (palabra_escogida_destruible, letra_usuario)):
                    print ("la letra estaba en la palabra")
                    palabra_escogida_destruible = eliminar_letra (palabra_escogida_destruible, letra_usuario)
                    print (palabra_escogida_destruible)
                    valido = False
                    
                else:
                    print ("Esta letra no estaba en la palabra")
                    print ("Pierdes una Vida")
                    vidas = vidas - 1
                    print ("Te quedan: ", vidas, "Vidas")
                    print (lista_pistas[(3-vidas)])
                    valido = False
                
                
                
                if (palabra_escogida_destruible == ""):
                    lista_palabras.remove(palabra_escogida)
                    comp_jugar = False
                    print (lista_palabras)
                    
                    print ("Adivinaste la Palabra!!!")
                    if (lista_palabras == []):
                        print ("Acabaste Todas Las Palabras")
                    else:
                        print ("Quieres Jugar Otra Vez?")
                        print ("Escribe: si o no")
                        while (comp_jugar == False):
                            jugar = input("")
                            if (jugar == "si" or jugar == "Si"):
                                print ("A Jugar")
                                palabra_escogida = palabra_lazar (lista_palabras)
                                lista_pistas, longitud_palabra = asignar_palabra(palabra_escogida)
                                prints_inicio (palabra_escogida, longitud_palabra, lista_pistas, vidas)
                                letras_usadas = []
                                palabra_escogida_destruible = palabra_escogida
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

"""Los imprime para comprobar si los datos son correctos,
en la version final esto sera elimiado"""