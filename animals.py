# On doit créer une classe animal avec avec une méthode bruit
# On doit créer une sous classe chat: renvoie miauler à la méthode bruit
# On doit créer une sous classe chien: renvoie aboyer à la méthode bruit

# On crée la classe principale
class Animal:

    # On définit son constructeur qui prendra le type d'animal
    def __init__(self, type):
        self.type = type

    # On crée la méthode qui renvoie le bruit fait selon le type d'animal
    def make_noise(self, sound):
        if self.type == 'chat' or self.type == "chien":
            return sound
        
#  On crée la classe Chat qui hérite de la classe Animal
class Cat(Animal):

    # On définit le constructeur hérité d'Animal, on lui donne comme paramètre le type d'animal 
    def __init__(self):
        super().__init__("chat")

    # On crée la méthode qui renvoit le résultat de la méthode make_noise en passant le type de bruit
    def noise(self):
        return self.make_noise("Miauler")

class Dog(Animal):

    # On définit le constructeur hérité d'Animal, on lui donne comme paramètre le type d'animal 
    def __init__(self):
        super().__init__("chien")

    # On crée la méthode qui renvoit le résultat de la méthode make_noise en passant le type de bruit
    def noise(self):
        return self.make_noise("Aboyer")

# On instancie les objets
my_cat = Cat()
my_dog = Dog()

# On appelle la méthode noise
print(f"Le type de cri pour un {my_cat.type} est {my_cat.noise()}.")
print(f"Le type de cri pour un {my_dog.type} est {my_dog.noise()}.")