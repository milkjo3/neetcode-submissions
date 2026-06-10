class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2}

        for i in range(3, n + 1):
            ways = 0
            ways += memo[i - 1]
            ways += memo[i - 2]
            memo[i] = ways

        return memo[n]