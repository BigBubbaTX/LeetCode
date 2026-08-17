class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = set()
        longest = 0
        left = 0
        for i in s:
            #print(cur)
            if i in cur:
                while i in cur:
                    cur.remove(s[left])
                    left +=1
            cur.add(i)
            if len(cur)>longest:
                longest = len(cur)
        return longest
           