class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        
        # Pick a number.
        for i in range(len(nums)):
            
            # Store previously seen values for this i.
            library = set()

            # Find the target sum. Back to 2sum.
            target = -nums[i]

            # Find the other two numbers that add up to the target.
            for j in range(i + 1, len(nums)):

                # If the complement has already been seen,
                # we've found a valid triplet.
                if target - nums[j] in library:
                    sol.append(tuple(sorted([nums[i], nums[j], target-nums[j]])))

                # Add potential "nums[k]" value candidates to the library.
                library.add(nums[j])
        
        return [x for x in set(sol)]
