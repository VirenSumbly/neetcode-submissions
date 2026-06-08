class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        # something that checks if two trees are equal
        arr1 = []
        arr2 = []
        def InTrav1(node):
            if not node:
                arr1.append("null")
                return
            arr1.append(node.val)
            InTrav1(node.left)
            InTrav1(node.right)
        
        def InTrav2(node):
            if not node:
                arr2.append("null")
                return
            arr2.append(node.val)
            InTrav2(node.left)
            InTrav2(node.right)
            
        InTrav1(root)
        InTrav2(subRoot)
        
        if arr1 == arr2:
            return True
            
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)