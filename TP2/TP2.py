class rectangle:
    def __init__(self, hauteur, largeur):
        self.hauteur = hauteur
        self.largeur = largeur
    def perimetre(self):
        return 2 * (self.hauteur + self.largeur)
    def surface(self):
        return self.hauteur * self.largeur
    def diagonal(self):
        return ((self.largeur ** 2 + self.hauteur **2) ** 0.5)
    def get_picture(self):
        if self.largeur > 50 or self.hauteur > 50:
            return "Trop gros."
        else:
            return ("*" * self.largeur + "\n") * self.hauteur

    def get_amount_inside(self, shape):
        return (self.largeur // shape.largeur) * (self.hauteur // shape.hauteur)

    def afficher(self):
        print("Hauteur :", self.hauteur)
        print("Largueur :", self.largeur)
        print("Perimetre :", self.perimetre())
        print("Surface :", self.surface())
        print("Diagonale :", self.diagonal())
        print(self.get_picture())

a, b = int(input("Entrez la Hauteur :")), int(input("Entrez la Largueur :"))
rect = rectangle(a, b)
rect.afficher()

class Carree(rectangle):
    def __init__(self, cote):
        self.cote = cote
        super().__init__(cote, cote)
    def afficher(self):
        print("Côté :", self.cote)
        print("Perimetre :", self.perimetre())
        print("Surface :", self.surface())
        print("Diagonale :", self.diagonal())
        print(self.get_picture())
a = int(input("Entrez le Côté :"))
car = Carree(a)
car.afficher()
