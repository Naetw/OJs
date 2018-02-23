# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.que = []
        self.leaf_num = 0

    def rightSideView(self, root):
        ret = []
        if root:
            self.que.append(root)
            self.leaf_num = 0
            remain_leaf = 1
            while self.que:
                node = self.que.pop(0)
                tmp = node                      # override the right-most leaf value
                self.append_node(node.left)
                self.append_node(node.right)

                remain_leaf -= 1

                if remain_leaf == 0:            # current node is the right-most leaf in its depth level
                    ret.append(tmp.val)
                    remain_leaf = self.leaf_num
                    self.leaf_num = 0
        return ret

    def append_node(self, node):
        if node:
            self.que.append(node)
            self.leaf_num += 1                  # gather the info of next depth level
