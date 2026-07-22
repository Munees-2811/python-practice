class Solution(object):
    def isPalindrome(self, x):
       original=x
       reverse=0
       if x <0:
        return False
       while x!=0:
        digit = x % 10
        reverse =reverse*10+digit
        x //=10
       return original == reverse
        