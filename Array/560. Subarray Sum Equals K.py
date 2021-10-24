class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixSum = {0: 1}
        curr_sum = 0

        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            res += prefixSum.get(diff, 0)
            prefixSum[curr_sum] = 1 + prefixSum.get(curr_sum, 0)

        return res