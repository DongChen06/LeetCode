class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            target = 0 - nums[i]
            while left < right:
                cur_sum = nums[left] + nums[right]

                if cur_sum < target:
                    left += 1
                elif cur_sum > target:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return res


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
