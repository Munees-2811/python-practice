class Solution(object):
    def duplicateNumbersXOR(self, nums):
     result=0
     for num in set(nums):
       if nums.count(num) == 2:
         result^=num
     return result
        