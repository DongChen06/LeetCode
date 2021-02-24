def rob(nums) -> int:
        if nums ==[]:
            return 0
        money_max = []
        for i in range(len(nums)):
            if i == 0:
                money_max.append(nums[0])
            elif i == 1:
                money_max.append(max(nums[0], nums[1]))
            else:
                money_max.append(max(money_max[i-2] + nums[i], money_max[i-1]))
        return money_max.pop()

print(rob([1, 2, 3, 1]))