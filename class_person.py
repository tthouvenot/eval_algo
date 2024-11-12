# On doit créer une classe Personne avec comme attribut le nom, le prénom et l'âge
# On doit créer une méthode qui renvoit une phrase de présentation

class Person:

    # On initialise le constructeur avec les attributs
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # On crée la méthode qui affiche la phrase de présentation
    def introducing(self):
        print(f"Bonjour je m'appelle {self.first_name} {self.last_name} et j'ai {self.age} ans.")

    # On défini la méthode qui ajout 1 an chaque fois qu'elle sera appelée (exercice anniversary)
    def anniversary(self):
        self.age += 1

# On instancie les objets Person
franck = Person("Franck", "Bansept", 37)
damien = Person("Damien", "Saez", 47)

# On appelle les méthode de présentation
franck.introducing()
damien.introducing()