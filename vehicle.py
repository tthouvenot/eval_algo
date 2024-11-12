# On doit créer une classe véhicule avec comme attribut nombre_de_roue et couleur
# On doit créer une sous classe Vélo
# On doit créer une sous classe Voiture: possède un attribut nombre de porte, pas nécessaire de définir qu'elle a 4 roues

# on crée la classe principale
class Vehicle:

    # on défini le constructeur
    def __init__(self, color, num_of_wheels):
        self.number_of_wheels = num_of_wheels
        self.color = color

# On crée la classe vélo qui hérite de la classe vehicule
class Bike(Vehicle):
    
    # On défini le constructeur du vélo
    def __init__(self, color, num_of_wheels):
        # Il hérite du constructeur Véhicule
        super().__init__(color, num_of_wheels)

# On crée la classe voiture qui hérite de la classe vehicule
class Car(Vehicle):

    # On définit le constructeur de la voiture. On passe le nombre de roue par défaut
    def __init__(self, num_of_door, color, num_of_wheels = 4):
        # Il hérite de la classe véhicule
        super().__init__(color, num_of_wheels)
        # On lui fournit un attribut pour le nombre de porte
        self.number_of_door = num_of_door

# On instancie le vélo
my_bike = Bike("Blanc", 2)
# on instancie la voiture
my_car = Car(3, "Bleu")

# On vérifie les informations
print()
print(f"Mon vélo: \ncouleur: {my_bike.color}\nNombre de roue(s): {my_bike.number_of_wheels}")
print()
print(f"Mon voiture: \ncouleur: {my_car.color}\nNombre de roue(s): {my_car.number_of_wheels}\nNombre de porte: {my_car.number_of_door}")