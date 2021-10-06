class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sumEven, sumOdd = 0, 0

        for i in range(len(nums) - 1, -1, -1):
            tempEven = max(sumOdd + nums[i], sumEven)
            tempOdd = max(sumEven - nums[i], sumOdd)
            sumEven, sumOdd = tempEven, tempOdd

        return sumEven