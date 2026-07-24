class Solution(object):
    def isPerfectSquare(self, num):
        root=int(math.sqrt(num))
        if math.sqrt(num) == root:
            return True
        else:
            return False
        