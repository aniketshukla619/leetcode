"""
Leetcode Solution for problem no. 704
"""

# Binary Search
# Easy

# Given an array of integers nums which is sorted in ascending order,
# and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

# Constraints:
# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.

from typing import List

class Solution: # pylint: disable=too-few-public-methods
    """Solution Class"""

    def search(self, nums: List[int], target: int) -> int:
        """Binary search algorithm"""

        first_index: int = 0
        last_index: int = len(nums) - 1

        while first_index <= last_index:
            mid_index: int = first_index + (last_index - first_index)//2

            if nums[mid_index] == target:
                return mid_index
            elif nums[mid_index] > target:
                last_index = mid_index - 1
            else:
                first_index = mid_index + 1

        return -1
