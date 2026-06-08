# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head != None:
            
            if head.next !=None:
                a,b = head, head.next.next
                while b!= None:
                    if b.next == a:
                        return True
                    else:
                        
                        a = a.next
                        try:
                            b = b.next.next
                        except:
                            return False
                return False
            else:
                return False
        else:
            return False

        
        