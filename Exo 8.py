
# Programme FizzBuzz de 1 à 50

for fizzbuzz in range(1, 51):  # De 1 à 50 inclus
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
    elif fizzbuzz % 3 == 0:
        print("fizz")
    elif fizzbuzz % 5 == 0:
        print("buzz")
    else:
        print(fizzbuzz)
