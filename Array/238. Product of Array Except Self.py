class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for i in range(len(nums))]

        pre_prod = 1
        for i in range(len(nums)):
            res[i] = pre_prod
            pre_prod = pre_prod * nums[i]

        pos_pro = 1
        for j in range(len(nums) - 1, -1, -1):
            res[j] = pos_pro * res[j]
            pos_pro = pos_pro * nums[j]

        return res