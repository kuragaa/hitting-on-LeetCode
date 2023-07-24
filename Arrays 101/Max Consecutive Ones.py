# Given a binary array nums, return the maximum number of consecutive 1's in the array.
# Input: nums = [1,0,1,1,0,1]
# Output: 2

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                res = max(res, count)
                count = 0
        res = max(res, count)
        return res