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

# On importe le module random pour gérer le nombre aléatoire de bâton
import random

# On crée une méthode pour afficher le nombre de bâton restant
def draw_stick(remaining):
    
    print(f"Bâtons restants : {'|' * remaining} ({remaining})")

# On crée la méthode qui gère le choix du nombre de bâton que le joueur prend
def take_stick(player, max_sticks):

    #  Boucle qui gère l'erreur de saisie
    while True:
        try:
            choice = int(input(f"Joueur {player}, combien de bâtons voulez-vous enlever (1 à 3) ? "))

            # On gère l'erreur dans le nombre de bâton choisi
            if 1 <= choice <= 3 and choice <= max_sticks:
                return choice
            print(f"Choix invalide. Vous pouvez retirer entre 1 et {min(3, max_sticks)} bâtons.")
        # On gère l'erreur de saisie si ce n'est pas un entier
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entier.")

#  On crée la méthode qui gère le tour du joueur.
def game_turn(player, stick_remaining):

    # On appelle la fonction pour afficher le nombre de bâton
    draw_stick(stick_remaining)
    # On appelle la fonction qui demande au joueur le nombre de bâton qu'il souhaite prendre
    choice = take_stick(player, stick_remaining)

    # On retourne le nombre de bâton restant
    return stick_remaining - choice

# On crée la fonction qui gère la partie
def starting_player(starting_player):

    #  On défini le nombre de bâton pour la partie
    sticks_remaining = random.randint(15, 20)
    player = starting_player

    print("Nouvelle partie !")

    # Boucle du jeu qui gère les tours et le joueur qui joue
    while sticks_remaining > 0:
        # On appelle la fonction qui gère le tour du joueur 1 ou 2
        sticks_remaining = game_turn(player, sticks_remaining)

        # S'il n'y a plus de bâton alors on retourne le joueur qui a pris le dernier bâton
        if sticks_remaining == 0:
            print(f"Joueur {player} a pris le dernier bâton. Joueur {3 - player} gagne !")
            return player 
        
        # On alterne entre joueur 1 et 2 à chaque tour
        player = 3 - player  

# On crée la fonction qui gère la boucle des parties
def sticks_game():

    # Le joueur 2 commence la première partie
    loser = 2  

    # Boucle qui gère le lancement du jeu et la nouvelle partie
    while True:
        # Le perdant de la partie précédente commence si c'est une nième partie, sinon c'est le joueur 2
        loser = starting_player(loser) 
        # On demande s'il veut rejouer
        replay = input("Voulez-vous rejouer ? (oui/non) : ").strip().lower()

        if replay != 'oui':
            print("Merci d'avoir joué !")
            break

# On Lance le jeu
sticks_game()