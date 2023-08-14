'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1
and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
'''

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        a = m - 1  # pointer to the last non-zero element of the nums1
        b = n - 1  # pointer to the last non-zero element of the nums2
        cur = m + n - 1  # pointer to the end of the nums1

        while b >= 0:  # using b pointer - until we have elements in nums2 to insert in nums1

            if a >= 0 and nums1[a] > nums2[b]:  # if we have nums1 element that > of its pair in nums2 we put it to the end of nums1
                nums1[cur] = nums1[a]
                a -= 1
            else:
                nums1[cur] = nums2[b]
                b -= 1

            cur -= 1

