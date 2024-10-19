# LeetCode Solutions

This repository contains solutions to various LeetCode problems, organized by topics. Each topic includes a list of relevant questions along with their difficulty levels, tags, hints, and time/space complexities.

## Topics

### 1. Arrays

| Question | Difficulty | Tags | Hints | Time Complexity | Space Complexity |
|----------|------------|------|-------|------------------|------------------|
| [How Many Numbers Are Smaller Than the Current Number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/) | Easy | Array, Hash Table | Use sorting of array | O(n log n) | O(n) |
| [Create Target Array in the Given Order](https://leetcode.com/problems/create-target-array-in-the-given-order/) | Easy | Array | Use insertion based on index | O(n^2) | O(n) | 
| [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | Array, Hash Table | Use a hash map to store the difference. | O(n) | O(n) |
| [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy | Array, Dynamic Programming | Track the minimum price seen so far. | O(n) | O(1) |
| [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy | Array, Hash Table | Use a set to track seen elements. | O(n) | O(n) |
| [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Medium | Array | Use two passes to calculate the left and right products. | O(n) | O(1) |

### 2. Strings

| Question | Difficulty | Tags | Hints | Time Complexity | Space Complexity |
|----------|------------|------|-------|------------------|------------------|
| [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | Hash Table, Sliding Window | Use a sliding window to track characters. | O(n) | O(min(n, m)) |
| [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy | Hash Table, String | Count character occurrences. | O(n) | O(1) |
| [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | Hash Table, String | Sort each string to group anagrams. | O(n * k log k) | O(n) |
| [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | Medium | String, Dynamic Programming | Expand around the center for potential palindromes. | O(n^2) | O(1) |

### 3. Linked Lists

| Question | Difficulty | Tags | Hints | Time Complexity | Space Complexity |
|----------|------------|------|-------|------------------|------------------|
| [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Easy | Linked List | Use three pointers to reverse the links. | O(n) | O(1) |
| [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy | Linked List | Use a dummy node to simplify merging. | O(n + m) | O(1) |
| [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy | Linked List, Two Pointers | Use two pointers to detect a cycle. | O(n) | O(1) |
| [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Medium | Linked List, Two Pointers | Use two pointers to find the node to remove. | O(n) | O(1) |

### 4. Trees

| Question | Difficulty | Tags | Hints | Time Complexity | Space Complexity |
|----------|------------|------|-------|------------------|------------------|
| [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Easy | Tree, Depth-First Search | Use recursion to find the depth. | O(n) | O(h) |
| [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) | Medium | Tree, Depth-First Search | Use a stack or recursion for traversal. | O(n) | O(h) |
| [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | Medium | Tree, Depth-First Search | Check the value range for each node. | O(n) | O(h) |
| [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | Medium | Tree, Depth-First Search | Use the properties of BST to find the ancestor. | O(n) | O(h) |

### 5. Dynamic Programming

| Question | Difficulty | Tags | Hints | Time Complexity | Space Complexity |
|----------|------------|------|-------|------------------|------------------|
| [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Easy | Dynamic Programming | Use a bottom-up approach to build solutions. | O(n) | O(1) |
| [House Robber](https://leetcode.com/problems/house-robber/) | Medium | Dynamic Programming | Use a DP array to track maximum loot. | O(n) | O(1) |
| [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | Medium | Dynamic Programming | Use binary search to optimize the DP solution. | O(n log n) | O(n) |
| [Coin Change](https://leetcode.com/problems/coin-change/) | Medium | Dynamic Programming | Use a DP array to track the minimum coins needed. | O(n * m) | O(n) |

### 6. Backtracking

| Question | Difficulty | Tags | Hints | Time Complexity | Space Complexity |
|----------|------------|------|-------|------------------|------------------|
| [Permutations](https://leetcode.com/problems/permutations/) | Medium | Backtracking | Use recursion to generate permutations. | O(n!) | O(n) |
| [Combination Sum](https://leetcode.com/problems/combination-sum/) | Medium | Backtracking | Use backtracking to explore combinations. | O(2^n) | O(n) |
| [Subsets](https://leetcode.com/problems/subsets/) | Medium | Backtracking | Use backtracking to generate subsets. | O(2^n) | O(n) |
| [Word Search](https://leetcode.com/problems/word-search/) | Medium | Backtracking | Use DFS to explore the board. | O(m * n * 4^k) | O(k) |

## Contributing

Feel free to contribute by adding more questions or solutions. Make sure to follow the structure of the existing topics.