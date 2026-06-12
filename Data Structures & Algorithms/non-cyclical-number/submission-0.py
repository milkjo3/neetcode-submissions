class Solution:
    def isHappy(self, n: int) -> bool:

        # Calculate the SoS for all digits in a number.
        def sumOfSquares(n: int) -> int:
            total = 0

            # For each digit, square it and add it to the total.
            while n:
                digit = n % 10
                square = digit ** 2
                total += square
                n = n // 10

            return total

        # Create a set 
        seen = set()

        # Until the number converges to 1 (or exits prematurely due to cycle)
        num = n
        while (num != 1):

            # Check if its apart of a cycle
            if num in seen:
                return False

            # Add the number to set that tracks cycles.
            seen.add(num)

            # Use the new value
            num = sumOfSquares(num)
            
        # Return True (Happy #.) as it converged to 1.
        return True

        

        