class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # choice - to add or not to add a number
        # constraint - can only add one number
        # goal - generate all subsets

        sol = []
        path = []

        # Case for empty lists.
        if not nums:
            return sol

        def backtrack(i):
            # Done making decisions about every number.
            if i == len(nums):
                sol.append(path.copy())
                return

            # Do not include nums[i]. "Make a choice."
            backtrack(i + 1)

            # Do include nums[i]. "Make a choice."
            path.append(nums[i])

            # Explore everything from that inclusion.
            backtrack(i+1)

            # Undo our choice to explore different branches of decision tree.
            path.pop()

        backtrack(0)
        return sol