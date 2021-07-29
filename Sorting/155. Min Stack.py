class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_count = len(nums) // 2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num

        # O(n)
        # counts = collections.Counter(nums)
        # return max(counts.keys(), key=counts.get)