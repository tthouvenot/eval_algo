# On doit créer une fonction qui vérifie si le nombre en paramètre est pair ou impair

def odd_or_even(number):

    # On utilise le modulo 2 pour savoir s'il y a un reste ou non. 
    if number % 2 == 0:
        # S'il n'y a pas de reste alors c'est que le nombre est pair
        return "Pair"
    else: 
        # S'il y a un reste alors c'est que le nombre est impair
        return "Impair"
    
print(odd_or_even(5))
print(odd_or_even(122))