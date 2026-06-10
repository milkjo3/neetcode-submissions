class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        library = {}

        for i in range(len(nums)):
            if nums[i] in library and abs(i - library[nums[i]]) <= k:
                return True
            library[nums[i]] = i
        return False