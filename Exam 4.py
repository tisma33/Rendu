class solution:
    def plusone(self, digits: list[int]) -> list[int] n : = len(digits)
for i in range(n - 1, -1, -1):
    if digits[i] <9:
        digits[i] += 1
        return digits
#Manque de temps et je n'arrive pas à corriger les erreurs.