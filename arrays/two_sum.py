"""
https://leetcode.com/problems/two-sum/
1. Two Sum
Solved
Easy
Topics: Array, Hash Table
Companies
Hint
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_dict = {}  # To store numbers and their indices
        for i, num in enumerate(nums):
            complement = target - num
            if complement in complement_dict:
                return [complement_dict[complement], i]
            # Else: Store the number with its index
            complement_dict[num] = i

def run_test_case(solution: 'Solution', nums: List[int], target: int, expected_output: List[int], test_case_number: int) -> None:
    assert solution.twoSum(nums, target) == expected_output, f"Test case {test_case_number} failed: {solution.twoSum(nums, target)}"
    print(f"Test case {test_case_number} passed! Input: {nums}, Target: {target}, Output: {expected_output}")

def test_two_sum() -> None:
    solution = Solution()

    # Test case 1
    run_test_case(solution, [2, 7, 11, 15], 9, [0, 1], 1)
    # Test case 2
    run_test_case(solution, [3, 2, 4], 6, [1, 2], 2)
    # Test case 3
    run_test_case(solution, [3, 3], 6, [0, 1], 3)

if __name__ == "__main__":
    test_two_sum()