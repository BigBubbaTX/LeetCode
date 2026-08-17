class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        for i in range(1, len(num)):
            if num[i-1] != num[len(num) - i]:
                return False
        return True