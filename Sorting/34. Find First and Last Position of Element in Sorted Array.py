# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         if len(nums) == 0:
#             return [-1, -1]
#         if len(nums) == 1:
#             if nums[0] != target:
#                 return [-1, -1]
#             else:
#                 return [0, 0]
#
#         # find the leftmost first and then find the rightmost
#         index = [-1, -1]
#
#         index[0] = self.findleft(nums, target)
#         index[1] = self.findright(nums, target)
#
#         return index
#
#     def findleft(self, nums, target):
#         l, r = 0, len(nums) - 1
#         while l <= r:
#             mid = (l + r) // 2
#             if nums[mid] == target:
#                 if mid == 0:
#                     return mid
#                 if nums[mid-1] != target:
#                     return mid
#                 else:
#                     r = mid - 1
#             else:
#                 if nums[mid] <= target:
#                     l = mid + 1
#                 else:
#                     r = mid - 1
#
#         return -1
#
#     def findright(self, nums, target):
#         l, r = 0, len(nums) - 1
#
#         while l <= r:
#             mid = (l + r) // 2
#             if nums[mid] == target:
#                 if mid == len(nums) - 1:
#                     return mid
#                 if nums[mid+1] != target:
#                     return mid
#                 else:
#                     l = mid + 1
#             else:
#                 if nums[mid] <= target:
#                     l = mid + 1
#                 else:
#                     r = mid - 1
#
#         return -1


class Solution:
    def searchRange(self, nums, target: int):
        left, right = 0, len(nums) - 1
        found = False

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                while nums[left] != target:
                    left += 1
                while nums[right] != target:
                    right -= 1
                found = True
                break
            else:
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

        return [left, right] if found else [-1, -1]

s = Solution()

print(s.searchRange([5, 7, 7, 8, 8, 10], 8))


