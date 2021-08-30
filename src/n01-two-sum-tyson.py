"""
Leetcode: two-sum
Lettcode #001
Date: [2021-08-30]
Author: Thai-Son Tu
Description: Given an array of integers nums and an integer target, return indices of the two numbers such that they
add up to target. You may assume that each input would have exactly one solution, and you may not use the same element
twice. You can return the answer in any order.
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""


# Idea: using Python build-in enumerate() method
class Solution:
    def twoSum(self, nums, target):
        hash_map = {}
        for index, value in enumerate(nums):
            if value not in hash_map:
                hash_map[value] = index
            if target - value in hash_map.keys() and hash_map[target - value] != index:
                result = [index, hash_map[target - value]]
                result.sort()
                return result


# Example 1 --
sol = Solution()
answer = sol.twoSum([2, 7, 11, 15], 9)
print(answer)
