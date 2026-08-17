# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        stack = []
        stack2 = []
        while l1 != None:
            stack.append(l1.val)
            l1 = l1.next
        while l2 != None:
            stack2.append(l2.val)
            l2 = l2.next
        
        l1_sum = 0
       
        
        a = (len(stack)-1)
        b = (len(stack2)-1)
        for i in range(len(stack)):
            l1_sum += stack.pop()*(10**(a-i))
        l2_sum = 0
        for i in range(len(stack2)):
            l2_sum += stack2.pop()*(10**(b-i))
        print(f"l1 sum is {l1_sum} and l2 is {l2_sum}")
        sum = l1_sum + l2_sum
        string_sum = str(sum)
        string_sum = string_sum[::-1]
        a = ListNode(int(string_sum[0]))
        cur = a
        for i in range(1,len(string_sum)):
            cur.next = ListNode(int(string_sum[i]))
            cur = cur.next
        return a

        