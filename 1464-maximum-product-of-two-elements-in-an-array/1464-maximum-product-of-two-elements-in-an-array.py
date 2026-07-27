class Solution(object):
    def maxProduct(self, nums):
       result=0
       for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            product=(nums[i]-1)*(nums[j]-1)
            result=max(result,product)
       return result
        

        