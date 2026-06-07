# Two Sum

## Problem Understanding

Input: array of integers + Integer called Target. 
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

requried that time comp is less than O(n^2).

## Brute Force Idea

Check every pair of numbers using two loops.

For each index i, compare it with every index after it, j.
If nums[i] + nums[j] equals the target, return [i, j].

This works, but it is slower because it checks many pairs.

Time: O(n^2)
Space: O(1)

## Better Idea / Pattern

Pattern: HashMap / Dictionary

For each number, calculate the number needed to reach the target.

needed = target - current number

If the needed number is already in the dictionary, return the index of needed and the current index.

If not, store the current number with its index.

## Edge Cases

- 
- 

## Mistakes I Mad
- I mixed Java syntax with Python syntax.
- I forgot that Python uses len(nums), not List.length.
- I needed to return the indices [i, j], not just return.
- I called the dictionary an array, but in Python {} creates a dictionary.
- The dictionary stores number -> index, so I can quickly find the needed number.

## Complexity
Better solution:
Time: O(n)
Space: O(n)

## Dictionary Note

A Python dictionary stores key-value pairs.

For Two Sum, I used:

number -> index

Example:
seen = {
    2: 0,
    7: 1
}

This means number 2 is at index 0, and number 7 is at index 1.

A dictionary is not the same as an array/list.
A list uses indexes to access values.
A dictionary uses keys to access values.

Python dictionary is similar to Java HashMap.