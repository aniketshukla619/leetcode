# 1056 Confusing Number
# Easy

# A confusing number is a number that when rotated 180 degrees becomes a different
# number with each digit valid.

# We can rotate digits of a number by 180 degrees to form new digits.

# When 0, 1, 6, 8, and 9 are rotated 180 degrees, they become 0, 1, 9, 8, and 6 respectively.
# When 2, 3, 4, 5, and 7 are rotated 180 degrees, they become invalid.
# Note that after rotating a number, we can ignore leading zeros.

# For example, after rotating 8000, we have 0008 which is considered as just 8.
# Given an integer n, return true if it is a confusing number, or false otherwise.

# Example 1:

# Input: n = 6
# Output: true
# Explanation: We get 9 after rotating 6, 9 is a valid number, and 9 != 6.


# Example 2:

# Input: n = 89
# Output: true
# Explanation: We get 68 after rotating 89, 68 is a valid number and 68 != 89.


# Example 3:

# Input: n = 11
# Output: false
# Explanation: We get 11 after rotating 11, 11 is a valid number but the value remains the same,
# thus 11 is not a confusing number


# Constraints:

# 0 <= n <= 109
# Accepted

class Solution:
    """
    Solution Class
    """

    def confusingNumber(self, n: int) -> bool:
        """
        Confusing number function
        """
        rotate_digits = {
            0: 0,
            1: 1,
            6: 9,
            8: 8,
            9: 6
        }

        exp = 1
        old_num = n
        new_num = 0
        while n > 0:
            temp = n % 10
            if temp in rotate_digits:
                new_num += (rotate_digits[temp] * exp)
            else:
                return False
            exp *= 10
            n //= 10
        new_num = int(str(new_num)[::-1])
        return new_num != old_num
