from Joc import *
from Cartes import *

import os

cartes = Joc.crearCartes()
jugada = 0
clear = lambda: os.system('clear')
cartes_jugada = []
diners = 1000
aposta = 0
jugada = 0

while True:
    

    while jugada <= 21:
        print("Jugador\n-----------------\nDiners: " + str(diners))
        print("Aposta: " + str(aposta))

        menu = input("-----------------\n1. Demanar carta\n2. Plantar-se\n3. Pujar aposta\n-----------------")

        if menu == '1' or menu == '2' or menu == '3':
            clear()
            break
        else:
            print("Has d'introduir un valor correcte")

    if menu == '1':

        clear()

        carta, cartes = Joc.obtenirCarta(cartes)
        cartes_jugada.append(carta)
      
        jugada += carta.numero
        print("Joc: " + str(jugada) + "\n")
        print("Nova carta: ")
        Cartes.printCarta(carta)
        print("\n\nCartes: ")
        Joc.veureCartes(cartes_jugada)
        print("\n\n")

    if menu == '2':
        print("hola")




    if menu == '3':
        aposta, diners = Joc.pujarAposta(aposta, diners)