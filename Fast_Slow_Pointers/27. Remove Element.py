class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                nums[n - 1] = val
                n -= 1
                k += 1
            else:
                i += 1

        return len(nums) - k

s = Solution()
print(s.removeElement([0,1,2,2,3,0,4,2], 2))