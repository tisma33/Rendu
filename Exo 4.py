
# Programme pour compter lettres et chiffres dans une chaîne

chaine = input("Saisissez une chaîne: ")

lettres = 0
chiffres = 0

for char in chaine:
    if char.isalpha():      # Vérifie si c'est une lettre
        lettres += 1
    elif char.isdigit():    # Vérifie si c'est un chiffre
        chiffres += 1

print("Lettres", lettres)
print("Chiffres", chiffres)
