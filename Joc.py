from Cartes import *
import random

class Joc:


    def crearCartes():

        cartes = []

        
        for x in range(1,13):
            cartes.append(Cartes("Picas", x))
        for x in range(1,13):
            cartes.append(Cartes("Corazones", x))
        for x in range(1,13):
            cartes.append(Cartes("Diamantes", x))
        for x in range(1,13):
            cartes.append(Cartes("Treboles", x))

        return cartes
        
   
    def veureCartes(cartes):

        for carta in cartes:
            print("%i de %s" % (carta.numero, carta.pal))

    def pujarAposta(aposta, diners):

        print("Aposta actual: " + str(aposta))

        while True:
            print("Els teus diners: " + str(diners))
            new_aposta = int(input("Quant vols pujar: "))

            if new_aposta <= diners and new_aposta > 1:
                diners -= new_aposta
                return new_aposta + aposta, diners
            else:
                print("L'aposta no pot ser superior als diners del jugador ni inferior a 1")


    def obtenirCarta(cartes):
        return random.choice(cartes)

