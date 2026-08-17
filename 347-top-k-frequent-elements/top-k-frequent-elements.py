class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 0
            dic[i]+=1
        solve = [[] for _ in range(len(nums)+1)]
        for i in dic:
            solve[dic[i]-1].append(i)
        true_solve = []
 
        for i in range(len(solve)-1,-1,-1):
            if len(solve[i])>0:
                for j in solve[i]:
                    if len(true_solve) == k:
                        return true_solve
                    true_solve.append(j)
        return true_solve
            
