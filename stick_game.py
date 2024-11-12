# Le jeu commence avec un nombre aléatoire de bâtons entre 15 et 20. À chaque tour, un joueur
# peut retirer entre 1 et 3 bâtons. Le but est d'éviter de retirer le dernier bâton, car celui qui enlève
# le dernier bâton perd la partie.
# Règles :
# 1. Le jeu commence avec 15 bâtons.
# 2. À chaque tour, un joueur doit choisir de retirer 1, 2 ou 3 bâtons.
# 3. Chaque joueur joue à tour de rôle, avec le joueur 1 et le joueur 2.
# 4. Le joueur qui prend le dernier bâton perd la partie.
# 5. Le jeu continue jusqu'à ce qu'un joueur prenne le dernier bâton.
# Instructions :
# 1. Le programme affiche le nombre de bâtons restants.
# 2. Demande au joueur actuel combien de bâtons il souhaite enlever (entre 1 et 3).
# 3. Si un joueur essaie de retirer un nombre de bâtons invalide (par exemple, plus que ce qui
# est disponible), le programme doit lui demander de choisir un nombre valide.
# 4. Le jeu se termine dès qu'un joueur enlève le dernier bâton et perd la partie.
# 5. Le programme affiche le nom du gagnant (le joueur qui n'a pas enlevé le dernier bâton).
# Une fois fini la partie reprend et c’est au perdant de commencer

# Pensez à vérifier le plus possible les différentes erreurs de saisie que l’utilisateur pourrait
# commettre
# Bonus : réalisez l’interface graphique de ce jeu

import random

number_of_stick = random.randint(15, 20)

player_one = input("Quel est le nom du joueur 1?: ")
player_two = input("Quel est le nom du joueur 2?: ")

def get_stick(player, stick):
    
    good_answer = False
    
    print(f"Vous disposez de {stick} bâtonnet(s).")

    while not good_answer:
        try: 
            number = int(input(f"Alors, {player}, combien de bâtonnet souhaitez vous retirer? (1, 2 ou 3): "))

            if number != 1 or number != 2 or number != 3:
                good_answer = True
                return number
            else:
                print("Vous devez choisir entre 1 et 3 bâtonnets")
        except:
            print("Erreur: veuillez entrer une valeur valide") 

is_playing = True

while is_playing:

    if number_of_stick > 1:
        choice_one = get_stick(player_one, number_of_stick)
        number_of_stick -= choice_one
        choice_two = get_stick(player_two, number_of_stick)
        number_of_stick -= choice_two
    else:
        print(choice_one)
        print(choice_two)