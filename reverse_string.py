# On doit créer une fonction qui inverse une chaîne de caractère et retourne la nouvelle chaîne

def reversed_string(string):

    # On utilise la méthode du slicing en parcourant la chaîne en sens inverse
    return string[::-1]

print(reversed_string("hello world"))

# En utilisant une boucle

def loop_reversed_string(string):

   # On définit une liste intermédiaire
    new_string = []

    # On boucle sur la chaîne de caractères en l'inversant
    for index in range(len(string) - 1, -1, -1):  # Parcours inversé des indices
        # On ajoute chaque lettre à la liste
        new_string.append(string[index])  # Utilise string[index] pour récupérer la lettre

    # On transforme la liste en string
    new_string = ''.join(new_string)
    
    return new_string

print(loop_reversed_string("Bonjour monde"))