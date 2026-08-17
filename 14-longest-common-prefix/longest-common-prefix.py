class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        j = 0
        return self.thing(j,strs)
 
    def thing(self,j,strs):
        total = ""
        for i in range(0, len(strs)):


            if self.shortest(strs) == j:
                for l in strs:
                    if len(l) ==j:
                        return l

            if strs[0][j] != strs[i][j]:
                print(f"false at the index: {j}")
                for k in range(0,j):
                    total = total + strs[0][k]
                return total
            elif i == len(strs) - 1:
                print(f"index {j} is all the same")
                j += 1
                return self.thing(j, strs)


    def shortest(self,strs):
        char = len(strs[0])
        for i in range(0, len(strs)):
            if len(strs[i]) <= char:
                char = len(strs[i])
        return char