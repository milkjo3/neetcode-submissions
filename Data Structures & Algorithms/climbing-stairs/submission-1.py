class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = [1, 2]
        for i in range(2, n + 1):
            ways = cache[0] + cache[1]
            
            cache.pop(0)
            cache.append(ways)

        return cache[0]