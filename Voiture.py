class Voiture:
    def __init__(self,marque,modele,puissanceFiscale,couleur,option=[]):
     self.__marque = marque
     self.__modele = modele
     self.__puissanceFiscale = puissanceFiscale
     self.__couleur = couleur
     self.__option = option

    def __str__(self):
        return f"Voici les caractéristiques de cette voiture : \n- Marque : {self.__marque} \n- Modele : {self.__modele} \n- Couleur : {self.__couleur} \n- puissanceFiscale : {self.__puissanceFiscale} \n-Options : {self.__option}"
    def ajouter_option(self, option):
        self.__option.append(option)

    def supprimer_option(self, option):
        self.__option.remove(option)

    def is_option_present(self, option):
        if option in self.option:
            print("option is in option")
        else:
            print("option is not in option")

    def get_marque(self):
        return self.__marque
    def get_modele(self):
        return self.__modele
    def get_puissanceFiscale(self):
        return self.__puissanceFiscale
    def get_couleur(self):
        return self.__couleur
    def get_option(self):
        return self.__option

    def set_marque(self,marque):
        self.__marque = marque
    def set_modele(self,modele):
        self.__modele = modele
    def set_puissanceFiscale(self,puissanceFiscale):
        self.__puissanceFiscale = puissanceFiscale
    def set_couleur(self,couleur):
        self.__couleur = couleur
    def set_option(self, option):
            self.__option = option