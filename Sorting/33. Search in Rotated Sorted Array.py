class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:  # mid check for target
                return mid
            if nums[0] <= nums[mid]:  # mid is searching in left sorted half
                if nums[0] <= target and nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target and nums[len(nums) - 1] >= target:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
