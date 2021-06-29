class Solution:
    def singleNumber(self, nums) -> int:
        nums.sort()

        for i in range(len(nums) // 2):
            if nums[i * 2] != nums[i * 2 + 1]:
                return nums[i * 2]

        return nums[-1]


input = [2, 2, 1]
s = Solution()

print(s.singleNumber(input))
