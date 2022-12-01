# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def traverse(root):
            nonlocal res
            if not root:
                return
              
            stack = [(root, root.val)]
            
            while stack:
                node, val = stack.pop()
                if not node.left and not node.right:
                    res += val
                if node.left:
                    stack.append((node.left, val * 10 + node.left.val))
                if node.right:
                    stack.append((node.right, val * 10 + node.right.val))
        
        traverse(root)
        
        return res
