# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head.next ==None:
            head = None
            return head

        slow,fast = head, head
        for i in range(0,n):
            fast = fast.next

        if fast== None:
            head = head.next
            return head


        while fast.next != None:
            slow = slow.next
            fast = fast.next
           
        temp=slow.next.next
        slow.next = temp
        print(slow,temp,head)
        return head