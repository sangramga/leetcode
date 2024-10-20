"""
1252. Cells with Odd Values in a Matrix
Easy
Topics
Companies
Hint
There is an m x n matrix that is initialized to all 0's. 
There is also a 2D array indices where each indices[i] = [ri, ci] represents a 0-indexed location 
to perform some increment operations on the matrix.

For each location indices[i], do both of the following:

Increment all the cells on row ri.
Increment all the cells on column ci.
Given m, n, and indices, return the number of odd-valued cells in the matrix 
after applying the increment to all locations in indices.

 

Example 1:


Input: m = 2, n = 3, indices = [[0,1],[1,1]]
Output: 6
Explanation: Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix is [[1,3,1],[1,3,1]], which contains 6 odd numbers.

Example 2:

Input: m = 2, n = 2, indices = [[1,1],[0,0]]
Output: 0
Explanation: Final matrix = [[2,2],[2,2]]. There are no odd numbers in the final matrix.
 

Constraints:

1 <= m, n <= 50
1 <= indices.length <= 100
0 <= ri < m
0 <= ci < n

"""
from typing import List
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        odd_count = 0
        matrix = [[0]*n for _ in range(m)]
        # Apply increments based on indices
        for r_i, c_i in indices:
            # Increment the specified row
            for j in range(n):
                matrix[r_i][j] += 1
            # Increment the specified column
            for i in range(m):
                matrix[i][c_i] += 1
        # Count the number of odd-valued cells
        for row in matrix:
            for value in row:
                if value % 2 != 0:
                    odd_count += 1
        # Time complexity O(k X (m+n) + (m X n))
        # Space complexity O(m X n)
        return odd_count  # Return the count of odd cells
    
    def oddCells_v2(self, m: int, n: int, indices: List[List[int]]) -> int:
        """
        Optimal Solution
        Time: O(k + m + n )
        Space: O(m + n)
        """
        row_increments = [0]*m
        column_increments = [0]*n

        for r_i, c_i in indices:
            # Add row increments
            row_increments[r_i] += 1
            # Add row increments
            column_increments[c_i] += 1

        # Calculating Odd Cells: The total number of odd cells is calculated
        # using the counts of odd rows and columns:
        # Cells in odd rows that are in even columns contribute to odd cells.
        # Cells in even rows that are in odd columns also contribute to odd cells.

        odd_incremented_rows = sum(1 for count in row_increments if count%2 == 0 )
        even_increment_rows = m - odd_incremented_rows
        odd_incremented_cols = sum(1 for count in column_increments if count%2 == 0)
        even_increment_cols = n - odd_incremented_cols

        odd_cells = (odd_incremented_rows * even_increment_cols) + \
                    (even_increment_rows * odd_incremented_cols)
        return odd_cells


def run_test_case(solution: 'Solution', m: int, n: int, indices: List[List[int]], expected_output: int, test_case_number: int) -> None:
    assert solution.oddCells(m, n, indices) == expected_output, f"Test case {test_case_number} failed: {solution.oddCells(m, n, indices)}"
    assert solution.oddCells_v2(m, n, indices) == expected_output, f"Test case {test_case_number} failed: {solution.oddCells_v2(m, n, indices)}"
    print(f"Test case {test_case_number} passed! Input: m={m}, n={n}, indices={indices}, Output: {expected_output}")

def test_odd_cells() -> None:
    solution = Solution()

    # Test case 1
    run_test_case(solution, 2, 3, [[0, 1], [1, 1]], 6, 1)
    # Test case 2
    run_test_case(solution, 2, 2, [[1, 1], [0, 0]], 0, 2)
    # Test case 3
    run_test_case(solution, 1, 1, [[0, 0]], 0, 3)
    # Test case 4
    run_test_case(solution, 4, 4, [[0, 0], [0, 1], [1, 0], [1, 1]], 0, 4)

if __name__ == "__main__":
    test_odd_cells()
