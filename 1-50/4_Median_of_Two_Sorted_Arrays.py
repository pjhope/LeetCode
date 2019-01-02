# /usr/bin/python
# -*- encoding:utf-8 -*-

# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.
#
# Example 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5

# 解法1  暴力求解 空间复杂度 O（m+n） 时间复杂度 O(m + n)




# 解法二  求第K大的数

class Solution(object):
    def get_media_of_two_sorted_arrays(self, array_one, array_two):

        def get_kth_number_of_array(array_A, array_B, k):
            if len(array_A) == 0:
                return array_B[k-1]
            if len(array_B) == 0:
                return array_A[k-1]
            if k == 1:
                return min(array_A[0, array_B[0]])
            a = array_A[ k/2 -1] if len(array_A) >= k/2 else None
            b = array_B[ k/2 -1] if len(array_B) >= k/2 else None

            if b is None or ( a is not None & a < b):
                return get_kth_number_of_array(array_A[k // 2:], array_B, k - k // 2)
            else:
                return get_kth_number_of_array(array_A, array_B[k // 2:], k - k // 2)

        n = len(array_one) + len(array_two)
        if n % 2 == 1:
            return get_kth_number_of_array(array_one, array_two, n//2 + 1)
        else:
            smaller = get_kth_number_of_array(array_one, array_two, n//2)
            bigger = get_kth_number_of_array(array_one, array_two, n // 2 + 1)
            return (smaller + bigger) / 2


