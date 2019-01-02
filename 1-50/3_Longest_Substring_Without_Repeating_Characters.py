# /usr/bin/python
# -*- encoding:utf-8 -*-

# Given a string, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution(object):

    def length_of_longest_sub_string(self, input_str):
        if not input_str or len(input_str) == 0:
            return 0
        res, start, n = 0, 0, len(input_str)
        maps = {}
        for i in range(n):
            start = max(start, maps.get(input_str[i], -1)+1)
            res = max(res, i - start + 1)
            maps[input_str[i]] = i
        return res


if __name__ == "__main__":
    solution = Solution()
    print solution.length_of_longest_sub_string("pwwkew")
    print solution.length_of_longest_sub_string("bbbbbb")