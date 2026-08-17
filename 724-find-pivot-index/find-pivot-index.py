class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)-nums[0]
        right = total_sum
        left = 0
        piviot = 0
 
        for i in range(len(nums)):
            if i != 0:
                left += nums[piviot-1]
            if right == left:
                return piviot
            if i == len(nums) -1:
                return -1
            
            right -= nums[piviot+1]
            piviot +=1