"""
https://leetcode.com/problems/transpose-matrix/
867. Transpose Matrix
Solved
Easy
Topics
Companies
Hint
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.


Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
-109 <= matrix[i][j] <= 109
"""
from typing import List
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        transpose_mat = [[None for _ in range(m)] for _ in range(n)]
        for row in range(m):
            for col in range(n):
                transpose_mat[col][row] = matrix[row][col]
        return transpose_mat

def run_test_case(solution: 'Solution', matrix: List[List[int]], expected_output: List[List[int]], test_case_number: int) -> None:
    assert solution.transpose(matrix) == expected_output, f"Test case {test_case_number} failed: {solution.transpose(matrix)}"
    print(f"Test case {test_case_number} passed! Input: {matrix}, Output: {expected_output}")

def test_matrix_transpose() -> None:
    solution = Solution()

    # Test case 1
    run_test_case(solution, [[1,2,3],[4,5,6],[7,8,9]], [[1,4,7],[2,5,8],[3,6,9]], 1)
    # Test case 2
    run_test_case(solution, [[1,2,3],[4,5,6]], [[1,4],[2,5],[3,6]], 2)
    # Test case 3
    run_test_case(solution, [[1]], [[1]], 3)

if __name__ == "__main__":
    test_matrix_transpose()