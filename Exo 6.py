
# Programme pour convertir Celsius <-> Fahrenheit

temp = input("Saisissez la température que vous souhaitez convertir ? (par ex., 45F, 102C etc.) : ")

# On récupère la valeur numérique et l'unité
valeur = int(temp[:-1])       # Tout sauf le dernier caractère
unite = temp[-1].upper()      # Dernier caractère (C ou F), en majuscule

if unite == "C":
    # Conversion Celsius -> Fahrenheit
    resultat = (valeur * 9/5) + 32
    print(f"La température en Fahrenheit est de {resultat:.2f} degrés.")
elif unite == "F":
    # Conversion Fahrenheit -> Celsius
    resultat = (valeur - 32) * 5/9
    print(f"La température en Celsius est de {resultat:.2f} degrés.")
else:
    print("Unité non reconnue. Utilisez C ou F.")
