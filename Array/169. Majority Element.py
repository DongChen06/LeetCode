class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = collections.Counter(nums)

        return max(count.keys(), key=count.get)