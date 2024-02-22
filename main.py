from Voiture import *

if __name__ == "__main__":
    myCar1 = Voiture("Mercedes-Benz", "C63", 4, "Noir")
    print(f"Voiture{myCar1}")
    myCar2 = Voiture(None,None,None,None)
    myCar3 = Voiture("Audi","RSQ6",5,"Gris Nardo")
    myCar4 = Voiture(None, None, None, "Noir")
    #partie 2 print(f"voiture{myCar1__couleur}")
    #print(f"Voiture : {myCar1.get_marque()} \nMarque de Voiture 2: {myCar2.get_marque()}")
    print((f"Voiture{myCar3}"))


myCar1.ajouter_option("Climatisation")
myCar1.supprimer_option("Climatisation")
print(myCar1)

