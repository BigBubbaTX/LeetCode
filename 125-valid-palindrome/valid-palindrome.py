class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for i in s:
            if i.isalnum():
                clean += i.lower()
        for i in range(len(clean)//2):
            if clean[i] != clean[-i-1]:
                return False
        return True