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
  def evulateAnswer(result: List[int], correctAnswer: List[int]) -> bool:
    # ...
  def main():
    testCases = [...]
    testCasesAnswer = [...]
    i = 0
    correctness = True
    for test in testCases:
      result = self.preorderTraversal(test)
      if evulateAnswer(result, testCasesAnswer[i]) is False:
        correctness = False
        break
      i = i + 1
    return correctness
  if __name__ == "__main__":
    main()