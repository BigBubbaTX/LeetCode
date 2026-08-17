# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:  
        try:
            a = ListNode(head.val)
        except AttributeError:
            return None
        clean_elements = [head.val]
        b = a
        while True:
            head = head.next
            try:
                if head.val not in clean_elements:
                    clean_elements.append(head.val)
                    b.next =ListNode(head.val)
                    b = b.next
                
            except AttributeError:
                return a
                break