
# Nombres divisibles par 7 et multiples de 5 entre 1500 et 2700 inclus

resultats = []
for x in range(1500, 2701):
    if x % 7 == 0 and x % 5 == 0:
        resultats.append(x)

# Affichage sur une seule ligne, séparés par des virgules
print(",".join(map(str, resultats)))
