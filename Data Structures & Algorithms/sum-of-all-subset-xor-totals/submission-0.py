class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0 

        def backtrack(idx, subset):
            nonlocal res
            xorr = 0
            for number in subset:
                xorr ^= number
            res += xorr

            for j in range(idx, len(nums)):
                subset.append(nums[j])
                backtrack(j+1, subset)
                subset.pop()

        backtrack(0, [])
        return res