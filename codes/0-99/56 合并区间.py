#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 11:20
# @Author  : XQZ
# @Site    : 
# @File    : 56 合并区间.py
# @Software: PyCharm


class Solution:
    def merge(self, intervals):
        if intervals is None:
            return []

        intervals.sort(key=lambda x: x[0])

        i = 0
        while i + 1 < len(intervals):
            A, B = intervals[i], intervals[i+1]
            new_interval = []

            if A[1] < B[0]:
                i += 1
                continue
            elif B[0] <= A[1] < B[1]:
                new_interval = [A[0], B[1]]
            elif B[1] <= A[1]:
                new_interval = A

            intervals.pop(i)
            intervals.pop(i)
            intervals.insert(i, new_interval)

        return intervals


if __name__ == "__main__":
    intervals = [[1, 3], [8, 15], [2, 6], [9, 10]]
    print(Solution().merge([]))
