class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i,num in enumerate(nums):
            last = len(nums)-1-i
            if last-1>=0 and nums[last-1]>=nums[last]:
                continue
            else:
                break
        if last == 0:
            nums.sort()
        else:
            idx = last
            for i in range(last,len(nums)):
                if nums[i]>nums[last-1]:
                    idx = i
            nums[last-1],nums[idx] = nums[idx],nums[last-1]
            nums[last:] = sorted(nums[last:])