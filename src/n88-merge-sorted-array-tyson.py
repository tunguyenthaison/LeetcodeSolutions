"""
Leetcode: two-sum
Lettcode #088
Date: [2021-08-30]
Author: Thai-Son Tu
Description: You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""


class Solution1:
    # Stupid solution
    def merge(self, nums1, m, nums2, n):
        """Do not return anything, modify nums1 in-place instead."""
        nums1[m:m + n] = nums2
        nums1.sort()


class Solution2:
    def merge(self, nums1, m, nums2, n):
        """Do not retun anything, modify nums1 in-place instead."""
        # Borderline case: m=0 or n=0
        if m == 0:
            for i in range(0, len(nums2)):
                nums1[i] = nums2[i]
        elif n == 0:
            pass
        else:
            p0 = m + n - 1
            p2 = n - 1
            p1 = m - 1
            while p2 >= 0 and p1 >= 0:
                print(f"p2 = {p2}")
                print(f"p1 = {p1}")
                print(f"p0 = {p0}")
                print(f"nums1[p1] = {nums1[p1]}")
                print(f"nums2[p2] = {nums2[p2]}")
                if nums1[p1] > nums2[p2]:
                    nums1[p0] = nums1[p1]
                    p1 -= 1
                else:
                    nums1[p0] = nums2[p2]
                    p2 -= 1
                print(nums1)
                p0 -= 1
                print("---------------- then ----------")
                print(f"p2 = {p2}")
                print(f"p1 = {p1}")
                print(f"p0 = {p0}")
                print("----------------")

            while p2 >= 0:
                nums1[p0] = nums2[p2]
                p2 -= 1
                p0 -= 1
        print(nums1)




sol = Solution2()
# sol.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
# sol.merge([1], 1, [], 0)
# sol.merge([0], 0, [1], 1)
nums1 = [2, 0]
m = 1
nums2 = [1]
n = 1
sol.merge(nums1, m, nums2, n)
print(nums1)