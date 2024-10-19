"""
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/
1365. How Many Numbers Are Smaller Than the Current Number
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.



Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]
Example 3:

Input: nums = [7,7,7,7]
Output: [0,0,0,0]


Constraints:

2 <= nums.length <= 500
0 <= nums[i] <= 100
"""
from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        first_occurence_dict = {}
        sorted_nums = sorted(nums)
        # Search in sorted array and store the 1st occurence index in dict
        for index, value in enumerate(sorted_nums):
            # get only 1st occurence of value in sorted array
            if value not in first_occurence_dict:
                first_occurence_dict[value] = index
        # 1st occurence index = count of numbers less than index
        output = []
        for i, value in enumerate(nums):
            output.append(first_occurence_dict[value])
        return output

def run_test_case(solution: 'Solution', nums: List[int], expected_output: List[int], test_case_number: int) -> None:
    assert solution.smallerNumbersThanCurrent(nums) == expected_output, f"Test case {test_case_number} failed: {solution.smallerNumbersThanCurrent(nums)}"
    print(f"Test case {test_case_number} passed! Input: {nums}, Output: {expected_output}")

def test_smaller_numbers_than_current() -> None:
    solution = Solution()

    # Test case 1
    run_test_case(solution, [8, 1, 2, 2, 3], [4, 0, 1, 1, 3], 1)
    # Test case 2
    run_test_case(solution, [6, 5, 4, 8], [2, 1, 0, 3], 2)
    # test case 3
    run_test_case(solution, [7, 7, 7, 7], [0, 0, 0, 0], 3)

if __name__ == "__main__":
    test_smaller_numbers_than_current()
