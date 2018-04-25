from Joc import *
from Cartes import *
import os

clear = lambda: os.system('clear')
diners = 1000

def menu2(jugada, aposta, cartes):
    global diners
    clear()

    print("La teva jugada és: " + str(jugada))
    print("La teva aposta és: " + str(aposta))

    print("\nAra juga la banca.....")

    jugada_banca = jocBanca(cartes)

    print("La jugada de la banca és: " + str(jugada_banca))

    if jugada > 21 and jugada_banca <= 21:
         print("\nLA BANCA GUANYA\n")
         startPartida()

    if jugada <= 21 and jugada_banca > 21:
        print("\nEL JUGADOR GUANYA\n")
        diners += aposta*2
        startPartida()

    if jugada > jugada_banca and jugada <= 21:
        print("\nEL JUGADOR GUANYA\n")
        diners += aposta*2
        startPartida()

    if jugada < jugada_banca and  jugada_banca <= 21:
        print("\nLA BANCA GUANYA\n")
        startPartida()

    if (jugada == jugada_banca) or (jugada > 21 and jugada_banca > 21):
        print("\nEMPAT\n")
        diners += aposta
        startPartida()


def menu1(cartes,jugada, cartes_jugada, aposta):
    carta, cartes = Joc.obtenirCarta(cartes)
    cartes_jugada.append(carta)

    jugada += carta.numero
    
    situacio(carta, cartes_jugada, jugada)

    if jugada > 21: 
        menu2(jugada, aposta,cartes)

    return jugada, carta

def jocBanca(cartes):

    cartes_jugada = []
    jugada_banca = 0

    while True:
        
        carta, cartes = Joc.obtenirCarta(cartes)
        cartes_jugada.append(carta)
        
        jugada_banca += carta.numero
        Cartes.printCarta(carta)
        
        if jugada_banca > 21:
            return jugada_banca

        if jugada_banca >= 19 and jugada_banca <= 21:
            return jugada_banca

        if jugada_banca >= 15:
            if jugada_banca % 2 == 0:
                return jugada_banca

        if jugada_banca < 15 and jugada_banca > 12:
            if jugada_banca % 2 == 0:
                return jugada_banca
                
def situacio(carta, cartes_jugada, jugada):

    print("Joc: " + str(jugada) + "\n")
    print("Nova carta: ")
    Cartes.printCarta(carta)
    print("\n\nCartes: ")
    Joc.veureCartes(cartes_jugada)
    print("\n\n")


def startPartida():

    cartes = Joc.crearCartes()
    jugada = 0
    cartes_jugada = []
    aposta = 0
    fin = False
    global diners

    diners -= 50
    aposta = 50

    while True:

        while True:
            print("Jugador\n-----------------\nDiners: " + str(diners))
            print("Aposta: " + str(aposta))

            menu = input("-----------------\n1. Demanar carta\n2. Plantar-se\n3. Pujar aposta\n-----------------")

            if menu == '1' or menu == '2' or menu == '3':
                clear()
                break
            else:
                print("Has d'introduir un valor correcte")

        if menu == '1':
            
            jugada, carta = menu1(cartes,jugada, cartes_jugada, aposta)

        if menu == '2':

            if jugada == 0:
                jugada, carta = menu1(cartes,jugada, cartes_jugada, aposta)
            
            menu2(jugada, aposta,cartes)

        if menu == '3':
            aposta, diners = Joc.pujarAposta(aposta, diners)
            clear()
            situacio(carta, cartes_jugada, jugada)

startPartida()