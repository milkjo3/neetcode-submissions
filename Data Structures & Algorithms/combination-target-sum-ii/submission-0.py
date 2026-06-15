class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # TC: O(n * 2^n) - Copy n elements into the result with O(2^n) possible results.
        # SC: O(n) - Recursion depth is atmost n.
        # choice - a number from candidates
        # constraint - number must be distinct and sum to target
        # goal - generate all distinct combinations of sums that lead to target

        sol = []
        path = []

        def backtrack(start, total):

            # Add solution to the result.
            if total == target:
                sol.append(path.copy())
                return
            
            # The total is greater than the target, wrong path we took.
            if total > target:
                return

            # Filter out duplicated solutions through sorting the candidates.
            candidates.sort()

            # Iterate through all choices starting with index start:
            for i in range(start, len(candidates)):
                
                # Prevent same combination by skipping duplicate choices
                # at the same decision level.
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Make a choice (add a number).        
                path.append(candidates[i]) 

                # Explore other paths using different numbers.
                backtrack(i + 1, total + candidates[i])

                # Undo that choice for future paths. 
                path.pop()

        # Start at the beginning of the array with total 0. 
        backtrack(0, 0)
        return sol