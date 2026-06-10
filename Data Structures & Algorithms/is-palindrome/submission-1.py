class Solution:
    def isPalindrome(self, s: str) -> bool:

        new = "".join([char.lower() for char in s if char.isalnum()])

        l = 0
        r = len(new) - 1

        while l < r:
            if new[l] != new[r]:
                return False
                
            r -= 1
            l += 1
            
        return True