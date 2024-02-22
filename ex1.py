import sys, os
def affiche(chemin):
    for p in os.listdir(chemin):
        print(p)
if __name__ == '__main__':
   if len(sys.argv)!= 2:
       print(f"Mauvais nombre d'arguments")

   else:
        if not os.path.exists(sys.argv[1]):
            print(f"Chemin fourni {sys.argv[1]}")

        else:
            affiche(sys.argv[1])

