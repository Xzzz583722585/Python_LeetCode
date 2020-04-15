#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 16:28
# @Author  : XQZ
# @Site    : 
# @File    : 257 二叉树的所有路径.py
# @Software: PyCharm


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode):
        traces = []
        self.preOrd(root, [], traces)
        return traces

    def preOrd(self, root, now_trace, traces):
        if root is None:
            return

        now_trace.append(str(root.val))
        self.preOrd(root.left, now_trace, traces)
        self.preOrd(root.right, now_trace, traces)

        if root.left is None and root.right is None:
            traces.append("->".join(now_trace))
        now_trace.pop()


if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n5 = TreeNode(5)

    n1.left = n2
    n1.right = n3

    n2.right = n5

    traces = Solution().binaryTreePaths(n1)
    print(traces)
