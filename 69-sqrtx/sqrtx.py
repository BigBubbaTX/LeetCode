class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        while True:
            i += 1
            if i * i > x:
                return i-1

        