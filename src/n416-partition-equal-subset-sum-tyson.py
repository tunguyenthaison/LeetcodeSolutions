"""
Leetcode: Partition Equal Subset Sum
Lettcode #416
Date: [2021-09-04]
Author: Thai-Son Tu
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets
such that the sum of elements in both subsets is equal.
Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""

# Idea: Say S = sum(all numbers), then the question is can we find a subset such that its sum is S/2
# Brute-force is bad, O(2^n) complexity in time
# Idea: Knapsack bottom-up (Dynamic Programming)
class Solution:
    def canPartition(self, nums):
        S = sum(nums)
        # if s is odd, return False
        if S % 2 != 0:
            return False
        s = int(S / 2)
        n = len(nums)
        # Create the DP array, rows are # of elements in the subsets, columns are the sum
        dp = []
        for i in range(0, n):
            dp.append([False for j in range(0, s + 1)])
        # Setting True to the case sum = 0
        for i in range(0, n):
            dp[i][0] = True
        # with only one number (index = 1 but  i = 0)
        for j in range(1, s + 1):
            dp[0][j] = (nums[0] == j)
        # dp[i][s] <------- dp[i-1][s] or dp[i-1][s-num[i]]

        for i in range(1, n):
            for j in range(1, s + 1):
            # if s < nums[i] then we have to exclude
                if nums[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = (dp[i-1][j] or dp[i-1][j - nums[i]])
        print(dp)
        return dp[n-1][s]






# Example 1
sol = Solution()
answer = sol.canPartition([1, 2, 3, 4])
print(answer)

# Example 2
sol = Solution()
answer = sol.canPartition([1, 2, 5])
print(answer)

