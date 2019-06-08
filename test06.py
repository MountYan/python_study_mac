class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        def depth(node):
            if not node:
                return 0
            return max(depth(node.left), depth(node.right)) + 1  # 深度加上根节点

        return self.isBalanced(root.left) and self.isBalanced(
            root.right) and abs(depth(root.left) - depth(root.right)) <= 1


if __name__ == '__main__':
    flag = Solution().isBalanced(root=TreeNode([3, 9, 20, None, None, 15, 7]))
    print(flag)
