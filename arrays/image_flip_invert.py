"""
https://leetcode.com/problems/flipping-an-image/description/
832. Flipping an Image

Given an n x n binary matrix image, flip the image horizontally, then invert it,
 and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.

For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

For example, inverting [0,1,1] results in [1,0,0].
 

Example 1:

Input: image = [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
Example 2:

Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
 

Constraints:

n == image.length
n == image[i].length
1 <= n <= 20
images[i][j] is either 0 or 1.
"""
from typing import List
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i, row in enumerate(image):
            image[i].reverse()
            for j, bit in enumerate(row):
                row[j] ^= 1 # XOR with 1 to invert (0 becomes 1 and 1 becomes 0)
        return image

def run_test_case(solution: 'Solution', image: List[List[int]], expected_output: List[List[int]], test_case_number: int) -> None:
    assert solution.flipAndInvertImage(image) == expected_output, f"Test case {test_case_number} failed: {solution.flipAndInvertImage(image)}"
    print(f"Test case {test_case_number} passed! Input: {image}, Output: {expected_output}")

def test_flip_and_invert_image() -> None:
    solution = Solution()

    # Test case 1
    run_test_case(solution, [[1,1,0],[1,0,1],[0,0,0]], [[1,0,0],[0,1,0],[1,1,1]], 1)
    # Test case 2
    run_test_case(solution, [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]], [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]], 2)

if __name__ == "__main__":
    test_flip_and_invert_image()