class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0
        end = len(nums) - 1
        out = -1
        found = False

        """ Pay attention to the end conditions"""
        while end >= first and found is not True:
            mid = (first + end) // 2

            if nums[mid] == target:
                out = mid
                found = True
            else:
                if nums[mid] > target:
                    end = mid - 1
                else:
                    first = mid + 1

        return out

