class Solution:
    def removeDuplicates(self, nums) -> int:
        len_ = 1
        if len(nums) == 0:
            return 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[len_] = nums[i]
                len_ += 1
        return len_


s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))