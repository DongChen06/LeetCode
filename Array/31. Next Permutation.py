class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums) - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1

        if i == 0:
            nums.reverse()
            return

        while nums[j] <= nums[i - 1]:
            j -= 1

        nums[i - 1], nums[j] = nums[j], nums[i - 1]

        l, r = i, len(nums) - 1  # reverse the second part
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


s = Solution()
s.nextPermutation([1, 5, 1])