class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        saved = {}
        for j in range(len(nums)):
            need = target - nums[j] 
            if need in saved:
                return [saved[need],j]
            saved[nums[j]] = j
            