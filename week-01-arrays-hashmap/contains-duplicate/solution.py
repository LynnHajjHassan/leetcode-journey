'''
# Brute Force Solution
# Time: O(n^2), because there are two loops.
# Space: O(1), because we do not use extra storage. 

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]==nums[j]:
                    return True
        return False     
'''


from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])

        return False
# Time: O(n), because we loop through the list once.
# Space: O(n), because in the worst case, all numbers are unique and we store them in the set.