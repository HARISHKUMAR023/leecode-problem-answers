# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def inor(node):
            if node == None:
                return
            inor(node.left)
            ans.append(node.val)
            inor(node.right)
        inor(root)
        return ans