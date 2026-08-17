class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        thedict = {}
        solve = []
        rember = []
        for i in strs:
            thedict[i] = {}
            for j in range(len(i)):
                if i[j] not in thedict[i]:
                    thedict[i][i[j]] = 0
                thedict[i][i[j]] +=1
        for i in range(len(strs)):
           
            cur = strs[i]
            curs = [cur]
            if cur not in rember:

                for j in range(i+1,len(strs)):
                    if thedict[cur]==thedict[strs[j]]:
                        curs.append(strs[j])
                        rember.append(strs[j])
                solve.append(curs)

        #print(solve)
        return solve