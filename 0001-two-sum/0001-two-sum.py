class Solution(object):
    def twoSum(self, nums, target):
     seen={}
     for i,n in enumerate(nums):
        value=target-nums[i]
        if value in seen:
            return[i,seen[value]]
        else:
            seen[n]=i