# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  ans = []
  def helper(self, root: TreeNode):
    if root is None:
      return
    self.ans.append(root.val)
    self.helper(root.left)
    self.helper(root.right)
  def preorderTraversal(self, root: TreeNode) -> List[int]:
    self.helper(root)
    return self.ans