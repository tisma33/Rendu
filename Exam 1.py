
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        
        start, max_len = 0, 1
        
        for i in range(len(s)):
            start, max_len = self.expandAroundCenter(s, i, i, start, max_len)

            start, max_len = self.expandAroundCenter(s, i, i + 1, start, max_len)
        
        return s[start:start + max_len]
    
    def expandAroundCenter(self, s, left, right, start, max_len):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
                start = left
            left -= 1
            right += 1
        return start, max_len
