class Solution:
    def searchInsert(self, nums, target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] < target:
                left += 1
            elif nums[mid] > target:
                right -= 1
            else:
                return mid
        return left if mid == left else right + 1


s = Solution()
print(s.searchInsert([1, 3, 5, 6], 5))
print(s.searchInsert([1, 3, 5, 6], 2))
print(s.searchInsert([1, 3, 5, 6], 7))
print(s.searchInsert([1], 7))
print(s.searchInsert([1], 0))