class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elements = set(nums)

        if len(nums) != len(elements):
            return True
            
        return False