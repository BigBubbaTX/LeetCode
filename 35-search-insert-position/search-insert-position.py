class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target <= nums[i]:
                if target == nums[i]:
                    return i
                return i
            elif i == len(nums)-1:
                return i+1