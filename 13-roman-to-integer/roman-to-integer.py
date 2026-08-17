class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        nums = []
        for ch in s:
            if ch == "I":
                nums.append(1)
            elif ch == "V":
                nums.append(5)
            elif ch == "X":
                nums.append(10)
            elif ch == "L":
                nums.append(50)
            elif ch == "C":
                nums.append(100)
            elif ch == "D":
                nums.append(500)
            elif ch == "M":
                nums.append(1000)
        for i in range(0,len(nums)):
            if i == len(nums)-1:
                total += nums[i]
                break
            if nums[i] < nums[i + 1]:
                total -= nums[i]
            else:
                total += nums[i]
        return total