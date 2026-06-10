class Solution:
    def validPalindrome(self, s: str) -> bool:
        def sub_palidrome(self, s:str, l:int, r:int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False

                l += 1
                r -= 1
            return True
            
        l = 0 
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return sub_palidrome(self, s, l, r - 1) or sub_palidrome(self, s, l + 1, r)
            l += 1
            r -= 1
        return True 




