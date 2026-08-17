class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s = {}
        dict_t = {}
        for i in s:
            if i not in dict_s:
                dict_s[i] = 0
            dict_s[i] +=1
        for i in t:
            if i not in dict_t:
                dict_t[i] = 0
            dict_t[i] +=1
        return dict_s == dict_t