class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        wave = 0
        for i in range(num2-num1+1):
            c = str(num1+i)
            for j in range(len(c)-2):
                if c[j] < c[j+1] > c[j+2]:
                    print(c)
                    wave +=1
                elif c[j] > c[j+1] < c[j+2]:
                    print(c)
                    wave += 1
        return wave