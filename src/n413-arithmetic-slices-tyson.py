"""
Leetcode: two-sum
Lettcode #413
Date: [2021-08-30]
Author: Thai-Son Tu
Description:An integer array is called arithmetic if it consists of at least three elements and if the difference
between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.
"""

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        result = []
        count = 0
        i = 0
        while i < n-1:
            j = i + 1
            current = [nums[i], nums[j]]
            step = nums[j] - nums[i]
            while j < n-1:
                if nums[j+1] - nums[j] != step:
                    break
                else:
                    current.append(nums[j+1])
                    j += 1
                    if len(current) >= 3:
                        count += 1
                        result.append(current.copy())
            i += 1
        return count
