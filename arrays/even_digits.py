"""
1295. Find Numbers with Even Number of Digits
Solved
Easy
Topics
Companies
Hint
Given an array nums of integers, return how many of them contain an even number of digits.

Example 1:
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.

Example 2:
Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
 

Constraints:

1 <= nums.length <= 500
1 <= nums[i] <= 105
"""
from typing import List
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_count = 0
        for num in nums:
            digit_count = 0
            while num != 0:
                num = num // 10
                digit_count += 1
            if digit_count % 2 == 0:
                even_count += 1
        return even_count

def run_test_case(solution: 'Solution', nums: List[int], expected_output: int, test_case_number: int) -> None:
    assert solution.findNumbers(nums) == expected_output, f"Test case {test_case_number} failed: {solution.findNumbers(nums)}"
    print(f"Test case {test_case_number} passed! Input: {nums}, Output: {expected_output}")

def test_find_numbers_with_even_digits() -> None:
    solution = Solution()

    # Test case 1
    run_test_case(solution, [12, 345, 2, 6, 7896], 2, 1)
    # Test case 2
    run_test_case(solution, [555, 901, 482, 1771], 1, 2)
    # Test case 3
    run_test_case(solution, [1, 22, 333, 4444], 2, 3)

if __name__ == "__main__":
    test_find_numbers_with_even_digits()