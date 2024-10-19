"""
1773. Count Items Matching a Rule
Easy
You are given an array items, where each 
items[i] = [typei, colori, namei] describes the type, color, and name of the ith item.
 You are also given a rule represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:

ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == colori.
ruleKey == "name" and ruleValue == namei.
Return the number of items that match the given rule.

 

Example 1:

Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
Output: 1
Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].

Example 2:
Input: items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"
Output: 2
Explanation: There are only two items matching the given rule,
 which are ["phone","blue","pixel"] and ["phone","gold","iphone"].
 Note that the item ["computer","silver","phone"] does not match.
 

Constraints:

1 <= items.length <= 104
1 <= typei.length, colori.length, namei.length, ruleValue.length <= 10
ruleKey is equal to either "type", "color", or "name".
All strings consist only of lowercase letters.
"""
from typing import List

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        match_count = 0
        rule_index = None
        match ruleKey:
            case "type":
                rule_index = 0
            case "color":
                rule_index = 1
            case _:
                rule_index = 2

        for item in items:
            if item[rule_index] == ruleValue:
                match_count += 1
        return match_count

def run_test_case(solution: 'Solution', items: List[List[str]], ruleKey: str, ruleValue: str, expected_output: int, test_case_number: int) -> None:
    assert solution.countMatches(items, ruleKey, ruleValue) == expected_output, f"Test case {test_case_number} failed: {solution.countMatches(items, ruleKey, ruleValue)}"
    print(f"Test case {test_case_number} passed! Input: {items}, RuleKey: {ruleKey}, RuleValue: {ruleValue}, Output: {expected_output}")

def test_count_matches() -> None:
    solution = Solution()

    # Test case 1
    run_test_case(solution, [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "silver", 1, 1)
    # Test case 2
    run_test_case(solution, [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], "type", "phone", 2, 2)
    # Test case 3
    run_test_case(solution, [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "name", "iphone", 1, 3)
    # Test case 4
    run_test_case(solution, [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "type", "tablet", 0, 4)

if __name__ == "__main__":
    test_count_matches()