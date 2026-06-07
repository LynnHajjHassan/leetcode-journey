# Brute force: check every pair of numbers.
# Time: O(n^2), because there are two loops.
# Space: O(1), because we do not use extra storage.
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
'''

class Solution:
     def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # array to store seen numbers
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in seen:
                # return the array of indices
                return [ seen[needed], i]
            # else if needed not in seen, add it to seen 
            seen[nums[i]] = i 
               



      