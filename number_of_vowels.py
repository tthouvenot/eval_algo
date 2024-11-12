# On doit créer une fonction qui compte le nombre de vooyelle dans le mot

def number_of_vowels(string):

    # On défini un tuple avec toutes les voyelles
    vowels = ("a", "e", "i", "o", "u", "y")
    # On initialise la variable qui fera le calcule
    result = 0
    # On s'assure qu'il n'y a que des minuscules
    string = string.lower()

    # On fait une première boucle pour récupérer chaque lettre de la chaîne de caractère
    for letter in string:

        # On fait une deuxième boucle pour comparer la lettre avec les voyelles
        for vowel in vowels:

            # Si la lettre est une voyelle on ajout 1 au résultate
            if vowel == letter:
                result += 1

    return result

print(number_of_vowels('Elegant'))
print(number_of_vowels('Argentine'))