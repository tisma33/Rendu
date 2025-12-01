class Solution: 
    def lengthoflastword(self, s: str) -> int:
        s = s.strip()
        mots = s.split()
        return len(mots[-1])