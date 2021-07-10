class Solution:
    # def containsDuplicate(self, nums) -> bool:
    #     if len(nums) == 0:
    #         return False
    #
    #     items = {}
    #
    #     for num in nums:
    #         if str(num) in items:
    #             items[str(num)] += 1
    #         else:
    #             items[str(num)] = 1
    #
    #     values = list(items.values())
    #
    #     for v in values:
    #         if v != 1:
    #             return True
    #
    #     return False

    def containsDuplicate(self, nums) -> bool:
        if len(nums) == 0:
            return False

        items = {}

        for num in nums:
            if num in items:
                return True
            else:
                items[num] = 1

        return False

s = Solution()

input = [1,2,3,1]
print(s.containsDuplicate(input))