def maxSubArray(nums):
        c_list = []
        if nums == []:
            return 
        largest_sum = nums[0]
        for num in nums:
            if sum(c_list) + num > sum(c_list) and sum(c_list) + num >= num:
                c_list.append(num)
                if largest_sum < sum(c_list):
                    largest_sum = sum(c_list)
            else:
                c_list = [num]
        return c_list

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))