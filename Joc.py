from Cartes import *
import random

class Joc:


    def crearCartes(): # crear totes les cartes de poker

        cartes = []

        
        for x in range(1,13):
            cartes.append(Cartes("Picas", x)) # es crea un objecte Cartes amb un string i un numero
        for x in range(1,13):
            cartes.append(Cartes("Corazones", x))
        for x in range(1,13):
            cartes.append(Cartes("Diamantes", x))
        for x in range(1,13):
            cartes.append(Cartes("Treboles", x))

        return cartes # retorna una llista amb totes les cartes
        
   
    def veureCartes(cartes): # printar una carta 

        for carta in cartes:
            print("%i de %s" % (carta.numero, carta.pal))

    def pujarAposta(aposta, diners):

        print("Aposta actual: " + str(aposta))

        while True:
            print("Els teus diners: " + str(diners))
            new_aposta = int(input("Quant vols pujar: "))

            if new_aposta <= diners and new_aposta > 1: # comprovacio de que no apostis mes diners dels que tens i que l'aposta sigui superior a 1
                diners -= new_aposta # es resta l'aposta dels diners del jugador
                return new_aposta + aposta, diners # retorna l'aposta que queda i els diners que li queden al jugador
            else:
                print("L'aposta no pot ser superior als diners del jugador ni inferior a 1")

    # obtenir una carta de forma aleatoria
    def obtenirCarta(cartes):
        carta = random.choice(cartes) # obte una carta aleatoria dins de la llista
        cartes.remove(carta) # s'elimina la carta obtinguda per que no torni a sortir 
        return carta, cartes