class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # goal - generate all combination sums
        # constraint - must add up to target
        # choice - a number in nums

        sol = []
        path = []

        def backtrack(start, total):
            # Add the solution to the target.
            if total == target:
                sol.append(path.copy())
                return

            # Undo that choice, it added up to over the target's value.
            if total >= target:
                return

            # Consider numbers from index start onward only (preventing duplicated combination sums).
            for i in range(start, len(nums)):

                # Make a choice (add a number).
                path.append(nums[i])

                # Explore all paths after making the choice.
                # Passing i instead of i + 1, because we can make the same choice multiple times.
                backtrack(i, total + nums[i])

                # Undo the choice.
                path.pop()

        backtrack(0,0)        
        return sol