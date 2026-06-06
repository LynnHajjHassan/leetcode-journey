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

Pattern:

Why this pattern works:

## Edge Cases

- 
- 

## Mistakes I Mad
- I mixed Java syntax with Python syntax.
- I forgot that Python uses len(nums), not List.length.
- I needed to return the indices [i, j], not just return.

## Complexity

Time:

Space: