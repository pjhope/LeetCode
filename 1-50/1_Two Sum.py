# /usr/bin/python
# -*- encoding:utf-8 -*-

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# 方法一：暴力双循环法：

# 时间复杂度：O(n2), 空间复杂度：O（1）
class SolutionOne(object):
    def two_sum(self, nums, target):
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# 方法二： 利用空间来换取时间：

# 时间复杂度：O(n), 空间复杂度：O（n）
class SolutionTwo(object):
    def two_sum(self, nums, target):
        lookup = {}
        for i, value in enumerate(nums):
            if (target - value) in lookup:
                return [i, lookup[target - value]]
            else:
                lookup[value] = i

