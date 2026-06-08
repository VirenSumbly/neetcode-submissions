# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        arr1 = []
        arr2 = []
        def InTrav1(root):
            if not root:
                arr1.append("null")
                return
            arr1.append(root.val)
            InTrav1(root.left)
           
            InTrav1(root.right)
        InTrav1(p)
        def InTrav2(root):
            if not root:
                arr2.append("null")
                return
            arr2.append(root.val)
            InTrav2(root.left)
            
            InTrav2(root.right)
        InTrav2(q)
        print(arr1)
        print(arr2)
        return arr1==arr2

        