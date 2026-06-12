class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total = 0

        # Go through each digit in the list.
        for i in range(len(digits) - 1, -1, -1):

            # If the addition goes to 10, set the digit to 0.
            if digits[i] + 1 > 9:
                digits[i] = 0
            
            # Else we can just add one to the digit and we are done.
            else:
                digits[i] += 1
                return digits
        
        # If we hit here, we had a list like [9,9,9] and we set the digits
        # to [0,0,0], so we'll have to insert a 1 at the start.
        digits.insert(0, 1);
        return digits