"""
1389. Create Target Array in the Given Order
Difficulty: Easy
Given two arrays of integers nums and index. Your task is to create target array under the following rules:

Initially target array is empty.
1. From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
2. Repeat the previous step until there are no elements to read in nums and index.
3. Return the target array.

It is guaranteed that the insertion operations will be valid.
Example 1:

Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]
Example 2:

Input: nums = [1,2,3,4,0], index = [0,1,2,3,0]
Output: [0,1,2,3,4]
Explanation:
nums       index     target
1            0        [1]
2            1        [1,2]
3            2        [1,2,3]
4            3        [1,2,3,4]
0            0        [0,1,2,3,4]
Example 3:

Input: nums = [1], index = [0]
Output: [1]
 

Constraints:

1 <= nums.length, index.length <= 100
nums.length == index.length
0 <= nums[i] <= 100
0 <= index[i] <= i
"""
from typing import List
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        # Assumption nums.length == index.length
        target = []

        for num, idx in zip(nums, index):
            # this will shift the elements in target array if needed
            target.insert(idx, num)

        return target

def run_test_case(solution: 'Solution', nums: List[int], index: List[int], expected_output: List[int], test_case_number: int) -> None:
    assert solution.createTargetArray(nums, index) == expected_output, f"Test case {test_case_number} failed: {solution.createTargetArray(nums, index)}"
    print(f"Test case {test_case_number} passed! Input: nums={nums}, index={index}, Output: {expected_output}")

def test_create_target_array() -> None:
    solution = Solution()

    # Test case 1
    run_test_case(solution, [0, 1, 2, 3, 4], [0, 1, 2, 2, 1], [0, 4, 1, 3, 2], 1)
    # Test case 2
    run_test_case(solution, [1, 2, 3, 4, 0], [0, 1, 2, 3, 0], [0, 1, 2, 3, 4], 2)
    # Test case 3
    run_test_case(solution, [1], [0], [1], 3)

if __name__ == "__main__":
    test_create_target_array()
