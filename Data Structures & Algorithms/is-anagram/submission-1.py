class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False

        freq_s, freq_t = {}, {}

        for i in range(len(s)):
            freq_s[s[i]] = 1 + freq_s.get(s[i], 0)
            freq_t[t[i]] = 1 + freq_t.get(t[i], 0)
        
        for j in freq_s.keys():
            if freq_s[j] != freq_t.get(j, 0):
                return False
                
        return True 