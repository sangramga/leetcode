"""1832. Check if the Sentence Is Pangram
Easy
A pangram is a sentence where every letter of the English alphabet 
appears at least once.

Given a string sentence containing only lowercase English letters, 
return true if sentence is a pangram, or false otherwise.


Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false
 

Constraints:

1 <= sentence.length <= 1000
sentence consists of lowercase English letters.
"""
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # char_set = set(sentence)
        # n = len(char_set)
        # return n == 26

        alphabet = [False]*26 # Fixed space list O(1) space complexity
        for c in sentence:
            if 'a' <= c <= 'z':
                index = ord(c) - ord('a')
                alphabet[index] = True

        return all(alphabet)

def run_test_case(solution: 'Solution', sentence: str, expected_output: bool, test_case_number: int) -> None:
    assert solution.checkIfPangram(sentence) == expected_output, f"Test case {test_case_number} failed: {solution.checkIfPangram(sentence)}"
    print(f"Test case {test_case_number} passed! Input: {sentence}, Output: {expected_output}")

def test_check_if_pangram() -> None:
    solution = Solution()

    # Test case 1
    run_test_case(solution, "thequickbrownfoxjumpsoverthelazydog", True, 1)
    # Test case 2
    run_test_case(solution, "leetcode", False, 2)
    # Test case 3
    run_test_case(solution, "abcdefghijklmnopqrstuvwxyz", True, 3)

if __name__ == "__main__":
    test_check_if_pangram()
