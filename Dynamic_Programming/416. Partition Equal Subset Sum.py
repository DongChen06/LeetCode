class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums)):
            newdp = set()
            for t in dp:
                newdp.add(t + nums[i])
                newdp.add(t)

            dp = newdp

        return True if target in dp else False