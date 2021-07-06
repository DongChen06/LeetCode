# class Solution:
#     def maxSubArray(self, nums) -> int:
#         max_sum = nums[0]
#         temp_sum = nums[0]
#
#         for i in range(1, len(nums) - 1):
#             if nums[i] > max_sum:
#                 temp_sum = nums[i]
#                 max_sum = nums[i]
#             else:
#                 if nums[i] + temp_sum >= max_sum:
#                     max_sum = temp_sum + nums[i]
#                 temp_sum += nums[i]
#
#         return max_sum


class Solution:
    def maxSubArray(self, nums) -> int:
        global_sum = nums[0]
        local_sum = nums[0]
        start = 0

        for i in range(1, len(nums)):
            if nums[i] + local_sum > global_sum:
                start = i
                global_sum = nums[i]
                local_sum = nums[i]
            else:
                if nums[i] + local_sum > global_sum:
                    global_sum = nums[i] + local_sum
                local_sum = nums[i] + sum(nums[start:i])
        return global_sum


s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

print(s.maxSubArray([5,4,-1,7,8]))
print(s.maxSubArray([1]))