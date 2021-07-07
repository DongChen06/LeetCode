class Solution:
    def permute(self, nums):
        """recursive approach"""
        out = []

        # base case
        if len(nums) == 1:
            return [nums]
        else:
            for i, n in enumerate(nums):
                nums_copy = [q for q in nums if q != n]
                for x in self.permute(nums_copy):
                    out.append([n] + x)
        return out


s = Solution()
print(s.permute([1, 2, 3]))
print(s.permute([1]))
