"""
https://leetcode.com/problems/find-the-highest-altitude/description/
1732. Find the Highest Altitude

Easy

There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes.
The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain 
in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). 
Return the highest altitude of a point.

 

Example 1:

Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
Example 2:

Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
 

Constraints:

n == gain.length
1 <= n <= 100
-100 <= gain[i] <= 100
"""
from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_altitude = 0
        current = 0
        for g in gain:
            current = current + g
            if current > highest_altitude:
                highest_altitude = current
            
        return highest_altitude
    
def run_test_case(solution: 'Solution', gain: List[int], expected_output: int, test_case_number: int) -> None:
    assert solution.largestAltitude(gain) == expected_output, f"Test case {test_case_number} failed: {solution.largestAltitude(gain)}"
    print(f"Test case {test_case_number} passed! Input: {gain}, Output: {expected_output}")

def test_largest_altitude() -> None:
    solution = Solution()

    # Test case 1
    run_test_case(solution, [1, 2, 3, 4], 10, 1)
    # Test case 2
    run_test_case(solution, [-1, -2, -3, -4], 0, 2)
    # Test case 3
    run_test_case(solution, [0, 0, 0, 0], 0, 3)

if __name__ == "__main__":
    test_largest_altitude()