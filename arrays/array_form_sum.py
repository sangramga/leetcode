"""
https://leetcode.com/problems/add-to-array-form-of-integer/description/
989. Add to Array-Form of Integer
Easy
The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

 

Example 1:
Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234


Example 2:
Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455

Example 3:

Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
 

Constraints:

1 <= num.length <= 104
0 <= num[i] <= 9
num does not contain any leading zeros except for the zero itself.
1 <= k <= 104
"""
from typing import List
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # convert k to array-form
        k_array = []
        while k != 0:
            k_array.append(k%10)
            k = k // 10
        # reverse to get k_array in array form
        k_array.reverse()
        k_len = len(k_array)
        num_len = len(num)

        # Add k_array and num array
        carry = 0
        k_ptr = k_len - 1
        num_ptr = num_len - 1
        result = []
        while (k_ptr >= 0 ) and (num_ptr >= 0):
            result.append( (k_array[k_ptr] + num[num_ptr] + carry) % 10 )
            carry = (k_array[k_ptr] + num[num_ptr] + carry) // 10
            k_ptr -= 1
            num_ptr -= 1

        # If num array has still digits left
        while num_ptr >= 0:
            result.append((num[num_ptr] + carry) % 10 )
            carry = (num[num_ptr] + carry) // 10
            num_ptr -= 1

        # if k_array has digits left
        while k_ptr >= 0:
            result.append((k_array[k_ptr] + carry ) % 10)
            carry = (k_array[k_ptr] + carry) // 10
            k_ptr -= 1

        # if carry is left
        if carry != 0:
            result.append(carry)

        result.reverse()
        return result

def run_test_case(solution: 'Solution', num: List[int], k: int, expected_output: List[int], test_case_number: int) -> None:
    assert solution.addToArrayForm(num, k) == expected_output, f"Test case {test_case_number} failed: {solution.addToArrayForm(num, k)}"
    print(f"Test case {test_case_number} passed! Input: {num}, {k}, Output: {expected_output}")

def test_add_to_array_form() -> None:
    solution = Solution()

    # Test case 1
    run_test_case(solution, [2, 7, 4], 181, [4, 5, 5], 1)
    # Test case 2
    run_test_case(solution, [2,1,5], 806, [1,0,2,1], 2 )

if __name__ == "__main__":
    test_add_to_array_form()