# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # Preorder traversal to visit each node and invert binary tree.
        def preorderTraversal(root: TreeNode):

            # First check if the root is None.
            if root is None:
                return

            # Swap the current left and right pointers. Since we 
            # swapped references, their children remain attached to them.
            root.left, root.right = root.right, root.left

            # Now traverse into the current node's left subtree.
            preorderTraversal(root.left)

            # Finally traverse into the current node's right subtree.
            preorderTraversal(root.right)

        # Visit each node and swap the children, inverting the binary tree.
        preorderTraversal(root)
        
        return root