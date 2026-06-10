class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two pointer approach: Start from both ends and converge inward.
        r = len(numbers) - 1
        l = 0

        # Calculate the current two sum. 
        two_sum = numbers[l] + numbers[r]

        # Keep iterating until we find the pair of indices (guaranteed solution) 
        while (two_sum != target):

            # If the two_sum is too big, since the array is sorted, move 
            # the right pointer to a smaller number.
            if two_sum > target:
                r -= 1

            # The two_sum is too small, since the array is sorted, move
            # the left point to a greater number. 
            else:
                l += 1

            # Recalculate the sum of the pair.
            two_sum = numbers[l] + numbers[r]

        # Return the indices plus one (1-indexed).
        return [l + 1,r + 1]
