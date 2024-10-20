"""
https://leetcode.com/problems/maximum-population-year
1854. Maximum Population Year
Difficulty: Medium
Topics: Array, Prefix Sum

You are given a 2D integer array logs where each
logs[i] = [birthi, deathi] indicates the birth and death years of the ith person.

The population of some year x is the number of people alive during that year.
The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1].
Note that the person is not counted in the year that they die.

Return the earliest year with the maximum population.
 

Example 1:

Input: logs = [[1993,1999],[2000,2010]]
Output: 1993
Explanation: The maximum population is 1, and 1993 is the earliest year with this population.
Example 2:

Input: logs = [[1950,1961],[1960,1971],[1970,1981]]
Output: 1960
Explanation: 
The maximum population is 2, and it had happened in years 1960 and 1970.
The earlier year between them is 1960.
 

Constraints:

1 <= logs.length <= 100
1950 <= birthi < deathi <= 2050
"""

from typing import List

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        "Using hashmap dictionary"
        max_year = 0
        min_year = 9999999
        max_pop = 0
        year_pop = dict()
        for birth, death in logs:
            min_year = min(min_year, birth)
            max_year = max(max_year, death)
            for year in range(birth, death):
                if year in year_pop:
                    year_pop[year] += 1
                else:
                    year_pop[year] = 1
                if max_pop < year_pop[year]:
                    max_pop = year_pop[year]

        # print(year_pop)
        min_year_for_max_pop = 21000
        for year in range(min_year, max_year):
            if year_pop.get(year,0) == max_pop:
                min_year_for_max_pop = year
                break
        return min_year_for_max_pop
    
    def maximumPopulation_prefix_sum(self, logs: List[List[int]]) -> int:
        "Using prefix sum difference range query"
        # initialize array 1950 .. 2050 or 0 .. 100
        max_year = 2051
        min_year = 1950
        prefix_sum_array = [0 for _ in range(max_year)]
        # +1 for birth and -1 for death
        for birth_year, death_year in logs:
            prefix_sum_array[birth_year] += 1
            prefix_sum_array[death_year] -= 1
        # Calculate prefix_sum/running sum
        for year in range(min_year, max_year):
            prefix_sum_array[year] += prefix_sum_array[year - 1]
        
        # Find 1st occurence of max_pop in prefix_sum will give minimum year for max pop
        max_pop = 0
        min_year_for_max_pop = max_year + 1
        for year in range(len(prefix_sum_array)):
            if max_pop < prefix_sum_array[year]:
                max_pop = prefix_sum_array[year]
                min_year_for_max_pop = year

        return min_year_for_max_pop

def run_test_case(solution: 'Solution', logs: List[List[int]], expected_output: int, test_case_number: int) -> None:
    assert solution.maximumPopulation(logs) == expected_output, f"Test case {test_case_number} failed: {solution.maximumPopulation(logs)}"
    print(f"Test case #{test_case_number} for maximumPopulation() passed! Input: {logs}, Output: {expected_output}")
    assert solution.maximumPopulation_prefix_sum(logs) == expected_output, f"Test case {test_case_number} failed: {solution.maximumPopulation_prefix_sum(logs)}"
    print(f"Test case #{test_case_number} for maximumPopulation_prefix_sum() passed! Input: {logs}, Output: {expected_output}")

def test_maximum_population() -> None:
    solution = Solution()
    # Test case 1
    run_test_case(solution, [[1993, 1999], [2000, 2010]], 1993, 1)
    # Test case 2
    run_test_case(solution, [[1950, 1961], [1960, 1971], [1970, 1981]], 1960, 2)
    # Test case 3
    run_test_case(solution, [[2033,2034],[2039,2047],[1998,2042],
                             [2047,2048],[2025,2029],[2005,2044],
                             [1990,1992],[1952,1956],[1984,2014]], 2005, 3)

if __name__ == "__main__":
    test_maximum_population()

