class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        for i in range(len(nums)-2):
            j, k = i + 1, len(nums)-1
            while j < k:
                val = nums[i] + nums[j] + nums[k]
                print(val)
                if abs(closest-target) > abs(val-target):
                    closest = val
                if val > target:
                    k -= 1
                elif val < target:
                    j += 1
                elif val == target:
                    return val
        return closest