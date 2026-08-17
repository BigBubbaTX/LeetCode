class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        saved = set()
        for i in nums:
            if i in saved:
                return True
           
            saved.add(i)
        return False