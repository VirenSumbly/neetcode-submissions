# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head):
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second 
        prev, curr = None, slow.next
        slow.next = None  

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # merge
        first, second = head, prev

        while second:
            t1 = first.next
            t2 = second.next

            first.next = second
            second.next = t1

            first = t1
            second = t2