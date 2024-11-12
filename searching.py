# On doit créer une fonction retourne vrai si un texte passé en premier paramètre contient le mot passé en deuxième paramètre

#  En utilisant la méthode str.find()
def contain_word(phrase, word):

    # On s'assure que tous les mots de la phrase et le mot en paramètre soit en minuscule
    phrase = phrase.lower()
    word = word.lower()

    # Si le mot est présent alors on retourne vrai
    # La méthode find retourne l'index où se trouve le mot, et s'il ne le trouve pas il renvoit -1
    if phrase.find(word) != -1: 
        return True
    else:
        return False
    
print(contain_word("Hello World", "world"))
print(contain_word("J'ai l'âme de l'enfant et la mémoire du vieux", "sucre"))

# En utilisant une boucle

def loop_contain_word(phrase, word):

    # on découpe la phrase en une liste de mot
    list_of_word = phrase.split()

    # On fait une boucle pour chaque mot dans la liste de mot
    for element in list_of_word:

        # Dès qu'on trouve une occurence on retourne Vrai
        if element == word:
            return True

    # S'il n'y a aucune occurence alors on retourne Faux
    return False

print(loop_contain_word("J'aime python", 'python'))
print(loop_contain_word("Ils sont beaux avec leurs cheveux plein de poux", 'averse'))