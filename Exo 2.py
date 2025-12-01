
# Programme pour trouver la médiane de trois nombres

# Entrée des trois nombres
a = int(input("Input the first number: "))
b = int(input("Input the second number: "))
c = int(input("Input the third number: "))

# Trouver la médiane
numbers = [a, b, c]
numbers.sort()  # Trie la liste
median = numbers[1]  # L'élément du milieu

# Affichage du résultat
print("Median of the above three numbers -")
print(median)
