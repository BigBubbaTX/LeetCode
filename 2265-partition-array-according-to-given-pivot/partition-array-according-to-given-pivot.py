class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        a = nums.count(pivot)
        j = 0    
        solve = []
        for i in range(a):
            nums.remove(pivot)
            solve.append(pivot)
        for i in range(len(nums)):
            if nums[i] < pivot:
                solve.insert(j,nums[i])
                j +=1             
            else:
                solve.append(nums[i])
        return solve