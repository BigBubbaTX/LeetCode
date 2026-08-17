class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        write = 1
        last = nums[0]

        for read in range(1, len(nums)):
            current = nums[read]

            if current != last:
                nums[write] = current
                write += 1
                last = current

        return write
