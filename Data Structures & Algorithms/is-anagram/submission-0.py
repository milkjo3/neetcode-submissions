class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = defaultdict(int)
        d2 = defaultdict(int)

        for i in range(len(s)):
            d1[s[i]] += 1

        for j in range(len(t)):
            d2[t[j]] += 1   

        return d1 == d2 