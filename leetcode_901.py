"""
Leetcode Solution for problem no. 901
"""
# Maximum Distance in Arrays
# Medium

# You are given m arrays, where each array is sorted in ascending order.

# You can pick up two integers from two different arrays(each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference | a - b | .

# Return the maximum distance.


# Example 1:

# Input: arrays = [[1, 2, 3], [4, 5], [1, 2, 3]]
# Output: 4
# Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
# Example 2:

# Input: arrays = [[1], [1]]
# Output: 0ki


# Constraints:

# m == arrays.length
# 2 <= m <= 105
# 1 <= arrays[i].length <= 500
# -104 <= arrays[i][j] <= 104
# arrays[i] is sorted in ascending order.
# There will be at most 105 integers in all the arrays.

from typing import List

class Solution: # pylint: disable=too-few-public-methods
    """Solution Class"""
    def maxDistance(self, arrays: List[List[int]]) -> int:
        """Max distance between elements of array."""
        min_dis: int = arrays[0][0]
        max_dis: int = arrays[0][-1]
        result_max_distance: int = 0

        for array in arrays[1:]:
            result_max_distance = max(result_max_distance,abs(min_dis - array[-1]))
            result_max_distance = max(result_max_distance,abs(max_dis - array[0]))

            min_dis = min(min_dis, array[0])
            max_dis = max(max_dis, array[-1])

        return result_max_distance
