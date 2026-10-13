# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         nSet=set()
#         node=head
#         while node is not None:
#             if node in nSet:
#                 return True
#             nSet.add(node)
#             node=node.next
#         return False
        

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # hare tortoise method
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                return True
        return False