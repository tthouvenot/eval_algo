# On crée une classe Compte bancaire qui attribut un solde et possède 2 méthodes
# déposer(): ajoute de l'argent au solde
# retirer(): retire de l'argent au solde

class BankAccount:

    # On définit le constructeur
    def __init__(self, balance):
        self.balance = balance

    # On crée la méthode pour retirer de l'argent du compte
    def withdraw(self, ammount):

        # On vérifie que le solde est positif et qu'il n'est pas plus petit que le montant retiré
        if self.balance >= ammount:
            # S'il y a assez d'argent alors on retire l'argent du solde
            self.balance -= ammount
            print(f"Votre nouveau solde est de: {self.balance}€")
        else:
            print(f"Vous ne disposez pas des fonds suffisant. Votre solde actuel est de: {self.balance}€")

    # On crée la méthode pour ajouter de l'argent au compte
    def deposit(self, ammount):
        
        # On ajoute le montant au solde existant
        self.balance += ammount
        print(f"Votre nouveau solde est de: {self.balance}€")

# On instancie l'objet BankAccount
my_bank_account = BankAccount(0)
my_old_bank_account = BankAccount(1250)

# On essaie de retirer de l'argent
my_bank_account.withdraw(50)
my_old_bank_account.withdraw(150)

# On ajoute de l'argent
my_bank_account.deposit(150)
my_old_bank_account.deposit(50)