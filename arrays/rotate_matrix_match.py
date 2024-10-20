"""
https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/
Given two n x n binary matrices mat and target, 
return true if it is possible to make mat equal to target by 
rotating mat in 90-degree increments, or false otherwise.

 

Example 1:


Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.
Example 2:


Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
Explanation: It is impossible to make mat equal to target by rotating mat.
Example 3:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.
 

Constraints:

n == mat.length == target.length
n == mat[i].length == target[i].length
1 <= n <= 10
mat[i][j] and target[i][j] are either 0 or 1.
"""
from typing import List
class Solution:
    def rotate_mat(self, mat: List[List[int]]):
        # Transpose the matrix
        n = len(mat)
        i, j = 0, 0
        for i in range(n):
            for j in range(i+1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        # Reverse the rows
        for i in range(n):
            mat[i].reverse()
    
    def rotate_mat_v2(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        for i in range(n):
            for j in range(n):
                mat[i][j] = mat[n-j-1][i]
        return mat
    
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        rotations = 0
        print(rotations,mat)
        for _ in range(3):
            self.rotate_mat(mat)
            # mat = self.rotate_mat_v2(mat)
            rotations += 1
            print(rotations, mat)
            if mat == target:
                return True
        return False

def run_test_case(solution: 'Solution', mat: List[List[int]], target: List[List[int]], expected_output: bool, test_case_number: int) -> None:
    assert solution.findRotation(mat, target) == expected_output, f"Test case {test_case_number} failed: {solution.findRotation(mat, target)}"
    print(f"Test case {test_case_number} passed! Input: {mat}, Target: {target}, Output: {expected_output}")

def test_rotate_matrix_match() -> None:
    solution = Solution()

    # Test case 1
    run_test_case(solution, [[0,1],[1,0]], [[1,0],[0,1]], True, 1)
    # Test case 2
    run_test_case(solution, [[0,1],[1,1]], [[1,0],[0,1]], False, 2)
    # Test case 3
    run_test_case(solution, [[0,0,0],[0,1,0],[1,1,1]], [[1,1,1],[0,1,0],[0,0,0]], True, 3)

if __name__ == "__main__":
    test_rotate_matrix_match()