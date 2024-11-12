from class_person import Person

# On instancie l'objet Person
tristan = Person("Tristan", "Thouvenot", 39)

# On vérifie les informations
print("*****")
print("Avant l'anniversaire")
tristan.introducing()

# On ajoute 1 an
tristan.anniversary()
print()
print("*****")
print("Aprés l'anniversaire")
# On vérifie que la méthode fonctionne
tristan.introducing()

# On ajoute 2 ans
tristan.anniversary()
tristan.anniversary()
print()
print("*****")
print("Aprés 2 anniversaires")
# On vérifie
tristan.introducing()