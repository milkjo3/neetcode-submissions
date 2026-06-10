class Solution:
    def tribonacci(self, n: int) -> int:
        cache = [0, 1, 1]

        if n < len(cache):
            return cache[n]

        for i in range(3, n+1):
            total = cache[-1] + cache[-2] + cache[-3]
            cache.pop(0)
            cache.append(total)

        return cache[-1]