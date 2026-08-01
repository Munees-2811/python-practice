class Solution(object):
    def predictTheWinner(self, nums):

        def solve(left, right):
            if left == right:
                return nums[left]

            pickLeft = nums[left] - solve(left + 1, right)
            pickRight = nums[right] - solve(left, right - 1)

            return max(pickLeft, pickRight)

        return solve(0, len(nums) - 1) >= 0