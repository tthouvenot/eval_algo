# On doit créer une fonction qui calcule la somme des n entier

def sum_of_int(int):

    # On initialise la variable du résultat de la somme
    result = 0

    # On boucle pour ajouter à la variable chaque entier entre 1 et n
    for i in range (1, int+1):

        result += i

    # On retourne le résultat
    return result

print(sum_of_int(5))
print(sum_of_int(10))
print(sum_of_int(42))