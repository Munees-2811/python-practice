class Solution(object):
    def judgeSquareSum(self, c):
      for a in range(int(math.sqrt(c))+1):
        b= sqrt(c-a*a)
        if b==int(b):
            return True
      return False