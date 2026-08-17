class Solution:
    def reverse(self, x: int) -> int:
        solve = 0
        string_int = str(x)
        j = 0
        is_neg = False
        if string_int[0] == "-":
            is_neg = True
            string_int=string_int[1:]
        for i in range(len(string_int)):
            temp = int(string_int[i])
            solve += temp*(10**i)
        if solve > 2147483647:
            return 0
        if is_neg:

            return -solve
        print(solve)
        
        return solve