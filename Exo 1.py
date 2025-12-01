
def test_distinct(sequence):
    # On compare la longueur de la liste avec celle de l'ensemble (qui supprime les doublons)
    return len(sequence) == len(set(sequence))

# Tests
print(test_distinct([1, 5, 7, 9]))       # True
print(test_distinct([2, 4, 5, 5, 7, 9])) # False
