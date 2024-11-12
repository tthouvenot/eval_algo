# On doit créer une classe rectangle avec comme attributs la largeur et la hauteur. On a deux méthodes
# calculer_aire()
# calculer_perimètre()

class Rectangle:

    # On défini le constructeur
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # On crée la méthode pour calculer l'aire du rectangle
    def calculate_area(self):

        return self.width * self.height
    
    # On crée la méthode pour calculer le périmètre du rectangle
    def calculate_perimeter(self):

        return (self.width + self.height)*2
    
my_first_rectangle = Rectangle(12, 4)
my_second_rectangle = Rectangle(38, 16)

print("Premier rectangle:")
print()
print(my_first_rectangle.calculate_area()) # Doit retourner 48
print(my_first_rectangle.calculate_perimeter()) # Doit retourner 32
print("Second rectangle:")
print()
print(my_second_rectangle.calculate_area()) # Doit retourner 608
print(my_second_rectangle.calculate_perimeter()) # Doit retourner 108