from Joc import *
from Cartes import *
import os

clear = lambda: os.system('clear')
diners = 1000


# Platar-se
def menu2(jugada, aposta, cartes): 
    global diners
    clear()

    print("La teva jugada és: " + str(jugada))
    print("La teva aposta és: " + str(aposta))

    print("\nAra juga la banca.....")

    jugada_banca = jocBanca(cartes)

    print("La jugada de la banca és: " + str(jugada_banca))

    if jugada > 21 and jugada_banca <= 21: # Jugador ha tret mes de 21 i la banca menys
         print("\nLA BANCA GUANYA\n")
         startPartida()

    if jugada <= 21 and jugada_banca > 21: #  La banca ha tret mes de 21 i el jugador menys
        print("\nEL JUGADOR GUANYA\n")
        diners += aposta*2 # el jugador guanya el doble dels diners que ha apostat 
        startPartida() 

    if jugada > jugada_banca and jugada <= 21: # jugada del jugador es mes gran que la de la banca i el jugador no s'ha pasat de 21
        print("\nEL JUGADOR GUANYA\n")
        diners += aposta*2
        startPartida()

    if jugada < jugada_banca and  jugada_banca <= 21: # jugada del jugador es mes petita que la de la banca i la banca no s'ha pasat de 21
        print("\nLA BANCA GUANYA\n")
        startPartida()

    if (jugada == jugada_banca) or (jugada > 21 and jugada_banca > 21): # en el cas de que les dues jugades siguin iguals o els dos es pasin de 21 la partida quedara empatada
        print("\nEMPAT\n")
        diners += aposta # com han empatat es reparteixen els diners, es a dir, el jugador recupera els diners de l'aposta 
        startPartida()

# Demanar carta
def menu1(cartes,jugada, cartes_jugada, aposta):
    carta, cartes = Joc.obtenirCarta(cartes) # la crida a aquesta funcio et retorna una carta aleatoria i la llista de cartes sense la carta que hi ha a la "taula"
    cartes_jugada.append(carta) # llista amb les cartes que ha tret el jugador

    jugada += carta.numero # es va sumant el numero de les cartes
    
    situacio(carta, cartes_jugada, jugada) # printa informacio de la partida

    if jugada > 21: # si la jugada pasa de 21 automaticament crida a la funcio de plantar-se
        menu2(jugada, aposta,cartes)

    return jugada, carta

# Jugada de la banca (automatica)
def jocBanca(cartes):

    cartes_jugada = []
    jugada_banca = 0

    while True:
        
        carta, cartes = Joc.obtenirCarta(cartes)
        cartes_jugada.append(carta)
        
        jugada_banca += carta.numero
        Cartes.printCarta(carta)
        
        #Condicions per deixa de demanar cartes
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

# printar la situacio de la partida
def situacio(carta, cartes_jugada, jugada):

    print("Joc: " + str(jugada) + "\n")
    print("Nova carta: ")
    Cartes.printCarta(carta)
    print("\n\nCartes: ")
    Joc.veureCartes(cartes_jugada)
    print("\n\n")

# Començar la partida
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

            if menu == '1' or menu == '2' or menu == '3': # si "menu" es igual a algun dels numeros demanars continua el programa
                clear()
                break
            else: # en cas contrari mostrara un missatge i tornara a demanar un numero
                print("Has d'introduir un valor correcte")

        if menu == '1':
            
            jugada, carta = menu1(cartes,jugada, cartes_jugada, aposta) #funcio menu1

        if menu == '2':

            if jugada == 0:
                jugada, carta = menu1(cartes,jugada, cartes_jugada, aposta) #funcio menu2
            
            menu2(jugada, aposta,cartes)

        if menu == '3': # augmentar aposta
            aposta, diners = Joc.pujarAposta(aposta, diners) # pujar aposta necesita els diners que tens actualment per poder fer comporvacions 
            clear()
            situacio(carta, cartes_jugada, jugada)

startPartida()