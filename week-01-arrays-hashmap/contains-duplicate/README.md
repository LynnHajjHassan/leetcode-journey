# Contains Duplicate

## Problem Understanding

Input: a list of numbers

Output: True if any number appears more than once, False if all numbers are unique

In my own words:
Check if the list has any repeated number. If I find the same number again, return True. If I finish checking all numbers and no repeat is found, return False.

## Brute Force Idea

Compare each number with every number after it using two loops.

This works, but it is slow because it checks many pairs.

## Better Idea / Pattern

Pattern: HashSet / Set

Why this pattern works:
A set stores values I already saw. For each number, I check if it is already in the set. If yes, that means it is a duplicate. If not, I add it to the set.

## Edge Cases

- Empty list or one number means no duplicate
- Duplicate at the end
- All numbers are unique

## Mistakes I Made

- I first used two loops, but it was too slow and caused time limit exceeded.
- I had to remember that Python uses True and False with capital letters.
- return False should be after the loop, not inside the loop.

## Complexity

Brute force:
Time: O(n^2)
Space: O(1)

Better solution:
Time: O(n)
Space: O(n)