#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 1:56
# @Author  : XQZ
# @Site    : 
# @File    : 55 跳跃游戏.py
# @Software: PyCharm


class Solution:
    def canJump(self, nums):
        dump_nums = 1    # 还能跳跃的能量，每跳一格消耗一格能量，进入第一个位置就消耗一个能量
        index = 0   # 位置标记

        while dump_nums > 0 and index < len(nums):
            dump_nums -= 1   # 消耗能量
            if nums[index] > dump_nums:  # 充能
                dump_nums = nums[index]
            index += 1

        return index == len(nums)


if __name__ == "__main__":
    nums = [2,3,1,1,4]
    print(Solution().canJump(nums))
