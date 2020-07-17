"""Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      
        largest = max(nums)
        to_check = set(range(0,largest))
        
        for value in nums:
            if value in to_check:
                to_check.remove(value)
        return to_check.pop()
   