# Pensamiento-computacional-para-ingenier-a-Gpo-405-

Fase inicial del programa

Este programa es una recreación del juego conocido como "Ahorcado". El programa inicia eligiendo una palabra a lazar de una lista de 5 palabras , despues de que esta
palabra es elegida y guardada el programa lee cuantas letras y posición tiene la palabra y lo representa al  jugador de la siguiente manera "Tu palabra tiene: ___ 
letras"(Ejemplo: Tu palabra tiene: 4 letras _ _ _ _ ), despues de esto el prorama le da una pista inicial de la palabra buscada (Ejemplo: "Es un animal que puede ser una 
mascota si lo tratas bien")

Fase De Juego
el programa le pide al jugador que ingrese una letra, el caso de que el jugador ingrese una letra correcta el programa mostrara la letra correcta y la mostrará (ejemplo
si adivinas la p: "Letra correcta!!! P _ _ _ "), en el caso de que el jugador pona una letras incorrecta entonces se mostrará el siguiente mensaje (ejemplo si no
adivinas la letra correcta: ""Letra incorrecta! _ _ _ _ Letras Intentadas Q Pista extra: Suele ser de color Amarillo, o café)

Finales del juego
En el caso de que tengas bien todas las letras del ahorcado entonces te saldra un mensaje felicitandote por haber acertado corretamente(ejemplo: "La Palabra era PATO,
Felicidades Ganaste!!!!")
En el caso de que tengas 3 errores entonces te saldra un mensaje diciendote la palabra correcta(ejemplo: "La Palabra era PATO, Mas suerte a la proxima")

# Biblioteca Random

La biblioteca random se utiiza para generar valores a lazar dentro de un rango, en este caso su uso es asignar una palabra a lazar al usuario para despues adivinarla, de 
esta manera se consigue que cada partida del juego sea diferente.

La pagina principal de donde se saco esta informacion es:
https://docs.python.org/3/library/random.html
