#Definition for a binary tree node.
#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3322/
'''
Cousins in Binary Tree

Solution
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.

'''
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
class Solution:
    '''
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        stack = [(root,0,root.val)]
        nx = None
        ny = None
        for node, level, parent in stack:
            if node.left: stack.append((node.left, level+1, node.val))
            if node.right: stack.append((node.right, level + 1, node.val))
            if node.val == x:
                nx = (node, level, parent)
            if node.val == y:
                ny = (node, level, parent)

            if nx and ny and nx[1]==ny[1] and nx[2] !=ny[2]:
                return True
        return False
        '''
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        xinforma = []
        yinforma = []
        depth = 0
        parent = None
        if root is None:
            return False

        self.dfs(root, x, y, 0, None, xinforma, yinforma)
        return xinforma[0][0] == yinforma[0][0] and xinforma[0][1] != yinforma[0][1]

def dfs(self, root, x, y, depth, parent, xinforma, yinforma):
    if root is None:
        return None
    if root.val == x:
        xinforma.append((depth,parent))
    if root.val == y:
        yinforma.append((depth,parent))

    self.dfs(root.left, x, y, depth+1, parent, xinforma, yinforma)
    self.dfs(root.right,  x, y, depth+1, parent, xinforma, yinforma)







