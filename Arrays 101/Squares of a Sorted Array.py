# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        left = 0
        right = n - 1
        for i in range(n - 1, -1, -1):
            sq_left = nums[left] ** 2
            sq_right = nums[right] ** 2

            if sq_left > sq_right:
                res[i] = sq_left
                left += 1
            else:
                res[i] = sq_right
                right -= 1
        return res