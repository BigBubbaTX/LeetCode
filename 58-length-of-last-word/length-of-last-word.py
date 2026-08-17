class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word =""
        for i in range(len(s)):
            if s[i]!= " ":
                word += s[i]
            if i == len(s)-1:
                return len(word)
            elif s[i] == " " and s[i+1] != " ":
                word = ""


        return len(word)
                