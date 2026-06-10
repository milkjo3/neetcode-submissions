class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize our library (hash) to store values for fast lookup.
        library = {}

        # Iterate through all candidates in the list, searching for target.
        for i in range(len(nums)):

            # Calculate the difference. 
            diff = target - nums[i]

            # Check if the difference exists in the library (ideal candidate).
            if diff not in library.keys():

                # If it is not in the library, add candidate to it.
                library[nums[i]] = i

            else:
                # Candidate is in library, return indices of the two sum.
                return [library[diff], i]