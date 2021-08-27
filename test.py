class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1:
            if nums[0] != target:
                return [-1, -1]
            else:
                return [0, 0]

        left = self.findleft(nums, target)
        right = self.findright(nums, target)
        return [left, right]

    def findleft(self, nums, target):
        pl = 0
        pr = len(nums) - 1
        while pl <= pr:
            mid = pl + (pr - pl) // 2
            if nums[mid] == target:
                if mid == 0:
                    return mid
                else:
                    if nums[mid - 1] != target:
                        return mid
                    else:
                        pr = mid - 1
            elif nums[mid] < target:
                pl = mid + 1
            else:
                pr = mid - 1

        return -1

    def findright(self, nums, target):
        pl = 0
        pr = len(nums) - 1
        while pl <= pr:
            mid = pl + (pr - pl) // 2
            if nums[mid] == target:
                if mid == len(nums) - 1:
                    return mid
                else:
                    if nums[mid + 1] != target:
                        return mid
                    else:
                        pl = mid + 1
            elif nums[mid] < target:
                pl = mid + 1
            else:
                pr = mid - 1

        return -1
