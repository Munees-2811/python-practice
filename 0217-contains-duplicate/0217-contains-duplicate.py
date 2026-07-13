class Solution(object):
    def containsDuplicate(self, nums):
     set={}
     for num in nums:
        if num not in set:
            set[num]=1
        else:
          return True
     return False
        