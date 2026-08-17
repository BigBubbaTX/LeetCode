class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = []
        last = 0
        for i in range(len(nums)):
            last += nums[i]
            sum.append(last)
        return sum