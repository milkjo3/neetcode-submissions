class Solution:
    def climbStairs(self, n: int) -> int:
        
        x = 1 # i - 1 ways before final step (1)
        y = 2 # i - 2 ways before final step (2)
        if n == 1:
            return x

        # At the start of each loop iteration, x stores the number of ways 
        # to climb to the current step, and y stores the number of ways to 
        # climb to the next step.
        for i in range(2, n):
            ways = x + y

            x = y
            y = ways
            
        return y