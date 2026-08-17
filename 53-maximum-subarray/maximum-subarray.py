class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        cur = nums[0]
        for i in range(1,len(nums)):
            if cur <= 0:
                cur = nums[i]
            else:
                cur += nums[i]
            if cur > best:
                best = cur
        return best