class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower() != s[r].lower():
                    return False
            elif s[l].isalnum():
                r -= 1
                continue
            elif s[r].isalnum():
                l += 1
                continue
            r -= 1
            l += 1
            
        return True