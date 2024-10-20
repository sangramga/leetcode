"""
https://leetcode.com/problems/matrix-diagonal-sum/
1572. Matrix Diagonal Sum
Solved
Easy
Topics
Companies
Hint
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and 
all the elements on the secondary diagonal that are not part of the primary diagonal.

Example 1:


Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8
Example 3:

Input: mat = [[5]]
Output: 5
 

Constraints:

n == mat.length == mat[i].length
1 <= n <= 100
1 <= mat[i][j] <= 100
"""
from typing import List
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        prime_diag_sum = 0
        secondary_diag_sum = 0
        n = len(mat)
        for i in range(n):
            prime_diag_sum += mat[i][i]
            if i != (n - i - 1): # skip prime_diag_element
                secondary_diag_sum += mat[i][n-i-1]
        return prime_diag_sum + secondary_diag_sum

def run_test_case(solution: 'Solution', mat: List[List[int]], expected_output: int, test_case_number: int) -> None:
    assert solution.diagonalSum(mat) == expected_output, f"Test case {test_case_number} failed: {solution.diagonalSum(mat)}"
    print(f"Test case {test_case_number} passed! Input: {mat}, Output: {expected_output}")

def test_diagonal_sum() -> None:
    solution = Solution()

    # Test case 1
    run_test_case(solution, [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 25, 1)
    # Test case 2
    run_test_case(solution, [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], 8, 2)
    # Test case 3
    run_test_case(solution, [[5]], 5, 3)
    # Test case 4 - Additional test case
    run_test_case(solution, [[2, 3], [4, 5]], 14, 4)

if __name__ == "__main__":
    test_diagonal_sum()
