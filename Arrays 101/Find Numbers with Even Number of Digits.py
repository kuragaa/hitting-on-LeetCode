# Given an array nums of integers, return how many of them contain an even number of digits.
# Input: nums = [555,901,482,1771]
# Output: 1
# Explanation:
# Only 1771 contains an even number of digits.

from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            if len(str(i))%2 == 0:
                res+=1
        return res