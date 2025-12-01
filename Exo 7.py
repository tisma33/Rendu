
# Programme pour compter les nombres pairs et impairs

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

pairs = 0
impairs = 0

for n in numbers:
    if n % 2 == 0:
        pairs += 1
    else:
        impairs += 1

print("Nombre de nombres pairs :", pairs)
print("Nombre de nombres impairs :", impairs)
