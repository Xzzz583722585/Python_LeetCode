#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 16:16
# @Author  : XQZ
# @Site    : 
# @File    : 100 相同的树.py
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None:
            if q is None:
                return True
            else:
                return False

        queue_p = [p]
        queue_q = [q]

        while queue_p and queue_q:
            now_p = queue_p.pop(0)
            now_q = queue_q.pop(0)

            if now_p is None and now_q is None:
                continue
            elif now_p is None and now_q is not None:
                return False
            elif now_p is not None and now_q is None:
                return False
            elif now_p.val != now_q.val:
                return False
            else:
                queue_p.append(now_p.left)
                queue_p.append(now_p.right)
                queue_q.append(now_q.left)
                queue_q.append(now_q.right)

        return True


if __name__ == "__main__":
    n1_1 = TreeNode(1)
    n1_2 = TreeNode(2)
    n1_3 = TreeNode(3)

    # n1_1.left = n1_2
    n1_1.right = n1_3

    n2_1 = TreeNode(1)
    n2_2 = TreeNode(2)
    n2_3 = TreeNode(4)

    # n2_1.left = n2_2
    n2_1.right = n2_3

    print(Solution().isSameTree(n1_1, n2_1))
