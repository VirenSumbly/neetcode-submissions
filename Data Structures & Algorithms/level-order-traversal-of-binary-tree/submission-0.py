# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        
        if root:
            queue.append(root)
        if not root:
            return []
        level = 0
        arr1 =[]
        while len(queue)>0:
            print("level:",level)
            arr2 =[]
            for i in range(len(queue)):
                curr = queue.popleft()
                print(curr.val)
                arr2.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                    #print(curr.left.val)
                    
                if curr.right:
                    queue.append(curr.right)
                    #print(curr.right.val)
                
            arr1.append(arr2)
            level +=1
            
        return arr1