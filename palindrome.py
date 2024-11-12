# On doit créer une fonction qui détermine si le mot est un palindrome

# En utilisant le slicing
def is_palindrome(string):

    # On compare le mot avec son inverse
    if string == string[::-1]:
        # Si c'est le même mot on print "est un palindrome"
        print(f"{string} est un palindrome")
    else:
        # Si c'est pas le même mot on print "n'est pas un palindrome"
        print(f"{string} n'est pas un palindrome")

is_palindrome("kayak")
is_palindrome("voiture")

# En utilisant une boucle (on utilise la même fonction que l'exercice 3, mais avec une petite modification)
def loop_palindrome(string):

    # On définit une liste intermédiaire
    new_string = []

    # On boucle sur la chaîne de caractères en l'inversant
    for index in range(len(string) - 1, -1, -1):  # Parcours inversé des indices
        # On ajoute chaque lettre à la liste
        new_string.append(string[index])  # Utilise string[index] pour récupérer la lettre

    # On transforme la liste en string
    new_string = ''.join(new_string)

    # On compare le mot avec son inverse
    if string == new_string:
        # Si c'est le même mot on print "est un palindrome"
        print(f"{string} est un palindrome")
    else:
        # Si c'est pas le même mot on print "n'est pas un palindrome"
        print(f"{string} n'est pas un palindrome")

loop_palindrome("laval")
loop_palindrome("constance")