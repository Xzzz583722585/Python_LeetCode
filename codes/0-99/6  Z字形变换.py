#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 10:35
# @Author  : XQZ
# @Site    : 
# @File    : 6  Z字形变换.py
# @Software: PyCharm


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 0:
            return ""
        if numRows == 1:
            return s
        length = len(s)
        n = 2 * numRows - 2     # Z中字符总数
        left, right = 0, n
        res = ""
        while left <= right:
            tmp = ""
            i = 0   # 当前Z的起始字符下标
            while i < length:
                if i + left < length:
                    tmp += s[i + left]
                if n > right != left and i + right < length:
                    tmp += s[i + right]
                i += n
            res += tmp

            left += 1
            right -= 1

        return res


if __name__ == "__main__":
    print(Solution().convert("A", 1))
    print("LDREOEIIECIHNTSG")
