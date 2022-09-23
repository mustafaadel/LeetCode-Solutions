# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy  = ListNode()
        ptr = dummy
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            columnSum = v1 + v2 + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            ptr.next = newNode
            ptr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
    
        return dummy.next