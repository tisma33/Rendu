class Solution: 
    def romanToInt(self, s: str) -> int:
        valeurs = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        total = 0
        i = 0

        while i < len(s):
            if i + 1 < len(s) and valeurs [s[i]] < valeurs[s[i + 1]]:
                total += valeurs[s[i + 1]] - valeurs[s[i]]
                i += 2
            else:
                total += valeurs[s[i]]
                i += 1
        return total 
