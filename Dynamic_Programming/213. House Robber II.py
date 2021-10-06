class Solution:
    def rob(self, nums: List[int]) -> int:

        def maxrob(num):
            rob1, rob2 = 0, 0
            for i in range(len(num)):
                tmp = max(rob1 + num[i], rob2)
                rob1 = rob2
                rob2 = tmp

            return rob2

        if len(nums) <= 3:
            return max(nums)
        return max(maxrob(nums[:-1]), maxrob(nums[1:]))


s = Solution()
print(s.rob([1]))
