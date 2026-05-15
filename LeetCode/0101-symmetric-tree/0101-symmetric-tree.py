# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def isMirror(left, right):
            # 둘 다 없으면 대칭
            if not left and not right:
                return True

            # 하나만 없으면 대칭 아님
            if not left or not right:
                return False

            # 값이 다르면 대칭 아님
            if left.val != right.val:
                return False

            # 거울처럼 비교
            return (
                isMirror(left.left, right.right) and
                isMirror(left.right, right.left)
            )

        return isMirror(root.left, root.right)