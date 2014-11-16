# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def visit(self, node):
        if node.left:
            self.visit(node.left)
        if self.previousNode and self.previousNode.val > node.val:
            if len(self.wrongNodes) == 0:
                self.wrongNodes = [self.previousNode, node]
            else:
                self.wrongNodes[1] = node
                return
        self.previousNode = node
        if node.right:
            self.visit(node.right)

    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        self.wrongNodes = []
        self.previousNode = None
        self.visit(root)
        # print self.wrongNodes[0].val, self.wrongNodes[1].val
        self.wrongNodes[0].val, self.wrongNodes[1].val = \
            self.wrongNodes[1].val, self.wrongNodes[0].val
        return root

# node1 = TreeNode(1)
# node2 = TreeNode(2)
# node3 = TreeNode(3)
# node4 = TreeNode(4)
# node5 = TreeNode(5)
# node6 = TreeNode(6)
# node7 = TreeNode(7)
# node4.left = node7
# node4.right = node6
# node7.left = node1
# node7.right = node3
# node6.left = node5
# node6.right = node2

# sol = Solution()
# print sol.recoverTree(node4)

# node0 = TreeNode(0)
# node1 = TreeNode(1)
# node0.left = node1

# sol = Solution()
# print sol.recoverTree(node0)

        